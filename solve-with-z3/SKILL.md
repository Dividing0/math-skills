---
name: solve-with-z3
description: "Encode and execute satisfiability, constraint and counterexample queries with Z3. Use for SMT theories, model witnesses, unsatisfiable cores and explicit unknown outcomes, preserving the distinction between encoded formulas and intended claims."
---

# Solve with Z3

## Workflow

1. State the claim and choose sorts deliberately: mathematical integers/reals, fixed-width bit-vectors, floating-point, arrays or uninterpreted functions have different semantics. Encode bounds, quantifiers and arithmetic side conditions explicitly.
2. For a validity query, assert the hypotheses and negation of the conclusion. Check that the hypotheses themselves are satisfiable before interpreting a proof-by-unsatisfiability; otherwise the conclusion may be vacuous.
3. Run the actual solver with a resource budget. Preserve sat, unsat and unknown separately; timeout or incomplete theory support is not a counterexample or proof.
4. For sat, inspect the model and validate it against the original problem, including finite bounds and omitted variables. For unsat, map the returned core to source assertions; a core need not be minimal and is not an independently checked proof certificate.
5. Check the encoding with a small known satisfiable and unsatisfiable case. Treat quantifiers, nonlinear arithmetic and machine arithmetic carefully; verify solver/version-dependent facilities before promising proof extraction.
6. Report the formula/sorts, command, version, resource limits, result and correspondence limitations. Use exact arithmetic for model values where supported rather than silently rounding a rational or algebraic witness.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [solve_smt.py](scripts/solve_smt.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
