# Session 2026-10-28: single-query QPS column (continues 2026-10-26-recall.md)

## 2026-10-28 — RED, table: single QPS column

- Prompt: "the table has only batch qps what about one at a time?" -> proposed column + test
  change; human: "start with the test"
- Spec: "Baseline:" line 15 (time one at a time and in batch); "IMPORTANT" line 4 (tables).
  SPEC.md unchanged (35 lines, same hash); lines 16-35 still deferred.
- Files touched: tests/test_tables.py (human-approved change to existing assertion)
- Summary: test_baseline_table_renders_header_and_one_row now expects a "single QPS" column
  after batch QPS (value 20 = 100 latencies / 5.05 s) and a 9-column separator.
  Fails at header line. 23 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, table: single QPS column

- Prompt: "ok"
- Spec: "Baseline:" line 15; "IMPORTANT" line 4
- Files touched: src/annbench/tables.py, README.md (table column list)
- Summary: single_qps = qps(len(latencies_s), sum(latencies_s)); header, separator, row
  updated. 24 passed, ruff clean. Rebuilt via --report-only (no recompute):
  full sift 57 / glove 54 single QPS (vs 2240 / 2100 batch); quick sift 600 / glove 714.
- Status: awaiting approval
- Outcome: approved implicitly; next prompt moved on

## 2026-10-28 — SPEC CLARIFICATION + PLAN (lines 16-35)

- Prompt: "let's work on the TODO. need a new plan. let's work out the ambiguities first"
- Spec: "Benchmarks:" (17-25), "Experiments on standard data:" (27-35). SPEC.md unchanged.
- Files touched: AI_LOGS/plans/2026-10-28-benchmarks.md (new), AI_LOGS/PROGRESS.md
  (spec read up to 35; rows point to plan)
- Answers (AskUserQuestion): FAISS for all; recall by IDs vs exact top-K + ties (supersedes
  found_dists design); single-query QPS for plot/table; --quick = smaller sweeps, 100k only;
  1 FAISS thread for single-query timing (re-time baseline); tune on first 5000, report on
  last 5000; QPS@recall = best measured config reaching it; hypothesis -> README + git commit.
- Plan: 24 steps (hypothesis+commit, recall rework, 3 wrappers, size, threads, build time,
  pareto/best/top, compute stages, tables, plots, scaling, glue). Proposed grids/defaults
  listed as unconfirmed; one open point (IVF nlist fixed vs scaled in scaling run).
- Status: awaiting approval
- Outcome: change request: "the recall function is misspecified: what i need is that if found
  distances are 0.1 0.2 0.2 0.2, and k = 2, said the third place retrieved index is actually
  in the top 10 GT, don't flag that as not-retrieved."

## 2026-10-28 — PLAN revision (recall definition)

- Prompt: (above)
- Files touched: AI_LOGS/plans/2026-10-28-benchmarks.md (recall decision, section B, HNSW grid)
- Summary: confirmed reading with worked example; answers: search k' = 20, GT = exact top-10
  ids only, IVF-PQ reported dists used as-is. Recall = |GT top-k ∩ {found with dist <= k-th
  found dist (1+rtol)}| / k; signature (found_ids, found_dists, gt_ids, k). efSearch 16
  dropped (must be >= 20). All searches incl. re-timed baseline at k' = 20.
- Status: awaiting approval (plan + nlist question still open)
- Outcome: "make sure tables don't overwrite others, explain problem 1 and 2 and 3 seem fine."
  -> explained nlist fixed vs sqrt(n); human: "do B for the sweep then for the later plots,
  best config should be picked"

## 2026-10-28 — PLAN approved + step 1 (README hypothesis)

- Prompt: "do B for the sweep then for the later plots, best config should be picked"
- Spec: "Experiments on standard data:" line 28-33
- Files touched: plan (status approved; IVF grid over c with nlist = round(c*sqrt(n));
  scaling picks best config per index/size; unique output names; baseline_1thread files),
  README.md (new "## Experiments" section with spec lines 30-32 copied byte-for-byte;
  diff vs spec: identical)
- Summary: doc-only. 24 passed. Prepared first commit: 39 files, none ignored-type.
  Awaiting OK on file list + message before committing.
- Status: awaiting approval
