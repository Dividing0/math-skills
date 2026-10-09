# Command reference

Exhaustively check a classical propositional formula encoded as a JSON tree.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-mathematical-logic/scripts/truth_table.py --example > /tmp/research-mathematical-logic-input.json
python research-mathematical-logic/scripts/truth_table.py --input /tmp/research-mathematical-logic-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

`formula` is a Boolean, a variable string, or a JSON tree using `not` (one operand), `and`, `or`, `implies`, `iff` (two operands). Up to 16 distinct variables are exhaustively enumerated. Results include satisfying count, validity, satisfiability and a model/countermodel. The logic is classical propositional; this does not decide first-order validity or prove syntactic derivability in an arbitrary calculus.
