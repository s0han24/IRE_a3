#!/usr/bin/env bash
# Full pipeline: regenerates every number, figure and table in the report.
#   bash run_all.sh                 # full datasets
#   bash run_all.sh --quick         # first 100,000 base vectors per dataset (< 15 min)
#   bash run_all.sh --report-only   # skip stage 1; re-make tables/figures from results/
# Flags combine, e.g. --quick --report-only.
# Run from src/ (or anywhere): paths below are relative to the repo root.
# Append new pipeline commands to the matching stage block.
set -euo pipefail

QUICK=""
REPORT_ONLY=0
for arg in "$@"; do
    case "$arg" in
        --quick) QUICK="--quick" ;;
        --report-only) REPORT_ONLY=1 ;;
        *) echo "unknown argument: $arg" >&2; exit 2 ;;
    esac
done

cd "$(dirname "$0")/.."

# ---- Stage 1: compute (reads data/, writes results/<mode>/*.json) ----
if [[ "$REPORT_ONLY" == 0 ]]; then
    uv run python src/compute_baseline.py $QUICK
fi

# ---- Stage 2: report (reads results/ only, writes tables and figures) ----
uv run python src/make_report.py $QUICK
