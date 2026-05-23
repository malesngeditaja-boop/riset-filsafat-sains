# Pipeline — Cara Kerja (di repo ini)

Repo ini punya **dua pipeline yang beda**:

1) **Pipeline paper (lane-based agents)** untuk naskah/argumen.
2) **Pipeline SLR (systematic review)** untuk bangun corpus literatur.

Dokumen rujukan utama:
- `PIPELINE.md` (lane-based paper pipeline)
- `AGENTS.md` (konstitusi agen: duty + stop/handoff)
- `CLAUDE.md` + `protocol.md` + `references/slr.md` (SLR pipeline + kriteria)

---

## 1) Pipeline paper (lane-based agents)

Intinya: **setiap “agen” punya lane sempit**, output wajib, dan *gate* yang harus dilewati sebelum lanjut.

Urutan kerja yang ditetapkan (`PIPELINE.md`):
1. **SLR Agent** → peta literatur + seed corpus.
2. **Scopus Retrieval Agent** → verifikasi kualitas & metadata sumber.
3. **Tafsir Agent** → batas Q vs Ti(Q), qath'i vs nazhari, risiko cocoklogi.
4. **Philosophy of Science Agent** → beda data/model/teori + overclaim checks.
5. **Mathematics Agent** → definisi formal + rule constraint/revision/diagnosis + simulasi.
6. **Reviewer Agent** → stress-test seperti reviewer jurnal.
7. **Synthesis Agent** → gabung yang lolos gate jadi draft final.

Rule penting:
- Paper hanya “maju” kalau artefak lane sekarang **usable**.
- Kalau lane belakangan nemu flaw di lane awal → **rollback** ke lane itu.

Output yang biasanya diharapkan per lane:
- Tafsir: verdict (sah/lemah/nazhari/qath'i terbatas/overreach) + batas revisi.
- Filsafat sains: status epistemik klaim ilmiah + peta data/model/teori.
- Matematika: definisi + bukti konsistensi simbol + simulasi + edge cases.
- Reviewer: rejection-risk list + prioritas revisi.
- Sintesis: outline final + argumen runtut + apa yang dibuang.

---

## 2) Pipeline SLR (systematic literature review)

Ini pipeline operasional untuk ngolah file import (RIS/BibTeX), screening, dan ekstraksi.

Rujukan:
- `CLAUDE.md` (struktur folder + urutan)
- `protocol.md` (inklusi/eksklusi)
- `references/slr.md` (seed corpus + target crawl)

Alurnya (`CLAUDE.md`):
- `Imported Papers/` (input) → *Importer/Deduplicator* → `Output/01_deduplicated.csv`
- `Output/01_deduplicated.csv` → *TA-Screener* → `Output/02_title_abstract_screen.csv`
- `Output/02_title_abstract_screen.csv` (+ PDF di `Full Texts/`) → *Full-Text Screener* → `Output/03_fulltext_screen.csv`
- `Output/03_fulltext_screen.csv` → *Data Extractor* → `Output/04_extraction_table.csv`

Rule penting (`CLAUDE.md`):
- Subagent **tidak boleh mengubah input**; hanya nambah output.
- Test satu tahap dulu sebelum full pipeline.

