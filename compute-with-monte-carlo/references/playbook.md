# Compute with Monte Carlo: playbook

## Variance and units

For IID contributions Y_i, the sample standard deviation divided by sqrt(n) estimates the standard error of the mean when the necessary variance assumptions hold. In antithetic sampling, average the paired contributions first and apply that formula across independent pairs.

The helper integrates a polynomial on a finite interval using uniform samples. A fixed control coefficient beta subtracts `beta*(X-E[X])` before interval scaling. For a linear integrand equal to X and beta=1, the adjusted contribution is constant; this is an analytic check, not a reason to expect zero variance generally.

A normal-approximation interval is not a finite-sample coverage guarantee. Repeatedly stopping when such an interval becomes favorable requires a sequentially valid method or an explicitly qualified result.

## Acceptance cases

- Antithetic pairs: use n pairs as independent units and report 2n evaluations.
- Constant integrand: report zero empirical variance without claiming a general estimator always has zero error.
- Importance weights miss part of the target support: reject the estimator's claimed correctness.
- Markov-chain samples are correlated: do not use IID standard errors unchanged.
- A control coefficient was fitted on the same sample: account for estimation or use independent pilot data.

## Primary sources

[NumPy random generator documentation](https://numpy.org/doc/stable/reference/random/generator.html) for generator control; mathematical variance and interval assumptions must be justified for the actual estimator.
