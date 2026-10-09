# Command reference

Compute conditional finite-class Hoeffding bounds from bounded binary losses.

From the collection root, or use the installed script's absolute path:

```sh
python research-statistical-learning-theory/scripts/finite_class_bound.py --example > /tmp/research-statistical-learning-theory.json
python research-statistical-learning-theory/scripts/finite_class_bound.py --input /tmp/research-statistical-learning-theory.json
```

Edit the example for your task before executing. Dependencies: Python standard library only. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`losses` is a rectangular matrix: hypothesis rows, common-example columns, entries exactly 0 or 1. At most 1,000,000 entries. `class_size` is an integer at least the number of supplied rows and at most 10**12; default supplied row count. `delta` is in (0,1), default 0.05.

The caller must explicitly supply `iid: true` and `class_fixed_before_data: true`. These are assumptions, not facts verified by the helper. Results give simultaneous risk intervals, the selected supplied hypothesis, and an excess-risk bound relative to the best supplied candidate. This is not a VC bound for an infinite class.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
