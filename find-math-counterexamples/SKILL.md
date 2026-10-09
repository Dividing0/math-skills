---
name: find-math-counterexamples
description: "Use to disprove mathematical statements, test necessity of hypotheses, challenge conjectures or construct examples that expose proof failures."
---

# Find Math Counterexamples

## Workflow

1. Write the exact target and its logical negation. Identify which hypotheses must hold and which conclusion must fail.
2. Search minimal finite or low-dimensional cases first, then boundary, singular, infinite and pathological constructions appropriate to the domain.
3. Use systematic enumeration, symbolic calculation or numerical searches as discovery tools. Record bounds and arithmetic; verify any candidate exactly or with rigorous certified bounds.
4. Check every hypothesis individually and show the failed conclusion explicitly. A candidate outside the domain is not a counterexample.
5. When testing one hypothesis, preserve the others. Distinguish refuting a theorem from refuting only a proposed proof step.
6. Return a reproducible witness, verification and implications for repairing the statement. If none is found, report search scope and inconclusiveness rather than validity.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

For finite classical propositional claims, use [truth_table.py](../research-mathematical-logic/scripts/truth_table.py) to obtain an exhaustive countermodel; see its [input reference](../research-mathematical-logic/references/command-line.md). For finite topological witnesses, use [finite_topology.py](../research-general-topology/scripts/finite_topology.py) to check open-set axioms, separation and closure; see its [input reference](../research-general-topology/references/command-line.md). These helpers require the owning skills alongside this skill. Adapt `--example` requests to the actual negation, check every original hypothesis, and retain the finite search scope; no counterexample found does not settle unrelated or infinite claims.
