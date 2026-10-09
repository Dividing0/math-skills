# Exact arithmetic and divisibility obligations

## Method branches
1. For linear congruences ax≡b mod m with m>0, set d=gcd(a,m). Solutions exist exactly when d divides b; reduction then uses modulus m/d and an invertible coefficient a/d. Lift back to all residue classes modulo m.
2. For simultaneous congruences, use the coprime Chinese remainder theorem only for pairwise coprime moduli. In the general two-modulus case, residues must agree modulo their gcd; the solution, when it exists, is unique modulo their least common multiple.
3. For Diophantine equations, use congruences as obstructions but not as universal sufficiency criteria. A local calculation must be followed by an actual integer construction, descent, bound or applicable local-global theorem.
4. For primality computation, distinguish deterministic certificates from probable-prime evidence. Trial division certifies primality after every prime up to the square root has been excluded, using exact integer arithmetic.

## Worked calculation
Solve 6x≡8 mod 14. Here d=2 divides 8, so reduce to 3x≡4 mod 7. The inverse of 3 modulo 7 is 5, giving x≡20≡6 mod 7. Thus modulo 14 the solutions are x=6 and x=13. Substitution gives 36≡8 and 78≡8 mod 14, confirming both classes.

## Tempting inference and counterexample
Coprimality of one pair cannot justify a many-modulus CRT calculation. The system x≡0 mod 4 and x≡1 mod 6 has no solution: the first demands an even x and the second an odd x. Applying an inverse of 4 modulo 6 is invalid because that inverse does not exist.

## Stop and handoff
Stop modular division when gcd conditions are unresolved. Pass signs, positivity restrictions, moduli, residue normalization, exact gcd witnesses and solution-lifting rules to algebra or algorithm work. An unsuccessful bounded search establishes only absence within its searched range unless a proof bounds all possible solutions. Record whether a claimed prime was proved, certified by an executed checker or merely subjected to a probabilistic test.
