# Domain playbook: research-riemannian-geometry

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For local computations specify chart, metric coefficients and curvature sign convention. Compute the Levi-Civita connection from g^(ij) and metric derivatives; tensor components change with coordinates while scalar conclusions must be invariant.
2. For geodesics derive the second-order equation or energy Euler–Lagrange equations. Local existence from smooth coefficients does not guarantee extension for every parameter value; check metric or geodesic completeness before global conclusions.
3. For distance, compactness and comparison statements verify connectedness, completeness, dimension and the exact curvature bound. In the connected finite-dimensional boundaryless setting, Hopf–Rinow links metric completeness, geodesic completeness and compactness of closed bounded sets. Curvature estimates without these global hypotheses give a more limited conclusion.

## Worked derivation

On R with metric g=a² dx² for constant a>0, g^xx=a^(−2) and ∂_xg=0, hence Γ^x_xx=0. Geodesics satisfy x''=0 and exist for all time as x(t)=x_0+vt. Length of a monotone segment from p to q is a|q−p|; every curve has length at least this by integrating |x'|. Thus distance is a|q−p| and the metric is complete.

## Invalid inference and witness

The open interval (0,1) with dx² has the same local zero connection but is incomplete: x(t)=1/2+t exits the manifold at t=1/2. A local geodesic computation therefore does not prove geodesic completeness or justify global minimizing-geodesic conclusions on every manifold.

## Stop and handoff

Report chart domain, metric regularity, sign convention and local versus global conclusion. Stop when a comparison theorem's completeness or curvature hypotheses are unavailable; pass exact missing inequalities and boundary behavior to downstream proof work.
