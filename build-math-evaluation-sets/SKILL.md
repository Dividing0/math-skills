---
name: build-math-evaluation-sets
description: "Build mathematical agent evaluation datasets with verified solutions, false premises, incomplete-input tasks, private rubrics, leakage audits and capability-stratified splits."
---

# Building Evaluation Sets

## Workflow

1. Define target abilities and coverage across fields, difficulty and failure modes.
2. Create or source problems with verified answers, including false premises and inconclusive cases.
3. Separate training examples, acceptance cases and hidden evaluation tasks.
4. Store inputs and private rubrics separately; record provenance and versions.
5. Audit ambiguity, answer leakage and duplicate tasks before use.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Runnable helper

Use [audit_dataset.py](scripts/audit_dataset.py) to audit task IDs, duplicate prompts, split leakage and evaluation score coverage. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
