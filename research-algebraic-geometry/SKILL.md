---
name: research-algebraic-geometry
description: "Analyze affine/projective schemes, coordinate rings, morphisms and base changes. Use when proving scheme equivalence, checking smoothness, distinguishing rational/geometric points or auditing ideal computations."
---

# Research Algebraic Geometry

## Workflow

1. Specify the base field or ring and whether objects are varieties or schemes.
2. Distinguish geometric points, rational points and scheme-theoretic structure.
3. Track reducedness, smoothness, irreducibility and base-change assumptions separately.
4. Use computational ideals with exact arithmetic and verify how affine calculations cover global objects.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `matrix` for exact finite matrix rank/nullspace or `groebner` for rational polynomial ideal reductions; retain the field, parameter and theorem hypotheses. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
