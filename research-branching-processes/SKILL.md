---
name: research-branching-processes
description: "Analyze Galton–Watson offspring laws, generating functions, extinction fixed points and expected population growth; check independence, critical degeneracy and model extensions."
---

# Branching Processes

## Workflow

1. Specify offspring law, generation structure and dependence.
2. Check generating functions and relevant moments.
3. Distinguish extinction probability, expected growth and survival-conditioned behavior.
4. Treat critical and degenerate cases explicitly.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Runnable helper

Use [extinction.py](scripts/extinction.py) to bracket the extinction probability of a finite-support Galton-Watson process with exact rationals. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
