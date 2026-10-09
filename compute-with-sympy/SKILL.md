---
name: compute-with-sympy
description: Perform exact symbolic calculations with SymPy, preserving assumptions, domains and branches. Use for symbolic equations, calculus, rational expressions, exact matrices, and generating numeric functions for other mathematical skills.
---

# Compute with SymPy

## Workflow

1. Record the expression, symbol assumptions, coefficient domain and original excluded points before transformation. Create exact numbers with `Integer`, `Rational` or strings; avoid Python float literals in exact tasks.
2. Select targeted transforms (`factor`, `cancel`, `together`, `expand`, `refine`) rather than relying on heuristic `simplify`. Preserve removed denominator restrictions in the result contract.
3. Use `solveset(expr, x, domain=S.Reals)` for real univariate sets; use `linsolve` for linear systems and `nonlinsolve` for suitable polynomial systems. Treat `ConditionSet`, unevaluated objects and fuzzy `None` predicates as unresolved. `nsolve` gives candidates, not complete solution sets.
4. Distinguish real and complex branches. A real symbol permits `sqrt(x**2)=Abs(x)`; positivity permits the stronger identity. Do not force power/log simplifications without their hypotheses.
5. Verify every candidate in the original expression and domain. Check an antiderivative by differentiation on stated intervals, an exact matrix solution by exact multiplication. Numeric samples are supplementary and cannot establish identities.
6. Use `lambdify` only after establishing branches and singularities; explicitly choose modules and array dtype. Do not parse or lambdify untrusted input: these APIs can evaluate generated code.
7. Hand off formulas and assumptions to `perform-symbolic-computation`, `construct-math-proofs` or `derive-executable-algorithm`; hand off numerical implementation to NumPy/SciPy skills and actual execution evidence to `run-math-python`.

## Resources

Read [library-playbook](references/library-playbook.md) for the worked example, failure analysis, API sources and inter-skill contract. Run [example.py](scripts/example.py) with `--self-test` as the dependency smoke check; assertions run even without the flag. Report dependency failures rather than simulated results.

## Runnable helper

Use [calculate.py](scripts/calculate.py) to run exact symbolic algebra, calculus, matrix, dynamics and local metric calculations. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
