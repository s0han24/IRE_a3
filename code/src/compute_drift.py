"""Stage 1 (compute): drift experiments on SIFT -> results/<mode>/drift_<kind>.json.

Wiring only; every piece it calls is unit-tested in annbench.
Usage: uv run python code/src/compute_drift.py [--quick]

Base: first 300k SIFT vectors (quick: 50k). Two drift kinds, never combined:
mean shift (c = 5, 10, 15; quick: 10) and pairwise rotation (2, 3, 5 degrees; quick: 5).
Conditions per setting:
  stale   - indexes built on the original base, searched with transformed queries;
  rebuilt - base and queries transformed, every index rebuilt.
"clean" (original base and queries) is measured once in the same run and written to
both files. Every Benchmarks-grid config plus exact search is measured with two recalls:
  recall_own      - vs exact neighbours of the queries it was given, in the base it was
                    built on;
  recall_original - vs exact neighbours of the original query in the original base.
"""

import argparse
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
from annbench.drift import mean_shift, rotate_pairs
from annbench.exact import FaissExact
from annbench.indexes import index_size_bytes
from annbench.metrics import qps
from annbench.recall import recall_at_k
from annbench.results_io import run_meta, save_results
from annbench.timing import faiss_threads, time_build, time_one_at_a_time
from compute_baseline import REPEATS, fetch
from compute_sweeps import K_SEARCH, K, build, grid

DATASET = "sift-128-euclidean"
KINDS = {  # kind -> (transform, full settings, quick settings)
    "mean_shift": (mean_shift, [5, 10, 15], [10]),
    "rotation": (rotate_pairs, [2, 3, 5], [5]),
}


def latencies(wrapper, report):
    """Median-of-REPEATS single-query latencies on 1 FAISS thread, after a warm-up."""
    search = partial(wrapper.search, k=K_SEARCH)
    with faiss_threads(1):
        search(report[:1])
        return time_one_at_a_time(search, report, perf_counter, REPEATS)


def measure(wrapper, values, queries, gt_own, gt_original):
    """One record fragment per search value: both recalls and latencies.

    queries / gt_own: dicts with "tune" and "report"; gt_original: report-query ids.
    """
    out = []
    for v in values:
        if v is not None:
            wrapper.set_search(v)
        t_ids, t_d = wrapper.search(queries["tune"], K_SEARCH)
        r_ids, r_d = wrapper.search(queries["report"], K_SEARCH)
        lat = latencies(wrapper, queries["report"])
        out.append(
            {
                "search_value": v,
                "tune_recall_own": recall_at_k(t_ids, t_d, gt_own["tune"], K),
                "report_recall_own": recall_at_k(r_ids, r_d, gt_own["report"], K),
                "report_recall_original": recall_at_k(r_ids, r_d, gt_original, K),
                "latencies_s": lat.tolist(),
            }
        )
    return out


def exact_gt(base, queries):
    """Exact index on base and its top-K ids for the tune and report queries."""
    exact = FaissExact().build(base)
    return exact, {h: exact.search(q, K)[0] for h, q in queries.items()}


def run_condition(tag, base, queries, builds, gt_original, prebuilt=None):
    """Measure exact search + every build config for one condition.

    prebuilt: {label: (wrapper, build_s, size)} to reuse (stale); else build on base.
    """
    exact, gt_own = exact_gt(base, queries)
    common = {"dataset": DATASET, "n_base": int(base.shape[0]), **tag}
    records = [
        {
            **common,
            "index": "exact",
            "build": "exact",
            "build_params": {},
            "search_param": None,
            "build_seconds": None,
            "size_bytes": None,
            "build_reused": False,
            **m,
        }
        for m in measure(exact, [None], queries, gt_own, gt_original)
    ]
    del exact
    for index, label, params, make, sname, values in builds:
        if prebuilt is not None:
            wrapper, build_s, size = prebuilt[label]
        else:
            wrapper, build_s = time_build(partial(build, make, base), perf_counter)
            size = index_size_bytes(wrapper)
        for m in measure(wrapper, values, queries, gt_own, gt_original):
            records.append(
                {
                    **common,
                    "index": index,
                    "build": label,
                    "build_params": params,
                    "search_param": sname,
                    "build_seconds": build_s,
                    "size_bytes": size,
                    "build_reused": prebuilt is not None,
                    **m,
                }
            )
        best = max(r["report_recall_original"] for r in records if r["build"] == label)
        lat = records[-1]["latencies_s"]
        print(
            f"{tag} {label}: best recall_original {best:.3f}, "
            f"last config {qps(len(lat), sum(lat)):.0f} QPS"
        )
        if prebuilt is None:
            del wrapper
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()
    out_dir = args.out / ("quick" if args.quick else "full")
    out_dir.mkdir(parents=True, exist_ok=True)
    n = 50_000 if args.quick else 300_000

    data = prepare_vectors(DATASET, load_hdf5(download(DATASET, args.data_dir, fetch)))
    base = subset_base(data["train"], n)
    tune, report = split_queries(data["test"])
    queries = {"tune": tune, "report": report}
    builds = grid(base.shape[1], n, args.quick)
    _, gt_clean = exact_gt(base, queries)
    gt_original = gt_clean["report"]

    # Clean indexes, built once: measured as "clean", then reused for every stale run.
    prebuilt = {}
    for _, label, _, make, _, _ in builds:
        wrapper, build_s = time_build(partial(build, make, base), perf_counter)
        prebuilt[label] = (wrapper, build_s, index_size_bytes(wrapper))
    clean = run_condition(
        {"kind": None, "setting": None, "condition": "clean"},
        base,
        queries,
        builds,
        gt_original,
        prebuilt,
    )

    for kind, (transform, full, quick) in KINDS.items():
        records = list(clean)
        for setting in quick if args.quick else full:
            moved = {h: transform(q, setting) for h, q in queries.items()}
            records += run_condition(
                {"kind": kind, "setting": setting, "condition": "stale"},
                base,
                moved,
                builds,
                gt_original,
                prebuilt,
            )
            records += run_condition(
                {"kind": kind, "setting": setting, "condition": "rebuilt"},
                transform(base, setting),
                moved,
                builds,
                gt_original,
            )
            meta = run_meta(
                {
                    "k": K,
                    "k_search": K_SEARCH,
                    "single_query_threads": 1,
                    "timing_repeats": REPEATS,
                    "n_base": n,
                    "kind": kind,
                    "settings": quick if args.quick else full,
                    "quick": args.quick,
                }
            )
            # Saved after every setting, so a long full run keeps finished settings.
            save_results(out_dir / f"drift_{kind}.json", records, meta)


if __name__ == "__main__":
    main()
