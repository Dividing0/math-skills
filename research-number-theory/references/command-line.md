# Command reference

Compute exact generalized CRT solutions and Bezout witnesses.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-number-theory/scripts/integer_tools.py --example > /tmp/research-number-theory-input.json
python research-number-theory/scripts/integer_tools.py --input /tmp/research-number-theory-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

`operation: "bezout"` takes signed integers `a`, `b` and returns a nonnegative gcd and coefficients satisfying `a*x+b*y=gcd`, including zero arguments. `operation: "crt"` takes nonempty `congruences: [[residue, positive_modulus], ...]`. Moduli need not be coprime: incompatible pairs return `consistent: false`; compatible pairs return the residue class modulo the least common multiple. This does not factor integers or certify primality.
