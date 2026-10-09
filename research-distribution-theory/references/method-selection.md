# Analytic methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Pointwise estimates and inequalities | Need boundedness, convergence or a norm estimate | Specify the norm, constants, domain and uniformity | Do not substitute pointwise control for uniform or integral control |
| Compactness and subsequences | Need existence through a limiting sequence | Check topology, compactness, limit membership and passage through nonlinear terms | Return only a convergent subsequence under proved hypotheses |
| Weak or distributional formulation | Classical derivatives or traces may be unavailable | Specify test spaces, weak derivatives and boundary terms | Do not multiply or evaluate distributions without a justified definition |
| Duality or spectral arguments | Operators or functional pairings expose structure | Check domains, boundedness, self-adjointness and applicable duality | Use a weaker operator statement if spectral decomposition is unavailable |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
