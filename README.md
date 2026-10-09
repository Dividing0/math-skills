# Math Skills

A collection of agent skills for mathematical research, proofs, modeling, computation, and Lean 4 formalization.

Each skill has a `SKILL.md` with its purpose and workflow, plus supporting references or examples where useful. Choose a skill directory and read its `SKILL.md` to get started.

For Lean 4, start with [formalize-math-proofs](formalize-math-proofs/SKILL.md), which links to skills for project setup, proof construction, Mathlib search, debugging, and auditing.

To check the Python scripts:

```sh
uv run ruff check
```

Publishing a GitHub release (including a prerelease) validates all skill metadata and Python scripts, then uploads `math-skills.zip` as a release asset. The ZIP contains only tracked skill directories and their resources; virtual environments, caches, build artifacts, and repository tooling are excluded.
