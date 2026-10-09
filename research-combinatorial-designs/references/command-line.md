# Command reference

Check every point and pair in a finite block design.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-combinatorial-designs/scripts/check_design.py --example > /tmp/research-combinatorial-designs-input.json
python research-combinatorial-designs/scripts/check_design.py --input /tmp/research-combinatorial-designs-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply integer parameters `v`, `k`, `lambda` with `2 <= k <= v <= 1000`, positive lambda, and `blocks` of distinct point indices `0..v-1`. Repeated blocks require `allow_repeated_blocks: true`. The checker counts every unordered pair, reports every failing pair, and reports point replication counts and necessary integrality conditions. `valid: true` comes from checking the explicit construction, not from integrality alone.
