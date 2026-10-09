import Lean

namespace MetaprogramExample

-- Quotation gives the generated binder a fresh scope.
macro "doubleNat " value:term:max : term =>
  `(let x : Nat := $value; x + x)

example : doubleNat 5 = 10 := by decide
example : (let x : Nat := 3; doubleNat (x + 1)) = 8 := by decide

open Lean Elab Tactic

-- Delegate to a tactic that constructs a kernel-checked equality proof.
elab "close_rfl" : tactic => do
  evalTactic (← `(tactic| rfl))

theorem generated_identity (n : Nat) : n = n := by close_rfl

end MetaprogramExample
