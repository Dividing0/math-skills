---
name: audit-lean4-proofs
description: "Audit Lean 4 mathematical proofs for correspondence to an informal claim, actual checker coverage, admitted obligations and transitive axiom dependencies. Use for proof review and verification claims."
---

# Audit Lean 4 Proofs

## Workflow

1. Record the requested mathematical claim, target declarations, project revision, toolchain and dependency pins. Compare domains, quantifiers, assumptions and conclusion with the elaborated statements. Detect extra hypotheses, vacuous premises and weakened conclusions even when Lean accepts the code.
2. Check the relevant files with `lake env lean Path/To/File.lean` and build the intended targets. Record warnings and exit status; an unimported file may be excluded from `lake build`, and `sorry` can compile successfully with a warning.
3. Search relevant sources for `sorry`, `admit`, added `axiom` declarations and suspicious proof bypasses. Treat text search as triage: comments and unused declarations can cause false positives, while imported assumptions can escape it. Inspect the target's actual dependencies.
4. In the pinned environment run `#print axioms Namespace.target` for each named target. Report `sorryAx`, custom axioms and standard foundations separately. `propext`, `Classical.choice` and `Quot.sound` may be expected in ordinary Mathlib mathematics; apply the requested constructive or axiom restrictions rather than declaring all classical proofs invalid.
5. Review nonstandard evaluation or trust mechanisms used in the proof path. Distinguish proof-producing computation from an external result asserted as an axiom, and report the pinned version's trust implications of mechanisms such as `native_decide`. Compilation success alone is not an axiom-free or correspondence certificate.
6. Report three independent conclusions: statement correspondence, checker coverage/status, and axiom/placeholder findings. Give declaration names and locations for gaps. If execution is unavailable, label the audit static and the verification status unchecked.

## Resources

Read [audit playbook](references/audit-playbook.md) for dependency commands, trust boundaries and acceptance cases. [Clean.lean](assets/Clean.lean) is a complete core proof; [Admitted.lean](assets/Admitted.lean) intentionally compiles with `sorry`; [WrongStatement.lean](assets/WrongStatement.lean) intentionally proves a weaker claim. Keep demonstration failures out of production proof targets.
