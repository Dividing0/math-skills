---
name: optimize-with-scip
description: "Formulate and run mixed-integer optimization with SCIP/PySCIPOpt, distinguishing feasible incumbents, primal and dual bounds, optimality gaps and solver termination. Use for discrete or nonconvex models beyond continuous convex workflows."
---

# Optimize with SCIP

## Workflow

1. Identify variable domains, objective sense, constraints, units and finite bounds. Derive any big-M constants from valid domain bounds; arbitrary large constants can change numerical behavior and invalidate the intended model.
2. Choose a supported SCIP formulation. Preserve integer/binary restrictions and nonlinear expression semantics; distinguish the linear helper from a general MINLP implementation.
3. Set time and other relevant resource limits before solving, and record solver versions and parameters. A time limit with an incumbent is a feasible-solution result, not an optimality proof.
4. Inspect termination, solution count, incumbent objective, dual bound and gap. Respect objective sense: for minimization the incumbent is an upper bound; for maximization it is a lower bound.
5. Recompute constraints, bounds and integrality residuals on the returned solution. Compare small models with exhaustive enumeration where practical. Numerical tolerances and solver-reported optimality are not exact rational certificates.
6. Report the model, actual status and evidence, including no-incumbent, infeasible, unbounded and unresolved cases. Use exact certificate checking separately when the task asks for a rigorous proof.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [solve_milp.py](scripts/solve_milp.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
