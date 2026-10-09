---
name: analyze-lean4-code
description: "Analyze weaknesses in Lean 4 libraries and executable code: specification gaps, boundary behavior, brittle proofs, API design, typeclass interactions and performance risks. Use for an evidence-based code review with prioritized findings; use proof auditing for dedicated theorem trust checks."
---

# Analyze Lean 4 Code

## Workflow

1. Establish the intended behavior, review scope and consumers. Read pinned versions, imports, target configuration and local conventions. Distinguish a mathematical library, executable, and metaprogram: they have different correctness and performance obligations.
2. Reproduce the baseline build and relevant tests. Verify that reviewed modules are actually included. Record source locations and separate existing failures from newly discovered issues. If tools cannot run, identify the review as static.
3. Compare exposed types and theorem statements with the requirements. Check overly strong hypotheses, vacuous claims, Nat/Int mismatches, implicit parameters and computability requirements. For executable code, examine empty inputs, bounds, default values, partial operations, error propagation and effects. A total Lean function can still implement the wrong specification.
4. Inspect maintainability with concrete callers: duplicate library code, leaked instances or notation, circular design dependencies, unnecessarily strong abstractions, broad imports, and proof scripts coupled to implementation unfolding or generated names. Identify an actual failure mechanism before treating a stylistic preference as a weakness.
5. Trace suspicious trust and execution paths. `partial`, `unsafe`, `noncomputable` and classical reasoning are not interchangeable defects. Inspect how a declaration is used, what is required of it, and whether compiled behavior is replaced separately from its logical model. Delegate a dedicated correspondence/axiom audit to [audit-lean4-proofs](../audit-lean4-proofs/SKILL.md) when available.
6. Support a finding with a minimal caller, failing test, checked counterexample, diagnostic, or reproducible measurement. Distinguish elaboration cost, typeclass search, build dependencies and runtime complexity. A broad `simp`, a large file or an elevated heartbeat setting is a lead to investigate, not sufficient evidence of a defect.
7. Return prioritized findings with file/declaration, trigger, impact, evidence, proposed remedy and confidence. Separate confirmed defects, conditional risks and optional improvements. State coverage and unresolved questions; if no actionable weakness is found, say so. Review requests do not require rewriting the code.

## Resources

Read the [weakness review guide](references/weakness-review.md) for severity decisions and acceptance cases. [BoundaryCases.lean](assets/BoundaryCases.lean) shows code that compiles while losing information, plus a conditional alternative API.

When installed alongside this skill, the [host checker](../audit-lean4-proofs/scripts/check_project.py) and [command reference](../audit-lean4-proofs/references/command-line.md) provide real file-check and axiom output. Its `checker_success` field does not assess runtime behavior, style or specification adequacy. Direct `lake env lean Path/To/File.lean`, target builds and project tests remain available without that helper. Use [improve-lean4-code](../improve-lean4-code/SKILL.md) when implementing requested repairs and [check-lean4-idiomaticity](../check-lean4-idiomaticity/SKILL.md) for style-specific review.
