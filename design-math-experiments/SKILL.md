---
name: design-math-experiments
description: "Design measurements or interventions for model discrimination and parameter estimation. Use when choosing design matrices, measurement times, noise-aware criteria or confirmatory experiments."
---

# Планування експериментів для моделей

## Workflow

1. Specify hypotheses, quantities to observe and controllable interventions.
2. Choose experiments that distinguish competing models or parameter combinations.
3. Account for observation noise, dependence and feasible design constraints.
4. Separate discovery, calibration and confirmatory analysis.
5. Predefine success criteria and report whether the design supports causal or merely predictive claims.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `matrix` for numerical singular values and rank diagnostics, or `propagate-covariance` with a supplied sensitivity matrix; rank is a local diagnostic with a stated cutoff. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
