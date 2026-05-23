# Agen Matematika — Worked Example Walkthrough (ETC)

## Worked example
Common Ancestry vs Common Design (human origins) as a diagnosis + constraint + revision walkthrough.

Catatan anti-halu:
- Ini bukan pembuktian empiris.
- Ini menunjukkan bagaimana *formalisme minimal* ETC menolak salah-level conflict statements.

---

## 1) Type system (minimal)

Define types:
- `Text` : Qur’anic text (`Q`)
- `Interpretation` : interpretive propositions about `Q` (`Ti(Q)`)
- `Data` : empirical data (`D`)
- `Model` : scientific models built from data (`Mj(D)`)

## 2) Objects for this case

- `Q_human` : set of Qur’anic verses about human creation (treated as `Text`).
- `Ti_firstHuman` : proposition “Adam is the first biological human with no biological ancestry.” (type `Interpretation`).
- `Ti_singleCouple` : proposition “All humans descend from a single-couple genetic bottleneck.” (type `Interpretation`).
- `D_gen` : placeholder for relevant empirical data (type `Data`).
- `Mj_CA` : common ancestry model (type `Model`).
- `Mj_CD` : common design model (type `Model`).

## 3) Well-typed conflict predicate

Rule:
- `Conflict(x, y)` is *well-typed* only if there is an explicit bridge or `type(x)=type(y)`.

In ETC, the default meaningful conflicts include:
- `Conflict(Model, Interpretation)`
- `Conflict(Model, Model)`
- `Conflict(Interpretation, Interpretation)`

But **not** (by default):
- `Conflict(Model, Text)` without stating the intermediate interpretive proposition.

## 4) Diagnosis examples

### 4.1. Public claim (misclassified)
Statement S1:
- “Conflict(Mj_CA, Q_human).”

Diagnosis:
- `type(Mj_CA)=Model`, `type(Q_human)=Text`.
- No bridge rule stated.
- Therefore S1 → `type_error`.

### 4.2. Properly decomposed claim (meaningful)
Statement S2:
- “Conflict(Mj_CA, Ti_firstHuman).”

Diagnosis:
- `type(Mj_CA)=Model`, `type(Ti_firstHuman)=Interpretation`.
- Well-typed.
- Therefore S2 → `interpretive_conflict`.

### 4.3. Model competition
Statement S3:
- “Conflict(Mj_CA, Mj_CD).”

Diagnosis:
- Model vs model.
- This is a *scientific/model-level* conflict about explanatory structure, not about text.

## 5) Constraint sets

- `C_text`: `Q` is immutable (no revision operator applies to `Text`).
- `C_tafsir`: revisions to `Interpretation` must satisfy tafsir constraints (see `TAFSIR_BOUNDARY_ETC.md`).
- `C_science`: revisions to `Model` must track evidential support and explicit assumptions.

## 6) Restricted revision step (sketch)

If S2 holds (a conflict is identified), ETC allows revision only in revisable objects:

- Option R1 (revise interpretation):
  - `Ti_firstHuman' = Rev( Ti_firstHuman | C_tafsir )`
  - Output is a weaker, better-typed interpretive claim that does not exceed textual warrant.

- Option R2 (revise model):
  - `Mj_CA' = Rev( Mj_CA | C_science )`
  - Only if new `D` or assumption-failure warrants it.

ETC does **not** allow:
- `Rev(Q_human, …)`.

## 7) What the worked example demonstrates

1) The popular slogan “science vs Qur’an” is almost always a missing-middle claim.
2) Once decomposed, the conflict is usually “model vs interpretation,” not “model vs text.”
3) Constraint sets prevent both:
   - concordist over-reading (revising interpretation to fit modern science without textual warrant), and
   - anti-science over-reading (claiming the text explicitly denies any ancestry without warrant).

