# Domain playbook

## Select the method

1. For polynomial-time many-one hardness, define a computable map f with x in A iff f(x) in B and bound its output size and runtime in input bit length. To transfer known hardness to B, the source A must be hard.
2. For NP membership, give a certificate of polynomial bit length and a deterministic polynomial-time verifier. Merely saying solutions are checkable ignores encoding and arithmetic cost.
3. For numerical algorithms, distinguish polynomial in a numeric value from polynomial in its encoding length. State whether the problem is decision, search, counting, promise or approximation; guarantees for one variant need not imply another.

## Worked check

The subset-sum dynamic program for nonnegative integers and target T fills a table with n(T+1) Boolean entries. Its O(nT) time is pseudo-polynomial: T encoded in binary has about log2 T bits. For T=2^k, the table is exponential in k even though its cost is linear in T. This establishes a runtime classification without claiming a complexity separation.

## Invalid inference and witness

Large observed runtime is no hardness proof. An algorithm intentionally taking 2^n steps to sort a list does not make sorting NP-hard; another algorithm sorts in polynomial time. Complexity is a property of the problem and model, not the slowness of one implementation.

## Completion and handoff

Return problem encoding, computational model, reduction map, verifier, size bounds and any conditional assumptions. Stop when a reduction omits a direction or uses exponential-sized output. Hand algorithm design the precise input and resource measure; keep empirical runtime separate from asymptotic upper bounds, lower bounds and unproved class separations.
