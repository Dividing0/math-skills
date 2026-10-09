# Command reference

Find pure equilibria and check supplied mixed strategies in a rational bimatrix game.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-game-theory/scripts/check_game.py --example > /tmp/research-game-theory-input.json
python research-game-theory/scripts/check_game.py --input /tmp/research-game-theory-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply equal-shaped rational `row_payoffs` and `column_payoffs` matrices. Every pure unilateral deviation is checked and all pure Nash equilibria returned. Optional `row_strategy` and `column_strategy` must be nonnegative rational vectors summing exactly to one. Reports expected payoffs, all pure-deviation payoffs, regrets and `mixed_equilibrium`. This checks supplied independent mixed strategies, not correlated equilibrium, and does not search for arbitrary mixed equilibria.
