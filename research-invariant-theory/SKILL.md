---
name: research-invariant-theory
description: "Compute and audit polynomial invariants of group actions, invariant-ring generation, relations and orbit separation with explicit fields, characteristic and quotient hypotheses."
---

# Invariant Theory

## Workflow

1. Specify group action, representation and base field.
2. Compute or characterize invariant objects and verify invariance.
3. Distinguish generation, relations and separation of orbits.
4. Check reductivity, characteristic and finiteness assumptions.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `matrix` for exact finite matrix rank/nullspace or `groebner` for rational polynomial ideal reductions; retain the field, parameter and theorem hypotheses. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
