# Domain playbook

## Select the method

1. For universal constructions, specify the category and the morphism class. Verify both existence and uniqueness of the mediating morphism for arbitrary test objects; two convenient structure maps do not establish universality.
2. For functors, check preservation of identities and composition. For natural transformations, write the naturality equation for every morphism; objectwise maps alone are insufficient.
3. For equivalence, construct functors in both directions and natural isomorphisms to identities, or establish full faithfulness and essential surjectivity under suitable size conventions. Equality of object counts or bijection on objects does not substitute for morphism-level evidence.

## Worked check

In Set, the equalizer of f,g:X->Y is E={x in X:f(x)=g(x)} with inclusion i. If h:Z->X satisfies fh=gh, every h(z) belongs to E, so define u(z)=h(z). Then iu=h. Since i is inclusion, any u with iu=h must take exactly those values, proving uniqueness and the universal property.

## Invalid inference and witness

An objectwise bijection need not be natural. On a two-element set choose a swap as its component but identities on other sets. For the map from a singleton selecting one of those elements, the two naturality composites choose different elements. Components that are isomorphisms do not repair missing naturality.

## Completion and handoff

Return categories, size assumptions, arrows and commuting equations. Stop when an alleged construction lacks a required map or uniqueness proof. Hand algebra or topology the explicit universal property and preserved structure; label equivalence separately from literal equality or isomorphism of particular objects.
