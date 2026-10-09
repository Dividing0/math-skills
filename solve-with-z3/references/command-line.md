# Command reference

Solve SMT-LIB assertions and retain sat, unsat and unknown outcomes.

From the collection root, or use the installed script's absolute path:

```sh
python solve-with-z3/scripts/solve_smt.py --example > /tmp/solve-with-z3.json
uv run --with z3-solver python solve-with-z3/scripts/solve_smt.py --input /tmp/solve-with-z3.json
```

Edit the example for your task before executing. Dependencies: z3-solver. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`smt2` is nonempty SMT-LIB2 text, at most 100,000 characters, intended to contain declarations and assertions. `timeout_ms` is an integer 1..60,000 (default 5,000) for the solver check, not a wall-clock limit for parsing. Run large or untrusted queries in an externally bounded process.

The result includes `solver_status`, assertion count, and either `model`/`assertion_evaluations`, `core_assertion_indices`, or `reason_unknown`. Parsing errors are input errors. It does not implement optimization, interactive SMT sessions or external certificate checking.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
