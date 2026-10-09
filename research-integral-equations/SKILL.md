---
name: research-integral-equations
description: "Analyze first-kind, second-kind and singular integral equations in named function spaces. Use when applying Neumann or Fredholm methods, checking compatibility or separating small residuals from stable inversion."
---

# Інтегральні рівняння

## Workflow

1. Specify kernel, function spaces and integral interpretation.
2. Distinguish first-kind, second-kind and singular equations.
3. Check boundedness, compactness and Fredholm hypotheses.
4. Separate solvability, uniqueness and numerical regularization.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `tikhonov` or `least-squares` for a supplied finite forward matrix and data; report residuals, numerical rank and regularization bias. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
