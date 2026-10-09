# Domain playbook

## Select the method

1. For sums of arithmetic functions, establish the summatory function and use partial summation only with its actual endpoint conventions. Track error terms after weighting, and state dependence of every constant on auxiliary parameters.
2. For Dirichlet series, first work in a half-plane of absolute convergence. Termwise operations and Euler products require convergence plus multiplicative structure; continuation to another region is a separate analytic statement.
3. For contour methods, locate all poles and zeros relevant to the integrand, justify truncation and horizontal-edge estimates, and account for every crossed residue. State zero-free assumptions explicitly rather than turning a conditional bound into an unconditional theorem.

## Worked check

Let H_N=sum from n=1 to N of 1/n. Since 1/x is decreasing, integral from 1 to N+1 of dx/x <= H_N <= 1+integral from 1 to N of dx/x. Hence log(N+1)<=H_N<=1+log N, so H_N=log N+O(1), uniformly for integers N>=1 with an explicit absolute error bound.

## Invalid inference and witness

An average estimate does not bound each term. The sequence a_n=1 when n is a power of two and zero otherwise has sum up to N equal to floor(log2 N)+1. Its average tends to zero, but infinitely many a_n equal one. An averaged arithmetic estimate cannot silently become a pointwise decay claim.

## Completion and handoff

Return the arithmetic object, limiting regime, convergence region, uniformity, constants and conditional assumptions. Stop if the available theorem omits the needed parameter range. Hand complex analysis the exact meromorphic integrand and contour; hand computation a finite range while retaining the distinction between verified values and asymptotic proof.
