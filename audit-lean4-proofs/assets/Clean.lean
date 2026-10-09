-- Complete proof: expect an empty target axiom list.
theorem audited_and_comm (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  exact ⟨h.2, h.1⟩

#print axioms audited_and_comm
