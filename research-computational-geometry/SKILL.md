---
name: research-computational-geometry
description: "Develop geometric algorithms with robust predicates and explicit degeneracy policies. Use for orientation, convex hulls, segment intersections, arrangements, exact input models and computational complexity."
---

# Computational Geometry

## Workflow

1. Specify dimension, geometric input model, degeneracies and output representation.
2. Distinguish exact predicates from approximate coordinate constructions.
3. Verify algorithm invariants and handling of ties, intersections and collinearity.
4. Analyze complexity in the declared computational model.
5. Validate with adversarial near-degenerate cases and independent geometric checks.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.

## Runnable helper

Use [planar_geometry.py](scripts/planar_geometry.py) to compute rational planar orientations and convex hulls with exact area. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
