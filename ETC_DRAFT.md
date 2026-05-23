# Epistemic Type‑Constraint Model (ETC)
## A Framework for Diagnosing Misclassified Qur’an–Science Conflicts

**Draft status:** lane‑assembled working draft (not yet submission‑ready).

**Core claim (calibrated):** Many public disputes labeled “science vs Qur’an” are misclassified because four epistemic objects—`Q` (Qur’anic text), `Ti(Q)` (human interpretation), `D` (empirical data), and `Mj(D)` (scientific model built from data)—are treated as if they occupy one level. ETC proposes a minimal diagnostic scaffold (type‑checking + constraints + restricted revision) to identify which conflicts are meaningful (typically `Conflict(Mj(D), Ti(Q))`) and which are category mistakes (often `Conflict(Mj(D), Q)` stated without an interpretive bridge).

**What this paper does not claim:** ETC does not claim that all tensions dissolve, that science cannot challenge religious commitments, or that the model itself resolves substantive theological disputes. It is a *classification‑first* and *revision‑restricted* framework.

---

## 1. Introduction

Public discourse frequently jumps directly to the slogan “science contradicts the Qur’an.” Yet the slogan often compresses multiple distinct objects into one: the Qur’anic text, human readings of that text, empirical observations, and theory‑laden scientific models. When these objects are collapsed, disagreement becomes harder to locate, and resolution attempts become rhetorically driven rather than analytically tractable.

A significant portion of the Qur’an‑and‑science debate concerns scientific exegesis (*tafsīr ʿilmī*)—whether, when, and how the Qur’an should be read as containing or anticipating scientific claims. Core critiques of scientific exegesis emphasize the need for methodological constraints and warn against concordist over‑reading. (Load‑bearing critique anchors: Ansari 2004; Mir 2004; Naguib 2019; Mohd‑Noor 2013.)

The ETC contribution is not to relitigate the entire Qur’an‑science relation, but to supply a minimal epistemic scaffold: (i) a typed distinction among `Q`, `Ti(Q)`, `D`, and `Mj(D)`; (ii) constraints that prevent arbitrary revision; and (iii) a restricted revision policy that preserves what is fixed while permitting movement where revision is legitimate.

**Citation anchors (Intro):** Ansari (2004); Mir (2004); Naguib (2019); Mohd‑Noor (2013); Khalil (1991).

---

## 2. Problem Setup: Four Epistemic Objects

We distinguish four objects:

- `Q`: the Qur’anic text (treated as fixed as mutawātir lafẓ).
- `Ti(Q)`: human interpretation(s) of `Q`.
- `D`: empirical data.
- `Mj(D)`: scientific models (and model families) constructed to explain `D`.

The ETC hypothesis is local and testable:

1) A large class of alleged conflicts is misclassified because it is stated as `Conflict(Mj(D), Q)` without making explicit the interpretive bridge that produced a specific `Ti(Q)`.
2) Once the bridge is made explicit, the meaningful conflict class is often `Conflict(Mj(D), Ti(Q))`, or a competition among models `Conflict(Mj1(D), Mj2(D))`, rather than model‑against‑text.

---

## 3. Tafsir Boundary: What Is Fixed and What Is Revisable

### 3.1. `Q` vs `Ti(Q)`

In ETC, `Q` is not an ordinary hypothesis subject to revision. `Ti(Q)`, by contrast, is the interpretive layer: the set of propositions that connect a text to particular meanings, including bridges to modern scientific taxonomies.

### 3.2. Default revisability and “qath’i (limited)” status

ETC does not assume that all interpretations are weak, nor that all are equally revisable. It proposes a conservative default: most science‑linked readings should be treated as *nazharī* (revisable) unless a strong hermeneutic case is made that a specific interpretive proposition has a “qath’i‑limited” status.

### 3.3. Anti‑cocoklogi constraint (tafsir‑side)

ETC requires a minimal `C_tafsir` constraint set: revisions to interpretive propositions must respect Arabic linguistic plausibility, immediate textual context (siyāq/qarā’in), and must not treat contemporary scientific models as the primary driver of meaning. Scientific models can function as compatibility checks, not as meaning‑generators.

(Operational memo basis: `agent_reports/TAFSIR_BOUNDARY_ETC.md`.)

**Citation anchors (Tafsir boundary):** Ansari (2004); Mir (2004); Naguib (2019); Mohd‑Noor (2013).

---

## 4. Philosophy of Science Boundary: Data, Models, and Overclaim

### 4.1. `D` is not `Mj(D)`

Scientific practice distinguishes data from the models used to organize and explain it. Data are measurement‑laden and processed, but still conceptually distinct from explanatory structures. A key ETC motivation is to block the move “science says X” when what is meant is “a current model suggests X under assumptions A.”

(Load‑bearing basis for the data/model distinction: Leonelli 2019; Antoniou 2021.)

### 4.2. Transfer‑of‑certainty error

ETC highlights two frequent errors:

- `D → Mj` transfer: treating the strength of data as if it automatically guarantees the finality of a model.
- `Ti(Q) → Q` transfer: treating a popular or traditional reading as if it has the same epistemic status as the text itself.

(Operational memo basis: `agent_reports/SCIENCE_WORKED_EXAMPLE_ETC.md`.)

**Citation anchors (Science boundary):** Leonelli (2019); Antoniou (2021); Okasha (2002).

---

## 5. Formal Model (Minimal, Usable)

### 5.1. Types

Define a minimal type universe:

- `Text` for `Q`
- `Interpretation` for `Ti(Q)`
- `Data` for `D`
- `Model` for `Mj(D)`

### 5.2. Conflict typing rule

`Conflict(x, y)` is well‑typed only when the comparison is licensed (same type, or an explicit bridge rule).

ETC treats these as default meaningful conflicts:

- `Conflict(Model, Interpretation)`
- `Conflict(Model, Model)`
- `Conflict(Interpretation, Interpretation)`

And treats `Conflict(Model, Text)` as ill‑typed unless the interpretive bridge is made explicit.

### 5.3. Constraint sets

- `C_text`: `Q` immutable.
- `C_tafsir`: interpretive revisions must satisfy tafsir constraints.
- `C_science`: model revisions must track evidence and assumptions.

### 5.4. Restricted revision

When a meaningful conflict is diagnosed, revision applies only in revisable layers:

- revise `Ti(Q)` under `C_tafsir`, and/or
- revise `Mj(D)` under `C_science`.

But never revise `Q`.

(Operational memo basis: `agent_reports/MATH_WORKED_EXAMPLE_ETC.md`; formal apparatus anchors: AGM 1985; Long et al. 2022; Thagard 1992.)

**Citation anchors (Formal model):** Alchourrón et al. (1985); Long et al. (2022); Thagard (1992); Delgrande & Schaub (2003).

---

## 6. Worked Example: Common Ancestry vs Common Design (Human Origins)

### 6.1. Scope

This paper uses one worked example: human origins debates framed as “common ancestry” vs “common design.” This counts as a single example because both positions are competing model‑level hypotheses about the same target domain and are commonly mapped onto a shared cluster of interpretive claims about Adam and human unity.

(See scope memo: `agent_reports/WORKED_EXAMPLE_SCOPE_ETC.md`.)

### 6.2. Tafsir‑side decomposition

Public claims typically move from a small set of textual motifs (creation from earth; Adam; human unity) to stronger propositions such as “Adam must be the first biological human with no biological ancestry” or “humanity must pass through a single‑couple genetic bottleneck.” ETC classifies these stronger propositions as `Ti(Q)`, not `Q`, unless a special hermeneutic argument is provided.

(See tafsir worked example memo: `agent_reports/TAFSIR_WORKED_EXAMPLE_ETC.md`.)

### 6.3. Science‑side level mapping

ETC represents the scientific side as `D` (data) plus `Mj(D)` (models). “Common ancestry” is treated as a model family `Mj_CA`; “common design” as a model/interpretive family `Mj_CD`. ETC does not assume either is true; it diagnoses how conflicts are stated.

(See science worked example companion: `agent_reports/SCIENCE_WORKED_EXAMPLE_ETC.md`.)

### 6.3.1. Model clarification (minimum for submission)

To keep the worked example honest and non‑hand‑wavy, the paper must anchor `Mj_CA` (common ancestry) to standard evolutionary biology usage, and must explicitly state what epistemic status is being assigned to “common design.”

- `Mj_CA` is treated as a family of evolutionary models in mainstream biology (textbook anchor: Futuyma & Kirkpatrick, *Evolution*, 4th ed., 2017).
- Claims about what counts as evidence for common ancestry (and how evidence should be understood) are treated as philosophy‑of‑biology questions, not as slogans (anchor: Sober, *Evidence and Evolution*, 2008).
- “Common design” is commonly presented as an explanatory alternative that may be metaphysical or theological in character; unless it is specified in a way that yields discriminating, testable expectations relative to `D`, ETC classifies it as *interpretive/metaphysical* rather than as a competing `Model` in the strict sense.

(General philosophy‑of‑science anchor for model talk, demarcation, and overclaim: Okasha, *Philosophy of Science: A Very Short Introduction*, 2002.)

**Citation anchors (Worked example, science-side):** Futuyma & Kirkpatrick (2017); Sober (2008); Okasha (2002).

### 6.4. Diagnosis and revision

A misclassified public statement often takes the form:

- S1: `Conflict(Mj_CA, Q_human)`.

ETC diagnosis:

- `type(Mj_CA)=Model`, `type(Q_human)=Text` → ill‑typed unless the interpretive bridge is provided.

A properly decomposed statement is:

- S2: `Conflict(Mj_CA, Ti_firstHuman)`.

ETC diagnosis:

- `Model` vs `Interpretation` → well‑typed and meaningful.

The restricted revision response is then constrained:

- revise the interpretive proposition (if it exceeds textual warrant) under `C_tafsir`, and/or
- revise the model (only if warranted by `D` and explicit assumptions) under `C_science`.

(See formal walkthrough: `agent_reports/MATH_WORKED_EXAMPLE_ETC.md`.)

---

## 7. Discussion

### 7.1. What ETC contributes

ETC contributes a discipline of *conflict location*. It does not replace tafsir, nor does it replace scientific inquiry. It aims to make explicit the epistemic objects being compared, prevent transfer‑of‑certainty errors, and restrict revision so that the framework cannot be used as a carte blanche for concordism or for immunizing any specific interpretation.

### 7.2. Why constraints matter

Scientific exegesis debates frequently fail because they operate with implicit bridges and implicit revision policies. ETC makes both explicit: the bridge must be written as `Ti(Q)`, and revision must be constrained.

---

## 8. Limitations

1) The worked example is currently framed at the level of diagnosis. A submission‑ready version must append a textual basis appendix listing the specific verses used (Arabic + transliteration + translation) and must justify the interpretive classification decisions.
2) A submission‑ready version should include a small, carefully chosen set of philosophy‑of‑biology sources clarifying what counts as `Mj_CA` and what would qualify (or fail to qualify) as `Mj_CD` as a scientific model.
3) The current SLR seed corpus is strong in critique + formal apparatus + data/model distinction, but needs direct usūl/tafsir sources for the qath’i‑limited vs nazhari boundary rule.

(Reviewer stress test: `agent_reports/REVIEWER_REPORT_ETC_COMMON_ANCESTRY.md`.)

---

## 9. Conclusion

Before asking whether a conflict can be reconciled, ETC asks whether the conflict has even been stated at the right epistemic level. By separating text, interpretation, data, and models—and by restricting revision through constraints—the framework converts a diffuse slogan (“science vs Qur’an”) into a set of explicit, auditable comparisons.

---

## References (seed + verified anchors; incomplete)

Note: This bibliography is intentionally partial and contains only items already present/verified in the current corpus artifacts.

- Alchourrón, C. E., Gärdenfors, P., & Makinson, D. (1985). On the Logic of Theory Change: Partial Meet Contraction and Revision Functions. *The Journal of Symbolic Logic*, 50(2), 510–530. https://doi.org/10.2307/2274239
- Ansari, Z. I. (2004). The Scientific Exegesis (Tafsīr) of the Qur'an. *Al-Fikr al-islāmī al-muʿāṣir*, 9(35). https://doi.org/10.35632/citj.v9i35.1449
- Antoniou, A. (2021). What is a data model? An anatomy of data analysis in high energy physics. *European Journal for Philosophy of Science*. https://doi.org/10.1007/s13194-021-00412-2
- Bigliardi, S. (2025). *Islam and Pseudoscience*. Cambridge Elements (Elements in Islam and Science). https://doi.org/10.1017/9781009608237
- Delgrande, J. P., & Schaub, T. (2003). A consistency-based approach for belief change. *Artificial Intelligence*. https://doi.org/10.1016/S0004-3702(03)00111-5
- Khalil, I. (1991). The Qur’an and Modern Science: Observations on Methodology. *American Journal of Islam and Society*, 8(1), 1–13. https://doi.org/10.35632/ajis.v8i1.2641
- Leonelli, S. (2019). What distinguishes data from models? *European Journal for Philosophy of Science*, 9, Article 22. https://doi.org/10.1007/s13194-018-0246-0
- Long, Z., Meng, H., Li, T., Li, H.-C., & Sioutis, M. (2022). A framework for belief revision under restrictions. *The Knowledge Engineering Review*, 37:54. https://doi.org/10.1017/S0269888922000054
- Mir, M. (2004). Scientific Exegesis of the Qurʾan—A Viable Project? *Journal of Islam & Science*, 2(1).
- Mohd-Noor, A. Y. (2013). *Scientific Exegesis Reappraised: A Critical Study of the al-Jawāhir fī Tafsīr al-Qur'ān al-Karīm* (Doctoral thesis). Durham University. https://etheses.dur.ac.uk/9390/
- Naguib, S. (2019). The Hermeneutics of Miracle… Part I. *Journal of Qur'anic Studies*, 21(3), 57–88. https://doi.org/10.3366/jqs.2019.0399
- Okasha, S. (2002). *Philosophy of Science: A Very Short Introduction* (1st ed.). Oxford University Press. Print ISBN 978-0-19-280283-5. https://doi.org/10.1093/actrade/9780192802835.001.0001
- Sober, E. (2008). *Evidence and Evolution: The Logic Behind the Science*. Cambridge University Press. ISBN 978-0-521-87188-4.
- Futuyma, D. J., & Kirkpatrick, M. (2017). *Evolution* (4th ed.). Sinauer Associates. ISBN 978-1-60535-696-9.
- Thagard, P. (1992). Coherence as constraint satisfaction. *Cognitive Science*. https://doi.org/10.1016/S0364-0213(99)80033-0
- Shaikh Mohd Saifuddeen Shaikh Mohd Salleh, & Baharuddin, A. (2011). Significance of science and scientific thought from the Islamic perspective. *QURANICA: International Journal of Quranic Research*, 1(1), 73–87. https://ejournal.um.edu.my/index.php/quranica/article/view/5268
