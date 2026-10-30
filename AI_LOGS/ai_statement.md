# AI use statement

AI tool used: Claude Opus 5.5 (Claude Code), working from a human-written specification
(`AI_LOGS/SPEC.md`) in small test-driven steps. Every step was reviewed and approved by the
human before the next one. Prompts and summarised responses for each step are in
`sessions/`; approved multi-step plans are in `plans/`.

Labels: **human-written**, **AI-assisted** (AI draft, substantially edited by the human),
**AI-generated** (written by the AI, reviewed line by line by the human).

| file | label |
|---|---|
| `AI_LOGS/SPEC.md` | human-written |
| `README.md`: hypotheses (copied verbatim from SPEC) | human-written |
| `README.md`: everything else | AI-generated |
| `CLAUDE.md` (agent instructions) | human-written |
| `report/report.tex` | AI-assisted |
| `code/run_all.sh` | AI-generated |
| `code/requirements.txt` | AI-generated (exported from `uv.lock`) |
| `pyproject.toml` | AI-generated |
| `code/src/annbench/agreement.py` | AI-generated |
| `code/src/annbench/data.py` | AI-generated |
| `code/src/annbench/drift.py` | AI-generated |
| `code/src/annbench/exact.py` | AI-generated |
| `code/src/annbench/indexes.py` | AI-generated |
| `code/src/annbench/metrics.py` | AI-generated |
| `code/src/annbench/recall.py` | AI-generated |
| `code/src/annbench/results_io.py` | AI-generated |
| `code/src/annbench/sweeps.py` | AI-generated |
| `code/src/annbench/tables.py` | AI-generated |
| `code/src/annbench/timing.py` | AI-generated |
| `code/src/annbench/__init__.py` | AI-generated |
| `code/src/compute_baseline.py` | AI-generated |
| `code/src/compute_drift.py` | AI-generated |
| `code/src/compute_scaling.py` | AI-generated |
| `code/src/compute_sweeps.py` | AI-generated |
| `code/src/make_report.py` | AI-generated |
| `code/tests/*.py` (all 11 test files) | AI-generated |
| `AI_LOGS/PROGRESS.md`, `AI_LOGS/plans/*`, `AI_LOGS/sessions/*` | AI-generated |
