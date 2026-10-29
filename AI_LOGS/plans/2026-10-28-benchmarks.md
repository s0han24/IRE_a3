# Plan: ANN benchmarks (SPEC "Benchmarks:" + "Experiments on standard data:", lines 16-35)

Status: approved 2026-10-28 (human: "2 and 3 seem fine", nlist option B). Spec read up to line 35.

## Decisions (human, 2026-10-28)
- Library: FAISS for all three: IndexHNSWFlat, IndexIVFFlat, IndexIVFPQ. Same
  `build(base)` / `search(queries, k) -> (ids, dists)` interface as `FaissExact`.
- Recall (revised by human 2026-10-28, supersedes both the 2026-10-26 found_dists design
  and the first version of this plan): ties are handled on the FOUND side. Each index
  returns k' = 2k = 20 results. Found set = found ids whose reported distance <= the k-th
  found distance * (1 + rtol). hits = |exact top-10 ids ∩ found set|; recall = hits / k.
  Example: found dists 0.1 0.2 0.2 0.2, k = 2: the 3rd/4th results tie the 2nd, so a GT
  id at found position 3 is a hit. Signature: `recall_at_k(found_ids, found_dists, gt_ids,
  k)`. GT = FaissExact's exact top-10 ids (no GT-side ties). Reported distances are used
  as-is, including IVF-PQ's approximate ones (documented caveat). All searches, including
  the re-timed exact baseline, use k' = 20.
- QPS: single-query QPS (one query per call) for the plot and the QPS@recall table.
- Threads: FAISS set to 1 thread during single-query timing for every index AND the exact
  baseline; baseline single-query timing is re-done that way. Thread count recorded in meta.
- Query halves: sweeps select on the tuning queries (first 5000); every plotted / tabled
  number is measured on the report queries (last 5000).
- QPS at recall r: best measured config with report recall >= r (config named); no
  interpolation. No config reaching 0.95 -> flagged in the table and stdout.
- `--quick`: smaller sweep grids on the 100k subset; scaling experiment at 100k only.
- Hypothesis: written verbatim to README, then the repo's first git commit, before any
  experiment code.

## Proposed defaults (not yet confirmed; change any)
- Grids, full mode (quick mode in brackets). IVF nlist is set as nlist = round(c * sqrt(n))
  (human 2026-10-28, option B), so the sweep grid is over c:
  - HNSW: M in {16, 32} [{16}], efConstruction 200, efSearch in {32, 64, 128, 256, 512}
    (>= k' = 20).
  - IVF-Flat: c in {1, 4} [{1}] (1M: nlist 1000 / 4000), nprobe in {1, 2, 4, 8, 16, 32, 64,
    128}.
  - IVF-PQ: c = 4 [1], m = d/2 (SIFT 64, GloVe 50) and d/4 (32, 25) [d/2 only], nbits 8,
    nprobe in {1, 2, 4, 8, 16, 32, 64, 128, 256}. No re-ranking: 0.95 may be unreachable
    for PQ, which the spec says to flag rather than work around.
- Build time: wall time of train + add. Index size: `len(faiss.serialize_index(index))`.
  Bytes per vector: size / n_base.
- Seeds: FAISS k-means and HNSW level assignment seeded and recorded.
- Scaling (SIFT 100k / 300k / 1M, first n vectors): run the best 3 configs per index at report
  recall >= 0.95 from the 1M sweep (HNSW: M, efSearch; IVF-Flat: c, nprobe, so nlist
  follows sqrt(n) at each size), plus exact. GT recomputed per size. Plots/tables show, per
  index and size, the best config: highest single-query QPS among those still reaching 0.95
  at that size (named). A size where none of the 3 reaches 0.95 is flagged.
- Output files: every table and figure has its own file name; nothing overwrites another.
  The 1-thread baseline re-time writes `baseline_1thread.json` / `tables/baseline_1thread.md`;
  the existing 8-thread `baseline.json` / `baseline.md` stay.

## Steps (each RED -> GREEN unless marked WIRING)

### A. Hypothesis first (spec line 28)
1. README: add a `### Hypothesis` section with the spec text verbatim. (doc only)
2. First git commit of the current tree (data/ and results/ stay ignored). Show file list
   and message first.

### B. Recall with found-side ties (spec line 18)
3. Show old -> new assertions for the 2 existing recall tests (new signature); on approval,
   RED: no-ties case.
4. A found id beyond position k, tied with the k-th found distance and in GT top-k, is a hit
   (the 0.1 0.2 0.2 0.2 example).
5. ~~Float-noise tie on the found side (rtol) still extends the set; a real gap does not.~~
   Covered by the rewritten test_recall_at_k_float_noise_at_kth_is_hit (human: "ok").

### C. Index wrappers (spec line 19), one per cycle, property tests on rng data
   (n=1000, d=16, seed fixed): shape (nq, k), ids in range, no duplicates, recall >= 0.9
   at generous params (IVF-PQ: looser threshold).
6. `FaissHNSW(M, ef_construction)` + `set_search(ef_search)`.
7. `FaissIVFFlat(nlist)` + `set_search(nprobe)`.
8. `FaissIVFPQ(nlist, m, nbits)` + `set_search(nprobe)`.
9. `index_size_bytes(wrapper)`: Flat index on known data -> ~ n*d*4 bytes.

### D. Timing and threads
10. `faiss_threads(n)` context manager: sets and restores `omp` thread count.
11. `time_build(build_fn, clock)` with fake clock.

### E. Sweep analysis (pure functions, hand-made records)
   (Revised 2026-10-28, human: "just estimate area under the tradeoff curve and take the
   best few according to that"; replaces the Pareto-front step.)
   A curve = one build config (HNSW: M; IVF-Flat: c; IVF-PQ: c, m) swept over its search
   parameter. Area = trapezoid area of log10(QPS) over recall, using only points with
   recall >= 0.5 (sorted by recall). Higher area = better trade-off.
12. `curve_area(recalls, qps)`.
13. `best_at_recall(records, target)` -> highest-QPS record with recall >= target, or None
    (flag). Used for the QPS@0.9/0.95 table and the build-cost table.
14. `top_build_configs(records, n)` -> the n build configs with the largest curve area.
    Used to pick which curve per index goes on the recall-QPS plot (best 1) and which
    configs go into the scaling run (best 3, search parameter re-swept at each size).

### F. Compute stage
15. WIRING: `compute_baseline.py --threads 1` single-query timing under `faiss_threads(1)`,
    k' = 20 -> `baseline_1thread.json` (existing 8-thread results kept); re-run.
16. WIRING: `compute_sweeps.py`: per dataset / index / build params: build (timed, size);
    per search param: tune recall, report recall, report single-query latencies.
    -> `results/<mode>/sweeps.json`. Flags any index without a 0.95 config.
17. Ask, then run `--quick`; ask, then run full (estimate given at that point).

### G. Report stage
18. `qps_at_recall_table(records, [0.9, 0.95])` (pure, tested).
19. `build_cost_table(records)` at each index's best 0.95 config (pure, tested).
20. WIRING: recall@10 vs single-query QPS plot per dataset, every index + exact point.

### H. Scaling experiment (spec line 35)
21. WIRING: `compute_scaling.py`: SIFT at 100k / 300k / 1M (quick: 100k), best 3 configs
    per index from the sweep + exact -> `results/<mode>/scaling.json`.
22. `scaling_table(records)` (pure, tested) + WIRING plot of cost vs n.

### I. Glue
23. `run_all.sh`: append sweeps + scaling to stage 1, new tables/plots to stage 2.
24. README: new pipeline steps, outputs, runtimes.

Status 2026-10-28 (late): steps 18-24 written in one go at human request ("these will not
have exact tests anyway, just give me the code at once"): tables (qps_at_recall,
build_cost, scaling) + sweeps.points without unit tests; compute_scaling.py; plots in
make_report.py; run_all.sh stage 1 extended; README updated. Verified on --quick data only.
Full sweep + full scaling NOT run (human: "don't run the full sweep for now").

## Addendum 2026-10-29: spec lines 22 (median of repeats) and 36 (all configs)
Decisions (human: "your recommendations are fine"): r = 3 repeats; single-query timing =
per-query median latency over r full passes; batch = median of r batch times; build time
measured once (documented); exact baseline timings also use r; JSON stores medians + r.
25. RED/GREEN: time_one_at_a_time(..., repeats) -> per-query median over repeats passes.
26. RED/GREEN: time_batch(..., repeats) -> median of repeats batch times.
27. WIRING: repeats=3 in compute_baseline / compute_sweeps / compute_scaling, r in meta;
    compute_scaling uses every HNSW and IVF-Flat build (TOP_N dropped).
28. WIRING: recall_vs_qps plot draws every build (best emphasised) so table configs appear.
29. README: medians, all-configs scaling, stale runtime + thread-count passages, results
    section vs hypothesis (after the re-run). PROGRESS refresh.
30. RUN (ask first): run_all.sh --quick timed; then full; then commit results.
