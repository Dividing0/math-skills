---
name: evaluate-math-agents
description: "Evaluate mathematics agents with hidden task rubrics, matched budgets and task-level evidence. Use when auditing correctness, comparing skill conditions, testing regressions or assessing claims of performance improvement."
---

# Оцінювання математичних агентів

## Workflow

1. Define the capability, task distribution and comparison question before evaluation.
2. Use fresh held-out tasks and keep rubrics and answers hidden from solving agents.
3. Match models, tool permissions, budgets and prompts across conditions except the tested skill.
4. Score correctness, hypothesis handling, evidence honesty and partial progress with adjudication.
5. Report task-level outcomes, uncertainty, costs and contamination risks; no causal benefit claim from an uncontrolled demonstration.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.
