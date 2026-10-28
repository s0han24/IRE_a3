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
| `--quick` | first 100,000 of each dataset | `results/quick/` | ~5 min on the first run (most of it is the ~1 GB download), ~20 s afterwards |
| full | 1,000,000 (SIFT), 1,183,514 (GloVe) | `results/full/` | ~3–4 min once the data is downloaded |

Other options:

```bash
bash run_all.sh --report-only           # re-make tables/figures from results/full without recomputing
bash run_all.sh --quick --report-only   # same for results/quick
```

The script can be run from any directory: it switches to the repo root itself, so `data/` and
`results/` always sit at the root. Unknown arguments are rejected.

## The pipeline

`src/run_all.sh` runs two stages. New experiments are added by appending their commands to the
matching stage block in that file.

**Stage 1: compute** (`src/compute_baseline.py`). This is the only stage that reads `data/` or
uses FAISS. For each dataset it:

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

It writes `results/<mode>/baseline.json`:

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

Stage 1 stores only raw measurements. Every derived number, such as QPS and the latency
percentiles, is computed in stage 2.

**Stage 2: report** (`src/make_report.py`). This stage reads `results/` only, so it can be re-run
on its own with `--report-only`. It writes:

- `results/<mode>/tables/baseline.md`: dataset, n_base, agreement, batch time, batch QPS,
  single-query QPS (queries / total one-at-a-time time), and p50/p95/p99 single-query latency;
- `results/<mode>/figures/baseline_latency_ecdf.png`: the distribution of single-query latency.

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
| `src/annbench/tables.py` | markdown tables from result records |
| `src/annbench/results_io.py` | results JSON save/load, run metadata |
| `src/compute_baseline.py`, `src/make_report.py` | stage 1 / stage 2 entry points (wiring only) |
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
