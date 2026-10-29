"""Stage 1 (compute): SIFT scaling experiment -> results/<mode>/scaling.json.

Wiring only. Needs results/<mode>/sweeps.json and baseline_1thread.json first.
Usage: uv run python src/compute_scaling.py [--quick]

Every HNSW and IVF-Flat build config from the sweep (spec line 36: all configs) is
re-run at each base size (full: 100k / 300k / 1M; quick: 100k), with its whole
search-parameter sweep, so the report can pick the cheapest config reaching recall 0.95
at each size. IVF nlist follows round(c * sqrt(n)). Exact search (1 thread, k' = 20) is
timed at each size. Every single-query timing is the per-query median of REPEATS passes.
Measurements that already exist at a size (the sweep's own base size, the 1-thread
baseline) are reused rather than repeated.
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
from annbench.indexes import FaissHNSW, FaissIVFFlat, index_size_bytes
from annbench.recall import recall_at_k
from annbench.results_io import load_results, run_meta, save_results
from annbench.timing import faiss_threads, time_build, time_one_at_a_time
from compute_baseline import REPEATS, fetch

DATASET = "sift-128-euclidean"
K = 10
K_SEARCH = 20


def make_wrapper(index: str, params: dict, n: int) -> FaissHNSW | FaissIVFFlat:
    """A fresh wrapper for a sweep build config at base size n."""
    if index == "hnsw":
        return FaissHNSW(params["M"], params["ef_construction"])
    return FaissIVFFlat(round(params["c"] * math.sqrt(n)))


def build(make, base):
    """Construct a wrapper from its factory and build it on base."""
    return make().build(base)


def single_query_latencies(search, report):
    """Report queries one at a time on 1 FAISS thread, after an untimed warm-up."""
    with faiss_threads(1):
        search(report[:1])
        return time_one_at_a_time(search, report, perf_counter, REPEATS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()
    out_dir = args.out / ("quick" if args.quick else "full")
    sizes = [100_000] if args.quick else [100_000, 300_000, 1_000_000]

    sweep = [
        r for r in load_results(out_dir / "sweeps.json")[0] if r["dataset"] == DATASET
    ]
    baseline = [
        r
        for r in load_results(out_dir / "baseline_1thread.json")[0]
        if r["dataset"] == DATASET
    ]
    chosen = {}  # build label -> its sweep records; all builds (spec line 36)
    for r in sweep:
        if r["index"] in ("hnsw", "ivf_flat"):
            chosen.setdefault(r["build"], []).append(r)
    print("scaling configs:", ", ".join(chosen))

    data = prepare_vectors(DATASET, load_hdf5(download(DATASET, args.data_dir, fetch)))
    _, report = split_queries(data["test"])
    meta = run_meta(
        {
            "k": K,
            "k_search": K_SEARCH,
            "single_query_threads": 1,
            "sizes": sizes,
            "timing_repeats": REPEATS,
            "configs": list(chosen),
        }
    )
    records = []
    for n in sizes:
        base = subset_base(data["train"], n)
        exact = FaissExact().build(base)
        exact_rec = next((r for r in baseline if r["n_base"] == n), None)
        if exact_rec is None:
            lat = single_query_latencies(partial(exact.search, k=K_SEARCH), report)
            exact_rec = {"latencies_s": lat.tolist()}
        records.append(
            {
                "dataset": DATASET,
                "index": "exact",
                "build": "exact",
                "build_params": {},
                "search_param": None,
                "search_value": None,
                "n_base": n,
                "report_recall": 1.0,
                "latencies_s": exact_rec["latencies_s"],
            }
        )

        reused = [r for recs in chosen.values() for r in recs if r["n_base"] == n]
        if reused:
            print(f"n={n}: reusing {len(reused)} sweep points")
            records += reused
        else:
            gt, _ = exact.search(report, K)
            for label, recs in chosen.items():
                records += sweep_at(n, base, report, gt, label, recs)
        del exact
        # Saved after every size, so a long full run keeps finished sizes.
        save_results(out_dir / "scaling.json", records, meta)


def sweep_at(n, base, report, gt, label, recs):
    """Rebuild one sweep build config at base size n and re-run its search sweep."""
    index, params, sname = (
        recs[0]["index"],
        recs[0]["build_params"],
        recs[0]["search_param"],
    )
    make = partial(make_wrapper, index, params, n)
    wrapper, build_s = time_build(partial(build, make, base), perf_counter)
    size = index_size_bytes(wrapper)
    out = []
    for v in [r["search_value"] for r in recs]:
        wrapper.set_search(v)
        ids, dists = wrapper.search(report, K_SEARCH)
        lat = single_query_latencies(partial(wrapper.search, k=K_SEARCH), report)
        out.append(
            {
                "dataset": DATASET,
                "index": index,
                "build": label,
                "build_params": params,
                "search_param": sname,
                "search_value": v,
                "n_base": n,
                "build_seconds": build_s,
                "size_bytes": size,
                "report_recall": recall_at_k(ids, dists, gt, K),
                "latencies_s": lat.tolist(),
            }
        )
        print(f"n={n} {label} {sname}={v}: recall {out[-1]['report_recall']:.3f}")
    return out


if __name__ == "__main__":
    main()
