---
name: research-dynamical-systems
description: "Study flows, maps, equilibria, invariant sets and local or global stability; select linearization, Lyapunov or invariance arguments and resolve nonhyperbolic cases."
---

# Research Dynamical Systems

## Workflow

1. Specify phase space, flow or map and invariant sets.
2. Distinguish local, global, Lyapunov and asymptotic stability.
3. Check hyperbolicity before linearization-based conclusions; investigate center behavior separately.
4. Use Lyapunov or bifurcation methods with explicit regimes; do not infer chaos solely from a plotted trajectory.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `dynamics` for an autonomous field Jacobian, equilibrium residual or candidate invariant Lie derivative; local symbolic identities do not settle global behavior. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
