# Definitions as contracts

## Choose a branch
- Substructure definition: state the ambient operations, all closure requirements, and whether an identity must be inherited. Test the zero object and empty set explicitly; these conventions can change whether an example qualifies.
- Construction from representatives: to define F on X/~ using f on X, prove x~y implies f(x)=f(y). For an operation, check changes in every argument. Existence of representatives is separate from the ability to choose all representatives simultaneously.
- Universal property: specify objects, admissible maps, existence and uniqueness of a mediating map. Prove that two realizations admit a unique isomorphism commuting with the defining structure maps or universal diagrams; arbitrary isomorphisms of the underlying objects need not be unique. Do not replace this structured uniqueness by literal equality of underlying sets. Primary definition: The Stacks Project, Categories §4, Definition 4.1 (tag 001S), https://stacks.math.columbia.edu/tag/001S, checked 2026-10-08.

## Worked definition
For integers modulo 5, define [a]+[b]=[a+b]. If a'=a+5k and b'=b+5l, then a'+b'-(a+b)=5(k+l), so the output class is unchanged. The same argument for multiplication uses a'b'-ab=5(kb+la+5kl). Thus both operations descend. The representative computation proves well-definedness before ring laws are transported from integers.

## Tempting inference and counterexample
A notation that resembles an operation need not define one. On integers modulo 5, proposed F([a])=a as an integer gives F([0])=0 and F([5])=5 although [0]=[5]. Selecting least nonnegative representatives repairs this particular function, but adds a convention and gives a function to {0,1,2,3,4}; it is not the original unrestricted rule. Do not confuse repairing notation with proving the initial definition valid.

## Stop or hand off
If the definition requires an object whose existence is unproved, label it conditional and hand the existence assertion to proof construction. If two conventions are compatible only under a nonzero, finite or choice assumption, record that assumption in both directions of the equivalence. Deliver the exact quantifiers, admissible objects, examples and nonexamples, along with a representative-independence argument wherever relevant. A finite catalogue of examples does not certify consistency of an axiomatic theory.
