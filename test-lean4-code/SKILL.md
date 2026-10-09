---
name: test-lean4-code
description: "Design and execute regression tests for Lean 4 definitions, programs and extensions, including boundary behavior, expected errors and consumer compatibility. Use for testing workflows beyond proving one theorem."
---

# Test Lean 4 Code

## Workflow

1. Identify the contract under test: mathematical equality, executable output/effects, API compatibility, or diagnostic behavior. Read the pinned toolchain, imports and project test conventions.
2. Use theorem examples for universal pure properties and checked concrete examples or runtime assertions for individual computations. Test empty inputs, failure branches and boundary values; a handful of evaluated values is not a proof for all inputs.
3. Add representative consumer declarations when changing binders, instances, attributes or reducibility. For macros/tactics, test shadowing, rejected input and unsolved goals as well as successful examples.
4. Make negative tests expect an actual relevant diagnostic. A missing dependency, failed toolchain setup or timeout must not count as successful rejection of the intended bad program. Keep intentional error fixtures outside ordinary successful build targets.
5. Build required imports and execute positive and negative tests with bounded commands. Inspect warnings: a file that uses sorry may compile successfully. For project-specific executables, also check exit status, output and observable effects using the project test harness.
6. Report cases run, expected and observed outcomes, runtime versus proof coverage and any skipped environment-dependent tests. Inspect the helper result passed field; its CLI exit status alone reports whether the test run was processed.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [run_cases.py](scripts/run_cases.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
