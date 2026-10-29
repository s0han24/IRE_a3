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
