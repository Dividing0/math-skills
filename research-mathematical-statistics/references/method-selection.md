# Probabilistic and statistical methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Exact finite model | State space or outcomes are finite | Specify dependence and enumerate all outcomes or prove the reduction | Sampling alone does not provide complete coverage |
| Moment, concentration or limit theorem | Need bounds or asymptotic behavior | Check moment, independence or dependence conditions and limiting regime | Report an empirical estimate if theorem assumptions are unverified |
| Likelihood or posterior inference | Data must estimate a model quantity | Check identifiability, sampling design, posterior propriety and approximation error | Report identifiable combinations rather than unsupported parameters |
| Conditional or causal model | Interest concerns interventions or conditional structure | State assumptions, support and selection mechanism | Keep predictive associations separate from identified causal effects |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
