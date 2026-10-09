# Geometric methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Local coordinates | The claim concerns derivatives or local structure | Track coordinate transformations and chart domain | Do not infer a global theorem from local calculations |
| Topological or geometric invariants | Need to distinguish or obstruct equivalence | Prove invariance and check whether the invariant is complete | Matching invariants may leave classification unresolved |
| Compactness or comparison | Seek global existence or a geometric bound | Check completeness, curvature, boundary and topology hypotheses | Find an incomplete or degenerate counterexample |
| Robust geometric computation | Finite geometry involves incidence or orientation | Handle degeneracy with exact predicates or certified bounds | Label uncertain configurations instead of arbitrary floating-point decisions |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
