---
name: analyze-bifurcations
description: "Analyze parameter-dependent equilibria and periodic orbits; classify saddle-node, transcritical, pitchfork or Hopf candidates by nondegeneracy, crossing conditions and local stability."
---

# Bifurcation Analysis

## Workflow

1. Specify dynamics, parameters and branch of equilibria or periodic solutions.
2. Locate loss of hyperbolicity and candidate critical parameters.
3. Check nondegeneracy and transversality for the proposed bifurcation theorem.
4. Derive a justified reduction or normal form and its valid neighborhood.
5. Separate local bifurcation from global structure and numerical diagrams from proof.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `dynamics` for an autonomous field Jacobian, equilibrium residual or candidate invariant Lie derivative; local symbolic identities do not settle global behavior. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
