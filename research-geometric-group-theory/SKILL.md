---
name: research-geometric-group-theory
description: "Analyze finitely generated groups through word metrics, Cayley graphs, growth and quasi-isometry. Use when comparing generating sets, deriving coarse bounds or distinguishing algebraic and geometric equivalence."
---

# Geometric Group Theory

## Workflow

1. Specify group, generators and metric construction.
2. Distinguish generator-dependent metrics from quasi-isometry classes.
3. Check finite-generation and properness assumptions.
4. Separate algebraic isomorphism, quasi-isometry and coarse invariants.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `research-abstract-algebra` skill is installed alongside this skill, check explicit finite group multiplication tables and element/conjugacy data; extending these results to group presentations or infinite groups requires separate justification. Use its [finite_group.py](../research-abstract-algebra/scripts/finite_group.py) helper and [input/command reference](../research-abstract-algebra/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
