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
- Correction: dry-run file count is 37, not 39 as written above.
- Outcome: approved ("ok")

## 2026-10-28 — plan step 2: first git commit

- Prompt: "ok"
- Files touched: none (commit only)
- Summary: commit 213015d on main, 37 files, 2912 insertions, author s0han24. data/,
  results/, .venv, caches excluded by .gitignore. Hypothesis is in this commit, before any
  ANN experiment code. (This log entry itself is written after the commit, so uncommitted.)
- Status: done
- (step 3 proposal: old -> new recall assertions shown) Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 3 (recall with found-side ties)

- Prompt: "ok"
- Spec: "Benchmarks:" line 18 + "Baseline:" line 13 (recall@10 with ties)
- Files touched: tests/test_recall.py (both tests rewritten to the new signature, as approved;
  one comment split for E501), src/annbench/recall.py (new signature, stub returns 0.0)
- Summary: recall_at_k(found_ids, found_dists, gt_ids, k, rtol). Expectations unchanged
  (0.75, 0.5). Both fail on assertion (0.0). 22 passed, 2 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 3

- Prompt: "ok"
- Spec: "Benchmarks:" line 18, "Baseline:" line 13
- Files touched: src/annbench/recall.py, AI_LOGS/PROGRESS.md
- Summary: d_k = found_dists[:, k-1] * (1+rtol); retrieved = found_dists <= d_k; in_gt via
  (nq, k', k) id comparison; recall = mean(sum(retrieved & in_gt)) / k. 24 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — TEST, plan step 4 (passes on arrival, as announced)

- Prompt: "ok"
- Spec: "Benchmarks:" line 18 (human's 0.1 0.2 0.2 0.2 example)
- Files touched: tests/test_recall.py
- Summary: test_recall_at_k_found_tie_beyond_kth_is_hit: GT id at found place 3, tied with
  the 2nd -> recall 1.0. Passes on arrival; plain top-k rule would give 0.5 (checked).
  25 passed.
- Status: awaiting approval
- Outcome: approved ("ok"); step 5 marked covered by the rewritten float-noise test

## 2026-10-28 — RED, plan step 6 (FaissHNSW)

- Prompt: "ok"
- Spec: "Benchmarks:" line 19 (HNSW)
- Files touched: tests/test_indexes.py (new), src/annbench/indexes.py (new; FaissHNSW stub
  returning zeros), plan (step 5 struck as covered)
- Summary: test_faiss_hnsw_returns_valid_neighbours_with_high_recall: rng(0) base 1000x16,
  50 queries, M=16 efC=100 efS=64, k'=20: shape, ids in range, no duplicates, ascending
  dists, recall@10 >= 0.9 vs FaissExact. Fails at the duplicates check (all-zero ids).
  25 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 6

- Prompt: "ok"
- Spec: "Benchmarks:" line 19
- Files touched: src/annbench/indexes.py, AI_LOGS/PROGRESS.md
- Summary: IndexHNSWFlat(d, M), efConstruction set before add; set_search sets efSearch;
  search returns (ids, sqrt(sq)). 26 passed. Ad-hoc on the test data: efSearch 20/32/64 ->
  recall 0.994 / 0.998 / 1.0 (threshold 0.9 is loose, as intended).
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 7 (FaissIVFFlat)

- Prompt: "ok"
- Spec: "Benchmarks:" line 19 (IVF-Flat)
- Files touched: tests/test_indexes.py, src/annbench/indexes.py (FaissIVFFlat stub zeros)
- Summary: test_faiss_ivf_flat_returns_valid_neighbours_with_high_recall: same data and
  property assertions, nlist=16, nprobe=8. Fails at duplicates check. 26 passed, 1 failed.
  Assertion block now duplicated across 2 tests (candidate REFACTOR after GREEN).
- Status: awaiting approval
- Outcome: "seems like a repeat, REFACTOR the tests" (requested mid-RED)

## 2026-10-28 — REFACTOR (tests only, during RED step 7)

- Prompt: "seems like a repeat, REFACTOR the tests"
- Spec: "Benchmarks:" line 19
- Files touched: tests/test_indexes.py
- Summary: two copy-pasted property tests -> one @pytest.mark.parametrize test over builder
  functions hnsw() / ivf_flat(); assertions unchanged. Outcomes unchanged: [hnsw] passes,
  [ivf_flat] still fails at the duplicates check (stub). 26 passed, 1 failed.
  Test ids renamed: test_faiss_hnsw_... / test_faiss_ivf_flat_... ->
  test_index_returns_valid_neighbours_with_high_recall[hnsw|ivf_flat].
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 7

- Prompt: "ok"
- Spec: "Benchmarks:" line 19
- Files touched: src/annbench/indexes.py, AI_LOGS/PROGRESS.md
- Summary: IndexIVFFlat(IndexFlatL2(d) kept on self, d, nlist); train + add; nprobe;
  (ids, sqrt). 27 passed. Ad-hoc nprobe 1/2/4/8/16 -> recall .356/.526/.778/.936/1.0, no
  -1 padding. Flagged: test's nprobe=8 leaves only 0.036 margin over 0.9.
- Status: awaiting approval
- Outcome: approved ("ok"), incl. raising ivf_flat test nprobe 8 -> 12

## 2026-10-28 — TEST tweak + RED, plan step 8 (FaissIVFPQ)

- Prompt: "ok"
- Spec: "Benchmarks:" line 19 (IVF-PQ)
- Files touched: tests/test_indexes.py (ivf_flat nprobe 8 -> 12, human-approved: recall
  0.936 -> 0.99; parametrize now (make_index, min_recall); new ivf_pq case at 0.5),
  src/annbench/indexes.py (FaissIVFPQ stub zeros)
- Summary: probed PQ on test data: m=8 nbits=4 -> 0.712 (no FAISS training warning);
  nbits=8 -> 0.928 but warns (needs 9984 training points). Chose m=8 nbits=4 nlist=16
  nprobe=16, threshold 0.5. [hnsw], [ivf_flat] pass; [ivf_pq] fails at duplicates check.
  27 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 8

- Prompt: "ok"
- Spec: "Benchmarks:" line 19
- Files touched: src/annbench/indexes.py, AI_LOGS/PROGRESS.md
- Summary: IndexIVFPQ(IndexFlatL2(d) kept on self, d, nlist, m, nbits); train + add;
  nprobe; (ids, sqrt of approximate sq dists). 28 passed, no FAISS training warnings.
- Status: awaiting approval
- Outcome: "ok" (read as yes to the proposed wrapper REFACTOR)

## 2026-10-28 — REFACTOR, index wrappers

- Prompt: "ok"
- Spec: "Benchmarks:" line 19
- Files touched: src/annbench/indexes.py (99 -> 86 lines)
- Summary: _FaissWrapper holds the shared search (ids, sqrt); _FaissIVF holds the shared
  quantizer + train/add build and set_search(nprobe); FaissIVFFlat / FaissIVFPQ only define
  _make_index. Public classes/signatures unchanged; FaissExact (exact.py) left as is to
  keep the step to one file. 28 passed, ruff clean.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 9 (index size)

- Prompt: "ok"
- Spec: "Benchmarks:" line 25 (index size, bytes per vector)
- Files touched: tests/test_indexes.py, src/annbench/indexes.py (stub index_size_bytes -> 0)
- Summary: test_index_size_bytes_of_flat_index_is_raw_vectors_plus_small_header:
  FaissExact on 1000x16 float32 -> 64,000 <= size <= 65,000. Fails: 64000 <= 0.
  28 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 9

- Prompt: "ok"
- Spec: "Benchmarks:" line 25
- Files touched: src/annbench/indexes.py, AI_LOGS/PROGRESS.md
- Summary: index_size_bytes = len(faiss.serialize_index(wrapper.index)). 29 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 10 (faiss_threads)

- Prompt: "ok"
- Spec: "Benchmarks:" line 23-24 (single-query QPS; human chose 1 FAISS thread)
- Files touched: tests/test_timing.py, src/annbench/timing.py (stub contextmanager, yields only)
- Summary: test_faiss_threads_sets_count_and_restores_it_even_on_error: inside -> 1, after
  -> previous, and previous restored after a RuntimeError in the block. Fails: 8 != 1.
  29 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 10

- Prompt: "ok"
- Spec: "Benchmarks:" lines 23-24
- Files touched: src/annbench/timing.py, AI_LOGS/PROGRESS.md
- Summary: save omp_get_max_threads, set n, try/yield/finally restore. 30 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 11 (time_build)

- Prompt: "ok"
- Spec: "Benchmarks:" line 25 (build time)
- Files touched: tests/test_timing.py (import list reformatted by ruff), src/annbench/timing.py
  (stub time_build: calls build, returns 0.0)
- Summary: test_time_build_calls_build_once_and_returns_result_and_clock_delta: fake clock
  [5.0, 7.5]; build called once, same object back, 2.5 s. Fails on seconds (0.0).
  30 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 11

- Prompt: "ok"
- Spec: "Benchmarks:" line 25
- Files touched: src/annbench/timing.py, AI_LOGS/PROGRESS.md
- Summary: t0 = clock(); result = build_fn(); return result, clock() - t0. 31 passed.
- Status: awaiting approval
- (proposed pareto_front definition) Outcome: replaced by human: "that's complicated. just
  estimate area under the tradeoff curve and take the best few according to that";
  answers: one curve per build config; area = log10 QPS over recall [0.5, 1]

## 2026-10-28 — PLAN revision + RED, plan step 12 (curve_area)

- Prompt: (above)
- Spec: "Benchmarks:" lines 20, 23; "Experiments on standard data:" line 35 ("best few")
- Files touched: plan (section E rewritten: curve_area, best_at_recall, top_build_configs;
  Pareto dropped), src/annbench/sweeps.py (new, stub 0.0; unused numpy import removed),
  tests/test_sweeps.py (new)
- Summary: test_curve_area_is_trapezoid_of_log10_qps_over_recall: (0.5,10), (0.75,100),
  (1.0,1000) -> 1.0. Fails 0.0. 31 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 12

- Prompt: "ok"
- Spec: "Benchmarks:" lines 20, 23
- Files touched: src/annbench/sweeps.py
- Summary: float(np.trapezoid(np.log10(qps), recalls)). 32 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 12b

- Prompt: "ok"
- Spec: "Benchmarks:" lines 20, 23 (area over recall [0.5, 1], human choice)
- Files touched: tests/test_sweeps.py
- Summary: test_curve_area_ignores_points_below_recall_half: extra (0.3, 1e5) point must not
  change the 1.0 area. Fails with 1.6.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 12b

- Prompt: "ok"
- Spec: "Benchmarks:" lines 20, 23
- Files touched: src/annbench/sweeps.py
- Summary: arrays + keep = recalls >= 0.5 before trapezoid. 33 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 12c

- Prompt: "ok"
- Spec: "Benchmarks:" lines 20, 23
- Files touched: tests/test_sweeps.py
- Summary: test_curve_area_sorts_points_by_recall: shuffled [1.0, 0.5, 0.75] -> 1.0.
  Fails with -0.625 (trapezoid walks backwards). 33 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 12c

- Prompt: "ok"
- Spec: "Benchmarks:" lines 20, 23
- Files touched: src/annbench/sweeps.py, AI_LOGS/PROGRESS.md
- Summary: filter, then argsort by recall before trapezoid. 34 passed. curve_area complete.
- Status: awaiting approval
- Outcome: "sort by qps instead of recalls" -> explained equivalence/negative-area issue;
  "qps needs to be x axis" -> proposed recall-over-log10(qps) with test changes + flagged
  range bias; human: "ok roll back"

## 2026-10-28 — ROLLBACK of proposal (no code change)

- Prompt: "ok roll back"
- Files touched: none. The qps-as-x proposal was never applied; curve_area stays as at
  GREEN 12c (log10 QPS over recall, recall >= 0.5, sorted by recall); its 3 tests unchanged.
  34 passed.
- Status: awaiting go for RED step 13
- Outcome: "ok" (fixture-realism refactor not taken up)

## 2026-10-28 — RED, plan step 13 (best_at_recall)

- Prompt: "ok"
- Spec: "Benchmarks:" lines 21, 24, 25 (QPS at recall 0.9/0.95; best config at 0.95)
- Files touched: tests/test_sweeps.py (RECORDS fixture + test), src/annbench/sweeps.py (stub)
- Summary: test_best_at_recall_is_fastest_record_reaching_target: target 0.9 -> "b".
  First stub (None) gave TypeError; changed stub to records[0] so it fails on the
  assertion ('a' != 'b'). 34 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 13

- Prompt: "ok"
- Spec: "Benchmarks:" lines 21, 24, 25
- Files touched: src/annbench/sweeps.py
- Summary: filter recall >= target, max by qps. No default yet (13b adds None). 35 passed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — RED, plan step 13b

- Prompt: "ok"
- Spec: "Benchmarks:" line 21 ("If such a config is elusive, flag it")
- Files touched: tests/test_sweeps.py
- Summary: test_best_at_recall_is_none_when_no_record_reaches_target: 0.999 -> None.
  Fails with ValueError from max() on empty (announced). 35 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 13b

- Prompt: "ok"
- Spec: "Benchmarks:" line 21
- Files touched: src/annbench/sweeps.py, AI_LOGS/PROGRESS.md
- Summary: max(..., default=None). 36 passed.
- Status: awaiting approval
- Outcome: approved ("ok"), incl. string build labels

## 2026-10-28 — RED, plan step 14 (top_build_configs)

- Prompt: "ok"
- Spec: "Benchmarks:" line 23 (plot: best curve per index); "Experiments on standard data:"
  line 35 ("best few hyperparameter configs")
- Files touched: tests/test_sweeps.py, src/annbench/sweeps.py (stub returns [])
- Summary: test_top_build_configs_ranks_builds_by_curve_area: interleaved records, A area
  0.75 > B 0.45, n=1 -> ["A"]. Fails [] != ["A"]. 36 passed, 1 failed.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — GREEN, plan step 14

- Prompt: "ok"
- Spec: "Benchmarks:" line 23; "Experiments on standard data:" line 35
- Files touched: src/annbench/sweeps.py, AI_LOGS/PROGRESS.md
- Summary: group by "build" into (recalls, qps), sort labels by curve_area desc, take n.
  37 passed. Section E complete.
- Status: awaiting approval
- Outcome: approved ("ok")

## 2026-10-28 — WIRING, plan step 15 (1-thread baseline re-time), not yet run

- Prompt: "ok"
- Spec: "Benchmarks:" line 23 (exact baseline point on the plot; single-query QPS, 1 thread)
- Files touched: src/compute_baseline.py (--threads, --k-search; single-query timing under
  faiss_threads(n); batch timing unchanged; output baseline_{n}thread.json when --threads,
  else baseline.json), src/make_report.py (renders any baseline_*thread.json to its own
  tables/<stem>.md)
- Summary: 37 passed, ruff clean, --help OK, run_all.sh --report-only OK (no new files yet).
  Existing baseline.json untouched. Not run on data.
- Status: awaiting approval to run
- Outcome: approved ("ok") to run --quick

## 2026-10-28 — RUN, plan step 15 (--quick, 1 thread, k'=20)

- Prompt: "ok"
- Files touched: none (results/quick/baseline_1thread.json + tables/baseline_1thread.md
  written; baseline.json untouched)
- Summary: exit 0, 21 s. 1-thread single QPS sift 487 (p50 2.18 ms) / glove 572 (1.66 ms) vs
  default-thread 600 / 714 -> only ~1.25x slower. Batch (default threads, k'=20) 0.357 /
  0.341 s vs 0.226 / 0.208 s at k=10. Full-run estimate ~5 min.
- Status: awaiting approval for full run
- Outcome: approved ("ok") to run full

## 2026-10-28 — RUN, plan step 15 (full, 1 thread, k'=20)

- Prompt: "ok"
- Summary: started in background (full_1thread.log in scratchpad).
- Status: running

## 2026-10-28 — DOC (README thread-count quirk), while full run is in progress

- Prompt: "mention this quirk in the README, one query at a time for baseline check doesn't
  restrict to 1 thread but it does restrict for the benchmark"
- Files touched: README.md (pipeline step 8 note: baseline.json = default threads, k=10;
  baseline_1thread.json + all ANN runs = 1 thread, k'=20; batch always default threads;
  ~1.25x on 100k; tables list adds baseline_1thread.md)
- Summary: doc only; no tests run (avoid CPU contention with the timing run).
- Status: awaiting review

## 2026-10-28 — RUN restart, plan step 15 (full, 1 thread, k'=20)

- Prompt: "restart, i just shut off all background processes"
- Summary: first full run had finished (exit 0, 246 s; batch 4.67 / 4.02 s, agree True both)
  but under contention from the human's other processes. Killed nothing useful (it had just
  exited). Moved its output to scratchpad baseline_1thread.contended.json; restarted the
  same command in background (full_1thread_rerun.log).
- Status: running
- Result: exit 0, 227 s. agree True both. 1-thread single QPS sift 49 (p50 20.34 ms), glove
  49 (19.63 ms) vs default-thread 57 / 54. Batch (default threads, k'=20) 3.51 / 3.81 s.
  Contended run (discarded) was worse mainly in batch (4.67 s) and GloVe tail (p99 44.6 ms).
  README note updated with full-data ratio (~1.1-1.15x). 37 passed, ruff clean. Step 15 done.
- Status: awaiting review
- Outcome: "go ahead" (write compute_sweeps.py)

## 2026-10-28 — WIRING, plan step 16 (compute_sweeps.py), not yet run

- Prompt: "go ahead"
- Spec: "Benchmarks:" lines 19-25
- Files touched: src/compute_sweeps.py (new)
- Summary: per dataset: exact GT top-10 for tune + report; per build (grid per plan,
  nlist = round(c*sqrt(n))): time_build + index_size_bytes; per search value: batch search
  tune + report (k'=20) -> recall_at_k; report queries one at a time under faiss_threads(1)
  after untimed warm-up -> raw latencies. FLAG line per index with no report recall >= 0.95.
  Saved to results/<mode>/sweeps.json after each dataset. Fixed ruff findings in my draft
  (dead duplicate block, loop-variable closures B023/F821 via functools.partial, import
  order, E501). Grid: quick 22 search configs/dataset, full 44. 37 passed. Not run.
- Status: awaiting approval to run --quick
- Outcome: approved ("ok")

## 2026-10-28 — RUN, plan step 17 (sweeps --quick)

- Prompt: "ok"
- Summary: started `uv run python -u src/compute_sweeps.py --quick` in background
  (sweeps_quick.log in scratchpad).
- Status: running
- Result: exit 0, 193 s, results/quick/sweeps.json 6.9 MB. Best report recall: SIFT hnsw
  1.000, ivf_flat 1.000, ivf_pq 0.894 (plateau); GloVe hnsw 0.978, ivf_flat 0.981, ivf_pq
  0.867. FLAG printed for ivf_pq on both datasets (spec line 21). Bytes/vec SIFT: hnsw 656,
  ivf_flat 522, ivf_pq 75 (= 64-byte codes + 8-byte id + overhead). Full estimate 30-45 min.
- Status: awaiting approval for full run
- Outcome: "write the remaining pipeline in the meanwhile" (read as: start the full run, and
  write steps 18-24 while it runs, in one go)

## 2026-10-28 — RUN, plan step 17 (sweeps full) — started

- Prompt: "write the remaining pipeline in the meanwhile"
- Summary: started `uv run python -u src/compute_sweeps.py` in background (sweeps_full.log).
- Status: running
- Outcome: human interrupted: "don't run the full sweep for now"

## 2026-10-28 — RUN stopped (sweeps full)

- Prompt: "don't run the full sweep for now"
- Summary: killed compute_sweeps.py (exit 144) while still building/sweeping SIFT; nothing
  had been printed or saved, so no results/full/sweeps.json exists. Other results untouched.
  Starting it was my over-reading of "in the meanwhile"; it had not been explicitly approved.
- Status: stopped; remaining pipeline (steps 18-24) not started
- Outcome: "these will not have exact tests anyway, just give me the code at once"

## 2026-10-28 — WIRING batch, plan steps 18-24 (no unit tests, by request)

- Prompt: "these will not have exact tests anyway, just give me the code at once"
- Spec: "Benchmarks:" 18-25; "Experiments on standard data:" 35; "IMPORTANT" line 4
- Files touched: src/annbench/sweeps.py (points), src/annbench/tables.py
  (qps_at_recall_table, build_cost_table, scaling_table), src/compute_scaling.py (new),
  src/make_report.py (sweep + scaling tables, recall_vs_qps and scaling plots, shared
  style_axes), src/run_all.sh (stage 1: 1-thread baseline, sweeps, scaling), README.md
- Summary: 4-slot palette validated (contrast WARN on slots 3-4 -> legend + markers +
  tables). Quick scaling reuses sweep + baseline (0.5 s). make_report --quick writes 5 tables
  + 3 figures; full mode skips missing sweep/scaling sections. Plots checked by eye; target
  lines labelled. 37 passed, ruff clean. Fixed in own draft: duplicated save block, wrong
  run_all comment. Not run: full sweep / full scaling / full run_all.
- Status: awaiting review
