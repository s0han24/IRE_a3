# annbench: benchmarking approximate nearest neighbour search

This repository is mostly for experimental verification and is written completely using Claude Opus 5.5. However, every line has been reviewed for correctness and TDD was followed. Further, the agent produces all plans based on the specifications in SPEC.md and then implements them. `AI_LOGS/` contains all the AI generated artifacts along with `SPEC.md`.

Benchmarks ANN search on SIFT-1M and GloVe-100 from
[ann-benchmarks](https://github.com/erikbern/ann-benchmarks), against an exact FAISS baseline.

## Experiments

Each hypothesis was written down before its experiments were implemented or run (copied
verbatim from the spec).

**Standard data** (scaling on SIFT):

### Hypothesis
1. exact search should have the worst scaling of the 3, the qps increases linearly with number of vectors but the recall saturates giving a exponential-looking increase in qps against the recall
2. HNSW and IVF-Flat should have better scaling than exact search, HNSW should perform better than IVF-Flat given the right hyperparameters, though it may perform worse on certain configs. 

**Drifted data** (mean shift and rotation on SIFT):

### Hypothesis
1. Two metrics are calculated, one is recall against the ground truth and recall against exact search. All indexes are expected to show some degradation against the ground truth but still show similar recall against the exact search.
2. QPS is measured too, this is expected to show no changes at all.
3. IVF-PQ is expected to show the greatest degradation and IVF-Flat the least because for well separated clusters, the drift may not affect step 1 which decides the cluster in which a query lands. Step 2 however will be affected by drift because of the brittle quantization. IVF-Flat for well separated clusters should show similar degradation behaviour to exact search.

## Setup

Requires [uv](https://docs.astral.sh/uv/) (Python 3.12 is picked up from `.python-version`).

```bash
uv sync
```

## Running

Run from `src/` (the script switches to the repo root, so `data/` and `results/` sit there):

```bash
cd src
bash run_all.sh                         # full datasets, ~55 min on an M-series laptop
bash run_all.sh --quick                 # first 100,000 base vectors, ~5 min
bash run_all.sh --report-only           # re-make tables/figures from existing results
bash run_all.sh --quick --report-only
```

The first run also downloads SIFT and GloVe-100 (~1 GB) into `data/` (git-ignored).
Outputs go to `results/full/` or `results/quick/` (`*.json` raw measurements, `tables/`,
`figures/`).

## Pipeline

`src/run_all.sh` runs two stages; new experiments are added by appending their commands to
the matching block.

1. **Compute** (reads `data/`, writes `results/<mode>/*.json`):
   - `compute_baseline.py`: exact FAISS search, agreement check against the stored
     neighbours (full mode only), batch and one-query-at-a-time timing. Run twice: default
     threads (`baseline.json`) and 1 thread, k' = 20 (`baseline_1thread.json`, the exact
     point compared with the ANN indexes).
   - `compute_sweeps.py`: HNSW / IVF-Flat / IVF-PQ parameter sweeps on both datasets
     (`sweeps.json`).
   - `compute_scaling.py`: SIFT at 100k / 300k / 1M (quick: 100k) for every HNSW and
     IVF-Flat config plus exact search (`scaling.json`).
2. **Report** (`make_report.py`, reads `results/` only): markdown tables and PNG figures.

## Code layout

| path | contents |
|---|---|
| `src/annbench/data.py` | download, HDF5 loading, query split, normalisation, `--quick` subset |
| `src/annbench/exact.py` | `FaissExact`: `build(base)` / `search(queries, k) -> (ids, dists)` |
| `src/annbench/indexes.py` | `FaissHNSW`, `FaissIVFFlat`, `FaissIVFPQ` (same interface), `index_size_bytes` |
| `src/annbench/recall.py` | `recall_at_k` with tie handling at the k-th place |
| `src/annbench/agreement.py` | `neighbours_agree`: tie-aware check against stored neighbours |
| `src/annbench/timing.py` | batch / one-at-a-time / build timing, `faiss_threads` |
| `src/annbench/metrics.py` | `latency_summary`, `qps` |
| `src/annbench/sweeps.py` | `curve_area`, `best_at_recall`, `top_build_configs`, `points` |
| `src/annbench/tables.py` | markdown tables from result records |
| `src/annbench/results_io.py` | results JSON save/load, run metadata |
| `src/compute_*.py`, `src/make_report.py` | stage entry points (wiring only) |
| `src/run_all.sh` | the full pipeline |
| `tests/` | one test file per module |

## Development

```bash
uv run pytest -q                        # unit tests (slow ones skipped by default)
uv run pytest -q -m "slow or not slow"  # include slow tests
uv run ruff check .                     # lint
uv run ruff format .                    # format
```

macOS + iCloud-synced folder: if `import annbench` fails outside pytest, run
`chflags nohidden .venv/lib/python3.12/site-packages/*.pth`.
