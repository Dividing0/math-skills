-- INTENTIONAL CORRESPONDENCE FAILURE: this proves only an implication.
-- It does not formalize the false unrestricted claim that every Nat is zero.
theorem every_nat_zero (n : Nat) (h : n = 0) : n = 0 := by
  exact h

#print axioms every_nat_zero
