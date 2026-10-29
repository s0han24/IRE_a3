# Session 2026-10-29: commit everything incl. results (continues 2026-10-28-single-qps.md)

## 2026-10-29 — COMMIT

- Prompt: "commit everything, don't ignore results, the files are small enough to commit"
- Spec: unchanged (35 lines, same hash).
- Found on disk: results/full/{baseline,baseline_1thread,sweeps,scaling}.json and full
  tables/figures, written 2026-10-29 ~10:19-10:47 local by a run outside this agent session
  (meta timestamps 04:49-05:13 UTC; scaling covers 100k/300k/1M). Not run by the agent.
- Files touched: .gitignore (results/ no longer ignored; data/ still ignored), this log.
- Summary: results/ is 36 MB, largest file 13.8 MB (full sweeps.json). Committed all
  pending code, tests, docs, AI_LOGS and results/. README runtime line and PROGRESS still
  say the full sweep was not run (stale; flagged to human, not edited).
- Outcome: committed as 7f15295. Human: "let's move on. check the completion of all specs"

## 2026-10-29 — SPEC COMPLETION CHECK (read-only, no code changed)

- Prompt: "let's move on. check the completion of all specs"
- Spec: lines 1-35 (unchanged)
- Files touched: this log only
- Summary: checked each spec line against code, committed results/full and figures.
  Done: datasets, split, GloVe normalisation, FAISS exact, recall@10 + tests, agreement
  (True both, all 10000), timing, 3 indexes swept on both datasets, flags (IVF-PQ both,
  IVF-Flat GloVe 0.949), QPS@0.9/0.95 table, build-cost table, scaling 100k/300k/1M,
  hypothesis committed before experiment code.
  Gaps found: (1) recall_vs_qps plot picks one build per index by tune-curve area, which on
  GloVe shows HNSW M=16 (max 0.92) while the table's 0.95 config is M=32; SIFT shows
  ivf_flat c=1 while table uses c=4. (2) `run_all.sh --quick` never run end-to-end with all
  steps (components ~4 min). (3) README full runtime "not yet measured" and thread-count
  note (1-thread slower) contradicted by today's results (1-thread 102 vs default 59 QPS).
  (4) No written analysis of scaling vs hypothesis / no report document. (5) "best few":
  grid has only 2 builds per index, so scaling uses 2. (6) PROGRESS.md stale.
- Status: reported to human

## 2026-10-29 — SPEC UPDATE (line 22 inserted, line 36 edited), no code

- Prompt: "Made a mistake, check the SPEC"
- Spec: 35 -> 36 lines (md5 cc9532cd...). Edited in place, not appended: new line 22 "Repeat
  each timing a few times and take the median"; line 36 "best few hyperparameter configs"
  -> "all the hyperparameter configs".
- Files touched: this log only
- Summary: reported SPEC UPDATE; questions on repeat count, what the median is taken over,
  whether build time and the exact baseline are included, raw-latency storage size, and the
  --quick 15-min budget.
- Status: awaiting human confirmation
- Outcome: confirmed: "your recommendations are fine, go with those"
- PROGRESS: spec read up to 36; new rows for line 22 and line 36, old line 36 superseded.
  Plan addendum (steps 25-30) appended to 2026-10-28-benchmarks.md.

## 2026-10-29 — RED, plan step 25 (single-query repeats)

- Prompt: "your recommendations are fine, go with those"
- Spec: "Benchmarks:" line 22
- Files touched: tests/test_timing.py, src/annbench/timing.py (stub: `repeats=1` param +
  docstring, behaviour unchanged)
- Summary: test_time_one_at_a_time_repeats_passes_and_takes_per_query_median: 2 queries,
  3 passes, fake clock deltas q0 1/5/2, q1 4/3/9 -> [2, 4], 6 calls. Fails: 2 calls != 6.
  Existing single-pass test unchanged (default repeats=1). 37 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-29 — GREEN, plan step 25

- Prompt: "ok"
- Files touched: src/annbench/timing.py
- Summary: (repeats, nq) latency array filled pass by pass; np.median(axis=0). 38 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-29 — RED, plan step 26 (batch repeats)

- Prompt: "ok"
- Files touched: tests/test_timing.py, src/annbench/timing.py (stub: `repeats=1` + docstring)
- Summary: test_time_batch_repeats_and_takes_median: batch times 4, 1, 2 -> 2.0, 3 calls on
  the full array. Fails on call count.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-29 — GREEN, plan step 26

- Prompt: "ok"
- Files touched: src/annbench/timing.py
- Summary: loop `repeats` timed calls, return float(np.median(times)). 39 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-29 — WIRING, plan step 27 (median timings in scripts, all configs in scaling)

- Prompt: "ok"
- Spec: "Benchmarks:" line 22; "Experiments on standard data:" line 36
- Files touched: src/compute_baseline.py (REPEATS = 3, passed to time_batch and
  time_one_at_a_time, timing_repeats in meta), src/compute_sweeps.py (REPEATS to single-query
  timing, meta), src/compute_scaling.py (REPEATS; TOP_N + top_build_configs selection removed,
  every HNSW / IVF-Flat build used; docstring; meta top_n -> timing_repeats)
- Summary: 39 passed, ruff clean, all three scripts import (--help). Not run. Existing
  results are now stale w.r.t. line 22 until re-run.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-29 — WIRING, plan step 28 (plot every build)

- Prompt: "ok"
- Spec: "Benchmarks:" line 24 (plot per dataset, every index + exact)
- Files touched: src/make_report.py (plot_recall_vs_qps: all builds per index, ranked by
  tune-recall curve area; best solid/large markers "(best area)", others dashed, thinner,
  alpha 0.6, same colour + marker)
- Summary: re-rendered full + quick figures from existing results (no recompute). Checked by
  eye: GloVe HNSW M=32 (reaches 0.965) and SIFT IVF-Flat c=4 now visible; legend lower-left
  clear of curves. 39 passed, ruff clean.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-29 — DOC, plan step 29 (README + PROGRESS)

- Prompt: "ok"
- Files touched: README.md (runtime table: measured ~4 min / ~28 min single-timing, 3-repeat
  estimates; new "Timing" paragraph: median of 3, per-query medians, builds once; thread-count
  note rewritten as measured on both days, not explained; scaling = all builds; plot = all
  builds with "best area" solid; results/ committed, data/ ignored), AI_LOGS/PROGRESS.md
  (rows for 4, 17-25, 22, 27-35, 36 refreshed)
- Summary: doc only. Results section vs hypothesis deferred until after the median re-run.
- Status: awaiting approval
- Outcome: "skip the quick run, only do the full one"

## 2026-10-29 — RUN, plan step 30 (full run_all.sh, 3 repeats) — started

- Prompt: "skip the quick run, only do the full one"
- Summary: spec unchanged (36 lines). Started `cd src && bash run_all.sh` in background
  (log: session scratchpad full_run_r3.log). --quick re-run skipped by human; quick results
  stay single-timing.
- Status: running
- Result: exit 0, wall 3249 s (54 min). All four full files have timing_repeats = 3;
  agreement True on both datasets (both baseline runs). Tables/figures regenerated 12:12.
  FLAGs: IVF-PQ both datasets, IVF-Flat GloVe (0.949). Scaling 100k/300k/1M QPS @ >=0.95:
  exact 593/242/70, HNSW 13192/12703/8190, IVF-Flat 13678/6261/3578.

## 2026-10-29 — SPEC COMPLETION CHECK (after median re-run), no code changed

- Prompt: "check completion"
- Spec: 36 lines, unchanged.
- Summary: all spec lines met for full mode. Open: (1) results/quick not re-run (single
  timings, human skipped it), so --quick under 15 min with 3 repeats is unverified and quick
  outputs don't follow line 22; (2) README runtime table still shows estimates (full now
  measured 54 min) and thread-count note lacks today's third run (1-thread faster again:
  70 vs 58, 62 vs 41); (3) no results section vs hypothesis; (4) new results + code
  uncommitted.
- Status: reported to human

## 2026-10-29 — SPEC COMPLETION CHECK #3, no code changed

- Prompt: "cool another check for completion now"
- Spec: 36 lines, unchanged (uncommitted edits to lines 22/36 still only in working tree).
- Found: human commit e8bad55 (AI use statement in README); results/quick re-run by human
  with timing_repeats = 3 (files 14:23:55-14:28:05 local; start time not recorded, ~5 min).
  Quick QPS ~2x higher than the 10-28 quick run (exact 487 -> 998, HNSW 12027 -> 24551);
  full-run exact at 100k (593) vs quick exact (998) disagree by 1.7x: large cross-run
  variance.
- Open: README runtime table + thread note stale; no results section; nothing committed
  since e8bad55; README AI statement says "TDD was followed" but steps 18-24 and wiring
  were not TDD (by request).
- Status: reported to human
- Outcome: "drop the things that don't agree. keep the README lean. It only needs info about
  HOW to run and what the structure of the code is. No need for additional stuff that the
  AI LOGS may already cover"

## 2026-10-29 — DOC: README trimmed (212 -> 85 lines)

- Prompt: (above)
- Files touched: README.md
- Summary: kept title, human's AI-use statement (untouched), hypothesis (spec line 30 requires
  it; verbatim vs spec 31-33), setup, running (both modes, --report-only, measured ~55 / ~5
  min), short pipeline description (spec line 4 requires one), code layout, dev commands,
  one-line macOS fix. Dropped: thread-count note (contradicted across runs), timing details,
  JSON example, sweep grid, recall definition, output list detail, stale estimates. Not
  committed.
- Status: awaiting review
- Outcome: "commit this now"

## 2026-10-29 — COMMIT

- Prompt: "commit this now"
- Summary: committed all pending changes (code, tests, human's SPEC.md edits, full + quick
  results with 3 repeats, README, AI_LOGS). data/ stays ignored.
- Outcome: committed as 0c968a4.

## 2026-10-29 — SPEC UPDATE (lines 37-64 appended: "Experiments on drifted data:"), no code

- Prompt: "check out the SPECs now"
- Spec: 36 -> 64 lines (md5 f95e682d...), appended at the bottom.
- Files touched: this log only
- Summary: reported SPEC UPDATE with questions (which recall decides "loses 0.95 first",
  rotation angle per pair, clean curve re-measured in same run, --quick budget, stale build
  numbers, README hypothesis vs lean README). Noted: both drifts are distance-preserving
  when applied to base and queries, so "rebuilt" should reproduce "clean" up to float effects.
- Status: awaiting human confirmation
