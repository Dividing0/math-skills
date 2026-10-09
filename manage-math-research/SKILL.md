---
name: manage-math-research
description: "Plan and track mathematical research projects through conjecture and lemma dependencies, bounded milestones, experiment records, evidence status and explicit pivot criteria."
---

# Manage Math Research

## Workflow

1. Define research goals, deliverables, constraints and a bounded first milestone.
2. Track definitions, conjectures, lemmas, proof attempts, failed approaches and sources in a dependency map.
3. Prioritize uncertainties and discriminating experiments; set stopping or pivot criteria.
4. Preserve reproducible calculations and record evidence status rather than only polished results.
5. Review progress against milestones and revise plans when hypotheses fail.
6. Return actionable next steps with dependencies and risks; do not promise resolution of an open problem on a schedule.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Runnable helper

Use [dependencies.py](scripts/dependencies.py) to audit a mathematical dependency ledger for cycles and unresolved prerequisites. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
