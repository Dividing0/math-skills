---
name: validate-mathematical-models
description: "Validate mechanistic or predictive models for a specified operating domain using independent observations, conservation checks, frozen calibration, error thresholds and uncertainty accounting."
---

# Validate Mathematical Models

## Workflow

1. Define intended use, accuracy thresholds, operating regimes and failure costs.
2. Separate calibration, model selection and independent validation data; respect temporal and grouped dependence.
3. Check conservation and known limiting behavior before empirical comparisons.
4. Compare residuals and predictive performance with baselines; test systematic errors, extrapolation and distribution changes.
5. Include observation and numerical uncertainty and assess whether the validation design supports the claimed scope.
6. Return a scoped validity assessment, failed conditions and revision needs; calibration fit alone does not establish validity.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

When the `analyze-data-with-statsmodels` skill is installed alongside this skill, fit an explicit OLS design with conventional or HC3 covariance and independent prediction rows; sampling assumptions and temporal/causal validity remain separate. Use its [fit_ols.py](../analyze-data-with-statsmodels/scripts/fit_ols.py) helper and [input/command reference](../analyze-data-with-statsmodels/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
