# Changelog

## v0.2.0

- Add 13 dedicated skills for Lean metaprogramming, migrations, testing, Mathlib contributions, Z3, SCIP, SDEs, DAEs, Monte Carlo, mathematical cryptography, ergodic theory, statistical learning theory, and stochastic control.
- Add 11 configurable helpers with documented mathematical limits, checked Lean fixtures, and 20 regression tests against analytic answers, finite enumeration, and invalid assumptions; include Z3 and SCIP runtimes in CI. The collection now has 162 skills and 41 configurable helpers.
- Add 30 configurable command-line helpers for mathematical computations, certificate checks, Lean audits, plotting, and host inspection.
- Document helper inputs, dependencies, examples, and evidence limitations; link reusable helpers from 72 additional skills.
- Record the review of all 146 skills and retain existing workflows where additional scripts would not help.
- Add 34 regression tests covering calculations, invalid inputs, and host execution.
- Translate 70 Ukrainian skill headings and their display names into English.
- Add `.gitignore` rules for macOS metadata, Python environments, caches, and build artifacts; remove tracked `.DS_Store` files.
- Add push and pull request CI for skill validation, release packaging, Python lint and syntax checks, and helper regression tests.
- Add three Lean 4 code skills for refactoring, weakness analysis, and idiomaticity review, with checked examples and reuse of the host checker.
- Add Pyright standard-mode checks for all Python files to project tooling, push/pull request CI, and release validation; fix helper typing and module-loader diagnostics.
- Add Claude Code plugin and marketplace metadata, installation instructions, and validated metadata inclusion in release archives.
- Add the MIT license with Yehor Smoliakov as copyright holder, declare it in project/plugin metadata, and include it in release archives.

## v0.1.0

- Init
