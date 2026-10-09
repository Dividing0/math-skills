---
name: optimize-with-cvxpy
description: Formulate and execute CVXPY optimization models with DCP checks, solver selection and postsolve validation. Use for constrained least squares, convex programs, parameter sweeps and infeasible or inaccurate solver results.
---

# Optimize with CVXPY

Read [library-playbook.md](references/library-playbook.md) for API locators, worked example, failure analysis and the integration contract. Run `scripts/example.py --self-test` using the task's selected Python interpreter before adapting it. Missing dependencies must be reported explicitly; do not invent executions.

## Workflow

1. Write dimensions, objective, feasible set and scaling. Separate continuous convex optimization from mixed-integer, DGP, DQCP or nonconvex extensions; do not silently change the mathematical problem.
2. Construct atoms and constraints; inspect `problem.is_dcp()` before ordinary solve. DCP is a sufficient syntactic convexity test: rejection does not prove nonconvexity. Do not use `gp=True` or `qcp=True` to bypass arbitrary errors.
3. Inspect `cp.installed_solvers()` and select a solver supporting the actual cones and integrality. Preserve solver/version/tolerances and explicit option names. For parameter sweeps use `Parameter`; distinguish DPP compilation reuse from numerical warm start.
4. Inspect `problem.status` before reading `.value`. For infeasible/unbounded results do not return variable values as a solution. Distinguish `OPTIMAL` and `OPTIMAL_INACCURATE`; the latter requires independent checks and a qualified result.
5. Recompute objective and primal violations from original data. Inspect stationarity, dual feasibility and complementary slackness when assumptions and dual values permit; report tolerances and scale. A numerical solver status is not a rigorous certificate. Cross-check a small analytic instance or independent method.

## Handoff

Use the existing mathematical skills (research-optimization-theory, research-convex-analysis, validate-math-implementation) to establish assumptions and interpret conclusions. Use `run-math-python` for reproducible execution records. Return the actual executed code, versions, inputs, status, diagnostics, oracle checks and artifacts. Label evidence as numerical, exact symbolic, validated enclosure or formal proof; do not upgrade evidence without a checker.
