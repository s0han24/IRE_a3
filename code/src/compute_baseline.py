"""Stage 1 (compute): exact FAISS baseline -> results/<mode>/baseline.json.

Wiring only; every piece it calls is unit-tested in annbench.
Usage: uv run python code/src/compute_baseline.py [--quick]
"""

import argparse
import shutil
from contextlib import nullcontext
from functools import partial
from pathlib import Path
from time import perf_counter
from urllib.request import Request, urlopen

from annbench.agreement import neighbours_agree
from annbench.data import (
    download,
    load_hdf5,
    prepare_vectors,
    split_queries,
    subset_base,
)
from annbench.exact import FaissExact
from annbench.results_io import run_meta, save_results
from annbench.timing import faiss_threads, time_batch, time_one_at_a_time

DATASETS = ("sift-128-euclidean", "glove-100-angular")
K = 10
QUICK_N = 100_000
REPEATS = 3  # every timing is the median of this many runs (spec line 22)


def fetch(url: str, dest: Path) -> None:
    """Like urlretrieve, but with a User-Agent: the CDN 403s Python-urllib's default."""
    req = Request(url, headers={"User-Agent": "annbench/0.1"})
    with urlopen(req) as resp, dest.open("wb") as f:
        shutil.copyfileobj(resp, f)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--out", type=Path, default=Path("results"))
    parser.add_argument(
        "--threads", type=int, help="FAISS threads for single-query timing"
    )
    parser.add_argument("--k-search", type=int, default=K, help="results per search")
    args = parser.parse_args()
    args.data_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for name in DATASETS:
        data = prepare_vectors(name, load_hdf5(download(name, args.data_dir, fetch)))
        base = subset_base(data["train"], QUICK_N) if args.quick else data["train"]
        _, report = split_queries(data["test"])
        index = FaissExact().build(base)

        agree = None  # stored neighbours only hold for the full base set
        if not args.quick:
            ids, _ = index.search(data["test"], K)  # all 10000 queries
            agree = neighbours_agree(ids, data["neighbors"], data["distances"], K)

        search = partial(index.search, k=args.k_search)
        search(report[:1])  # untimed warm-up: page faults, thread pool start
        batch_seconds = time_batch(search, report, perf_counter, REPEATS)
        with faiss_threads(args.threads) if args.threads else nullcontext():
            latencies = time_one_at_a_time(search, report, perf_counter, REPEATS)
        records.append(
            {
                "dataset": name,
                "n_base": int(base.shape[0]),
                "n_queries": int(report.shape[0]),
                "k": K,
                "k_search": args.k_search,
                "single_query_threads": args.threads,  # None = FAISS default
                "agrees_with_stored": agree,
                "batch_seconds": batch_seconds,
                "latencies_s": latencies.tolist(),
            }
        )
        print(name, "agree:", agree, "batch_s:", records[-1]["batch_seconds"])

    mode = "quick" if args.quick else "full"
    out_dir = args.out / mode
    out_dir.mkdir(parents=True, exist_ok=True)
    params = {
        "k": K,
        "k_search": args.k_search,
        "single_query_threads": args.threads,
        "timing_repeats": REPEATS,
        "quick": args.quick,
        "quick_n": QUICK_N,
        "datasets": DATASETS,
    }
    # One file per thread setting: the default-thread baseline is never overwritten.
    stem = f"baseline_{args.threads}thread" if args.threads else "baseline"
    save_results(out_dir / f"{stem}.json", records, run_meta(params))


if __name__ == "__main__":
    main()
