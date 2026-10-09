# Command reference

Bracket the extinction probability of a finite-support Galton-Watson process with exact rationals.

## Run

From the collection root, or use an installed absolute script path:

```sh
python research-branching-processes/scripts/extinction.py --example > /tmp/research-branching-processes-input.json
python research-branching-processes/scripts/extinction.py --input /tmp/research-branching-processes-input.json
```

Only the Python standard library is required. Edit the example for the actual task. `--input -` reads stdin. JSON output records `status`, `evidence`, `result`, dependency/Python versions and `input_sha256`. Exit 0 means the calculation completed; inspect `is_matroid`, `stationary` and other result fields before interpreting the result. Invalid input exits 1. Use the `run-math-python` execution runner to bound expensive tasks and retain logs.

## Inputs and interpretation

Supply `offspring_probabilities` as exact integers or rational/decimal strings for counts 0 through at most 20. They must be nonnegative and sum exactly to one. Optional `bisections` (1–256, default 80) controls exact rational refinement. The helper returns the exact mean and a rational interval for eventual extinction from one ancestor. If p0=0, extinction is impossible, including deterministic one-child reproduction; otherwise a mean at most one gives extinction probability one. In the supercritical case, sign-certified bisection brackets the least PGF fixed point below one. This relies on the specified independent, identically distributed finite-support Galton–Watson model, not an observed population process. Near-critical bracketing is capped at 512 refinements and reports failure if unresolved.
