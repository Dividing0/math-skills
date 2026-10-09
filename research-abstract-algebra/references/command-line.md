# Command reference

Exhaustively check a finite operation table and report group invariants.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-abstract-algebra/scripts/finite_group.py --example > /tmp/research-abstract-algebra-input.json
python research-abstract-algebra/scripts/finite_group.py --input /tmp/research-abstract-algebra-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `table`, a square multiplication table with 1–80 elements indexed `0..n-1`. Entries must lie in that range. The helper exhaustively checks associativity, finds a two-sided identity and inverses, and then returns element orders, center and conjugacy classes. Failed axioms include a witness where possible. The result is about this finite table; it is not a classification of abstract groups or a ring/module checker.
