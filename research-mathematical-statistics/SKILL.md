---
name: research-mathematical-statistics
description: "Develop estimators, confidence procedures and asymptotic inference under specified sampling and dependence; verify identifiability, coverage, selection and uncertainty interpretation."
---

# Research Mathematical Statistics

## Workflow

1. Specify estimand, sampling mechanism, model and dependence.
2. Check identifiability and distinguish likelihood, estimator and inferential procedure.
3. State finite-sample versus asymptotic guarantees and handle multiple comparisons.
4. Distinguish statistical significance, effect size and practical meaning; validate intervals and avoid data leakage.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Host computation

When the `analyze-data-with-statsmodels` skill is installed alongside this skill, fit an explicit OLS design with conventional or HC3 covariance and independent prediction rows; sampling assumptions and temporal/causal validity remain separate. Use its [fit_ols.py](../analyze-data-with-statsmodels/scripts/fit_ols.py) helper and [input/command reference](../analyze-data-with-statsmodels/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.

## Related workflow

For population-risk guarantees after hypothesis selection, use the learning-theory workflow to identify the comparator, class complexity and data-reuse assumptions. Read [research-statistical-learning-theory](../research-statistical-learning-theory/SKILL.md) when that specialization is needed and available.
