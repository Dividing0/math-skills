---
name: formulate-math-problem
description: "Turn informal mathematical requests into explicit domains, quantifiers, feasible sets and success criteria. Use when specifying existence, optimization, approximation or inverse problems before solving."
---

# Formulate Math Problem

## Workflow

1. Extract the goal, given information and desired output before selecting methods. Preserve the original question alongside the formal version.
2. Define objects, domains, notation, units where relevant, quantifier order and dependencies. Distinguish fixed parameters, variables and unknowns.
3. Separate supplied facts from modeling assumptions. Record ambiguities and provide conditional formulations when they change the answer; ask only for consequential missing information.
4. Specify existence, uniqueness, exact versus approximate solutions and required tolerances separately. Check feasibility, empty domains and degenerate cases.
5. Produce a problem specification with assumptions, examples, nonexamples, success criteria and unresolved choices. Route proof, literature or implementation work to the relevant skill.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.
