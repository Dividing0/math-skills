### Worked example: catastrophic cancellation
Compute √(1+h)−1 for h=10⁻⁴⁰. Use h/(√(1+h)+1) as a stable independent identity. The executable compares direct calculations at 30 and 100 decimal digits with the stable form; checks the ratio to h/2 and an algebraic reconstruction. Reconstruct h from a string inside each context.

### Invalid inference
Agreement at 100 and 200 digits is not a certificate: both computations can share a model error, branch error, or missed singularity. A tiny residual alone does not bound root error without conditioning information. Float-created decimal inputs retain their float approximation after increasing precision.

## Integration contract

Accept `{statement, assumptions, domain, inputs, input_uncertainty, required_accuracy, resource_limit}` from a mathematical skill. Return `{code_path, command, interpreter_version, library_versions, exact_inputs, method, assumptions, result, validation_checks, claim_status, unresolved_obligations, output_files}`. Set `claim_status` to `exact-computation`, `numerical-evidence`, `validated-enclosure`, or `blocked`; never merge these statuses. Record nonzero exit codes and full failures. Do not install dependencies globally or change an existing project lockfile implicitly. Execute in the user's project environment or an isolated environment prepared by the execution skill. The bundled demo is one smoke example, not coverage of the full library.

## Primary API sources

Checked 2026-10-08; documentation pages may track a newer release than the runtime. Confirm installed signatures before adaptation. APIs: `mp.workdps`, `mp.mpf`, `mp.nstr`, `mp.findroot`, `mp.quad`, `mp.expm1`, `mp.log1p`

- https://mpmath.readthedocs.io/en/latest/basics.html
- https://mpmath.readthedocs.io/en/latest/calculus/optimization.html#root-finding-findroot
- https://mpmath.readthedocs.io/en/latest/calculus/integration.html#numerical-integration-quadrature
