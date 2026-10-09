# Optimization and variational methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| First-order conditions | Find or classify candidate solutions | Check differentiability, constraints and qualification conditions | A stationary or KKT point is not automatically optimal |
| Convexity and dual certificates | Prove global optimality | Verify convexity, feasibility, dual bounds and any strong-duality assumptions | Separate optimal value, attainment and uniqueness |
| Direct existence method | Need an optimizer or minimizer | Check compactness or coercivity, topology and lower semicontinuity | In infinite dimensions identify the required weak compactness explicitly |
| Numerical optimization | Need computable candidates | Check derivative accuracy, feasibility and optimality residuals | Report local or approximate status when global certification is unavailable |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
