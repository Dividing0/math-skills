---
name: research-linear-algebra
description: "Analyze linear maps, exact systems, rank, null spaces, eigenstructure and singular values; choose valid decompositions and separate exact algebra from conditioned numerical solves."
---

# Research Linear Algebra

## Workflow

1. Specify the scalar field, dimensions, maps and chosen bases.
2. Separate basis-independent statements from matrix representations; track rank, null spaces and compatibility.
3. Use decompositions with verified assumptions; distinguish eigenvalues from singular values and diagonalizable from defective matrices.
4. For numerical work use conditioning and stable solves rather than explicit inverses; distinguish exact rank from tolerance-based rank.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.
