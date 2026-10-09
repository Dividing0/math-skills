# Equation and dynamics methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Linearization or modes | Local behavior near an equilibrium | Check hyperbolicity, boundary conditions and nonlinear remainder | Zero eigenvalues or critical modes require further analysis |
| Energy or Lyapunov method | Need estimates, invariance or stability | Derive valid boundary terms and check coercivity and dissipation | A bound in one norm need not control regularity |
| Fixed-point or compactness method | Need existence of a solution | Verify preserved domain, completeness or compactness and continuity | Prove uniqueness separately if no contraction applies |
| Numerical trajectory or continuation | Explore behavior or candidate branches | Check discretization, events, refinement and solver residuals | Label global conclusions conjectural without analytic or certified coverage |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
