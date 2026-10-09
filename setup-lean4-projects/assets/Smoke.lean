-- Core-only checker smoke test; no Mathlib dependency.
theorem smoke_and_comm (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  exact ⟨h.2, h.1⟩
