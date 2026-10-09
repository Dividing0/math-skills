import Mathlib.Data.Nat.Basic

-- A sufficient Mathlib import can expose a declaration from core Lean.
#check Nat.add_comm

theorem reversed_nat_sum (a b : Nat) : a + b = b + a := by
  exact Nat.add_comm a b

#print axioms reversed_nat_sum
