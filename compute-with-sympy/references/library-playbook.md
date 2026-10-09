### Worked example: a removable singularity
Let f=(x²−1)/(x−1) with real x≠1. The executable example cancels to x+1 but records the excluded point. Solving f=2 gives an empty set: the only candidate is excluded. Independently check f(0)=1 and the original denominator at x=1.

### Invalid inference
Canceling a factor does not extend the original function's domain. A successful simplification also does not prove an identity across log branch cuts. Distinguish `.equals()` returning `None` from `False` and never coerce unknown to a proof.

## Integration contract

Accept `{statement, assumptions, domain, inputs, input_uncertainty, required_accuracy, resource_limit}` from a mathematical skill. Return `{code_path, command, interpreter_version, library_versions, exact_inputs, method, assumptions, result, validation_checks, claim_status, unresolved_obligations, output_files}`. Set `claim_status` to `exact-computation`, `numerical-evidence`, `validated-enclosure`, or `blocked`; never merge these statuses. Record nonzero exit codes and full failures. Do not install dependencies globally or change an existing project lockfile implicitly. Execute in the user's project environment or an isolated environment prepared by the execution skill. The bundled demo is one smoke example, not coverage of the full library.

## Primary API sources

Checked 2026-10-08; documentation pages may track a newer release than the runtime. Confirm installed signatures before adaptation. APIs: `solveset`, `S.Reals`, `cancel`, `Rational`, `Symbol(real=True)`, `lambdify`

- https://docs.sympy.org/latest/modules/solvers/solveset.html#sympy.solvers.solveset.solveset
- https://docs.sympy.org/latest/guides/assumptions.html
- https://docs.sympy.org/latest/modules/utilities/lambdify.html
