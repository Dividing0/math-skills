---
name: research-percolation-theory
description: "Analyze site or bond connectivity probabilities and infinite-cluster events. Use when checking edge dependence, finite-size evidence, path bounds and graph-specific threshold claims."
---

# Теорія перколяції

## Workflow

1. Specify graph, site or bond model and independence.
2. Distinguish finite connection probabilities from infinite-cluster events.
3. Check dimension and geometry in threshold results.
4. Separate numerical threshold estimates from rigorous bounds.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Runnable helper

Use [bond_connection.py](scripts/bond_connection.py) to enumerate exact two-terminal connection probabilities in a small independent bond-percolation graph. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
