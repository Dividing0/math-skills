---
name: compute-high-precision
description: Use mpmath for arbitrary-precision numerical calculations, roots, quadrature and special functions. Use when binary64 loses useful digits or when mathematical skills need precision studies and numerical evidence without a certified enclosure.
---

# Compute with mpmath

## Workflow

1. Record target absolute/relative accuracy, input accuracy, domains, branches and conditioning. Import `mp` from mpmath; construct decimal inputs from strings inside the precision context. Increasing precision cannot recover digits already lost to a float.
2. Use `with mp.workdps(p)` so precision is restored after errors. Rebuild all inputs and recompute at each precision, rather than reusing low-precision values. Keep outputs as `mp.nstr` strings, never float-convert high-precision values for storage.
3. Select numerically stable formulas first: `expm1`/`log1p`, rationalized differences, or scaled special functions. Raising precision alone can be expensive and still obscure an ill-conditioned problem.
4. For roots use `findroot` with a specified method and justified initial region. Check the original residual, domain and derivative/conditioning. Multiple seeds do not establish completeness or uniqueness; obtain those separately or hand off to exact/certified methods.
5. For `quad`, split at known singularities/discontinuities and establish integrability before choosing finite/infinite intervals. Refinement or agreement at p and 2p is empirical evidence, not a rigorous error bound.
6. Run a precision ladder and an independent analytic identity or alternative algorithm; report discrepancies and which error sources were excluded. Label output `numerical-evidence`; use `certify-with-python-flint` or `certify-math-computations` when guaranteed bounds are required.
7. Hand off high-precision candidates and precision/conditioning evidence to `analyze-math-asymptotics`, `solve-inverse-problems` or `review-math-proofs`. Use `run-math-python` to retain environment and actual execution logs.

## Resources

Read [library-playbook](references/library-playbook.md) for the worked example, failure analysis, API sources and inter-skill contract. Run [example.py](scripts/example.py) with `--self-test` as the dependency smoke check; assertions run even without the flag. Report dependency failures rather than simulated results.
