# Proof playbook

## Statement first

For “every integer multiple of four is a multiple of two”, retain `Int` and the existential witness. The core asset encodes:

```lean
theorem multiple_four_is_multiple_two
    (n : Int) (h : ∃ k : Int, n = 4 * k) :
    ∃ m : Int, n = 2 * m := by
  obtain ⟨k, hk⟩ := h
  refine ⟨2 * k, ?_⟩
  calc
    n = 4 * k := hk
    _ = (2 * 2) * k := by rfl
    _ = 2 * (2 * k) := Int.mul_assoc 2 2 k
```

Changing the statement to naturals or adding `n = 0` changes the correspondence even if the code compiles. The witness construction is the proof; numeric testing of many values is supplementary evidence only.

## Tactic selection

| Goal shape | Approach | Constraint |
|---|---|---|
| Implication, conjunction, existential | Introduce, split, destruct, provide witness | Preserve binder order and witness type |
| Known theorem modulo normal form | `exact`, `apply`, `simpa using` | Check all theorem assumptions |
| Polynomial identity | `ring` | Requires supported algebraic structure and import |
| Numeric equality or inequality | `norm_num` | Numeric automation does not prove an arbitrary identity |
| Linear inequalities | `linarith` | Supply bounds and sign assumptions |
| Natural/integer linear arithmetic | `omega` | Truncated subtraction differs from integer subtraction |
| Rational expression | Establish nonzero denominators, then `field_simp` and normalization | Do not silently remove excluded points |

The Mathlib asset imports only `Mathlib.Tactic.Ring` and proves `(a + b)^2 = a^2 + 2*a*b + b^2` for rationals. Check it with the compatible Mathlib project, not a bare Lean invocation outside the project.

Prefer a short library proof when it transparently matches the claim. Search tactics may suggest a proof, but the resulting term still needs checking. Avoid imposing a blanket ban on automation or classical reasoning.

## Acceptance cases

- Integer multiples: preserve `Int`, extract the hypothesis witness and construct `2*k`.
- Requested unrestricted claim, supplied proof requires an extra assumption: expose the missing assumption; do not silently add it.
- `a / a = 1`: check the domain and handle `a = 0` rather than using unconditional cancellation.
- Checker unavailable: deliver an unchecked draft and actual tooling blocker, not invented logs.
- Compilation succeeds with `sorry`: report the outstanding obligation and withhold completion.

## Sources

- [Mathematics in Lean, basics](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html): proof structure and library reuse.
- [Lean tactic proofs](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/): core tactic semantics.
- [Mathlib tactic documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Tactic.html): tactic modules; verify against the pinned local source.
