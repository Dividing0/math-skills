---
name: research-matroid-theory
description: "Analyze finite matroids through independence, rank, exchange, representations and minors. Use when verifying axioms, checking field dependence or justifying greedy optimization for bases or independent sets."
---

# Теорія матроїдів

## Workflow

1. Specify ground set and independent-set, rank or other axiom system.
2. Verify exchange and compatibility axioms.
3. Track duality, minors and representability over the stated field.
4. Use greedy optimality only with an applicable matroid structure.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Runnable helper

Use [check_matroid.py](scripts/check_matroid.py) to check every hereditary and exchange axiom in an explicitly listed finite independence system. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
