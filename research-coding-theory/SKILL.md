---
name: research-coding-theory
description: "Analyze finite-field and nonlinear error-correcting codes. Use for generator matrices, minimum Hamming distance, rate bounds, unique or list decoding, erasures and exact code constructions."
---

# Теорія кодування

## Workflow

1. Specify alphabet, channel, block length and code class.
2. Track rate, distance and decoding criterion.
3. Distinguish unique, list and probabilistic decoding.
4. Verify bounds and encoding or decoding assumptions with exact finite constructions.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.

## Runnable helper

Use [linear_code.py](scripts/linear_code.py) to enumerate a small linear code over a prime field and find its minimum distance. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
