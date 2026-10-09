# Simulate Stochastic Differential Equations: playbook

## Calibration model

For Ito `dX = a X dt + b X dW`, the exact solution is `X_T = X_0 exp((a-b²/2)T + bW_T)`. A Stratonovich drift coefficient `a` becomes Ito drift `a+b²/2`. The helper uses this conversion and compares Euler-Maruyama and scalar Milstein on two coupled step sizes against the same exact terminal paths.

Strong RMSE compares approximate and exact values on each shared Brownian path. Mean error is a different statistic and has sampling uncertainty. A two-level observed order, especially near roundoff or zero diffusion, does not certify an asymptotic rate.

For general SDEs, use an appropriate solver such as Diffrax after checking noise structure and convention. Preserve reproducible paths during adaptive refinement; drawing a fresh increment after each rejected step changes the experiment.

## Acceptance cases

- Ito and Stratonovich models share written coefficients: account for their different drift semantics.
- Refined trajectories use independent noise: do not report their difference as strong error.
- Zero diffusion: reduce to a deterministic problem; do not force an SDE rate interpretation.
- Euler produces negative GBM values: report the scheme limitation instead of silently clipping.
- Finite trajectory sample looks stable: do not infer global nonexplosion.

## Primary sources

[Diffrax solver selection](https://docs.kidger.site/diffrax/usage/how-to-choose-a-solver/) documents convention and noise-dependent solver choices.
