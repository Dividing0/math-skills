# Math Skills

A collection of agent skills for mathematical research, proofs, modeling, computation, and Lean 4 formalization.

Each skill has a `SKILL.md` with its purpose and workflow, plus supporting references or examples where useful. Choose a skill directory and read its `SKILL.md` to get started.

For Lean 4, start with [formalize-math-proofs](formalize-math-proofs/SKILL.md), which links to skills for project setup, proof construction, Mathlib search, debugging, and auditing.

For existing Lean 4 code, use [improve-lean4-code](improve-lean4-code/SKILL.md) to enhance implementations, [analyze-lean4-code](analyze-lean4-code/SKILL.md) to investigate weaknesses, and [check-lean4-idiomaticity](check-lean4-idiomaticity/SKILL.md) to review style and library conventions.

30 skills include configurable command-line helpers for host calculations. Each accepts JSON with `--input`, provides a sample request with `--example`, and returns results with evidence scope and dependency versions. The collection contains 149 skills; individual workflows link to relevant helpers and their command references. For example:

```sh
python research-number-theory/scripts/integer_tools.py --example > /tmp/crt.json
python research-number-theory/scripts/integer_tools.py --input /tmp/crt.json
```

To check the Python scripts:

```sh
uv run ruff check
uv run pyright --warnings
```

Pyright checks all repository Python files in standard mode. Scientific runtimes are installed per skill, so missing optional imports are not reported; library types come from available stubs and typed packages rather than inference from untyped library source. Runtime checks still require the relevant dependencies.

Run the helper regression suite in an isolated dependency environment (Lean checks also run when Elan and a Lean 4 toolchain are installed):

```sh
uv run --with sympy --with numpy --with scipy --with networkx --with statsmodels --with matplotlib python -m unittest discover -s tests -v
```

Every push and pull request runs CI to lint, type-check, and syntax-check Python files, validate skill metadata and links, check release packaging, and run the helper regression suite. The Lean integration test is skipped when no Lean toolchain is installed on the runner.

Publishing a GitHub release (including a prerelease) validates all skill metadata and Python scripts, then uploads `math-skills.zip` as a release asset. The ZIP contains only tracked skill directories and their resources; virtual environments, caches, build artifacts, and repository tooling are excluded.
