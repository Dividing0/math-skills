---
name: setup-lean4-projects
description: "Set up or repair Lean 4 mathematical projects using Elan, Lake, pinned toolchains, Mathlib dependencies and build caches. Use for environment and dependency problems rather than tactic failures."
---

# Set Up Lean 4 Projects

## Workflow

1. Find the project root and read `lean-toolchain`, `lakefile.toml` or `lakefile.lean`, `lake-manifest.json`, and project instructions. Establish whether the request concerns a new project or an existing one; preserve existing package names and dependency revisions.
2. Run version and build commands from that root. `lean --version` outside the project can select a different Elan toolchain. Check `elan toolchain list`, `lake --version`, and the project's Lean version before diagnosing imports.
3. For a new Mathlib project, choose a released Mathlib revision and its matching `lean-toolchain`, not independently selected latest versions. For an existing project, restore the pinned environment first. Run `lake update` only when creating or intentionally changing dependency resolution; it can change the manifest and toolchain.
4. Fetch the compatible Mathlib cache when available using the project's documented `lake exe cache get` workflow. A cache miss is an environment/build issue, not a failed theorem. Do not repeatedly delete caches or upgrade dependencies to hide a proof error.
5. Check a module with `lake env lean Path/To/File.lean` and build declared targets with `lake build`. Ensure the new module is reachable through a target's imports; a passing default build may omit an unreferenced file.
6. Report the project root, toolchain, Mathlib revision, commands, exit status and remaining blockers. Distinguish missing executables, network failures, incompatible artifacts and mathematical errors. Stop repeated setup attempts when the same external blocker persists; return the concrete next requirement.

## Resources

Read [project playbook](references/project-playbook.md) for setup commands, failure cases and acceptance checks. Copy [Smoke.lean](assets/Smoke.lean) into a temporary project to test the checker without Mathlib. Do not install or upgrade a global toolchain unless the task calls for it.

## Host computation

When the `run-math-python` skill is installed alongside this skill, discover Lean/Lake executable paths without invoking or installing a toolchain; then follow this skill’s pinned project setup workflow. Use its [host_capabilities.py](../run-math-python/scripts/host_capabilities.py) helper and [input/command reference](../run-math-python/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.

## Related workflow

For upgrading an existing pinned project, use the migration workflow to record the baseline, coordinate Lean/Mathlib revisions and check downstream compatibility. Read [migrate-lean4-projects](../migrate-lean4-projects/SKILL.md) when that specialization is needed and available.
