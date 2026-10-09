---
name: compute-with-monte-carlo
description: "Design and execute Monte Carlo estimates with reproducible random streams, correct independent sampling units, variance reduction and uncertainty reporting. Use for integration and simulation estimates beyond fitting Bayesian models."
---

# Compute with Monte Carlo

## Workflow

1. Define the target expectation/integral, sampling law, estimator and required accuracy. Check integrability and variance assumptions; unbiasedness alone does not give a usable standard error.
2. Choose plain sampling or a justified variance-reduction method. Control variates require a known expectation and careful treatment of estimated coefficients; importance sampling requires support coverage and appropriate weights.
3. Use local random generators and record seeds, versions and workloads. Identify the independent unit: antithetic pairs, correlated chain samples and randomized quasi-Monte Carlo replicates do not share the same standard-error formula.
4. Separate sampling uncertainty from discretization, truncation and floating error. State whether intervals are approximate or based on a finite-sample theorem, and whether stopping was fixed or adaptive.
5. Validate the implementation on a known expectation and compare equal computational budgets where claiming efficiency. Avoid choosing a favorable seed or reusing evaluation data to tune the estimator without accounting for that selection.
6. Report the estimator, sample units, function evaluations, uncertainty, analytic checks and limitations. The polynomial helper is a controlled example; extend to task-specific integrands with the same evidence discipline.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [integrate_polynomial.py](scripts/integrate_polynomial.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
