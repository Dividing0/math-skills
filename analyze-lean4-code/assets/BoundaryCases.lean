/-! A default loses information; whether that is a defect depends on the contract. -/

namespace BoundaryExample

def firstOrZero (xs : List Nat) : Nat := xs.headD 0

example : firstOrZero [] = 0 := rfl
example : firstOrZero [0] = 0 := rfl

-- An alternative API when callers must distinguish absence from a present zero.
def first? (xs : List Nat) : Option Nat := xs.head?

example : first? [] = none := rfl
example : first? [0] = some 0 := rfl

-- The existing API is recoverable by explicitly choosing a default.
theorem firstOrZero_eq_default (xs : List Nat) :
    firstOrZero xs = (first? xs).getD 0 := by
  cases xs <;> rfl

end BoundaryExample
