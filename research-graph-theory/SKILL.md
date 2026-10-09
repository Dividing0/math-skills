---
name: research-graph-theory
description: "Analyze finite or infinite graph structure, connectivity, paths, Euler trails and extremal bounds. Use when producing graph witnesses or auditing directedness, loops and parallel-edge conventions."
---

# Research Graph Theory

## Workflow

1. Specify directedness, loops, parallel edges, weights and finite or infinite scope.
2. Distinguish walks, paths, trails and induced subgraphs.
3. Verify structural theorem hypotheses and construct extremal examples.
4. For computational outputs check witnesses and distinguish failure to find from proof of absence.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Host computation

When the `analyze-graphs-with-networkx` skill is installed alongside this skill, use `summary`, `shortest-path` or `max-flow` for an explicit finite simple graph; preserve isolates, directions and weight semantics. Use its [graph_report.py](../analyze-graphs-with-networkx/scripts/graph_report.py) helper and [input/command reference](../analyze-graphs-with-networkx/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
