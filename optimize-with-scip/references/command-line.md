# Command reference

Solve a bounded-size linear mixed-integer model with SCIP diagnostics.

From the collection root, or use the installed script's absolute path:

```sh
python optimize-with-scip/scripts/solve_milp.py --example > /tmp/optimize-with-scip.json
uv run --with pyscipopt python optimize-with-scip/scripts/solve_milp.py --input /tmp/optimize-with-scip.json
```

Edit the example for your task before executing. Dependencies: pyscipopt. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`variables`: 1..200 objects with distinct identifier `name`, `type` (`C`, `I`, `B`; default `C`), `lower` (default 0) and `upper` (default unbounded). JSON null denotes an unbounded side; binary bounds are intersected with [0,1].

`objective`: finite coefficients in variable order. `sense`: `minimize` (default) or `maximize`. `constraints`: at most 2,000 objects with `coefficients`, `sense` (`<=`, `>=`, `==`), and finite `rhs`. `time_limit`: seconds in (0,300], default 10. All coefficients use floating arithmetic.

Read `solver_status`, solution count and bounds first. Solution values, recomputed objective/residuals and gap appear only when an incumbent exists. Null bounds represent unavailable/infinite values. This helper handles MILP, not arbitrary nonlinear strings.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
