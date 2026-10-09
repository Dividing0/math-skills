# Command reference

Classify a finite measure-preserving permutation and compute exact orbit averages.

From the collection root, or use the installed script's absolute path:

```sh
python research-ergodic-theory/scripts/finite_dynamics.py --example > /tmp/research-ergodic-theory.json
python research-ergodic-theory/scripts/finite_dynamics.py --input /tmp/research-ergodic-theory.json
```

Edit the example for your task before executing. Dependencies: Python standard library only. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`permutation` is a bijection of 0..n-1, with 1..10,000 states. `observable` has n exact integer/rational-string values. Optional `weights` has n nonnegative exact probabilities summing to one, default uniform.

If the measure is not invariant, only that failure is reported. Otherwise outputs include cycles, ergodicity, mixing, orbit averages and the space average. Classification is exhaustive for this finite invertible model only; zero-weight states are retained in orbit output but ignored in almost-everywhere classification.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
