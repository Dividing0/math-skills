-- Every integer multiple of four is a multiple of two.
theorem multiple_four_is_multiple_two
    (n : Int) (h : ∃ k : Int, n = 4 * k) :
    ∃ m : Int, n = 2 * m := by
  obtain ⟨k, hk⟩ := h
  refine ⟨2 * k, ?_⟩
  calc
    n = 4 * k := hk
    _ = (2 * 2) * k := by rfl
    _ = 2 * (2 * k) := Int.mul_assoc 2 2 k

#print axioms multiple_four_is_multiple_two
