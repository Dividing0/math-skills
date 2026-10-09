---
name: research-symplectic-geometry
description: "Analyze symplectic forms, Hamiltonian vector fields and local/global canonical structures. Use when checking closedness, nondegeneracy, exactness, Darboux scope or completeness of Hamiltonian flows."
---

# Symplectic Geometry

## Workflow

1. Specify the manifold, nondegenerate closed two-form and sign conventions.
2. Check nondegeneracy and closedness separately.
3. Distinguish symplectic, Hamiltonian and arbitrary vector fields.
4. Track local Darboux statements versus global topology and integrability.
5. Verify compactness and boundary assumptions before global flow or action claims.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `simplify`, `factor`, `differentiate`, `integrate` or `solve` on specified expressions; retain denominator exclusions and branch assumptions. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
