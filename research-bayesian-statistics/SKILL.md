---
name: research-bayesian-statistics
description: "Derive and assess Bayesian posteriors, predictive distributions and decision rules. Use when checking normalization, improper priors, conjugacy, Monte Carlo approximations or credible-region interpretations."
---

# Баєсівська статистика

## Workflow

1. Specify likelihood, prior, parameter domain and decision target.
2. Check posterior propriety and identifiability.
3. Separate exact posterior statements from approximation and sampling error.
4. Validate computation and sensitivity to priors, including weakly identified directions.
5. Distinguish credible regions, predictive distributions and frequentist coverage.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.
