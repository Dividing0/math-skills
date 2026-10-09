# Affine computations with scheme and field checks

## Method branches
1. For affine equations over a field k, specify the coordinate ring k[x₁,…,xₙ]/I. Radical ideals encode reduced closed subschemes; replacing I by its radical changes nilpotent structure. Over an algebraically closed field, point-set questions can use the Nullstellensatz with its actual hypotheses.
2. For a morphism, write the contravariant coordinate-ring map and verify that defining relations vanish. Check localization on each chosen open set; a formula with denominators does not automatically define a global regular map.
3. For a smoothness claim, specify finite presentation and the field or base scheme. Use the appropriate Jacobian criterion in its valid setting, distinguishing smoothness over the base from merely having a nonsingular-looking set of rational points.
4. For projective objects, use homogeneous equations and compatible affine charts. An affine calculation proves a global statement only after charts cover the object and transition maps preserve the claimed structure.

## Worked calculation
Over a field k, the affine curve xy=1 has coordinate ring k[x,y]/(xy-1). Map it to k[t,t⁻¹] by x↦t and y↦t⁻¹. Conversely t↦x and t⁻¹↦y is well-defined because xy=1. Composing both maps fixes their generators, so the rings are isomorphic. The curve is the multiplicative group scheme as an affine scheme, not the whole affine line.

## Tempting inference and counterexample
No rational points does not imply an empty scheme. Over R, Spec(R[x]/(x²+1)) has no real-valued point, but the ring is isomorphic to C and its spectrum contains a prime ideal. Base-changing to C gives two geometric points. Always name the notion of point being counted.

## Stop and handoff
Stop before asserting a global isomorphism if only one chart or one direction of the ring map has been checked. Pass the base, ideals, exact maps, covered opens, localization conditions and reducedness information to computational algebra or proof review. Numerical roots cannot certify radical membership or scheme equality; request exact ideal identities or an applicable algebraic certificate.
