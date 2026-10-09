# Domain playbook: research-coding-theory

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a linear code over a finite field, use the rank of a generator matrix for dimension and enumerate nonzero codewords only when the space is small enough for exact coverage. For minimum distance, compute Hamming weights in a linear code; nonlinear codes require pairwise distances. For unique adversarial decoding, disjoint radius-t balls require 2t<d. For erasure decoding, a known erasure pattern is recoverable when the surviving coordinates distinguish codewords; d-1 arbitrary erasures are guaranteed, which differs from unknown-position errors.

## Worked valid example

The binary repetition code C={00000,11111} has two words, dimension one and minimum distance five. If at most two coordinates are flipped, the received word has at least three coordinates matching the transmitted bit, so majority decoding returns it. Equivalently, radius-two balls are disjoint because a word in both would imply distance≤4 by the triangle inequality. Three flips from 00000 can produce 11100, which majority-decoding sends to 11111.

## Tempting invalid inference

Large minimum distance does not imply a proposed decoder attains the information-theoretic correction radius. A decoder that always outputs 00000 fails even on the uncorrupted input 11111 in the repetition code. State both the code property and the implemented decoding guarantee.

## Stop and handoff

Return alphabet, codebook or matrices, channel assumption and decoder criterion. Stop finite-length optimality claims when only a feasible construction is given; hand exact constructions to computational certification and probabilistic channel models to statistics.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
