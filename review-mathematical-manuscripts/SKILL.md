---
name: review-mathematical-manuscripts
description: "Review theorem dependencies, proofs, contribution and reproducibility in a supplied mathematical manuscript. Use when assigning severity to gaps, proposing repairs and scoping correctness or novelty assessments."
---

# Review Mathematical Manuscripts

## Workflow

1. Read the complete supplied manuscript and state review scope and inaccessible materials.
2. Map main claims, proofs and dependencies; audit decisive steps before stylistic issues.
3. Check cited prior work from primary sources when available and qualify novelty assessments.
4. Separate fatal gaps, missing hypotheses, repairable arguments and exposition issues with precise locations.
5. Assess computational reproducibility and formal-checking claims from actual artifacts.
6. Return constructive findings and a justified recommendation if requested; respect confidentiality and do not contact others without authorization.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.
