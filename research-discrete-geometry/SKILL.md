---
name: research-discrete-geometry
description: "Analyze finite configurations, incidence counts, convexity, packings and coverings. Use for convex-combination certificates, separating functionals, realizability, general-position assumptions and extremal bounds."
---

# Research Discrete Geometry

## Workflow

1. Specify dimension, metric and degeneracy or general-position assumptions.
2. Check incidence and orientation predicates using exact or robust arithmetic.
3. Separate combinatorial and geometric realizability requirements.
4. For packing and covering distinguish feasible constructions from proven optimality bounds.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.

## Host computation

When the `research-computational-geometry` skill is installed alongside this skill, compute exact planar orientation or convex hulls from rational coordinates; this addresses finite planar constructions only. Use its [planar_geometry.py](../research-computational-geometry/scripts/planar_geometry.py) helper and [input/command reference](../research-computational-geometry/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
