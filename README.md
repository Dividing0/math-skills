# Math Skills

A collection of agent skills for mathematical research, proofs, modeling, computation, and Lean 4 formalization.

Each skill has a `SKILL.md` with its purpose and workflow, plus supporting references or examples where useful. Choose a skill directory and read its `SKILL.md` to get started.

For Lean 4, start with [formalize-math-proofs](formalize-math-proofs/SKILL.md), which links to skills for project setup, proof construction, Mathlib search, debugging, and auditing.

30 skills include configurable command-line helpers for host calculations. Each accepts JSON with `--input`, provides a sample request with `--example`, and returns results with evidence scope and dependency versions. See the [review of all 146 skills](docs/script-review.md) for available helpers and reuse routes. For example:

```sh
python research-number-theory/scripts/integer_tools.py --example > /tmp/crt.json
python research-number-theory/scripts/integer_tools.py --input /tmp/crt.json
```

To check the Python scripts:

```sh
uv run ruff check
```

Run the helper regression suite in an isolated dependency environment (Lean checks also run when Elan and a Lean 4 toolchain are installed):

```sh
uv run --with sympy --with numpy --with scipy --with networkx --with statsmodels --with matplotlib python -m unittest discover -s tests -v
```

Every push and pull request runs CI to lint and syntax-check Python files, validate skill metadata and links, check release packaging, and run the helper regression suite. The Lean integration test is skipped when no Lean toolchain is installed on the runner.

Publishing a GitHub release (including a prerelease) validates all skill metadata and Python scripts, then uploads `math-skills.zip` as a release asset. The ZIP contains only tracked skill directories and their resources; virtual environments, caches, build artifacts, and repository tooling are excluded.
