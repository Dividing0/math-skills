---
name: prove-with-energy-methods
description: "Derive ODE or PDE energy estimates, decay and uniqueness bounds using justified integration by parts, boundary fluxes, coercivity and Gronwall inequalities."
---

# Доведення енергетичними методами

## Workflow

1. Define the energy, solution space and allowed regularity.
2. Derive the balance with boundary terms and justify integration by parts.
3. Check coercivity and signs; identify dissipation and forcing.
4. Use the appropriate integral inequality and track constants and time dependence.
5. Distinguish a priori estimates from existence, uniqueness or regularity; close each additional obligation.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `dynamics` for an autonomous field Jacobian, equilibrium residual or candidate invariant Lie derivative; local symbolic identities do not settle global behavior. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
