# Project playbook

## Existing project

Inspect pins before running commands. From the project root:

```sh
cat lean-toolchain
elan toolchain list
lean --version
lake --version
lake env lean Path/To/File.lean
lake build
```

Read the Lake configuration to identify targets and the manifest to identify resolved dependency commits. An import requires both source availability and compatible compiled artifacts. If the error is a missing Mathlib `.olean`, follow the project's cache instructions before considering a source build. `lake exe cache get` retrieves Mathlib artifacts; this is different from Lake's own evolving cache commands. Check the pinned revision's cache help when requesting a subset of modules.

## New Mathlib project

Create a dedicated directory and initialize a library package using the installed version's `lake init --help`. Add a Mathlib dependency pinned to a release or commit, and use the `lean-toolchain` from that revision. A concrete tested pair for the examples is Mathlib tag `v4.29.1` with `leanprover/lean4:v4.29.1`; it is an example, not a universal upgrade policy.

For a TOML package, a dependency entry has this shape:

```toml
[[require]]
name = "mathlib"
scope = "leanprover-community"
git = "https://github.com/leanprover-community/mathlib4.git"
rev = "v4.29.1"
```

Resolve with `lake update`, retrieve artifacts with `lake exe cache get`, add the proof module to the library root's imports, and run `lake build`. Keep the toolchain and manifest with the project. Confirm the configuration syntax against the selected Lake release; do not overwrite an existing Lean configuration with TOML just to follow this example.

## Worked smoke check

Copy `assets/Smoke.lean` from this skill into the project's source root and run `lake env lean Smoke.lean`. It uses only core Lean and checks conjunction commutativity. Success establishes that the checker runs, not that Mathlib or all library targets build.

## Acceptance cases

- A project pins an older Lean release: use that release rather than the global default.
- Mathlib was changed but the toolchain was not: identify the mismatch and restore a compatible pair; preserve unrelated files.
- Cache download is unavailable: report the actual error and offer a source build if feasible; do not fabricate proof results.
- A new unimported module fails but `lake build` succeeds: check the file directly and connect it to the intended target.

## Sources

- [Lake reference](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/): package configuration, dependency resolution, builds and environment commands.
- [Elan toolchains](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/): project-specific version selection.
- [Mathlib repository](https://github.com/leanprover-community/mathlib4): revision-specific toolchain, manifest and cache instructions. Read files at the project's pinned revision.
