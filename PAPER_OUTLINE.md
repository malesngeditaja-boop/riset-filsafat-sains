# Paper Outline

## Working title
**Epistemic Type-Constraint Model: A Framework for Distinguishing Qur'anic Text, Human Tafsir, Empirical Data, and Scientific Models**

## Core thesis
Many alleged conflicts between science and the Qur'an are misclassified because the Qur'anic text, human tafsir, empirical data, and scientific models are treated as if they occupy the same epistemic level.

The paper's claim is limited and specific:
- `Q` is the Qur'anic text as mutawatir lafaz.
- `Ti(Q)` is human interpretation of `Q`.
- `D` is empirical data.
- `Mj(D)` is a scientific model built from `D`.
- The strongest disagreement usually lies between `Mj(D)` and `Ti(Q)`, not between `Mj(D)` and `Q`.

## Section 1. Introduction

### Purpose
Frame the problem without overstating it.

### Points to make
- Popular discourse often says "science vs Qur'an" too quickly.
- That phrase can hide a category mistake.
- The paper proposes a narrower and more testable framing.
- The paper does not claim that every conflict disappears.
- The paper claims only that the level of conflict must be identified first.

### What not to claim
- Do not claim science can never challenge religion.
- Do not claim every tension is merely verbal.
- Do not claim the model solves all Qur'an-science issues.

### Sources to lean on
- Ansari
- Mir
- Naguib
- Ismail & Asnawi

## Section 2. Problem Setup

### Purpose
Define the paper's target object.

### Points to make
- Distinguish text, interpretation, data, and model.
- Explain why these four should not be collapsed.
- State that the paper is about epistemic classification before reconciliation.

### Working claim
The first mistake in many Qur'an-science debates is not a bad conclusion; it is a bad level assignment.

### What not to claim
- Do not treat the paper as a blanket defense of scientific exegesis.
- Do not treat the paper as a rejection of scientific findings.

## Section 3. Tafsir Boundary

### Purpose
Define what is fixed and what is revisable on the textual side.

### Points to make
- `Q` is fixed as mutawatir text.
- `Ti(Q)` is interpretive and may be revisable.
- Some interpretations may be `qath'i al-dalalah`, but that status needs argument.
- Most scientific readings should be treated cautiously unless the hermeneutic case is strong.

### What not to claim
- Do not say all tafsir is weak.
- Do not say all tafsir is revisable.
- Do not say `Q` itself is part of ordinary revision.

### Sources to lean on
- Naguib
- Mir
- Mohd-Noor
- Luqman et al.
- Ansory & Kholis

## Section 4. Philosophy of Science Boundary

### Purpose
Explain what science is allowed to do in the model.

### Points to make
- Separate data from model.
- Separate empirical support from ontological interpretation.
- Science can pressure a model or an interpretation, but not the tawatur status of the text.
- The paper should avoid saying "science says X" when what is really meant is "a model currently suggests X."

### What not to claim
- Do not treat scientific models as final truth.
- Do not treat data as identical to theory.
- Do not flatten all scientific disagreement into interpretation.

### Sources to lean on
- Thagard
- Data/model philosophy sources in `references/slr.md`
- Islam and Pseudoscience

## Section 5. Formal Model

### Purpose
Present the minimal formal apparatus.

### Objects
- `Q`
- `Ti(Q)`
- `D`
- `Mj(D)`
- `Conflict`
- `constraint`
- `revision`
- `diagnosis`

### Claims to formalize
- `Conflict(Mj(D), Q)` is usually a type error in the paper's framework.
- `Conflict(Mj(D), Ti(Q))` is the meaningful conflict class.
- Revision should apply only in the nazhari layer.
- Constraints prevent arbitrary concordism.

### What not to claim
- Do not claim the formalism is a full logic of religion and science.
- Do not claim the notation already proves the thesis.
- Do not use undefined symbols.

### Sources to lean on
- AGM literature
- Thagard
- Belief revision under restrictions

## Section 6. Constraint and Diagnosis

### Purpose
Show how the model handles disagreement without collapsing into either relativism or concordism.

### Points to make
- `constraint` should protect the textual side from uncontrolled revision.
- `diagnosis` should identify whether the conflict is textual, interpretive, scientific, or a transfer-of-certainty error.
- The paper should keep diagnosis subordinate to the epistemic classification.

### What not to claim
- Do not claim diagnosis always resolves the conflict.
- Do not claim every mismatch is due to interpretive error.

## Section 7. Limited Revision

### Purpose
Explain what can move and what cannot.

### Points to make
- Revision is allowed in `Ti(Q)` and in scientific models when evidence warrants it.
- Revision is not applied to `Q` as mutawatir text.
- The paper must explain the rule for when a reading is revisable and when it is not.

### What not to claim
- Do not imply the framework immunizes all interpretations.
- Do not imply empirical pressure automatically determines the correct tafsir.

## Section 8. Worked Example

### Purpose
Demonstrate the model on one concrete case.

### Requirements
- Pick one case only.
- Show the input claim.
- Identify the epistemic objects.
- Run the type check.
- State whether the conflict is valid.
- Show the constraint step.
- Show the revision outcome or the reason revision fails.

### What not to do
- Do not use multiple examples in the main body.
- Do not pick a case without enough literature support.
- Do not overclaim that the example settles the broader debate.

## Section 9. Discussion

### Purpose
State what the model contributes.

### Points to make
- The model improves conflict classification.
- It separates textual status from interpretive status.
- It preserves room for both hermeneutic caution and scientific criticism.
- It offers a controlled space for limited revision without textual revision.

### What not to claim
- Do not claim the model is complete.
- Do not claim universal applicability.
- Do not treat the model as replacing tafsir or science.

## Section 10. Limitations

### Purpose
Show the paper knows its own limits.

### Points to make
- The model depends on how `qath'i al-dalalah` is argued.
- The model does not resolve every hermeneutic dispute.
- The model is only as good as the formal definitions and the chosen case study.
- The paper does not prove scientific exegesis as a general method.

## Section 11. Conclusion

### Purpose
Close narrowly and clearly.

### Final claim
The phrase "science versus the Qur'an" is often too coarse. The more accurate question is whether a scientific model conflicts with a particular human tafsir, and whether that tafsir is actually revisable.

### Final boundary
`Q` remains text under tawatur; `Ti(Q)` remains the revisable interpretive layer.

## Draft safety rules

- Every claim must be traceable to either the corpus or the formal model.
- Every strong claim must be marked with its evidence base.
- If a claim is not directly supported, it stays out of the draft.
- If a section needs more evidence, mark it as `TODO: source needed` rather than guessing.

## Open items before drafting prose

- Choose the worked example.
- Finalize the exact rule for `qath'i al-dalalah`.
- Finalize the semantics of `Conflict`.
- Decide whether the paper will include a short algorithm or only formal definitions.
- Expand the SLR corpus with more English-language Scopus-valid sources.
