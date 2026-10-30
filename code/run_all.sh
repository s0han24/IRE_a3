#!/usr/bin/env bash
# Full pipeline: regenerates every number, figure and table in the report.
#   bash run_all.sh                 # full datasets
#   bash run_all.sh --quick         # first 100,000 base vectors per dataset (< 15 min)
#   bash run_all.sh --report-only   # skip stage 1; re-make tables/figures from results/
# Flags combine, e.g. --quick --report-only.
# Can be run from anywhere: it first changes to the repo root, so paths below are
# relative to it. Append new pipeline commands to the matching stage block.
set -euo pipefail
cd "$(dirname "$0")/.."

QUICK=""
REPORT_ONLY=0
for arg in "$@"; do
    case "$arg" in
        --quick) QUICK="--quick" ;;
        --report-only) REPORT_ONLY=1 ;;
        *) echo "unknown argument: $arg" >&2; exit 2 ;;
    esac
done

# ---- Stage 1: compute (reads data/, writes results/<mode>/*.json) ----
if [[ "$REPORT_ONLY" == 0 ]]; then
    uv run python code/src/compute_baseline.py $QUICK            # baseline check (default threads)
    uv run python code/src/compute_baseline.py $QUICK --threads 1 --k-search 20  # exact ANN point
    uv run python code/src/compute_sweeps.py $QUICK              # HNSW / IVF-Flat / IVF-PQ sweeps
    uv run python code/src/compute_scaling.py $QUICK             # needs the two lines above
    uv run python code/src/compute_drift.py $QUICK               # SIFT drift (300k; quick 50k)
fi

# ---- Stage 2: report (reads results/ only, writes tables and figures) ----
uv run python code/src/make_report.py $QUICK
