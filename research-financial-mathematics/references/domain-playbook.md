# Pricing as a conditional mathematical model

## Choose a branch
- One-period replication: assume a frictionless model, a tradable risky asset, a positive risk-free gross return R and unrestricted borrowing and shorting. For two risky returns d<u with d<R<u, the risk-neutral weight q=(R-d)/(u-d) lies strictly between zero and one and prices replicable payoffs by discounted expectation.
- Finite-state incompleteness: solve the linear payoff-span problem before claiming a unique price. No-arbitrage can leave several positive pricing measures; a payoff outside the traded span need not have one replication value.
- Continuous-time pricing: state a filtered probability space, admissible self-financing strategies and integrability assumptions. An equivalent martingale measure is a model property, not the historical return distribution. Avoid invoking a continuous-time no-arbitrage equivalence without its precise admissibility and topology conditions.

## Worked replication
Set S_0=100, terminal stock prices 120 and 80, and R=1. A call with strike 100 pays 20 or 0. Solve 120*Delta+B=20 and 80*Delta+B=0, where B is the terminal risk-free holding. Subtraction yields Delta=1/2 and B=-40. Initial cost is 50-40=10. Risk-neutral q=(1-0.8)/(1.2-0.8)=1/2 gives the same discounted expected payoff 10. This equality follows from replication assumptions; no historical probability was used.

## Tempting inference and counterexample
A q value is not an observed frequency forecast. The same terminal stock levels can have historical up probability p=0.9 while replication still gives q=0.5 and price 10. The historical expected payoff 18 is therefore not the model's replication price. Equating the measures is an additional assumption and changes what is being asserted.

## Stop or hand off
If transaction costs, trading constraints or missing instruments matter, hand off the payoff span and constraints rather than reusing the frictionless conclusion. Return model parameters, measure, admissibility and calibration provenance; do not represent a price calculation as a guaranteed return. Primary educational source: MIT OCW, 18.366, Financial Derivatives notes, risk-neutral binomial valuation discussion pp.5–6, https://ocw.mit.edu/courses/18-366-random-walks-and-diffusion-fall-2006/365b24f3b4d11990849fa85ed7a9ed58_iap00_lecture.pdf, checked 2026-10-08. These are abstract pricing examples, not current market facts.
