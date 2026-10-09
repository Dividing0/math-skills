/-! A value-preserving refactor; reduction-sensitive callers still need checking. -/

namespace RefactorExample

namespace Before

def countItems {α : Type u} : List α → Nat
  | [] => 0
  | _ :: xs => countItems xs + 1

end Before

namespace After

def countItems {α : Type u} (xs : List α) : Nat := xs.length

end After

theorem countItems_eq {α : Type u} (xs : List α) :
    Before.countItems xs = After.countItems xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simpa only [Before.countItems, After.countItems, List.length_cons] using
      congrArg (fun n => n + 1) ih

example : After.countItems ([] : List Nat) = 0 := rfl
example : After.countItems [4, 7, 9] = 3 := rfl

end RefactorExample
