# Incidence counts versus existence

## Method branches
1. For a 2-(v,k,λ) design, require every unordered pair to occur in exactly λ blocks and specify whether repeated blocks are allowed. Counting incidences gives bk=vr and r(k-1)=λ(v-1). Integrality is necessary, not a universal construction theorem.
2. For an explicit finite candidate, enumerate blocks and count each point and each pair exactly. A total incidence count can conceal uneven distribution; return the offending pair if verification fails.
3. For algebraic constructions, identify the finite field or group, prove that generated blocks have the required cardinality, and count how group actions distribute incidences. Orbit sizes depend on stabilizers and must not be assumed equal.
4. For theorem-based existence, match all parameter, parity and size conditions to the exact theorem statement. Computational search failure does not establish nonexistence unless exhaustive coverage is certified.

## Worked construction
On points {1,2,3,4}, take all six two-element subsets as blocks. Every pair occurs once because it is itself one block; hence k=2 and λ=1. Every point occurs in three blocks, so r=3 and b=6. Check bk=12=vr and r(k-1)=3=λ(v-1). The construction proves existence, while the equations are independent consistency checks rather than the proof alone.

## Tempting inference and counterexample
Matching v,b,k,r is insufficient for pair balance. On {1,2,3,4}, use blocks {1,2},{1,2},{3,4},{3,4}. Each point has replication two and each block size two, but pair {1,2} occurs twice and {1,3} never occurs. The incidence total is uniform across points and still fails the design property.

## Stop and handoff
If parameters are admissible but no construction or applicable existence theorem is supplied, report admissibility only. Hand off point labels, sorted block list, repetition policy, target λ and a per-pair count certificate. For larger computations record whether checking covered every pair or only a sample; sampled pair agreement cannot establish the complete incidence requirement.
