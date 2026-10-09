---
name: analyze-perturbations
description: "Analyze small-parameter equations and asymptotic approximations; choose regular expansions, boundary layers or multiple scales with explicit remainder norms and time horizons."
---

# Perturbation Analysis

## Workflow

1. Specify small parameter, limiting problem and output norm.
2. Check whether the limit is regular or singular.
3. Choose regular expansion, matched scales or another justified perturbation method.
4. Track solvability, resonances, boundary layers and remainders.
5. State uniformity and avoid extrapolating beyond the proved regime.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `series` to compute candidate expansions while retaining a separate remainder and uniformity argument. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
