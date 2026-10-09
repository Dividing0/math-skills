-- INTENTIONAL FAILURE: Nat equality is not an Int equality proof.
theorem cast_equality_failure (n m : Nat) (h : n = m) :
    (n : Int) = (m : Int) := by
  exact h
