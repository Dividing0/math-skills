# Command reference

Exhaustively check perfect secrecy and decryptability of a finite cipher table.

From the collection root, or use the installed script's absolute path:

```sh
python research-mathematical-cryptography/scripts/finite_secrecy.py --example > /tmp/research-mathematical-cryptography.json
python research-mathematical-cryptography/scripts/finite_secrecy.py --input /tmp/research-mathematical-cryptography.json
```

Edit the example for your task before executing. Dependencies: Python standard library only. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`encryption_table` contains 1..128 key rows and 1..128 message columns. Ciphertexts are integer or string labels. `key_probabilities` are exact integers or rational strings, nonnegative and summing to one; omitted means uniform keys.

Outputs include conditional ciphertext laws, perfect-secrecy status, the maximum pairwise total-variation distance with a witness message pair, and decryptability for positive-probability keys. The model assumes independent single-use keys and deterministic encryption given key/message. It does not analyze computational security, protocols or side channels.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
