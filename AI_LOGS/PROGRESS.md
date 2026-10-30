# Progress

Spec read up to: line 66

Agents update this after each GREEN or REFACTOR step and after each confirmed spec update.
Status: todo / in progress / done / superseded (keep superseded rows; don't delete them).

| Spec item (heading, lines) | Status | Notes |
|---|---|---|
| "IMPORTANT" (4): src/run_all.sh + --quick (<15 min), README how-to + pipeline description | superseded | location overridden by line 66 |
| "IMPORTANT" (4) + line 66: code/run_all.sh + --quick (<15 min), README how-to + pipeline description | in progress | moved to code/run_all.sh 2026-10-30; --quick end-to-end not yet timed |
| "Datasets:" (7): SIFT + GloVe-100 from ann-benchmarks | done | plan F done; both files downloaded and used in full + quick runs |
| "Datasets:" (8): queries split tune [:5000] / report [5000:] | done | plan B6; split_queries in data.py |
| "Datasets:" (9, original): l2-normalise euclidean benchmarks, use cosine | superseded | line 9 edited in place |
| "Datasets:" (9, edit 2): normalise all, euclidean throughout | superseded | line 9 edited again |
| "Datasets:" (9): normalise GloVe only; euclidean throughout | done | prepare_vectors in pipeline; GloVe agreement True on full run |
| "Baseline:" (12): FAISS exact search as reference | done | FaissExact (IndexFlatL2, plain L2) used in compute_baseline.py |
| "Baseline:" (13): recall@10 from scratch, ties at 10th not misses, unit-tested | done | recall_at_k reworked 2026-10-28: ties on found side (found_ids, found_dists, gt_ids, k) |
| "Baseline:" (14): exact search agrees with stored neighbours (sets, tie-aware) | done | full run 2026-10-26: agree True on all 10000 queries, SIFT and GloVe |
| "Baseline:" (15): time exact search single-query and batch | done | full run: batch + one-at-a-time on 5000 report queries -> results/full/baseline.json |
| "Benchmarks:" (17-25) | in progress | all 3 indexes swept on both datasets; flags: IVF-PQ both, IVF-Flat GloVe (0.949); tables + plot (all builds) done; timings to be re-run as medians |
| "Experiments on standard data:" (27-35) | in progress | hypothesis committed (213015d); scaling 100k/300k/1M done once; analysis vs hypothesis after the median re-run |
| "Benchmarks:" (22, inserted 2026-10-29): repeat each timing, take the median | in progress | time_batch / time_one_at_a_time repeats + median (tested); REPEATS=3 wired into all 3 scripts; results not yet re-run |
| "Experiments on standard data:" (36, original): best few hyperparameter configs | superseded | line 36 edited 2026-10-29 |
| "Experiments on standard data:" (36): all hyperparameter configs (HNSW, IVF-Flat, exact) | done | compute_scaling uses every HNSW / IVF-Flat build (TOP_N removed); data in results/full/scaling.json already covers all 4 builds |
| "Experiments on drifted data:" (38-45): hypothesis in README, committed first | done | committed 0263641 |
| "Experiments on drifted data:" (47-64): mean shift / rotation, stale + rebuilt, two recalls, plots + tables, run_all + --quick | done | plan 2026-10-29-drift.md; quick + full (300k) run 2026-10-29; committed 2026-10-30 |
