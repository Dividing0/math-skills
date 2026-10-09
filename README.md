# Math Skills

[![CI](https://github.com/Dividing0/math-skills/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Dividing0/math-skills/actions/workflows/ci.yml)

A collection of **149 agent skills** for mathematical research, proofs, modeling, computation, and Lean 4 formalization. **30 skills** include configurable command-line helpers for host calculations.

## Getting started

1. Choose a skill directory for your task and read its `SKILL.md`.
2. Follow its workflow and linked references.
3. For executable helpers, read the command reference and install the dependencies required by that skill.

Skill directories contain the resources they need:

| Resource | Purpose |
|---|---|
| `SKILL.md` | Skill description and workflow |
| `agents/openai.yaml` | Agent interface metadata |
| `references/` | Supporting guidance and command documentation |
| `scripts/` | Executable helpers and examples, where available |
| `assets/` | Sample files and other workflow resources, where available |

## Lean 4 workflows

Start with [formalize-math-proofs](formalize-math-proofs/SKILL.md), or choose a focused workflow:

| Task | Skill |
|---|---|
| Set up toolchains, Lake, and dependencies | [setup-lean4-projects](setup-lean4-projects/SKILL.md) |
| Construct and check proofs | [prove-with-lean4](prove-with-lean4/SKILL.md) |
| Find library definitions and theorems | [search-mathlib](search-mathlib/SKILL.md) |
| Diagnose proof failures | [debug-lean4-proofs](debug-lean4-proofs/SKILL.md) |
| Audit statements and proof dependencies | [audit-lean4-proofs](audit-lean4-proofs/SKILL.md) |
| Refactor and enhance existing code | [improve-lean4-code](improve-lean4-code/SKILL.md) |
| Investigate code weaknesses | [analyze-lean4-code](analyze-lean4-code/SKILL.md) |
| Review style and library conventions | [check-lean4-idiomaticity](check-lean4-idiomaticity/SKILL.md) |

## Command-line helpers

Configurable helpers accept JSON with `--input`, provide a sample request with `--example`, and return results with evidence scope and dependency versions. Individual workflows link to relevant helpers and their command references.

For example, generate and run a Chinese remainder theorem request:

```sh
python research-number-theory/scripts/integer_tools.py --example > /tmp/crt.json
python research-number-theory/scripts/integer_tools.py --input /tmp/crt.json
```

## Development

Use Python **3.14 or newer** and `uv` for repository checks. Scientific runtimes are installed separately as needed by each skill.

### Lint and type checks

```sh
uv run ruff check
uv run pyright --warnings
```

Pyright checks all repository Python files in standard mode. Scientific runtimes are installed per skill, so missing optional imports are not reported; library types come from available stubs and typed packages rather than inference from untyped library source. Runtime checks still require the relevant dependencies.

### Regression tests

Run the helper regression suite in an isolated dependency environment:

```sh
uv run --with sympy --with numpy --with scipy --with networkx --with statsmodels --with matplotlib python -m unittest discover -s tests -v
```

The Lean integration test also runs when Elan and a Lean 4 toolchain are installed; otherwise it is skipped.

### Continuous integration

The [CI workflow](.github/workflows/ci.yml) runs on every push and pull request and supports manual runs. It checks:

- Python lint, types, and syntax.
- Skill metadata, links, and release packaging.
- Helper regression tests.

## Releases

Publishing a GitHub release, including a prerelease, runs the [release workflow](.github/workflows/release.yml) to validate skills and scripts and upload `math-skills.zip` as a release asset.

The ZIP contains only tracked skill directories and their resources. Root-level tests and repository tooling, virtual environments, caches, and build artifacts are excluded.

Download packages from [Releases](https://github.com/Dividing0/math-skills/releases). See [CHANGELOG.md](CHANGELOG.md) for version history.
