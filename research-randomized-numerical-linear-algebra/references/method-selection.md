# Numerical methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Exact or independent small reference | Need implementation correctness on finite cases | Use analytic cases, exact arithmetic or an independent formulation | Two implementations sharing the same formula can share the same mistake |
| Stable iterative or direct method | Need an approximate solution | Analyze conditioning, residual, stopping and scaling | Separate stagnation from convergence and return failure explicitly |
| Refinement or precision study | Need empirical error behavior | Change resolution or precision while controlling other errors | Observed rates are not universal convergence proofs |
| Certified enclosure | Need a rigorous numerical conclusion | Use outward rounding and a validated mathematical criterion | High precision and a small residual alone do not certify |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
