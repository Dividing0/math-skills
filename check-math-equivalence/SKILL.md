---
name: check-math-equivalence
description: "Check equivalence of equations, substitutions, optimization or differential formulations. Use when auditing transformations, lost solutions, domain restrictions, inverse maps or one-way implications."
---

# Mathematical Equivalence Checking

## Workflow

1. State the two formulations and common domain.
2. Construct transformations in both directions.
3. Check inverses, lost solutions, boundary cases and auxiliary choices.
4. For solution sets distinguish bijection, implication and approximation.
5. Report equivalence only under explicitly verified assumptions.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `simplify`, `factor`, `differentiate`, `integrate` or `solve` on specified expressions; retain denominator exclusions and branch assumptions. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
