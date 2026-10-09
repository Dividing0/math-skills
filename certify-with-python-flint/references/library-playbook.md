### Worked example: enclosure and exact factor identity
At 160 bits compute the real Arb enclosure of √2. Check its separation from 7/5 and 3/2; independently verify the rational squares bracket 2. Also check (x−1)(x+1)=x²−1 over fmpz_poly. Keep the full enclosure string in JSON, and restore precision even on failure.

### Invalid inference
If F(X) contains zero, this alone does not guarantee an x in X with F(x)=0. For X=[−1,1], an interval evaluation of x²+1 can include zero under dependency overestimation although the function is strictly positive. A narrow Arb result also does not account for unstated measurement uncertainty in input.

## Integration contract

Accept `{statement, assumptions, domain, inputs, input_uncertainty, required_accuracy, resource_limit}` from a mathematical skill. Return `{code_path, command, interpreter_version, library_versions, exact_inputs, method, assumptions, result, validation_checks, claim_status, unresolved_obligations, output_files}`. Set `claim_status` to `exact-computation`, `numerical-evidence`, `validated-enclosure`, or `blocked`; never merge these statuses. Record nonzero exit codes and full failures. Do not install dependencies globally or change an existing project lockfile implicitly. Execute in the user's project environment or an isolated environment prepared by the execution skill. The bundled demo is one smoke example, not coverage of the full library.

## Primary API sources

Checked 2026-10-08; documentation pages may track a newer release than the runtime. Confirm installed signatures before adaptation. APIs: `arb`, `arb.sqrt`, `arb.contains`, `arb.is_finite`, `fmpq`, `fmpz_poly`, `ctx.prec`

- https://python-flint.readthedocs.io/en/latest/arb.html#flint.arb.sqrt
- https://python-flint.readthedocs.io/en/latest/arb.html#flint.arb.contains
- https://python-flint.readthedocs.io/en/latest/fmpz_poly.html
- https://python-flint.readthedocs.io/en/latest/general.html
