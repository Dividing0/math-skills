---
name: simulate-stochastic-differential-equations
description: "Formulate and simulate SDEs with explicit Ito or Stratonovich interpretation, coupled Brownian paths and strong/weak error checks. Use for stochastic numerical integration, not deterministic ODE tolerances alone."
---

# Simulate Stochastic Differential Equations

## Workflow

1. Specify state, filtration, drift, diffusion, initial law, time horizon and integral convention. Check existence/uniqueness or identify the intended solution notion; local Lipschitz conditions alone need an additional nonexplosion argument for global conclusions.
2. Match the method to the convention, noise dimensions and regularity. Include the drift correction when converting Stratonovich to Ito. Do not assume multidimensional diagonal noise automatically satisfies the required commutativity condition.
3. Use a local seeded generator and record its implementation/version. Couple refinements with aggregated Brownian increments; independent paths at different step sizes confound pathwise discretization error with sampling variation.
4. Separate strong pathwise error, weak observable bias and Monte Carlo uncertainty. Use a known exact solution or a justified fine reference; empirical convergence slopes are evidence rather than a convergence theorem.
5. Inspect positivity, explosions, boundary conditions and scheme bias. Euler updates can violate positivity even when the exact process stays positive; projection or clipping changes the scheme and must be justified.
6. Report the actual method, convention, workload, seed, error measures and confidence limitations. Use the scalar GBM helper as a calibrated experiment and a task-specific solver for other SDE families.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [simulate_gbm.py](scripts/simulate_gbm.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
