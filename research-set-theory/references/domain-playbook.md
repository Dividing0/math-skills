# Axioms, arithmetic and size arguments

## Choose a branch
- Cardinal comparisons: name injections, surjections or bijections and the foundational axioms. Cantor–Bernstein turns two injections into a bijection without the axiom of choice. Avoid using an arbitrary simultaneous selection unless the needed choice principle is established.
- Ordinal calculations: define order type and use ordinal addition as ordered concatenation. It is not commutative; limit stages use suprema. Cardinal arithmetic forgets ordering, so matching underlying size does not justify ordinal equalities.
- Consistency or independence: specify the base theory and distinguish a theorem within it from a metatheoretic relative-consistency result. A genuine structure satisfying every axiom of a first-order theory establishes its syntactic consistency by soundness, even when that model is finite. A finite sample or a model of only a finite fragment does not establish satisfaction of the entire theory. Do not confuse an actual full-theory model with finitely many checks. Primary reference: Open Logic Text, first-order tableaux soundness, Corollary 21.31 (printed p. 330), https://builds.openlogicproject.org/open-logic-complete.pdf, release 9620cc7 (2026-07-12), checked 2026-10-08. Do not infer negation merely because a statement is not derivable by a supplied proof.

## Worked countability map
Define f:Z→N by f(0)=0, f(k)=2k-1 for k>=1, and f(-k)=2k for k>=1. Positive integers hit the odd natural numbers, negative integers hit the positive evens, and zero hits zero. These image classes are disjoint and cover N, while each branch is injective. Hence f is a bijection and Z is countably infinite. The construction is explicit and does not rely on a choice of one representative from an unspecified family.

## Tempting inference and counterexample
Ordinal addition cannot be commuted like addition of finite numbers. The order 1+omega is one first point followed by an omega sequence and is order-isomorphic to omega by shifting the sequence labels. The order omega+1 has a largest element, whereas omega has none; therefore omega+1 is not omega. Both have countably infinite cardinality, showing why cardinal equality is insufficient to identify order types.

## Stop or hand off
If a statement implicitly uses well-ordering of arbitrary sets, mark the dependence on choice in ZF. For a putative set of all objects, check whether separation is applied inside an existing set or a proper class is being treated as a set. Return explicit maps or the precise missing axiom to foundational review. For independence claims seek the actual model construction and base-theory assumptions before assigning proof status.
