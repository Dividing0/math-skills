-- INTENTIONAL FAILURE: h is absent; arbitrary P is not provable.
-- Adding h : P would change the theorem, not solve the original claim.
theorem missing_hypothesis (P : Prop) : P := by
  exact h
