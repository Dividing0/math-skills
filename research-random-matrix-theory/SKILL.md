---
name: research-random-matrix-theory
description: "Analyze random matrix ensembles, trace moments and empirical spectra with explicit normalization. Use when checking Wigner hypotheses, dependence and moment conditions, or distinguishing bulk laws from edge and eigenvector claims."
---

# Random Matrix Theory

## Workflow

1. Specify matrix ensemble, normalization and dependence.
2. Check moment, symmetry and dimensional-limit assumptions.
3. Distinguish bulk, edge and eigenvector conclusions.
4. Separate typical, expected and almost-sure results.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `matrix` for a supplied finite discretization or sampled matrix; finite spectral diagnostics do not establish infinite-dimensional operator claims or asymptotic ensemble laws. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
