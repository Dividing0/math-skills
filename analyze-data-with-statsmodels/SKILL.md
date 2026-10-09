---
name: analyze-data-with-statsmodels
description: Fit and diagnose statistical models with statsmodels. Use for regression, GLM, hypothesis tests, uncertainty estimates, time-series estimation and comparisons of statistical specifications.
---

# Analyze Data with statsmodels

## Workflow
1. Specify the estimand, observational unit, sampling process, variables, transformations, missing-data policy and train/test split. Distinguish prediction, association and causal identification.
2. Align response and design rows before conversion. For `sm.OLS`, explicitly add an intercept when intended and set `missing="raise"`; formula interfaces may add one. Check finite inputs, sample size, design rank and conditioning before interpreting coefficients.
3. Match response support to likelihood and link for GLM. Detect logistic separation; a convergence flag does not establish a finite MLE. For time series preserve chronology and sampling interval; inspect residual dependence and avoid future-data leakage.
4. Choose covariance using the sampling/error structure: conventional, HC3, cluster or HAC with justified groups/lags. Robust covariance does not repair omitted confounders or endogeneity. State null, alternative, test level and multiple-testing handling.
5. Validate estimates with an independent analytic/small-data calculation, inspect residuals, confidence or prediction intervals and out-of-sample loss as appropriate. Hand interpretation to `research-mathematical-statistics`, `research-causal-inference` or `research-time-series-analysis`.

## Execution and handoff
Read [the library playbook](references/library-playbook.md) for the API map, worked example and integration contract. Run `python scripts/example.py --self-test` with the interpreter selected by `run-math-python`; preserve stdout, stderr, exit status and dependency versions. Missing dependencies must produce a failed run, never a fabricated result. Keep the demonstration separate from the user's implementation.

Receive a mathematical statement, assumptions, input schema, target quantity, precision/tolerance and resource budget. Return runnable code, input provenance, versions, diagnostics, measured results, failed checks and limitations. Mark the result as exact on a specified finite object, numerical approximation, Monte Carlo estimate, or unexecuted; never label a computation a universal proof. Hand results to the named mathematical skill for interpretation and to `validate-math-implementation` for implementation checks.

## Runnable helper

Use [fit_ols.py](scripts/fit_ols.py) to fit a user-supplied full-rank OLS design with conventional or HC3 uncertainty. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
