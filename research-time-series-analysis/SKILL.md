---
name: research-time-series-analysis
description: "Analyze dependence, stationarity, AR models and forecast uncertainty; derive temporal moments, distinguish ergodicity and evaluate forecasts with leakage-free chronological validation."
---

# Аналіз часових рядів

## Workflow

1. Specify time index, sampling, target horizon and observation mechanism.
2. Check stationarity, ergodicity and dependence assumptions separately.
3. Distinguish descriptive fitting, prediction and causal inference.
4. Use temporal validation and handle seasonality, missingness and regime changes.
5. Verify residual structure and uncertainty calibration; avoid random-split leakage.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.
