# Complexes, resolutions and derived information

## Method branches
1. For a chain complex C, specify homological grading dₙ:Cₙ→Cₙ₋₁ and verify dₙ₋₁dₙ=0 before taking Hₙ=ker dₙ/im dₙ₊₁. A displayed quotient is undefined if the image is not contained in the kernel.
2. For a chain map, check commutation with every differential. A quasi-isomorphism means induced maps on all homology groups are isomorphisms. A chain-homotopy equivalence is stronger without additional hypotheses; do not replace one by the other silently.
3. For Tor of modules, choose a projective resolution in the appropriate variable, tensor it, and compute homology. Tensor is right exact; flatness is the condition needed for preservation of arbitrary short exact sequences.
4. For Ext, apply Hom to a projective resolution in the first variable or an injective resolution in the second, tracking contravariance and cohomological degree. State module sides for noncommutative rings.

## Worked calculation
Resolve Z/2 over Z by 0→Z --2→ Z→Z/2→0. Tensor the projective part with Z/2. Multiplication by 2 becomes the zero map on Z/2, so the degree-one homology is Z/2 and Tor₁^Z(Z/2,Z/2)=Z/2. The degree-zero homology is also Z/2. The nonzero first group records information lost if one only looks at the ordinary tensor product.

## Tempting inference and counterexample
Isomorphic graded modules need not have isomorphic homology. The two-term complexes Z --1→ Z and Z --0→ Z have the same modules in degrees one and zero. The first has zero homology in both degrees; the second has Z in both. Differentials are essential data, not decoration.

## Stop and handoff
Stop derived-functor calculations if module sides, grading or the resolution's exactness is missing. Pass differentials, augmentation, projectivity or injectivity witnesses, chain-map equations and indexing conventions to proof review. An acyclic complex need not be contractible in an arbitrary module category; identify the splitting or projective boundedness assumptions before making that stronger claim.
