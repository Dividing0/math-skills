---
name: build-math-definitions
description: "Define mathematical objects and operations with explicit domains and quantifiers. Use when constructing quotient operations, checking representative independence, comparing conventions or proving equivalence of definitions."
---

# Build Math Definitions

## Workflow

1. State the purpose and ambient setting, including underlying sets, structures, equivalence relations and notation.
2. Write the definition with explicit quantifiers and domain restrictions. Distinguish a definition from an existence assertion or theorem.
3. Check well-definedness: independence from representatives, coordinate choices, orderings and auxiliary constructions wherever applicable.
4. Construct ordinary examples, boundary examples and nonexamples. Check empty, singleton, zero and infinite cases when relevant.
5. Test compatibility with standard terminology. Verify proposed equivalent formulations in both directions under stated assumptions.
6. Return the definition, scope, examples, well-definedness argument and any unresolved existence or consistency obligations. Avoid claiming consistency of a foundational system from a few examples.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.
