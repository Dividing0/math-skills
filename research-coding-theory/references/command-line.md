# Command reference

Enumerate a small linear code over a prime field and find its minimum distance.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-coding-theory/scripts/linear_code.py --example > /tmp/research-coding-theory-input.json
python research-coding-theory/scripts/linear_code.py --input /tmp/research-coding-theory-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `prime` (a prime integer from 2 through 251) and a nonempty rectangular `generator` with entries `0..prime-1`. The helper enumerates messages, deduplicates codewords when generator rows are dependent, and reports dimension, minimum nonzero Hamming weight and a witness. Enumeration is capped at 100,000 messages and five million scalar terms. Prime-power extension fields are not represented by modular integers. For the zero code, distance and correction radius are `null`; no decoder implementation is certified.
