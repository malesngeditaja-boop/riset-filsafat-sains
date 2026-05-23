# Run Log (high-level)

This is a human-readable log of what was executed/produced so work is portable across devices.

## Repo / branch

- Repo: `malesngeditaja-boop/riset-filsafat-sains`
- Branch: `codex/epistemic-type-constraint-model`

## Outputs created

- Draft manuscript: `ETC_DRAFT.md`
- Appendix textual basis: `ETC_APPENDIX_TEXTUAL_BASIS.md`
- Lane outputs: `agent_reports/*`
- Seed corpus updated: `references/slr.md`

## Key commands used

### Clone (one-time)

```bash
git clone --branch codex/epistemic-type-constraint-model --single-branch https://github.com/malesngeditaja-boop/riset-filsafat-sains.git
```

### Verse text + transliteration fetch (used to fill appendix)

We used an API call pattern like:

```bash
curl -s "https://api.islamic.app/v1/verses/by_key/4:1?fields=text_uthmani&words=true&word_fields=transliteration"
```

Then extracted `text_uthmani` and the per-word transliterations (joined) into the appendix. The appendix transliteration is explicitly marked as “working transliteration” and should be aligned to the target journal’s transliteration standard before submission.

### Math simulation (cosine similarity paper helper)

```bash
python3 agent_reports/math_simulation.py
```

## Commit / push

Work was committed and pushed to the branch. To verify on another device:

```bash
git fetch origin
git checkout codex/epistemic-type-constraint-model
git log -1 --oneline
```

