---
name: construct-math-proofs
description: "Use for proving mathematical claims, selecting proof strategies, building lemmas and turning proof sketches into complete arguments."
---

# Construct Math Proofs

## Workflow

1. Normalize the exact claim, quantifier order, hypotheses and ambient definitions. Check simple counterexamples before committing to a proof strategy.
2. Choose direct proof, contrapositive, contradiction, induction, construction, extremal argument or another justified method. Explain the obligations introduced by the choice.
3. Decompose into lemmas and record dependencies. Verify cited theorem hypotheses at the application site and avoid circular arguments.
4. Write each substantive implication with justification. Track domains, signs, division by zero, convergence, compactness and interchange of limits or integrals as relevant.
5. Check endpoints and degenerate cases. Distinguish existence from uniqueness, necessity from sufficiency and local from global conclusions.
6. Return a complete proof only when every obligation is discharged. Otherwise return a labeled partial argument with the exact gap; never fabricate a lemma to bridge it. Route formal checking separately and report actual checker status.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.
