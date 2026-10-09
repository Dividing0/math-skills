### Worked example: coefficient field changes factorization
Factor x²+1 over QQ and over GF(5). The script verifies both reconstructed products, then independently enumerates all residues mod 5 using Python integer arithmetic. It records irreducibility over QQ and the finite-field roots with their multiplicities.

### Invalid inference
Irreducibility over QQ does not imply irreducibility over every finite field. Results over GF(5) cannot be lifted to QQ without a valid argument. Sage syntax R.<x>=QQ[] belongs to preparsed Sage input, not a normal Python file; use PolynomialRing(QQ,'x').

## Integration contract

Accept `{statement, assumptions, domain, inputs, input_uncertainty, required_accuracy, resource_limit}` from a mathematical skill. Return `{code_path, command, interpreter_version, library_versions, exact_inputs, method, assumptions, result, validation_checks, claim_status, unresolved_obligations, output_files}`. Set `claim_status` to `exact-computation`, `numerical-evidence`, `validated-enclosure`, or `blocked`; never merge these statuses. Record nonzero exit codes and full failures. Do not install dependencies globally or change an existing project lockfile implicitly. Execute in the user's project environment or an isolated environment prepared by the execution skill. The bundled demo is one smoke example, not coverage of the full library.

## Primary API sources

Checked 2026-10-08; documentation pages may track a newer release than the runtime. Confirm installed signatures before adaptation. APIs: `PolynomialRing`, `QQ`, `GF`, `factor`, `is_irreducible`, `roots`, `parent`; invoke `.py` through `sage -python`

- https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_element.html
- https://doc.sagemath.org/html/en/tutorial/tour_polynomial.html
- https://doc.sagemath.org/html/en/reference/repl/sage/repl/preparse.html
