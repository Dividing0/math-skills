---
name: research-mathematical-cryptography
description: "Analyze mathematical cryptographic constructions, security games, reductions and finite information-theoretic models. Use for correctness, perfect secrecy, computational assumptions and explicit security-loss arguments rather than production cryptographic implementation."
---

# Research Mathematical Cryptography

## Workflow

1. Define the primitive, key/message spaces, randomness, correctness condition and adversary model. Distinguish information-theoretic secrecy from computational security and distinguish one-use from reusable-key guarantees.
2. Write the exact security experiment and advantage convention. Include oracle access, query limits and the security parameter; a small numerical attack experiment is not an asymptotic security reduction.
3. For a reduction, specify the simulator, distribution of its transcript, abort events and advantage/runtime loss. State the assumed hard problem and its instance distribution; do not equate related assumptions without a proved reduction.
4. Check edge cases in algebraic constructions: subgroup/order conditions, invertibility, sampling biases and invalid encodings. Separate correctness of algebra from semantic security and implementation properties.
5. Use exhaustive finite calculations for toy models and counterexamples. The finite cipher helper can establish single-use perfect secrecy and per-key decryptability for its table, but cannot establish security of a practical parameterized scheme.
6. Report definitions, assumptions, proved implications, concrete witnesses and unresolved reductions. Label toy arithmetic explicitly; do not present an educational construction as a production-ready cryptographic library.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [finite_secrecy.py](scripts/finite_secrecy.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
