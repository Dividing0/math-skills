# Migrate Lean 4 Projects: playbook

## Migration record

Record old/new Lean pins, Mathlib revisions, affected Lake targets and the exact baseline build. A project failing before migration needs a separate baseline finding. Snapshot the old state before editing; do not reconstruct it from memory after a failed upgrade.

The helper reads configuration/source hashes and the toolchain text. Its compare operation identifies added, removed and changed files; it does not execute Git, update Lake, fetch dependencies or prove equivalence. Hidden dependency/build trees and symlinks are excluded.

## Common repairs

| Symptom | Check before editing |
|---|---|
| Missing declaration | Target namespace, import and replacement signature |
| Instance failure | Changed assumptions and available instances, not just tactic syntax |
| Broken `rfl` | Definitional reduction and public abstraction boundary |
| Timeout | Comparable cold/warm work, changed elaboration and local options |

## Acceptance cases

- Mathlib requires a different Lean pin: align the pair before debugging proofs.
- A replacement theorem has a stronger premise: expose that mismatch rather than silently changing the original result.
- The default target omits a changed module: check the module and its consumers directly.
- A source-only snapshot is unchanged but dependencies changed: still rebuild; identical source does not imply compatibility.
- The desired revision cannot be fetched: report the blocker without upgrading to another version unasked.

## Primary sources

[Lean release notes](https://lean-lang.org/doc/reference/latest/releases/) and the [Mathlib repository](https://github.com/leanprover-community/mathlib4). Read the specific target revision, including its toolchain and contributing instructions.
