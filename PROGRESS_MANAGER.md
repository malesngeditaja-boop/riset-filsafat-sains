# ETC Pipeline Manager — Current Status

Branch: `codex/epistemic-type-constraint-model`

This file is the single entrypoint for understanding what has been done, what remains, and how to continue on another device.

## What exists now (clickable artifacts)

### Manuscript (ETC)
- `ETC_DRAFT.md` — lane-assembled draft manuscript with a tightened formal rule block (still not fully submission-ready).
- `ETC_APPENDIX_TEXTUAL_BASIS.md` — worked-example textual basis (Arabic + working transliteration + gloss + `Ti(Q)` propositions).

### Lane outputs (ETC)
- `agent_reports/SLR_REPORT_ETC.md`
- `agent_reports/SLR_CORPUS_TABLE_ETC.md`
- `agent_reports/SCOPUS_METADATA_ETC.md`
- `agent_reports/TAFSIR_BOUNDARY_ETC.md`
- `agent_reports/TAFSIR_WORKED_EXAMPLE_ETC.md`
- `agent_reports/SCIENCE_WORKED_EXAMPLE_ETC.md`
- `agent_reports/MATH_WORKED_EXAMPLE_ETC.md`
- `agent_reports/FORMAL_RULE_BLOCK_ETC.md`
- `agent_reports/REVIEWER_REPORT_ETC_COMMON_ANCESTRY.md`
- `agent_reports/SYNTHESIS_PLAN_ETC_COMMON_ANCESTRY.md`

### Corpus seed (updated)
- `references/slr.md`

## Worked example currently implemented

Single worked example: **Common Ancestry vs Common Design (human origins)**.

Scope memo:
- `agent_reports/WORKED_EXAMPLE_SCOPE_ETC.md`

## Pipeline status (lane-by-lane)

1) SLR lane
- Status: usable (seed corpus + claim-to-citation map + flagged sources).
- Remaining: lock a final “core/supporting/optional/flagged” list and add any missing metadata still not pinned in `references/slr.md`.

2) Scopus retrieval lane
- Status: metadata verification done for several load-bearing items; indexing proof not fully done.
- Remaining: evidence-based “Scopus indexed yes/no” via Scopus source list, publisher metadata, OpenAlex, or another auditable legal source if required by the target journal.

3) Tafsir lane
- Status: boundary rule + worked-example decomposition written; appendix includes specific verses.
- Remaining: adjust transliteration/translation to the target journal’s required standard; optionally add classical usūl/tafsir anchors for the qath’i-limited vs nazhari discussion.

4) Philosophy of science lane
- Status: `D` vs `Mj(D)` memo + worked-example companion written; minimal anchors added.
- Remaining: if the target journal expects more, add a small number of philosophy-of-biology references specifically on evidence for common ancestry.

5) Math/formal lane
- Status: improved. `agent_reports/FORMAL_RULE_BLOCK_ETC.md` now exists and `ETC_DRAFT.md` includes typed objects, bridge relation, conflict predicate, diagnosis function, constraint sets, restricted revision operator, and transfer-of-certainty rule.
- Remaining: polish prose for target journal style and decide whether to keep the formal block in the main text or move the expanded version to appendix.

6) Reviewer lane
- Status: stress-test + rejection risks captured.
- Remaining: implement target-journal-specific reviewer risks after journal selection.

7) Synthesis lane
- Status: assembled into `ETC_DRAFT.md`; formal section tightened.
- Remaining: formatting pass for the target journal; finalize bibliography style; remove or quarantine anything still flagged.

## Current blockers to “submission-ready”

- Target journal constraints not locked (citation style, transliteration standard, word count, required Arabic + transliteration conventions).
- Indexing/venue verification not completed for all non-core sources (some sources intentionally flagged).
- Common design framing must stay consistent: unless operationalized with discriminating empirical expectations, it should be treated as interpretive/metaphysical rather than as a strict scientific model competitor.

## Next actions (recommended order)

1) Choose target journal + citation style and apply formatting consistently in `ETC_DRAFT.md`.
2) Lock the Scopus/source-status table: core/supporting/optional/flagged.
3) Decide how you want to treat “common design” (explicitly metaphysical/interpretive vs a scientific competitor) and make the framing consistent throughout.
4) Optional: expand worked example with a few additional vetted biology/philosophy-of-biology citations if required by the journal.
5) Run a final reviewer pass after target journal is selected.
