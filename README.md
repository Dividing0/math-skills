# Math Skills

[![CI](https://github.com/Dividing0/math-skills/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Dividing0/math-skills/actions/workflows/ci.yml)

A collection of **162 agent skills** for mathematical research, proofs, modeling, computation, and Lean 4 formalization. **41 skills** include configurable command-line helpers for host calculations.

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

### Claude Code

Add this repository as a marketplace and install its plugin from Claude Code:

```text
/plugin marketplace add Dividing0/math-skills
/plugin install math-skills@math-skills
```

Invoke a skill by its plugin-qualified name, for example:

```text
/math-skills:prove-with-lean4
```

For local development, run `claude --plugin-dir .` from the repository root. The [plugin manifest](.claude-plugin/plugin.json) discovers the existing skill directories; the [marketplace catalog](.claude-plugin/marketplace.json) provides the installation entry. Claude reads skill instructions from `SKILL.md`; `agents/openai.yaml` supplies metadata for OpenAI clients.

See the [Claude Code plugin reference](https://code.claude.com/docs/en/plugins-reference) for the metadata format. Validate the manifest and catalog with `claude plugin validate .claude-plugin/plugin.json` and `claude plugin validate .claude-plugin/marketplace.json` when Claude Code is installed.

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
| Build macros, elaborators, and tactics | [metaprogram-lean4](metaprogram-lean4/SKILL.md) |
| Upgrade toolchains and library versions | [migrate-lean4-projects](migrate-lean4-projects/SKILL.md) |
| Test programs, extensions, and expected errors | [test-lean4-code](test-lean4-code/SKILL.md) |
| Prepare upstream library contributions | [contribute-to-mathlib](contribute-to-mathlib/SKILL.md) |

## Specialized computation and research

These workflows complement the collection's symbolic, numerical, proof, and modeling skills:

| Task | Skill | Included helper |
|---|---|---|
| SMT constraints and counterexamples | [solve-with-z3](solve-with-z3/SKILL.md) | Models, unsatisfiable cores, and solver status |
| Mixed-integer optimization | [optimize-with-scip](optimize-with-scip/SKILL.md) | Linear MILP solutions, bounds, gaps, and residuals |
| Stochastic differential equations | [simulate-stochastic-differential-equations](simulate-stochastic-differential-equations/SKILL.md) | Coupled Euler–Maruyama and Milstein paths for scalar GBM |
| Differential-algebraic equations | [solve-differential-algebraic-equations](solve-differential-algebraic-equations/SKILL.md) | Constant linear index-one DAE checks and refinement |
| Monte Carlo estimation | [compute-with-monte-carlo](compute-with-monte-carlo/SKILL.md) | Polynomial integration with variance reduction |
| Mathematical cryptography | [research-mathematical-cryptography](research-mathematical-cryptography/SKILL.md) | Exact finite secrecy and decryptability analysis |
| Ergodic theory | [research-ergodic-theory](research-ergodic-theory/SKILL.md) | Finite invariant measures, cycles, and mixing |
| Statistical learning theory | [research-statistical-learning-theory](research-statistical-learning-theory/SKILL.md) | Conditional finite-class generalization bounds |
| Stochastic control | [research-stochastic-control](research-stochastic-control/SKILL.md) | Exact finite-horizon MDP policies and values |

Each skill covers the broader mathematical workflow; its helper implements the limited task family shown above. Read the command reference for assumptions and input limits.

## Command-line helpers

Configurable helpers accept JSON with `--input`, provide a sample request with `--example`, and return results with evidence scope and dependency versions. Individual workflows link to relevant helpers and their command references.

For example, generate and run a Chinese remainder theorem request:

```sh
python research-number-theory/scripts/integer_tools.py --example > crt.json
python research-number-theory/scripts/integer_tools.py --input crt.json
```

On Windows PowerShell, select UTF-8 explicitly when creating the request:

```powershell
python research-number-theory/scripts/integer_tools.py --example | Set-Content -Encoding utf8 crt.json
python research-number-theory/scripts/integer_tools.py --input crt.json
```

File inputs accept UTF-8 with or without a BOM. Invoke helpers with `python`; executable permission bits and Unix shebangs are not required on Windows. See [platform verification and limitations](docs/platform-compatibility.md).

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
uv run --with pyyaml --with sympy --with numpy --with scipy --with networkx --with statsmodels --with matplotlib --with z3-solver --with pyscipopt --with nbformat --with nbclient --with ipykernel python -m unittest discover -s tests -v
```

Lean integration tests also run when Elan and a Lean 4 toolchain are installed; otherwise they are skipped. They use installed toolchains without downloading one and check proof audits, macros, and positive/negative fixtures. An installed but broken toolchain fails the checks.

### Continuous integration

The [CI workflow](.github/workflows/ci.yml) runs on every push and pull request and supports manual runs. Its Python 3.14 matrix uses `ubuntu-latest`, `windows-latest`, and `macos-latest`, with independent results for each platform. It checks:

- Python lint, types, and syntax.
- Skill metadata, Claude plugin/catalog consistency, links, and release packaging.
- Helper regression tests.

The platform regressions exercise UTF-8 and BOM inputs under a legacy locale, Unicode paths, process arguments and diagnostics, temporary-file cleanup, notebook execution, and ZIP round trips. Missing optional scientific runtimes are reported as skips, not successful runtime checks.

## Releases

Publishing a GitHub release, including a prerelease, runs the [release workflow](.github/workflows/release.yml) to validate skills and scripts and upload `math-skills.zip` as a release asset.

The ZIP contains tracked skill directories and their resources, the `LICENSE` file, and `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` for Claude Code. Root-level tests and repository tooling, virtual environments, caches, and build artifacts are excluded. Keep the plugin version aligned with `pyproject.toml` when preparing a release; CI checks this consistency.

Download packages from [Releases](https://github.com/Dividing0/math-skills/releases). See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

[MIT License](LICENSE) — Copyright (c) 2026 Yehor Smoliakov.
