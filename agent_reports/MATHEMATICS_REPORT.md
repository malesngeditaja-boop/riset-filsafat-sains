# Agen Matematika — Validasi Simulasi Cosine Similarity

Repo: `malesngeditaja-boop/riset-filsafat-sains` (branch `codex/epistemic-type-constraint-model`)

## Ringkas

- **Rumus cosine similarity yang dipakai sah** (baik di UI `cosine_similarity_explorer.jsx` maupun di naskah `build_final_paper.py`).
- Dengan struktur dataset yang dinyatakan (**n=57 variabel**, **k=20 shared foundations**), angka **0.5923 konsisten** dan menyederhana menjadi identitas **`cos = √(k/n)`**.
- Konsekuensinya: di konfigurasi biner spesifik ini, skor **ditentukan oleh rasio desain (k/n)**, bukan “temuan empiris” yang independen dari pemilihan variabel.

## Basis artefak di repo

- UI + self-tests: `cosine_similarity_explorer.jsx`
- Naskah (docx builder) menuliskan substitusi angka:
  - `cos(θ) = 20 / (7.5498 × 4.4721) ≈ 0.5923`
  - `cos(θ) = 20 / (√57 · √20) = √(20/57) ≈ 0.5923`
  - `θ = arccos(0.5923) ≈ 53.66°`

## Hasil simulasi (reproducible)

Script: `agent_reports/math_simulation.py`

Untuk **n=57, k=20**:
- `dot = 20`
- `||a|| = √57 ≈ 7.5498`
- `||b|| = √20 ≈ 4.4721`
- `cos(θ) = 20 / (√57 · √20) = √(20/57) ≈ 0.592300`
- `θ ≈ 53.66°`

## Validitas: “hitung benar” vs “klaim metodologis”

Yang terjamin oleh matematika:
- Perhitungan dan penyederhanaan identitas `√(k/n)` di bawah asumsi vektor biner yang dipakai.

Yang belum bisa dijamin matematika semata:
- Validitas konstruk dataset (definisi variabel, reliabilitas coding, bobot, dan framing normatif).
- Justifikasi band/threshold interpretasi (Very Close … Very Far) kecuali dinyatakan stipulatif atau diberi rujukan.

## Cara menjalankan

Di root repo:
- `python3 agent_reports/math_simulation.py`
