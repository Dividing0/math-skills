---
name: research-queueing-theory
description: "Analyze queue occupancy, delay and stability using arrival and service laws, stationary balance and Little’s relation; verify M/M/1 or M/G/1 formula hypotheses."
---

# Теорія масового обслуговування

## Workflow

1. Specify arrival, service, routing and capacity assumptions.
2. Check stability and stationary-regime existence.
3. Distinguish sample-path, expected and tail quantities.
4. Verify assumptions before Little or special queue formulas.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Runnable helper

Use [mm1.py](scripts/mm1.py) to evaluate exact stationary M/M/1 queue formulas with an explicit stability check. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
