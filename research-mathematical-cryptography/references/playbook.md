# Research Mathematical Cryptography: playbook

## Finite secrecy versus correctness

For a key K independent of message M, perfect secrecy for all priors is equivalent in a finite message space to identical conditional laws P(C=c | M=m) for every message m. The helper enumerates these laws exactly from key probabilities and an encryption table. It also checks whether each positive-probability key row is injective, which permits deterministic decryption with that key.

For one-bit XOR, the two uniformly weighted key rows `[0,1]` and `[1,0]` are decryptable and perfectly secret. Biasing the key breaks the equality of conditional laws. A constant ciphertext table can have identical conditional laws while failing decryptability; secrecy and correctness are separate requirements. Reusing an XOR key across two messages reveals their XOR even when each single-use experiment passes.

## Reduction record

For a left/right indistinguishability game, specify equal-length challenge messages, a uniform hidden bit, the permitted encryption/decryption queries, and the adversary's final guess. Declare whether advantage means `|Pr[guess=bit]-1/2|` or twice that quantity. Query restrictions depend on the chosen CPA/CCA notion and cannot be omitted.

For each change of game, record either equality of distributions, a distinguishing reduction with its resource cost, or a bound on a specified failure event. Sum the losses across the complete sequence, including a security-parameter-dependent number of transitions. See [Shoup, Sequences of Games, Section 1.1](https://www.shoup.net/papers/games.pdf) for this proof organization.

## Acceptance cases

- Uniform single-use XOR: prove finite secrecy and correctness under independence.
- Biased keys: provide an exact distinguishing pair/distribution.
- Constant encryption: do not call it a valid cipher solely because the secrecy check passes.
- A DDH-based claim assumes only discrete-log hardness: demand the appropriate reduction/assumption.
- Tiny parameter enumeration succeeds: do not extrapolate computational hardness.

## Primary sources

[Victor Shoup, A Computational Introduction to Number Theory and Algebra](https://www.shoup.net/ntb/) for computational algebra and probability foundations. State cryptographic game definitions explicitly in each task.
