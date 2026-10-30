# AGENTS.md

Instructions for AI coding agents working in this repository.

## 1. Source of truth: `SPEC.md`

- **Read `SPEC.md` before doing anything.** It defines what this project must do.
- `SPEC.md` overrides your assumptions. If the spec and the existing code disagree, stop and ask. Don't silently "fix" either one.
- **Never edit, reorder or reformat `SPEC.md`.** Only the human writes to it.
- If the spec is ambiguous or silent on something you need, **ask one specific question** instead of guessing. Say which part is unclear and what the options are.
- When you start a task, name the part of the spec it implements by **quoting its heading** (e.g. `SPEC "Query tokenization"`). Don't invent section numbers.

### `SPEC.md` is an append-only log

The human adds to `AI_LOGS/SPEC.md` at the bottom whenever they want, without restructuring or cleaning up older text. Read it like this:

1. **Read the whole file, top to bottom, every time.** Don't rely on a summary from earlier in the session.
2. **Later text wins.** If something appended later contradicts earlier text, the later text is what the human currently wants. The earlier text is not deleted, just superseded.
3. **Later text adds, unless it says otherwise.** New requirements apply on top of earlier ones. They don't replace them unless they clearly contradict them or say so (e.g. "drop the X requirement").
4. **Check for new text before every RED step.** `AI_LOGS/PROGRESS.md` records the last spec line you processed (`Spec read up to: line N`). If `SPEC.md` now has more lines than that, there's new text.

### When there's new text in `SPEC.md`

Stop before writing any code and report:

```
SPEC UPDATE (lines N+1 to M)
New:        <each new requirement, one line each>
Overrides:  <earlier spec text it supersedes, quoted, or "none">
Breaks:     <existing tests or code that no longer match, or "none">
Unclear:    <questions, or "none">
Proposal:   <how this changes the next steps>
```

Then wait for the human to confirm. After they confirm:

- Update `Spec read up to:` and the checklist in `AI_LOGS/PROGRESS.md`.
- Mark superseded items as `superseded` instead of deleting them.
- If existing tests contradict the new spec, changing them is its own small step. Show the old and new assertion and get approval. Don't quietly rewrite tests.
- If the new text arrives in the middle of a RED/GREEN step, finish that step (or ask to abandon it) before acting on the update.

## 2. The core rule: small, reviewable steps

The human reviews every change. Your job is to produce changes they can read and understand in **under 2 minutes**.

Hard limits per step:

- **One behaviour per step.** One function, one branch, one edge case.
- **About 30 changed lines of non-test code at most.** If a step would be bigger, split it first.
- **One or two files at most.** Touching more than that means the step is too big.
- **No drive-by changes.** Don't rename, reformat, refactor or "clean up" anything unrelated to the current step.
- **No speculative code.** Don't add parameters, abstractions, config options or helpers that the current test doesn't need.

If you think a big change is truly needed (a new module, a restructure), **propose it as a plan first** (a list of small steps) and wait for approval. Don't write it in one go.

## 3. The TDD loop

Every step goes through this loop. Do not skip phases, and do not merge phases together.

### 🔴 RED: write one failing test
1. Pick the next smallest behaviour from the spec (or from the agreed plan).
2. Write **one** test for it. Give it a name that describes the behaviour, e.g. `test_tokenizer_lowercases_input`.
3. Run the test suite and **confirm the new test fails for the expected reason** (an assertion failure, not an import error or typo).
4. **STOP.** Show the human:
   - the spec section being covered
   - the test code
   - the failure output (trimmed to the relevant lines)

   Then wait for approval.

### 🟢 GREEN: make it pass with the simplest code
1. Write the **minimum** code that makes the test pass. Hardcoding and naive solutions are fine at this point; later tests will force generalisation.
2. Run the **full** test suite. Everything must pass.
3. **STOP.** Show the human the diff and the test results, then wait for approval.

### 🔵 REFACTOR: optional, and only if it's worth it
1. Only refactor when there's clear duplication or a clarity problem.
2. Behaviour must not change. No new tests, no new features.
3. Run the full suite again. It must stay green.
4. **STOP.** Show the diff, then wait for approval.

Then go back to RED with the next behaviour.

### Loop rules
- **Never write production code without a failing test that requires it.**
- **Never change a test to make it pass** unless the human agrees the test was wrong.
- **Never delete, skip or weaken an existing test** without asking.
- If a test fails unexpectedly, **report it**. Don't push on and pile more changes on top.
- If you're stuck after two attempts at GREEN, stop and explain what you tried. The step is probably too big; suggest splitting it.

## 4. How to present each step

Use this format at every STOP:

```
Phase:   RED | GREEN | REFACTOR
Spec:    SPEC "<heading>" (lines A to B): <one-line summary>
Files:   <path(s)>
Change:  <one sentence on what changed and why>

<diff or code>

Tests:   <command run> → <N passed, M failed>
<relevant output, trimmed>

Next:    <the step you plan to do next>
```

Keep the explanation short. The code should speak for itself. Don't paste whole files when a diff will do.

## 5. When the human gives feedback

- "ok" / "next" / "go": move on to the next phase.
- Any change request: apply it **inside the current step only**, re-run the tests, and present the step again.
- "plan": stop coding and write out the next few small steps as a numbered list.

## 6. General conventions

- Run the tests yourself. Never claim they pass without running them.
- Match the existing code style, naming and structure.
- Don't add dependencies without asking.
- Don't commit, push or create branches unless asked.

## 7. `AI_LOGS/`: everything agent-related goes here

Every file you create for your own process (as opposed to project code and tests) belongs in `AI_LOGS/`. Never write plans, notes, scratch files or logs to the repo root or the source tree.

```
AI_LOGS/
├── PROGRESS.md            # "Spec read up to" line + checklist of spec items
├── plans/                 # approved multi-step plans, one file per plan
│   └── YYYY-MM-DD-<topic>.md
└── sessions/              # one log per working session
    └── YYYY-MM-DD-<topic>.md
```

- **`PROGRESS.md`**: update it at the end of every GREEN or REFACTOR step, and after every confirmed spec update. It records `Spec read up to: line N` and each spec item with its status (`todo` / `in progress` / `done` / `superseded`).
- **`plans/`**: when the human asks for a plan or approves one, save it here before you start on step 1.
- **`sessions/`**: create one file at the start of each session and append to it after **every** STOP. Each entry has:
  - the timestamp and phase (RED / GREEN / REFACTOR)
  - the human's prompt or feedback that led to this step (verbatim)
  - the spec section and files touched
  - a short summary of the change and the test result
  - whether the human approved it, asked for changes, or rejected it

  Append only. Never rewrite or delete earlier entries.
- If you're unsure where an agent-related file belongs, put it in `AI_LOGS/`.

## 8. Python setup and commands

The project is in Python and is managed with [`uv`](https://docs.astral.sh/uv/). Always run things through `uv run` so you use the project's virtualenv. Never call bare `python` or `pip`, and never `pip install`.

| Task | Command |
|---|---|
| Install / sync deps | `uv sync` |
| Add a dependency (ask first) | `uv add <pkg>` / `uv add --dev <pkg>` |
| Run all fast tests | `uv run pytest -q` |
| Run one test | `uv run pytest -q tests/test_x.py::test_name` |
| Run slow tests too | `uv run pytest -q -m "slow or not slow"` |
| Lint | `uv run ruff check .` |
| Format | `uv run ruff format .` |

Conventions:

- The layout is `code/src/annbench/` for code and `code/tests/` for tests, with one test file per module (`code/src/annbench/recall.py` → `code/tests/test_recall.py`).
- Add type hints to every public function. Use `numpy.typing.NDArray` for arrays, and document shapes and dtypes in the docstring (e.g. `(n, d) float32`).
- Run `ruff check` and `ruff format` before every STOP. Formatting-only changes to lines you didn't touch don't count toward the step.
- Prefer NumPy vectorised code over Python loops in anything that touches vectors.

## 9. Testing an ANN benchmark

This project benchmarks approximate nearest neighbour (ANN) search. These rules keep the TDD loop fast and the results trustworthy.

### Unit tests must be small, fast and deterministic
- **Use tiny synthetic data**, e.g. `n ≤ 1000`, `d ≤ 32`, from `np.random.default_rng(seed)` with a fixed seed. Never load the real datasets in unit tests.
- **Make hand-checkable fixtures where possible.** For example, 5 points in 2-D where you can work out the true neighbours on paper.
- **Use brute-force exact search as the oracle.** Test ground truth, recall and distance code against a simple brute-force implementation first. Once the brute-force search itself is tested, it becomes the reference for everything else.
- **Never assert on timing values** (QPS, latency, build time), because they're nondeterministic. Test that timing code *returns the right shape and type* or *calls the clock correctly* (inject or mock the clock), not that something is fast.
- **For ANN indexes, test properties, not exact outputs.** Check that results have the right shape, IDs are in range, distances are sorted, there are no duplicate IDs, and recall@k on easy data is at or above a loose threshold (e.g. `≥ 0.9`). Don't test that it returned exactly the brute-force answer, unless the parameters make it exact.
- **Compare floats with tolerances**: `np.testing.assert_allclose` and `pytest.approx`, never `==`.
- **Mark anything over about 1 second with `@pytest.mark.slow`.** Slow tests are skipped by default so the RED/GREEN loop stays quick.

### Keep the metric code separate from the benchmark run
- Metrics (recall@k, QPS, latency percentiles, build time, memory) are **pure functions** that are unit-tested on their own.
- Index wrappers (FAISS, HNSWlib, Annoy, etc.) sit behind **one common interface** (e.g. `build(data)`, `search(queries, k) -> (ids, dists)`), so the benchmark runner doesn't care which library it's using. Add one library at a time, each as its own small TDD sequence.
- The benchmark runner itself doesn't contain logic worth testing beyond wiring. Keep it thin.

### Data, results and reproducibility
- **Datasets** (SIFT, GloVe, etc.) go in `data/`, which is git-ignored. Download code must be idempotent and is never run inside tests.
- **Benchmark results** are project output, not agent logs. They go in `results/` (not `AI_LOGS/`), with the parameters, seed, library versions and machine info saved next to every result file.
- **Fix all random seeds** (NumPy, plus any library-level seed), and record the parameters for every run.
- **Don't run full benchmarks without asking.** They can take a long time. Propose the command and expected runtime first.
- **Document** commands to test, lint, run evaluations, etc in `README.md`
