# Command reference

Check exact rational linear-system and linear-program optimality certificates.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python verify-proof-certificates/scripts/check_certificate.py --example > /tmp/verify-proof-certificates-input.json
python verify-proof-certificates/scripts/check_certificate.py --input /tmp/verify-proof-certificates-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Use `operation: "linear-system"` with a rectangular `A`, matching `b` and candidate `x`; the result checks `Ax=b` exactly without certifying uniqueness. Use `operation: "linear-program"` with additional `c` and `y` for **min cᵀx subject to Ax≥b, x≥0**, dual **max bᵀy subject to Aᵀy≤c, y≥0**. All primal and dual feasibility conditions and objective equality are checked. `valid: false` rejects the certificate even if objectives happen to agree. Inputs are integers or rational/decimal strings; floating JSON numbers are rejected.
