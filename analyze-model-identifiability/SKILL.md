---
name: analyze-model-identifiability
description: "Determine structural or practical identifiability from parameter-to-observation maps. Use for parameter symmetries, local versus global uniqueness, sensitivity rank, likelihood profiles or ambiguous inverse estimates."
---

# Analyze Model Identifiability

## Workflow

1. Specify the forward map, observations, unknown parameters, nuisance variables and admissible domain.
2. Distinguish structural uniqueness with ideal data from practical estimation under finite noisy data.
3. Search symmetries and invariant parameter combinations; use rank or sensitivity diagnostics with their local limitations.
4. Test global ambiguities and parameter boundaries; do not interpret local Jacobian rank as automatic global identifiability.
5. Quantify practical ambiguity through profiles, posterior structure or singular values with justified scaling.
6. Return identifiable combinations, assumptions, ambiguous alternatives and experiments that can distinguish them.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.
