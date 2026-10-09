-- Concrete boundary checks and a universal property have different scope.
def first? (xs : List Nat) : Option Nat := xs.head?

example : first? [] = none := by decide
example : first? [0] = some 0 := by decide
example : first? [2, 7] = some 2 := by decide

example (xs : List Nat) : xs.reverse.reverse = xs := List.reverse_reverse xs
