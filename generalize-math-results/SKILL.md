---
name: generalize-math-results
description: "Extend a mathematical theorem to weaker assumptions, larger spaces or sharper bounds by mapping proof dependencies, testing counterexamples and proving the original as a special case."
---

# Generalize Math Results

## Workflow

1. Capture the original theorem exactly, with its proof and definitions when available. Build a map from each hypothesis to proof steps that use it.
2. Choose an axis of generalization: weaker assumption, broader space, stronger bound, parameter extension or alternate structure. Change one axis at a time initially.
3. Construct counterexamples at the proposed boundary and identify replacement conditions or invariants sufficient for the proof.
4. Rework the proof rather than copying it unchanged. Check that the proposed result contains the original as a special case under an explicit translation.
5. Distinguish a proved extension, plausible conjecture and failed generalization. Verify related literature before asserting novelty or sharpness.
6. Return original and proposed statements, hypothesis comparison, proof or exact unresolved gaps, counterexamples and limits. Claim an optimal bound only with a matching obstruction or proof of optimality.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.
