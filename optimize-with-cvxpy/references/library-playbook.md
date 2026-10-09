# Library playbook

## Primary documentation

Retrieved/checked 2026-10-08. Recheck documentation against installed versions before adapting API calls.

- https://www.cvxpy.org/tutorial/dcp/index.html
- https://www.cvxpy.org/tutorial/solvers/index.html

The workflow names the relevant API locators; use the actual installed signatures and recorded version, especially for release/development discrepancies.

## Worked calculation

Project b=(2,-1) onto {x>=0, sum(x)=1}. The independent geometric minimizer is (1,0), squared distance 2. Check objective, constraints and an explicitly infeasible companion problem.

Execute `../scripts/example.py --self-test`. The script emits JSON and fails its assertions if the independent oracle disagrees. An unavailable dependency emits a dependency-unavailable status and exits 2; that is not a passed numerical check. Assertions run in ordinary Python, so do not launch with `-O`.

## False inference

A returned `optimal_inaccurate` value proves exact optimality. It does not; report numerical evidence and residuals.

## Integration contract

Receive a precise mathematical statement, assumptions, units, dimensions, data provenance, desired error/accuracy, available interpreter and runtime constraints from the mathematical skill. Return the exact implementation, dependency versions, executed inputs, raw outcomes, failure/status information, and independent checks. Keep numerical tolerance separate from mathematical guarantees. If an assumption or dependency is missing, return the missing item and any valid partial analysis rather than a fabricated computed result.

## Scope and escalation

Hand back to research-optimization-theory, research-convex-analysis, validate-math-implementation when the issue concerns mathematical assumptions or justification rather than an API. Prefer the smaller supported calculation to an unvalidated large model. Preserve input data and task-local outputs; avoid modifying environments or external services without the task's authorization.

## API locators and selection

- DCP guide: `Variable`, signed `Parameter`, `sum_squares`, `Problem.is_dcp`; convex minimization and affine equalities.
- Solver guide: `installed_solvers`, `Problem.solve(solver=...)`, `.status`, `.solver_stats`, constraint `.violation()` and `.dual_value`. Select conic support before passing options; solver option names differ.
- Analytic oracle for the example: set x=(t,1-t), 0<=t<=1. Objective is 2(t-2)^2, minimized at the feasible endpoint t=1.
- Example execution checked CVXPY 1.9.3 with CLARABEL; future versions require checking compatible solver options.
