# Domain playbook: research-general-topology

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. Establish continuity through open-set preimages in the stated topology. For product maps check coordinate continuity; for a quotient map q, a map out of the quotient is continuous exactly when its composition with q is continuous, using the quotient topology.
2. Prove compactness with open covers unless metrizability or another applicable theorem justifies sequential arguments. Continuous images of compact spaces are compact without separation assumptions. Closed subsets of compact spaces are compact; compact subsets are closed only under an additional Hausdorff assumption.
3. For separation and convergence questions compute neighborhoods rather than importing Euclidean intuition. A sequence can have multiple limits in a non-Hausdorff space. Check countability hypotheses before treating sequences as complete detectors of closure or continuity.

## Worked derivation

Let X={a,b} have topology {∅,{a},X}. It is compact because any open cover of this finite space has a finite subcover. The subset {a} is compact for the same reason, but it is not closed since its complement {b} is not open. The constant sequence a,a,… converges both to a and b, because the only neighborhood of b is X.

## Invalid inference and witness

Thus “every compact subset is closed” is false in arbitrary spaces. Its Hausdorff proof separates an external point from each point of the compact set and extracts finitely many neighborhoods; without pairwise separation that step fails.

## Stop and handoff

Report the topology, separation and countability hypotheses used by each theorem. If only sequence tests were performed in a nonmetrizable space, preserve the open-cover or net obligation. Transfer specialized counterexample construction rather than assert metric equivalences universally.
