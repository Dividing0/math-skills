# Modules with scalar-field and splitting conditions

## Method branches
1. For a representation of a presented group, verify that assigned matrices satisfy every relation and are invertible. A collection of matrices is not a representation until relations hold; a Lie-algebra representation instead checks bracket preservation.
2. For finite groups over a field whose characteristic does not divide the group order, use averaging to produce invariant complements. Division by the group order is essential. Specify finite-dimensionality and the scalar field for the decomposition desired.
3. For character calculations over C and finite groups, use the normalized inner product (1/|G|)Σχ(g)conjugate(ψ(g)). Integral multiplicities require characters of actual representations and a complete irreducible list; traces of arbitrary matrices do not suffice.
4. For intertwiners or Schur-type arguments, check irreducibility and field hypotheses. Over an algebraically closed field, an endomorphism of a finite-dimensional irreducible representation is scalar; over other fields its endomorphism division algebra can be larger.

## Worked calculation
Over C, the two-dimensional representation of C₂ sends its generator to A=[[0,1],[1,0]], with A²=I. The vectors (1,1) and (1,-1) are eigenvectors with eigenvalues +1 and -1, respectively. Their spans are invariant and form a direct sum because the vectors are linearly independent. Thus this representation is the sum of the trivial and sign representations, with a concrete change-of-basis witness.

## Tempting inference and counterexample
Schur's lemma does not always mean real scalar endomorphisms. Let C₃ act on R² by rotation through 2π/3. It has no invariant real line, hence is irreducible over R. The matrix J=[[0,-1],[1,0]] commutes with the rotation but is not a real scalar multiple of I. Scalar conclusions require the appropriate field setting.

## Stop and handoff
Stop semisimple decomposition in modular characteristic unless a separate valid theorem applies. Pass generator matrices, relations, field, characteristic, invariant-subspace bases and intertwiner equations to algebra or character computations. Distinguish irreducibility after base extension from irreducibility over the original field, and retain indecomposable structure when invariant complements cannot be justified.
