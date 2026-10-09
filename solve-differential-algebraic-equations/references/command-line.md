# Command reference

Solve a constant linear index-one DAE by elimination and backward Euler.

From the collection root, or use the installed script's absolute path:

```sh
python solve-differential-algebraic-equations/scripts/linear_dae.py --example > /tmp/solve-differential-algebraic-equations.json
uv run --with numpy --with scipy python solve-differential-algebraic-equations/scripts/linear_dae.py --input /tmp/solve-differential-algebraic-equations.json
```

Edit the example for your task before executing. Dependencies: numpy, scipy. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

Supply matrices `A` (n*n), `B` (n*m), `C` (m*n), `D` (m*m), vectors `f` (n), `g` (m), and differential `initial` (n). All entries must be finite; n+m <=50. D must have finite 2-norm condition number <=1e12. Optional `algebraic_initial` must agree with the computed value within rtol 1e-10/atol 1e-12.

`steps` is an integer 1..10,000 (default 40), `duration` positive finite (default 1). Two backward-Euler runs use steps and twice steps. Results report terminal states, algebraic/discrete-differential residuals and error against a floating matrix exponential. This is a constant linear index-one tool, not an IDA binding or rigorous enclosure.

Each step matrix must also have finite 2-norm condition number <=1e12. Singular or ill-conditioned step matrices and nonfinite reference/trajectory values fail the calculation; reduce the step size or inspect the model before retrying.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
