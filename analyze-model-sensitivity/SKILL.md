---
name: analyze-model-sensitivity
description: "Analyze parameter/input sensitivity using Jacobians, adjoints, finite perturbations and variance attribution. Use when ranking model influence, validating derivatives or assessing robustness under declared perturbations."
---

# Analyze Model Sensitivity

## Workflow

1. Define output quantities, parameter ranges, units and the distribution or feasible region of inputs.
2. Choose local derivatives, adjoints, perturbation experiments or global sensitivity according to nonlinearity and interactions.
3. Distinguish absolute and normalized sensitivity; treat zero baselines and disparate scales explicitly.
4. Validate derivatives or surrogate approximations and separate solver error from genuine model response.
5. Account for dependent inputs before using variance-based decompositions; test interaction and structural model changes.
6. Report sensitivity measures, validity ranges and numerical uncertainty without confusing sensitivity with causality or identifiability.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.
