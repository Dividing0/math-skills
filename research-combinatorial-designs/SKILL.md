---
name: research-combinatorial-designs
description: "Construct and verify block designs using incidence counts, parameter constraints and exact pair coverage. Use when auditing design existence or checking finite block lists and repetitions."
---

# Комбінаторні дизайни

## Workflow

1. Specify block parameters, repetitions and incidence conditions.
2. Derive necessary divisibility and counting conditions.
3. Distinguish necessary conditions from constructive existence.
4. Verify every incidence count in proposed designs.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Runnable helper

Use [check_design.py](scripts/check_design.py) to check every point and pair in a finite block design. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
