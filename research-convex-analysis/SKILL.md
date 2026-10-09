---
name: research-convex-analysis
description: "Study convex functions, subgradients, normal cones and duality in stated topologies. Use when checking minimizer attainment, nonsmooth optimality, qualification conditions or finite versus infinite-dimensional arguments."
---

# Опуклий аналіз

## Workflow

1. Specify the ambient space, topology and extended-real conventions.
2. Check properness, convexity and lower semicontinuity separately.
3. Distinguish gradients, subgradients and normal cones.
4. Verify qualification conditions for subdifferential rules and duality.
5. Track attainment, zero duality gap and existence of multipliers as separate properties.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

For attainment, distinguish finite-dimensional compact sublevel arguments from infinite-dimensional weak compactness and lower semicontinuity in the chosen topology.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `verify-proof-certificates` skill is installed alongside this skill, check rational primal-dual LP witnesses with the documented inequality convention; feasibility and objective equality must all hold. Use its [check_certificate.py](../verify-proof-certificates/scripts/check_certificate.py) helper and [input/command reference](../verify-proof-certificates/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
