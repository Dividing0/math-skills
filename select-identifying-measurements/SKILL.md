---
name: select-identifying-measurements
description: "Choose sensors, sampling times or interventions that identify model parameters. Use to remove observation-map nullspaces, break global symmetries, compare noisy information and assess feasible measurement costs."
---

# Вибір ідентифікувальних вимірювань

## Workflow

1. Specify forward model, unknowns and current observation map.
2. Identify symmetries, null directions and practical weak information.
3. Propose additional sensors, times or interventions that break these ambiguities.
4. Compare local information criteria with global distinguishability.
5. Return cost-aware designs and explicit identifiability limitations.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.
