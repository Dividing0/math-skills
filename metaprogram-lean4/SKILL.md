---
name: metaprogram-lean4
description: "Build and debug Lean 4 tactics, hygienic macros and elaborators. Use when extending Lean syntax or proof automation, including quotation, metavariable handling and kernel-checked output."
---

# Metaprogram Lean 4

## Workflow

1. Read the pinned Lean version, existing extensions and imports. Decide whether the task needs a syntax-to-syntax macro, a type-directed elaborator, or tactic code operating on goals; keep ordinary proofs in ordinary Lean when no extension is needed.
2. Specify the accepted syntax and expected result, including failure diagnostics. Use syntax quotations and antiquotations instead of concatenating source strings; preserve hygiene and source locations.
3. For elaborators and tactics, track local context, expected types, unresolved metavariables and goal lists. Use supported elaboration APIs under the appropriate context and restore state when trying alternatives; a tactic that returns without discharging its goals has not proved the theorem.
4. Construct proof terms that the kernel checks. Distinguish meta-level execution from object-level proofs; do not add axioms or admitted terms to make an extension appear successful.
5. Test positive cases, binding/shadowing, type errors, and unsolved goals in the pinned project. Run direct file checks and affected Lake targets, then inspect axiom dependencies for representative generated theorems.
6. Report the extension boundary, version, checked examples and deliberate error behavior. Describe unsupported syntax or missing tooling rather than inventing successful elaboration.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.
