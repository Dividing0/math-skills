# Command reference

Run pinned Lean positive and negative test files with explicit diagnostics.

From the collection root, or use the installed script's absolute path:

```sh
python test-lean4-code/scripts/run_cases.py --example > /tmp/test-lean4-code.json
python test-lean4-code/scripts/run_cases.py --input /tmp/test-lean4-code.json
```

Edit the example for your task before executing. Dependencies: Python standard library only. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`project` names a pinned Lake project. `cases` is a list of 1..100 objects with `file` (project-relative `.lean` file), `expect` (`"success"` or `"error"`), and optional `contains` (literal combined-output substring). An error expectation requires a nonempty substring. `timeout` is an integer 1..300 seconds per command, default 60.

Results contain the toolchain preflight, each command's stdout/stderr/status/timeout and a top-level `passed` Boolean. Success cases reject Lean's sorry warning. This is regression checking, not a transitive axiom audit; use [audit-lean4-proofs](../../audit-lean4-proofs/SKILL.md) for that when available.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
