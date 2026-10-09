---
name: research-calculus-of-variations
description: "Analyze integral functionals, admissible curves and variational minimizers. Use when deriving first variations and boundary conditions, applying the direct method, testing second variations or separating stationarity from minimality."
---

# Calculus of Variations

## Workflow

1. Specify the functional, admissible space, constraints and boundary conditions.
2. Derive first variations with justified regularity and boundary terms.
3. Separate Euler-Lagrange stationarity from local or global minimality.
4. For existence check coercivity, compactness and lower semicontinuity in the chosen topology.
5. Examine relaxation, weak solutions and singular minimizers where relevant.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `simplify`, `factor`, `differentiate`, `integrate` or `solve` on specified expressions; retain denominator exclusions and branch assumptions. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
