# Domain playbook: research-mathematical-statistics

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For estimation specify a probability model and an identifiable estimand before optimizing likelihood. Derive bias and variance under the actual sampling dependence; formulas for independent observations cannot be copied to clustered or serial data.
2. For finite-sample confidence statements construct a pivot or invert a test with verified distributional assumptions. Coverage is a probability over repeated datasets at fixed parameter, not a probability assigned to the fixed parameter after observing the interval.
3. For asymptotic inference identify the limiting sequence, regularity and variance estimator. Boundary parameters, misspecification or heavy tails can invalidate standard normal approximations. Multiple testing needs a declared family and procedure; post-selection estimates require additional treatment.

## Worked derivation

For independent X₁,…,X_n distributed N(μ,σ²) with known σ, the mean is N(μ,σ²/n). Consequently P_μ(|X̄−μ|≤1.96σ/√n) is approximately 0.95, giving [X̄−1.96σ/√n,X̄+1.96σ/√n]. The approximation here is the rounded normal quantile, not a central-limit approximation; normality makes the pivot exact with the precise quantile.

## Invalid inference and witness

If X₁=⋯=X_n=Z with Var Z=σ², then Var(X̄)=σ², not σ²/n. Treating identical dependent measurements as n independent observations creates a falsely narrow interval despite the same marginal distributions.

## Stop and handoff

Report estimand, sampling law, dependence, finite-sample or asymptotic status and actual uncertainty interpretation. When the observation mechanism is absent, provide a conditional analysis rather than certify coverage; hand off the required design information.
