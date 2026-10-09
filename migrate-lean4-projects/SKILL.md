---
name: migrate-lean4-projects
description: "Upgrade an existing Lean 4 or Mathlib project deliberately, compare dependency pins, repair API changes and verify downstream compatibility. Use for version migrations rather than initial setup or isolated proof debugging."
---

# Migrate Lean 4 Projects

## Workflow

1. Record current and requested toolchain/dependency versions, project instructions, target names and baseline diagnostics. Preserve unrelated working changes; use an isolated checkout when the migration requires substantial experimentation.
2. Capture a baseline snapshot and build/test results. Choose compatible Lean and Mathlib revisions together by reading the target Mathlib lean-toolchain; do not independently select two latest releases.
3. Change the requested pins and intentionally regenerate dependency resolution using the pinned Lake workflow. Inspect manifest changes, including transitive dependencies. Fetch compatible caches only after the new pin is established.
4. Repair the first meaningful failure: imports or renamed declarations, signatures and implicit arguments, instance inference, tactics, then actual changed mathematical obligations. Consult the target source and release notes instead of blindly replacing identifiers.
5. Compare public elaborated statements and executable behavior. Do not preserve a green build by weakening hypotheses, inserting sorry, broadly disabling linters or silently changing a public API. Check consumer modules and project tests as well as the default build.
6. Return the version change, focused repairs, before/after diagnostics and remaining blockers. A manifest or source hash comparison records changes; it does not establish compatibility. Retain enough information to reproduce or revert the migration.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [project_snapshot.py](scripts/project_snapshot.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
