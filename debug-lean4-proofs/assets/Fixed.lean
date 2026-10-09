-- This conditional statement differs from the unrestricted failing claim.
theorem proposition_with_hypothesis (P : Prop) (h : P) : P := by
  exact h

-- This repair preserves the cast-equality statement and its hypotheses.
theorem cast_equality_fixed (n m : Nat) (h : n = m) :
    (n : Int) = (m : Int) := by
  cases h
  rfl
