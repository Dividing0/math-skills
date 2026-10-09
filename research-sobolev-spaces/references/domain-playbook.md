# Domain playbook

## Select the method

1. For weak derivatives, use integration against compactly supported smooth test functions with the correct sign. Piecewise classical derivatives need jump terms checked; pointwise differentiability almost everywhere is not enough for membership in W1,p.
2. On a bounded Lipschitz domain, apply the appropriate embedding with dimension and exponent fixed. When p<d, W1,p embeds continuously into L^(dp/(d-p)); at the critical exponent do not replace the result by unrestricted L-infinity embedding.
3. For traces and H0^1, specify boundary regularity and the closure or trace-zero characterization being used. Compactness requires a strictly subcritical target in the usual bounded-domain Rellich setting, not just the continuous critical embedding.

## Worked check

On (-1,1), u(x)=|x| belongs to H1: it is square integrable and its weak derivative is sign(x), also square integrable. Split integral uφ' at zero and integrate by parts on each side; the zero values of u at the junction cancel the boundary contribution, giving integral uφ'=-integral sign(x)φ. Classical differentiability at zero is unnecessary.

## Invalid inference and witness

The Heaviside function on (-1,1) has classical derivative zero away from zero, but its distributional derivative is δ0: integral Hφ'=-φ(0). Since δ0 is not an L2 function, H is not H1. Ignoring a jump would wrongly conclude zero weak derivative.

## Completion and handoff

Return domain, dimension, exponent, representative, weak derivatives, boundary conditions and continuous versus compact embedding. Stop before evaluating a class at a point without justified representative regularity. Hand PDE work the exact weak space and trace interpretation; hand approximation the density and extension hypotheses required by the mesh or mollification argument.
