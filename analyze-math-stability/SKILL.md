---
name: analyze-math-stability
description: "Analyze Lyapunov, asymptotic, exponential or input stability of equilibria and dynamical systems; use for linearization, decay bounds, basin claims or perturbation robustness."
---

# Mathematical Stability Analysis

## Workflow

1. Define the object, topology, admissible perturbations and exact stability notion.
2. Choose Lyapunov, spectral, structural or numerical analysis to match that notion.
3. Verify linearization and regularity assumptions.
4. Quantify bounds, neighborhoods and parameter dependence.
5. Distinguish boundedness, attraction, robustness and well-conditioning.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `stability` on a supplied continuous or discrete state matrix; boundary spectra and nonlinear stability require additional analysis. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
