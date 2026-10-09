# Posterior measures before posterior summaries

## Method branches
1. For a conjugate model, multiply likelihood and prior, collect exponents and check a finite positive normalizer. State parameter support and whether observations are conditionally independent; conjugacy is an algebraic shortcut rather than an excuse to skip the measure.
2. For an improper prior, test the posterior normalizing integral explicitly for the actual data. An improper density is not itself a probability distribution, and evidence or Bayes factors may remain undefined even when a posterior is proper.
3. For MCMC, define the invariant target and report convergence diagnostics, effective sample sizes and Monte Carlo error. Multiple chains and diagnostics can expose failures but cannot automatically prove mixing or independence.
4. For decision making, integrate the declared loss under the posterior and compare actions. A posterior mean is optimal for squared loss when the required second moments and action space are suitable; absolute loss instead leads to medians.

## Worked calculation
Let θ∈(0,1), θ∼Beta(2,3), and observe one Bernoulli success. The likelihood contributes θ, so posterior density is proportional to θ²(1-θ)², namely Beta(3,3). Its mean is 3/(3+3)=1/2. The posterior predictive success probability for another conditionally independent trial is E[θ|data]=1/2. This predictive statement integrates parameter uncertainty rather than substituting an arbitrary point estimate.

## Tempting inference and counterexample
A 95% credible region need not have 95% repeated-sampling coverage at each true parameter. With a uniform Beta(1,1) prior and one Bernoulli trial, the posteriors are Beta(1,2) after failure and Beta(2,1) after success. Their equal-tailed 95% intervals have lower endpoints 1-sqrt(0.975) and sqrt(0.025), respectively. Both exceed 0.001, so at true θ=0.001 neither possible interval contains θ. Each still has posterior probability 0.95 under its stated posterior.

## Stop and handoff
Stop posterior-probability reporting when normalization is infinite or unresolved. Hand off likelihood, support, prior measure, normalization argument, approximation method, diagnostics and prior-sensitivity results. Distinguish posterior predictive uncertainty, parameter uncertainty and Monte Carlo noise. For coverage claims route to a frequentist evaluation using a stated data-generating family and repeated-sampling criterion.
