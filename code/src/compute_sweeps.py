"""Stage 1 (compute): HNSW / IVF-Flat / IVF-PQ sweeps -> results/<mode>/sweeps.json.

Wiring only; every piece it calls is unit-tested in annbench.
Usage: uv run python code/src/compute_sweeps.py [--quick]

Per dataset and build config: build once (timed, sized), then per search parameter:
  - tune recall@10: batch search of the 5000 tuning queries (used to pick configs);
  - report recall@10: batch search of the 5000 report queries;
  - report latencies: the report queries one at a time, FAISS limited to 1 thread.
All searches return k' = 20 results so recall can handle ties at the 10th place.
"""

import argparse
import math
from functools import partial
from pathlib import Path
from time import perf_counter

from annbench.data import (
    download,
    load_hdf5,
    prepare_vectors,
    split_queries,
    subset_base,
)
from annbench.exact import FaissExact
from annbench.indexes import FaissHNSW, FaissIVFFlat, FaissIVFPQ, index_size_bytes
from annbench.metrics import qps
from annbench.recall import recall_at_k
from annbench.results_io import run_meta, save_results
from annbench.sweeps import best_at_recall
from annbench.timing import faiss_threads, time_build, time_one_at_a_time
from compute_baseline import DATASETS, QUICK_N, REPEATS, fetch

K = 10
K_SEARCH = 20
NPROBES = [1, 2, 4, 8, 16, 32, 64, 128]


def grid(d: int, n: int, quick: bool) -> list[tuple[str, str, dict, object, str, list]]:
    """(index, build label, build params, factory, search param, values) per build."""
    builds = []
    for M in [16] if quick else [16, 32]:
        params = {"M": M, "ef_construction": 200}
        builds.append(
            (
                "hnsw",
                f"hnsw M={M}",
                params,
                lambda p=params: FaissHNSW(**p),
                "ef_search",
                [32, 64, 128, 256, 512],
            )
        )
    for c in [1] if quick else [1, 4]:
        params = {"c": c, "nlist": round(c * math.sqrt(n))}
        builds.append(
            (
                "ivf_flat",
                f"ivf_flat c={c}",
                params,
                lambda p=params: FaissIVFFlat(p["nlist"]),
                "nprobe",
                NPROBES,
            )
        )
    c = 1 if quick else 4
    for m in [d // 2] if quick else [d // 2, d // 4]:
        params = {"c": c, "nlist": round(c * math.sqrt(n)), "m": m, "nbits": 8}
        builds.append(
            (
                "ivf_pq",
                f"ivf_pq c={c} m={m}",
                params,
                lambda p=params: FaissIVFPQ(p["nlist"], p["m"], p["nbits"]),
                "nprobe",
                NPROBES + [256],
            )
        )
    return builds


def build(make, base):
    """Construct a wrapper from its factory and build it on base."""
    return make().build(base)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()
    mode = "quick" if args.quick else "full"
    out_dir = args.out / mode
    out_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for name in DATASETS:
        data = prepare_vectors(name, load_hdf5(download(name, args.data_dir, fetch)))
        base = subset_base(data["train"], QUICK_N) if args.quick else data["train"]
        tune, report = split_queries(data["test"])
        exact = FaissExact().build(base)
        gt_tune, _ = exact.search(tune, K)
        gt_report, _ = exact.search(report, K)
        del exact

        n, d = base.shape
        for index, label, params, make, sname, values in grid(d, n, args.quick):
            wrapper, build_s = time_build(partial(build, make, base), perf_counter)
            size = index_size_bytes(wrapper)
            print(f"{name} {label}: built in {build_s:.1f} s, {size / n:.1f} B/vec")
            for v in values:
                wrapper.set_search(v)
                t_ids, t_d = wrapper.search(tune, K_SEARCH)
                r_ids, r_d = wrapper.search(report, K_SEARCH)
                search = partial(wrapper.search, k=K_SEARCH)
                with faiss_threads(1):
                    search(report[:1])  # untimed warm-up
                    lat = time_one_at_a_time(search, report, perf_counter, REPEATS)
                rec = {
                    "dataset": name,
                    "index": index,
                    "build": label,
                    "build_params": params,
                    "search_param": sname,
                    "search_value": v,
                    "n_base": int(n),
                    "build_seconds": build_s,
                    "size_bytes": size,
                    "tune_recall": recall_at_k(t_ids, t_d, gt_tune, K),
                    "report_recall": recall_at_k(r_ids, r_d, gt_report, K),
                    "latencies_s": lat.tolist(),
                }
                records.append(rec)
                print(
                    f"  {sname}={v}: recall {rec['report_recall']:.3f}, "
                    f"{qps(len(lat), lat.sum()):.0f} QPS"
                )
            del wrapper, search  # free the index before building the next one

        for index in ("hnsw", "ivf_flat", "ivf_pq"):
            mine = [
                {
                    "recall": r["report_recall"],
                    "qps": qps(len(r["latencies_s"]), sum(r["latencies_s"])),
                }
                for r in records
                if r["dataset"] == name and r["index"] == index
            ]
            if best_at_recall(mine, 0.95) is None:
                print(f"FLAG: {name} {index}: no config reaches recall@10 >= 0.95")

        params = {
            "k": K,
            "k_search": K_SEARCH,
            "timing_repeats": REPEATS,
            "single_query_threads": 1,
            "quick": args.quick,
            "quick_n": QUICK_N,
            "datasets": DATASETS,
            "faiss_seeds": "FAISS default seeds (k-means, HNSW levels)",
        }
        # Saved after every dataset, so a long full run keeps finished datasets.
        save_results(out_dir / "sweeps.json", records, run_meta(params))


if __name__ == "__main__":
    main()
