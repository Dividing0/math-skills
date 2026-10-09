---
name: research-optimal-transport
description: "Analyze transport plans/maps, marginals, cost integrability and dual certificates. Use when proving discrete optimality or auditing Monge existence, moment assumptions and regularization bias."
---

# Оптимальне транспортування

## Workflow

1. Specify spaces, measures, cost and moment assumptions.
2. Distinguish Kantorovich plans from Monge maps and their existence conditions.
3. Verify primal and dual feasibility, attainment and applicable duality.
4. Track entropic regularization bias and discretization separately.
5. For numerical work report transport marginal residuals and objective gaps rather than only solver termination.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.
