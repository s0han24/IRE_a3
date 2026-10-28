# Progress

Spec read up to: line 35

Agents update this after each GREEN or REFACTOR step and after each confirmed spec update.
Status: todo / in progress / done / superseded (keep superseded rows; don't delete them).

| Spec item (heading, lines) | Status | Notes |
|---|---|---|
| "IMPORTANT" (4): src/run_all.sh + --quick (<15 min), README how-to + pipeline description | done | run_all.sh (stages 1+2, --quick, --report-only); quick 18 s end-to-end with data cached (~5 min incl. first download); README: how to run, pipeline, results format, dev commands |
| "Datasets:" (7): SIFT + GloVe-100 from ann-benchmarks | done | plan F done; both files downloaded and used in full + quick runs |
| "Datasets:" (8): queries split tune [:5000] / report [5000:] | done | plan B6; split_queries in data.py |
| "Datasets:" (9, original): l2-normalise euclidean benchmarks, use cosine | superseded | line 9 edited in place |
| "Datasets:" (9, edit 2): normalise all, euclidean throughout | superseded | line 9 edited again |
| "Datasets:" (9): normalise GloVe only; euclidean throughout | done | prepare_vectors in pipeline; GloVe agreement True on full run |
| "Baseline:" (12): FAISS exact search as reference | done | FaissExact (IndexFlatL2, plain L2) used in compute_baseline.py |
| "Baseline:" (13): recall@10 from scratch, ties at 10th not misses, unit-tested | done | recall_at_k + unit tests (no ties, float-noise ties); used for ANN later |
| "Baseline:" (14): exact search agrees with stored neighbours (sets, tie-aware) | done | full run 2026-10-26: agree True on all 10000 queries, SIFT and GloVe |
| "Baseline:" (15): time exact search single-query and batch | done | full run: batch + one-at-a-time on 5000 report queries -> results/full/baseline.json |
| "Benchmarks:" (17-25) | todo | plan 2026-10-28-benchmarks.md (proposed); ambiguities resolved 2026-10-28 |
| "Experiments on standard data:" (27-35) | todo | plan 2026-10-28-benchmarks.md; hypothesis to README + first git commit before experiment code |
