---
name: build-mathematical-models
description: "Construct stock-flow, compartment and spatial models with units, constitutive assumptions and measurement maps. Use when translating a practical system into equations and identifying calibration or validation needs."
---

# Build Mathematical Models

## Workflow

1. Define the decision or prediction target, observables, system boundary and time and length scales.
2. Choose variables, units, parameters, conservation laws and constitutive assumptions; separate measured facts from modeling choices.
3. Write equations, constraints, initial and boundary conditions and a measurement model.
4. Check dimensional consistency, conservation, positivity and well-posedness; identify simplifications and competing model classes.
5. Analyze identifiable parameters and data needs before calibration; choose a baseline model and independent validation conditions.
6. Return equations, assumptions, valid regimes, calibration plan and testable predictions; route numerical implementation to existing algorithm skills.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Host computation

When the `nondimensionalize-models` skill is installed alongside this skill, compute rational dimensionless exponent vectors for supplied quantities and base units; physical assumptions and transformed initial/boundary data remain separate. Use its [dimensionless_groups.py](../nondimensionalize-models/scripts/dimensionless_groups.py) helper and [input/command reference](../nondimensionalize-models/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
