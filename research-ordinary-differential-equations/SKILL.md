---
name: research-ordinary-differential-equations
description: "Analyze initial-value ODEs, maximal solution intervals, equilibria and numerical trajectories. Use when checking local existence, uniqueness, continuation, invariant regions, blow-up or stability hypotheses."
---

# Research Ordinary Differential Equations

## Workflow

1. State state space, regularity, initial conditions and solution notion.
2. Check local existence, uniqueness and maximal interval separately.
3. Analyze equilibria, invariants, blow-up and stiffness.
4. For numerics monitor tolerances and events; distinguish a solver trajectory from a proof of global existence.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `compute-with-scipy` skill is installed alongside this skill, use `polynomial-ivp` for a specified autonomous polynomial vector field; a successful trajectory is numerical evidence with local solver tolerances. Use its [numerical.py](../compute-with-scipy/scripts/numerical.py) helper and [input/command reference](../compute-with-scipy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.

## Related workflow

When algebraic constraints accompany differential equations, use the DAE workflow to establish consistent initial data, index assumptions and constraint residuals. Read [solve-differential-algebraic-equations](../solve-differential-algebraic-equations/SKILL.md) when that specialization is needed and available.
