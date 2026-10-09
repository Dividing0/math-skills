# Domain playbook

## Select the method

1. For a Lipschitz parametrization, use the area formula with the appropriate Jacobian and image multiplicity. Injectivity almost everywhere can simplify the multiplicity term; otherwise count preimages explicitly.
2. For slicing a Lipschitz scalar map on Euclidean space, the coarea formula integrates level-set Hausdorff measure against the gradient magnitude. Check measurability, dimension and normalization; merely continuous maps do not supply this Lipschitz theorem.
3. For finite-perimeter sets, define perimeter through the distributional derivative of the indicator, not the topological boundary. State the open region and distinguish the reduced boundary, null modifications and classical smooth-boundary special cases.

## Worked check

For the line segment parametrized by f(t)=(3t,4t), 0<=t<=1, |f'(t)|=5. The map is injective, so normalized one-dimensional Hausdorff measure of its image equals integral_0^1 5 dt=5. This matches the endpoint distance; injectivity makes multiplicity one rather than concealing an overlap.

## Invalid inference and witness

Topological boundary size need not equal perimeter. Let E=Q intersect (0,1) as a subset of R. Its indicator is zero almost everywhere, so its distributional derivative and perimeter vanish. Yet its topological boundary is [0,1], which has infinitely many points and hence infinite H0 measure. Null-set changes preserve perimeter but can change topological boundaries drastically.

## Completion and handoff

Return the representative conventions, measure normalization, dimension, multiplicity, almost-everywhere qualifiers and relevant regularity. Stop if rectifiability or Lipschitz assumptions are absent; route to a weaker result rather than importing an area formula. For source checking use Leon Simon, Introduction to Geometric Measure Theory, chapter 2 area/coarea discussion, https://math.stanford.edu/~lms/ntu-gmt-text.pdf; verify the precise version needed before extending these special cases.
