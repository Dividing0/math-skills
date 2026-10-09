---
name: design-computer-assisted-proofs
description: "Design rigorous enumeration, interval and algebraic-certificate proofs. Use when splitting analytic and computational obligations, proving coverage, selecting arithmetic, or minimizing the trusted checker."
---

# Проєктування комп’ютерних доведень

## Workflow

1. Decompose the mathematical claim into analytic and finite computational obligations.
2. Specify exact domains, arithmetic and coverage of the search.
3. Design certificates or rigorous enclosures and a minimal trusted checker.
4. Account for rounding, termination and excluded cases.
5. Report discharged and unresolved obligations separately; an experimental program is not automatically a proof.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.
