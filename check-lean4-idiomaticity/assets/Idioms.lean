/-! Both styles are valid; this small claim needs no intermediate fact. -/

namespace IdiomExample

namespace Before

theorem swap_and (p q : Prop) (h : p ∧ q) : q ∧ p := by
  have hp : p := h.left
  have hq : q := h.right
  have result : q ∧ p := by
    constructor
    · exact hq
    · exact hp
  exact result

end Before

namespace After

theorem swap_and (p q : Prop) (h : p ∧ q) : q ∧ p := ⟨h.2, h.1⟩

end After

-- Both declarations satisfy the same caller contract.
example (p q : Prop) : p ∧ q → q ∧ p := Before.swap_and p q
example (p q : Prop) : p ∧ q → q ∧ p := After.swap_and p q

end IdiomExample
