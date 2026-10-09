---
name: prove-with-duality
description: "Construct proofs using primal-dual bounds, feasible witnesses, convex constraint qualifications and continuous-dual pairings. Use when certifying optimality or auditing duality gaps and attainment."
---

# Доведення через двоїстість

## Workflow

1. Specify primal and dual objects, pairing and ambient topology.
2. Prove weak duality with the correct inequality direction.
3. Verify hypotheses for strong duality or separation.
4. Track dual attainment and multipliers independently from equality of optimal values.
5. Construct primal-dual witnesses and quantify any remaining gap.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `verify-proof-certificates` skill is installed alongside this skill, check rational primal-dual LP witnesses with the documented inequality convention; feasibility and objective equality must all hold. Use its [check_certificate.py](../verify-proof-certificates/scripts/check_certificate.py) helper and [input/command reference](../verify-proof-certificates/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
