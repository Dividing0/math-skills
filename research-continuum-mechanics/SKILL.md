---
name: research-continuum-mechanics
description: "Analyze deformation gradients, stress measures, mass balance and constitutive objectivity. Use when deriving continuum models, checking finite/small-strain assumptions or preparing mechanical PDEs."
---

# Continuum Mechanics

## Workflow

1. Specify reference and current configurations and kinematics.
2. Track conservation laws, constitutive assumptions and units.
3. Check objectivity, admissibility and boundary conditions.
4. Separate material-model validity from mathematical solvability.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `nondimensionalize-models` skill is installed alongside this skill, compute rational dimensionless exponent vectors for supplied quantities and base units; physical assumptions and transformed initial/boundary data remain separate. Use its [dimensionless_groups.py](../nondimensionalize-models/scripts/dimensionless_groups.py) helper and [input/command reference](../nondimensionalize-models/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
