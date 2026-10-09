# Chain calculations and limits of invariants

## Choose a branch
- Cellular homology: use a CW structure, chosen coefficient ring and oriented cells. Compute actual attaching-map degrees for boundary maps; merely counting cells does not determine differentials.
- Mayer–Vietoris: for an open cover X=U union V, write inclusion-induced maps with consistent signs. Compute intersections and connected components before using exactness; a drawing does not certify the cover hypotheses.
- Fundamental groups: use van Kampen with a basepoint and path-connected open sets and intersection in its basic form. Homology H_1 gives the abelianization, so it loses commutator information.

## Worked cellular calculation
Give S¹ one 0-cell and one 1-cell. The endpoints of the oriented 1-cell attach to the same vertex, so the cellular differential is 1-1=0. Over Z the chain complex is 0→Z→Z→0 with zero arrow. Hence H_1(S¹;Z)=Z and H_0(S¹;Z)=Z; higher groups vanish. The constant map S¹→S¹ acts by zero on H_1, whereas the identity acts by one. They therefore cannot be homotopic, by homotopy invariance of induced homology maps.

## Tempting inference and counterexample
Equality of homology groups does not prove homeomorphism. For a direct separation of classification notions: R and a point both are contractible and have identical homology, but are not homeomorphic because their underlying cardinalities differ. Likewise a homology calculation alone cannot certify a homeomorphism. When homotopy equivalence is requested, produce maps and homotopies or invoke a theorem with its full hypotheses, rather than upgrading agreement of groups.

## Stop or hand off
If attaching degrees or maps are unspecified, return the chain groups and the missing differentials, not invented Betti numbers. Hand coefficient changes to algebra with torsion and the exact chain complex. For classification tasks record which invariants obstruct the proposed equivalence and which leave it undecided. Keep reduced versus unreduced H_0, basepoints, coefficients and orientations visible. If a stronger theorem such as a CW equivalence criterion is needed, verify all connectivity and map hypotheses before applying it.
