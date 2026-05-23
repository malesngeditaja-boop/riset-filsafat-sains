# Formal Rule Block — Epistemic Type-Constraint Model

This block is intended to be inserted or adapted into the manuscript as the minimal formal spine of ETC.

## 1. Typed objects

Let the universe of discourse contain four primary object classes:

- `Text`: Qur'anic textual units treated as mutawatir lafaz.
- `Interpretation`: human interpretive propositions about `Text`.
- `Data`: empirical observations, measurements, or processed evidential records.
- `Model`: scientific explanatory structures built to account for `Data`.

For the paper's notation:

- `Q ∈ Text`
- `Ti(Q) ∈ Interpretation`
- `D ∈ Data`
- `Mj(D) ∈ Model`

`Ti(Q)` is not identical to `Q`. It is an interpretive proposition generated from `Q` under linguistic, contextual, and usul-based constraints.

`Mj(D)` is not identical to `D`. It is a model or model-family constructed to explain, organize, predict, or infer from `D`.

## 2. Bridge relation

Define a bridge relation:

`Bridge(Q, Ti(Q))`

This relation states that an interpretation `Ti(Q)` claims textual warrant from `Q`.

A public claim of conflict with the Qur'an is formally incomplete unless it specifies the bridge from `Q` to a concrete `Ti(Q)`.

## 3. Conflict predicate

Define:

`Conflict(x, y)`

as a relation of asserted incompatibility between two propositions, models, or interpretive commitments.

ETC treats `Conflict(x, y)` as well-typed only when at least one of the following is true:

1. `type(x) = type(y)`
2. `{type(x), type(y)} = {Model, Interpretation}`
3. There is an explicit bridge relation that converts a text-level claim into an interpretive proposition

Therefore:

- `Conflict(Mj(D), Ti(Q))` is well-typed.
- `Conflict(Mj1(D), Mj2(D))` is well-typed.
- `Conflict(Ti(Q), Tk(Q))` is well-typed.
- `Conflict(Mj(D), Q)` is ill-typed unless the relevant `Ti(Q)` is made explicit.

This is the model's primary diagnostic move.

## 4. Diagnosis function

Define a diagnosis function:

`Diagnose(Claim) → {type_error, interpretive_conflict, model_conflict, mixed_conflict, unresolved}`

Rules:

1. If a claim compares `Model` directly with `Text`, return `type_error` unless a bridge is supplied.
2. If a claim compares `Model` with `Interpretation`, return `interpretive_conflict`.
3. If a claim compares `Model` with `Model`, return `model_conflict`.
4. If the source of incompatibility cannot be located, return `unresolved`.

## 5. Constraint sets

ETC uses three constraint families:

### `C_text`

- `Q` is not revised.
- The text is not treated as an empirical hypothesis.
- The model does not evaluate tawatur.

### `C_tafsir`

Interpretive revision must satisfy:

- Arabic linguistic plausibility
- immediate and broader textual context
- relevant qarinah
- usul-based reasoning
- non-arbitrary relation to earlier tafsir discourse
- no forced concordism

### `C_science`

Scientific model revision must satisfy:

- evidential accountability to `D`
- explicit assumptions
- explanatory and predictive relevance where applicable
- openness to revision under new evidence
- no elevation of a model into a revelation-like authority

## 6. Restricted revision operator

Define restricted revision:

`Rev(x | C)`

as a revision operation permitted only when `x` belongs to a revisable type and the revised output satisfies the relevant constraint set.

Allowed:

- `Rev(Ti(Q) | C_tafsir)`
- `Rev(Mj(D) | C_science)`

Not allowed:

- `Rev(Q | C_science)`
- `Rev(Q | C_tafsir)`

The reason is not that interpretive claims are immune from evidence, but that `Q` and `Ti(Q)` have different epistemic types. Scientific evidence may pressure an interpretation that makes claims about the natural world; it does not revise the mutawatir text as text.

## 7. Transfer-of-certainty fallacy

ETC rejects the automatic inference:

`Cert(Q)=1 ⇒ Cert(Ti(Q))=1`

The certainty of the text's transmission does not automatically transfer to every human interpretation of that text.

A particular `Ti(Q)` may be strong, even qath'i-limited, but that requires a separate hermeneutic argument.

## 8. Worked-example schema

Given the public claim:

`Claim = Conflict(Mj_CA, Q_human)`

ETC first asks whether a bridge exists:

`Bridge(Q_human, Ti_firstHuman)`

If no bridge is specified:

`Diagnose(Claim) = type_error`

If the bridge is specified:

`Claim' = Conflict(Mj_CA, Ti_firstHuman)`

Then:

`Diagnose(Claim') = interpretive_conflict`

Revision may then proceed only as:

- `Rev(Ti_firstHuman | C_tafsir)`, if the interpretation exceeds textual warrant
- `Rev(Mj_CA | C_science)`, if the model fails against relevant data or assumptions

But never:

- `Rev(Q_human | C_science)`

## 9. Manuscript use

This formal block should be used modestly. It does not prove that a scientific model is true or false, nor does it settle the theological interpretation of a verse. It only prevents misclassification of the conflict and defines which layer may be revised.
