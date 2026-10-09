# Command reference

Find exact rational dimensionless exponent vectors from a base-unit matrix.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python nondimensionalize-models/scripts/dimensionless_groups.py --example > /tmp/nondimensionalize-models-input.json
uv run --with sympy python nondimensionalize-models/scripts/dimensionless_groups.py --input /tmp/nondimensionalize-models-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: sympy. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

`quantities` gives unique column names; `dimensions` is a rectangular matrix of rational base-unit exponents, one base unit per row. The exact nullspace produces independent dimensionless monomials; rational basis vectors are scaled to integer exponents and checked against the dimension matrix. The basis is not canonical and does not choose physical scales, transform initial/boundary data, or justify discarding small terms.
