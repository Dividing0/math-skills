import Mathlib.Tactic.Ring

-- Check in a compatible, pinned Mathlib project.
theorem rational_square_sum (a b : ℚ) :
    (a + b)^2 = a^2 + 2*a*b + b^2 := by
  ring

#print axioms rational_square_sum
