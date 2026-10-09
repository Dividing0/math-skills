---
name: compute-with-sagemath
description: Execute SageMath computations with explicit mathematical parents, exact coefficient domains and independently checked results. Use for number theory, algebraic fields, polynomial factorization, Groebner bases and exact structural computations beyond lightweight symbolic formulas.
---

# Compute with SageMath

## Workflow

1. Check `sage --version` and availability of a Sage interpreter. Use `sage -python scripts/example.py --self-test` with normal Python imports; Sage is a separate environment and must not be assumed to install as an ordinary lightweight pip dependency. Fail visibly if absent.
2. Declare parents (`ZZ`, `QQ`, `GF(q)`, `PolynomialRing`, `NumberField`) and embeddings/coercions before computing. Print `.parent()` in results. Use `**` in Python files; `^` is XOR without the Sage preparser. Use exact Sage rationals rather than Python `/` on integers.
3. Choose algorithms according to the question: `.factor()` in a stated ring, `.roots(ring=...)` in a stated extension, `.groebner_basis()` for a specified ideal/order, `.is_irreducible()` for a stated coefficient field. Factorization depends on the ring; roots may require an extension.
4. Reconstruct factor products with multiplicities in the original parent, substitute roots, verify defining field polynomials, and check characteristic changes. In finite fields distinguish prime characteristic from field cardinality; test whether a purported modulus defines a field before constructing it.
5. For ideal or group properties, preserve the algorithm's mathematical assumptions and exact versus probabilistic status. Record seeds and proof settings if algorithms are probabilistic; do not silently disable arithmetic proof options for speed.
6. Avoid promoting a finite search to a general theorem. Capture commands, exact inputs, Sage version, parents and independent checks. Do not call an arbitrary exact CAS computation proof-assistant verification.
7. Hand off structural results to `research-abstract-algebra`, `research-number-theory`, `research-computational-algebra` or `construct-math-proofs`; hand off reproducible execution records to `run-math-python` and certificates to `verify-proof-certificates`.

## Resources

Read [library-playbook](references/library-playbook.md) for the worked example, failure analysis, API sources and inter-skill contract. Run [example.py](scripts/example.py) with `--self-test` as the dependency smoke check; assertions run even without the flag. Report dependency failures rather than simulated results.
