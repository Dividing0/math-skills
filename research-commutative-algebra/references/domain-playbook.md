# Rings, localization and exactness

## Choose a branch
- Quotient or ideal calculations: fix a commutative unital ring and distinguish radical, prime and maximal ideals. An ideal I is prime exactly when R/I is a nonzero integral domain; zero divisors can decisively refute primeness.
- Localization: specify a multiplicatively closed set S. Fractions a/s and b/t agree if some u in S annihilates ta-sb. Localization of modules is exact; localization need not be faithful, so a vanishing localized element need not vanish globally.
- Tensor arguments: tensor product is right exact. To preserve all injections, require the tensoring module to be flat; freeness is a sufficient special case. A failed injection may be measured by a Tor term, whose ring and module arguments must be named.

## Worked quotient
Let k be a field and R=k[x]. Division by x² gives a unique remainder a+bx, so R/(x²) is a two-dimensional k-vector space with basis [1],[x]. Its multiplication satisfies [x]²=0 while [x] is nonzero, since x is not divisible by x². Thus (x²) is not prime. The radical is (x): if f has nonzero constant term, no power is divisible by x²; if f is divisible by x, f² is divisible by x². The quotient's nilpotents distinguish it from R/(x).

## Tempting inference and counterexample
Tensoring does not preserve an arbitrary injection. The injection Z→Z given by multiplication by 2 becomes the zero map Z/2→Z/2 after tensoring with Z/2, so it is no longer injective. Right exactness remains valid, but left exactness was imported without flatness.

## Stop or hand off
If a dimension or associated-prime theorem requires Noetherian hypotheses, check them rather than infer them from familiar examples. Return the exact ring, ideal, module maps and localization set to downstream homological work. Do not conclude a module is zero from one localization. Primary reference for flatness definitions and exactness: The Stacks Project, Section 10.39 (tag 00H9), https://stacks.math.columbia.edu/tag/00H9, checked 2026-10-08. Read the applicable lemma at the point of use.
