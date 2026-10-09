# Domain playbook: research-information-theory

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For finite discrete variables, write the probability mass function and logarithm base, then compute H(X)=−Σp log p with 0 log 0=0. For mutual information verify the joint distribution and use I(X;Y)=H(X)−H(X|Y), not a correlation proxy.
2. For continuous variables require a density and integrability sufficient for the requested differential entropy. Under Y=aX+b, a≠0, h(Y)=h(X)+log|a| when these entropies exist; negativity is allowed and units matter.
3. For channels distinguish an achievable input distribution from capacity, which optimizes over allowed inputs. Coding conclusions require block model, memory assumptions and error criterion. Data-processing bounds apply to an actual Markov chain, not to variables merely named “processed”.

## Worked derivation

Let X be a fair bit and Y=X⊕N where N is independent Bernoulli(p). Then Y is fair, H(Y)=1 bit, and H(Y|X)=H_b(p)=−p log₂p−(1−p)log₂(1−p). Therefore I(X;Y)=1−H_b(p). At p=1/2 it vanishes, consistent with independence; at p=0 it is one bit. Capacity equals this value for this binary symmetric channel, but the mutual-information calculation itself used the specified fair input.

## Invalid inference and witness

For X uniform on (0,1/4), density is 4 and h(X)=−∫_0^(1/4)4 log 4 dx=−log 4. Rejecting this distribution because its differential entropy is negative confuses it with discrete entropy.

## Stop and handoff

Return units, distribution, support, independence and finiteness conditions. If an entropy expression is undefined or infinite, avoid subtracting infinities; use a well-defined relative-entropy formulation or hand off the integrability question.
