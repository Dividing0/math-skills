# Domain playbook

## Select the method

1. For Cauchy formulas, require holomorphicity on a neighborhood of the relevant region and account for contour orientation. For multiply connected domains, use the appropriate homology or winding-number statement instead of assuming every closed integral vanishes.
2. For residues, list isolated singularities, compute their orders and coefficients, and sum with winding numbers. A pole on the contour invalidates the ordinary residue formula unless a separate prescription is supplied.
3. For identity or uniqueness arguments, zeros must accumulate inside a connected holomorphic domain. For logarithms and powers, specify a branch domain and prove compatibility; algebraic identities can fail after a branch choice.

## Worked check

For f(z)=1/(z(z-2)), partial fractions give -1/(2z)+1/(2(z-2)). On the positively oriented circle |z|=1 only zero is enclosed. Its residue is -1/2, so the integral is 2πi(-1/2)=-πi. The pole at two is outside, and neither pole lies on the contour.

## Invalid inference and witness

Infinitely many zeros are not enough for the identity theorem. The holomorphic function sin(πz) on C has every integer as a zero but is not identically zero. These zeros have no finite accumulation point in the domain. Similarly a zero sequence tending only to a boundary point does not meet the theorem hypothesis.

## Completion and handoff

Return domain, connected component, contours, branch conventions, singularities and theorem hypotheses. Stop when the path crosses a singularity or a branch is unspecified; propose a justified restriction rather than assigning a formal expression an unsupported global meaning. Hand symbolic computation expressions together with the chosen branch and excluded set.
