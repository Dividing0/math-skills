# Prepare Mathlib Contributions: playbook

## Worked decision

A proposed lemma asserting `n + 0 = n` should first be checked against `Nat.add_zero` and existing abstraction-level results. If the goal is already served, reuse the existing declaration. If the missing result is an appropriate specialization with a useful discovery/API role, justify that role and test its actual usage before adding it.

For a genuinely new statement, inspect nearby files and importing consumers. A lemma needed by a low-level module should not be placed in a module that imports that consumer. A proof using a powerful tactic may be fine when it is transparent and the import cost fits the module.

## Host checks

Use `lake env lean Path/To/Changed.lean` and the targets/checks documented by the pinned checkout. Reuse [search-mathlib](../../search-mathlib/SKILL.md) and [audit-lean4-proofs](../../audit-lean4-proofs/SKILL.md) when installed; otherwise inspect local sources and use scratch `#check`/`#print axioms` declarations directly.

## Acceptance cases

- The result exists under another name: demonstrate its application instead of duplicating it.
- Generalization requires an unjustified stronger assumption: explain the gap before preparing a claim of improvement.
- New placement creates an import cycle: split a lower-level lemma or choose an appropriate existing layer.
- A style-only change is outside documented upstream guidance: do not present it as a required fix.
- Contribution policy requires human expertise or limits generated communications: explain the relevant requirement and prepare only work allowed by the task and policy.
- Local checks pass: report their scope without claiming maintainer approval.

## Primary sources

[Mathlib contribution policy](https://leanprover-community.github.io/contribute/index.html), [style guide](https://leanprover-community.github.io/contribute/style.html), and [naming conventions](https://leanprover-community.github.io/contribute/naming.html). Consult current policy when preparing an upstream submission.
