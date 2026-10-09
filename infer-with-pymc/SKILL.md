---
name: infer-with-pymc
description: Build and execute Bayesian models using PyMC and ArviZ. Use for priors and likelihoods, posterior sampling, posterior predictive checks, Bayesian uncertainty and model diagnostics.
---

# Infer with PyMC

## Workflow
1. Specify generative assumptions, parameter support, units, shapes/dimensions and prior rationale. Confirm data independence or explicitly model dependence; aggregation to Binomial is justified only for common independent Bernoulli trials.
2. Build `pm.Model`, assign supported priors and observed likelihood; inspect shapes and initial log probability. Run prior predictive checks before posterior fitting and investigate impossible observations.
3. Inspect the installed PyMC version and sampling signature. Select sampler explicitly when backend defaults matter; use multiple chains, fixed seed, bounded warmup/draws and CPU cores. Preserve tuning separately from retained draws.
4. Use ArviZ to report R-hat, bulk/tail ESS and Monte Carlo standard errors; inspect divergences, energy and traces. A short smoke run is not a production convergence assessment. Fix parameterization or model identification before simply extending chains.
5. Compare with a conjugate or simulated known case when available; run posterior predictive checks and sensitivity to plausible priors. Separate posterior uncertainty from Monte Carlo error and model uncertainty. Hand interpretation to `research-bayesian-statistics`, `quantify-model-uncertainty` and `analyze-model-identifiability`.

## Execution and handoff
Read [the library playbook](references/library-playbook.md) for the API map, worked example and integration contract. Run `python scripts/example.py --self-test` with the interpreter selected by `run-math-python`; preserve stdout, stderr, exit status and dependency versions. Missing dependencies must produce a failed run, never a fabricated result. Keep the demonstration separate from the user's implementation.

Receive a mathematical statement, assumptions, input schema, target quantity, precision/tolerance and resource budget. Return runnable code, input provenance, versions, diagnostics, measured results, failed checks and limitations. Mark the result as exact on a specified finite object, numerical approximation, Monte Carlo estimate, or unexecuted; never label a computation a universal proof. Hand results to the named mathematical skill for interpretation and to `validate-math-implementation` for implementation checks.
