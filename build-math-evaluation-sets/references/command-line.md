# Command reference

Audit task IDs, duplicate prompts, split leakage and evaluation score coverage.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python build-math-evaluation-sets/scripts/audit_dataset.py --example > /tmp/build-math-evaluation-sets-input.json
python build-math-evaluation-sets/scripts/audit_dataset.py --input /tmp/build-math-evaluation-sets-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `tasks` with unique string `id`, nonempty `prompt` and `split`; optional `family` groups mathematical variants and optional `category` supports stratified scores. Reports normalized lexical duplicates, declared families crossing splits and split counts. Optional `scores` contains unique known IDs and finite scores in [0,1]; reports mean, missing IDs and category coverage. Rubrics and answers need not be passed to the tool. Semantic duplicates, answer leakage inside prose, reference correctness and causal agent comparisons still need review.
