# Domain playbook: quantify-model-uncertainty

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For deterministic parameter bounds, propagate the admissible set by monotonicity or verified interval optimization. The resulting enclosure has no probabilistic coverage unless a probability model is independently supplied.
- For smooth stochastic propagation, use a first-order delta approximation only when local linearization is justified. Retain the full covariance matrix; correlation can amplify or cancel uncertainty.
- For simulation, sample from the specified joint distribution and report Monte Carlo error separately from model discrepancy and uncertainty in distribution parameters. Tail probabilities require adequate effective sample size or a justified rare-event method.

## Worked valid example

Let Y=A+B with E[A]=2, E[B]=3, Var(A)=1, Var(B)=4 and Cov(A,B)=1. Then E[Y]=5 and Var(Y)=1+4+2=7 exactly, irrespective of normality. If (A,B) is jointly Gaussian, Y is Gaussian and a central interval is 5±1.96√7 approximately. Without joint Gaussianity, that interval is not automatically a 95% interval; only the first two moments have been established.

## Tempting inference and counterexample

Independence cannot be inferred from equal marginal variances. Let B=A and A take ±1 with equal probabilities. Var(A+B)=4, whereas discarding covariance gives 2. For B=-A, the actual variance is 0. Marginals alone cannot determine propagated variance.

## Stop conditions and handoff

Stop probability statements when distributions or dependence are unsupported. Hand off the joint assumptions, uncertainty source decomposition, propagation approximation and coverage interpretation to sensitivity analysis, statistical estimation or measurement design.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
