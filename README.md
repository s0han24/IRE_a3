# annbench: benchmarking approximate nearest neighbour search

Benchmarks ANN search on SIFT-1M and GloVe-100 from
[ann-benchmarks](https://github.com/erikbern/ann-benchmarks), against an exact FAISS baseline.

## Experiments

The hypothesis below was written down before any ANN experiment was implemented or run
(copied verbatim from the spec).

### Hypothesis
1. exact search should have the worst scaling of the 3, the qps increases linearly with number of vectors but the recall saturates giving a exponential-looking increase in qps against the recall
2. HNSW and IVF-Flat should have better scaling than exact search, HNSW should perform better than IVF-Flat given the right hyperparameters, though it may perform worse on certain configs. 

## Setup

Requires [uv](https://docs.astral.sh/uv/) (Python 3.12 is picked up from `.python-version`).

```bash
uv sync
```

## Reproducing every number, figure and table

Run from `src/`:

```bash
cd src
bash run_all.sh            # full datasets
bash run_all.sh --quick    # first 100,000 base vectors per dataset
```

| mode | base vectors | output | time on a laptop (M-series, 8 cores) |
|---|---|---|---|
| `--quick` | first 100,000 of each dataset | `results/quick/` | ~4 min once the data is downloaded (first run adds the ~1 GB download) |
| full | 1,000,000 (SIFT), 1,183,514 (GloVe) | `results/full/` | **not yet measured**; estimated ~1 h (baselines ~8 min, sweeps ~30–45 min, scaling ~15 min) |

`--quick` runs the same experiments with smaller sweep grids, and the scaling experiment at
100k vectors only.

Other options:

```bash
bash run_all.sh --report-only           # re-make tables/figures from results/full without recomputing
bash run_all.sh --quick --report-only   # same for results/quick
```

The script can be run from any directory: it switches to the repo root itself, so `data/` and
`results/` always sit at the root. Unknown arguments are rejected.

## The pipeline

`src/run_all.sh` runs two stages. New experiments are added by appending their commands to the
matching stage block in that file. Stage 1 is the only stage that reads `data/` or uses FAISS.

**Stage 1a: exact baseline** (`src/compute_baseline.py`). For each dataset it:

1. downloads `<name>.hdf5` from ann-benchmarks into `data/` if it isn't there yet. The file is
   written to `<name>.hdf5.part` and renamed when complete, so an interrupted download is never
   mistaken for a finished one;
2. loads `train`, `test`, `neighbors` and `distances`, with vectors as float32;
3. L2-normalises GloVe (`*-angular`) vectors. SIFT stays raw. Euclidean distance is used for
   both datasets; on unit vectors it ranks neighbours exactly as cosine similarity does;
4. in `--quick` mode, keeps only the first 100,000 base vectors;
5. splits the 10,000 queries: the first 5,000 are for tuning and experimentation, the last 5,000
   for every reported number;
6. builds exact search (FAISS `IndexFlatL2`, distances reported as plain L2);
7. full mode only: checks that exact search agrees with the neighbours stored in the file on all
   10,000 queries, with tie-aware matching at the 10th place. This is skipped in `--quick`,
   because the stored neighbours are only valid for the full base set;
8. times search on the 5,000 report queries, once as a single batch and once one query at a
   time, after one untimed warm-up query.

It writes `results/<mode>/baseline.json`. Run with `--threads 1 --k-search 20`, it instead
writes `results/<mode>/baseline_1thread.json`, which never overwrites `baseline.json`.

> **Thread count of the one-query-at-a-time numbers.** The two baseline files time single
> queries differently, so don't compare them directly:
>
> - `baseline.json` is the baseline check: single queries run with FAISS's default thread
>   count (all cores, 8 here), searching for k = 10. FAISS can spread even one query's flat
>   scan across threads, so these latencies are *not* single-threaded.
> - `baseline_1thread.json` is restricted to 1 FAISS thread during single-query timing and
>   searches for k' = 20 (recall@10 needs the extra results to handle ties). The ANN
>   benchmarks time single queries the same way, and this is the exact-search point plotted
>   against HNSW / IVF-Flat / IVF-PQ.
>
> Batch timing always uses the default thread count. The 1-thread single-query exact search
> was about 1.25x slower than the default-thread one on the 100k subset, and about 1.1-1.15x
> slower on the full data (SIFT 49 vs 57 QPS, GloVe 49 vs 54).

```json
{
  "meta": {
    "params": {"k": 10, "quick": false, "quick_n": 100000, "datasets": ["..."]},
    "versions": {"python": "...", "numpy": "...", "faiss": "...", "h5py": "..."},
    "machine": {"platform": "...", "processor": "...", "cpu_count": 8, "faiss_threads": 8},
    "timestamp": "2026-10-26T13:25:31+00:00"
  },
  "records": [
    {"dataset": "sift-128-euclidean", "n_base": 1000000, "n_queries": 5000, "k": 10,
     "agrees_with_stored": true, "batch_seconds": 2.23, "latencies_s": [0.017, "..."]}
  ]
}
```

**Stage 1b: ANN sweeps** (`src/compute_sweeps.py`, FAISS `IndexHNSWFlat`, `IndexIVFFlat`,
`IndexIVFPQ`). For each dataset it computes the exact top-10 of every query, then builds each
index config once (build time and serialised size recorded) and sweeps its search parameter:

| index | build configs, full (quick) | search sweep |
|---|---|---|
| HNSW | M ∈ {16, 32} ({16}), efConstruction 200 | efSearch 32 … 512 |
| IVF-Flat | c ∈ {1, 4} ({1}) | nprobe 1 … 128 |
| IVF-PQ | c = 4 (1), m ∈ {d/2, d/4} ({d/2}), 8 bits | nprobe 1 … 256 |

IVF uses `nlist = round(c · √n)`. For every search value it records recall@10 on the tuning
queries (used only to choose configs), recall@10 on the report queries, and the latency of
each report query run one at a time on 1 FAISS thread (after an untimed warm-up). Every search
returns k' = 20 results. Output: `results/<mode>/sweeps.json`. An index with no config reaching
recall@10 ≥ 0.95 is flagged on stdout and in the tables (IVF-PQ without re-ranking plateaus
below it, around 0.87–0.89 on the 100k subsets).

**Recall@10** (`annbench.recall.recall_at_k`): a returned id counts if its reported distance is
≤ the 10th returned distance (with a 1e-5 relative tolerance), so an index's arbitrary order
among ties at the 10th place cannot hide a true neighbour; recall = |exact top-10 ∩ counted
ids| / 10. IVF-PQ reports approximate distances, so its ties are judged on those.

**Stage 1c: scaling** (`src/compute_scaling.py`, SIFT only). The 3 best build configs per index
for HNSW and IVF-Flat, ranked by the area under log10(QPS) vs tuning-query recall (recall ≥ 0.5),
are re-run with their full search sweep at 100k, 300k and 1M base vectors (quick: 100k), plus
exact search. IVF's `nlist` follows `c · √n` at each size. Measurements that already exist at a
size (the sweep at its own base size, the 1-thread baseline) are reused. Output:
`results/<mode>/scaling.json`.

Stage 1 stores only raw measurements. Every derived number, such as QPS and the latency
percentiles, is computed in stage 2.

**Stage 2: report** (`src/make_report.py`). This stage reads `results/` only, so it can be re-run
on its own with `--report-only`. It writes:

- `results/<mode>/tables/baseline.md`: dataset, n_base, agreement, batch time, batch QPS,
  single-query QPS (queries / total one-at-a-time time), and p50/p95/p99 single-query latency;
- `results/<mode>/tables/baseline_1thread.md`: the same table for `baseline_1thread.json`,
  if it exists;
- `results/<mode>/figures/baseline_latency_ecdf.png`: the distribution of single-query latency;
- `results/<mode>/tables/qps_at_recall.md`: per dataset and index, the best single-query QPS
  reaching recall@10 0.9 and 0.95, with that config named ("not reached" if none does);
- `results/<mode>/tables/build_cost_at_0.95.md`: build time, index size and bytes per vector of
  each index's best config at recall 0.95 (or its highest-recall config, flagged);
- `results/<mode>/figures/recall_vs_qps.png`: recall@10 against single-query QPS per dataset,
  showing each index's best build config (by curve area) and the exact baseline;
- `results/<mode>/tables/scaling.md` and `figures/scaling_qps_at_0.95.png`: per base size, the
  cheapest config of each index reaching recall 0.95.

Selection (which build is plotted, which configs are scaled) uses tuning-query recall; every
reported recall and QPS is on the report queries.

`data/` and `results/` are git-ignored.

## Code layout

| path | contents |
|---|---|
| `src/annbench/data.py` | download, HDF5 loading, query split, normalisation, `--quick` subset |
| `src/annbench/exact.py` | `FaissExact`: `build(base)` / `search(queries, k) -> (ids, dists)` |
| `src/annbench/recall.py` | `recall_at_k`: recall@k where a tie at the k-th distance counts as a hit |
| `src/annbench/agreement.py` | `neighbours_agree`: tie-aware check against stored neighbours |
| `src/annbench/timing.py` | batch and one-at-a-time timing with an injectable clock |
| `src/annbench/metrics.py` | `latency_summary` (p50/p95/p99/mean), `qps` |
| `src/annbench/indexes.py` | `FaissHNSW`, `FaissIVFFlat`, `FaissIVFPQ` (same interface), `index_size_bytes` |
| `src/annbench/sweeps.py` | `curve_area`, `best_at_recall`, `top_build_configs`, `points` |
| `src/annbench/tables.py` | markdown tables from result records |
| `src/annbench/results_io.py` | results JSON save/load, run metadata |
| `src/compute_baseline.py`, `compute_sweeps.py`, `compute_scaling.py` | stage 1 entry points (wiring only) |
| `src/make_report.py` | stage 2 entry point (wiring only) |
| `tests/` | one test file per module |

## Development

```bash
uv run pytest -q                        # fast unit tests (slow ones skipped by default)
uv run pytest -q -m "slow or not slow"  # include slow tests
uv run pytest -q tests/test_recall.py   # one file
uv run ruff check .                     # lint
uv run ruff format .                    # format
```

Unit tests use tiny synthetic data and never touch `data/` or the network.

**macOS note:** if this repo is inside an iCloud-synced folder (e.g. `~/Documents`), macOS can set
the `hidden` flag on the venv's `.pth` files, and Python 3.12 then skips them. pytest is not
affected (`pythonpath = ["src"]` in `pyproject.toml`), and the pipeline scripts are run as files
in `src/`, so they find `annbench` too. Only an ad-hoc `uv run python -c "import annbench"` fails;
prefix it with `PYTHONPATH=src`, or run `chflags nohidden .venv/lib/python3.12/site-packages/*.pth`.
