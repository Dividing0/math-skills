# Command reference

Check every hereditary and exchange axiom in an explicitly listed finite independence system.

## Run

From the collection root, or use an installed absolute script path:

```sh
python research-matroid-theory/scripts/check_matroid.py --example > /tmp/research-matroid-theory-input.json
python research-matroid-theory/scripts/check_matroid.py --input /tmp/research-matroid-theory-input.json
```

Only the Python standard library is required. Edit the example for the actual task. `--input -` reads stdin. JSON output records `status`, `evidence`, `result`, dependency/Python versions and `input_sha256`. Exit 0 means the calculation completed; inspect `is_matroid`, `stationary` and other result fields before interpreting the result. Invalid input exits 1. Use the `run-math-python` execution runner to bound expensive tasks and retain logs.

## Inputs and interpretation

Supply `elements` (0–16) and an explicit complete list of `independent_sets` (up to 1024). Every set contains distinct integer indices. The helper checks the empty set, hereditary closure and every augmentation pair, returning a failing witness when available. For a valid matroid it reports rank and all bases. Optional exact rational `weights` runs greedy maximum-weight independent-set selection, skips nonpositive weights, and checks the result against enumeration of the supplied family. The entire family must be supplied; a list of bases alone is not an independence-family encoding.
