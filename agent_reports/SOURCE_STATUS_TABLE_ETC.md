# Agen Scopus Retrieval — Source Status Table (ETC)

Tujuan: mengunci status sumber agar draft ETC tidak “ngawang” saat pindah device atau masuk tahap submission.

Catatan anti-halu:
- Tabel ini **tidak** mengklaim “Scopus-indexed” kecuali ada bukti eksplisit yang dicatat.
- Status “Verified metadata” = author/year/venue/DOI/URL sudah dipakukan di repo (lihat `references/slr.md` dan `agent_reports/SCOPUS_METADATA_ETC.md`).
- Status “Flagged” = jangan dipakai untuk klaim load-bearing.

## Legend

- `Core` = boleh menopang klaim inti ETC.
- `Supporting` = boleh dipakai untuk memperkuat, bukan tulang punggung.
- `Optional` = background only.
- `Flagged` = jangan dipakai untuk klaim inti sebelum audit venue/peer-review/indexing.

## Table (current)

| ID | Tag | Area | Citation key | Metadata | Indexing proof | Allowed use |
|---:|---|---|---|---|---|---|
| A1 | Core | Qur’an–science critique | Ansari 2004 | Verified (DOI) | Not checked | Load-bearing |
| A2 | Core | Qur’an–science critique | Mir 2004 | Verified (URL) | Not checked | Load-bearing |
| A3 | Core | Qur’an–science critique | Naguib 2019 | Verified (DOI) | Not checked | Load-bearing |
| A4 | Supporting | Survey/emergence | Ismail & Asnawi 2021 | Verified (URL) | Not checked | Supporting |
| A5 | Flagged | Conditions list | Luqman et al. 2023 | Verified (URL) | Not checked | Background only |
| A6 | Core | Deep critique (thesis) | Mohd-Noor 2013 | Verified (URL) | N/A (thesis) | Load-bearing (clearly labeled as thesis) |
| A7 | Supporting | Methodology framing | Khalil 1991 | Verified (DOI) | Not checked | Supporting |
| A8 | Supporting | Islam–science framing | Saifuddeen & Baharuddin 2011 | Verified (URL) | Not checked | Supporting/background |
| A9 | Flagged | Boundaries overview | (islamicreligious) JRS paper | Metadata incomplete/ambiguous | Not checked | Do not cite for core claims |
| A10 | Supporting | Comparative study | Zubaidi et al. 2025 | Verified (DOI) | Not checked | Supporting |
| A11 | Supporting | Pseudoscience boundary | Bigliardi 2025 | Verified (DOI) | Not checked | Supporting |
| B12 | Core | Belief revision | AGM 1985 | Verified (DOI) | Not checked | Load-bearing |
| B13 | Supporting | Belief dynamics | Gärdenfors 1988 | Verified (MIT Press; ISBN 9780262071093) | Not checked | Supporting |
| B14 | Supporting | Revision operators | Chandler & Booth 2022 | Verified (URL) | Not checked | Supporting |
| B15 | Core | Constraint satisfaction | Thagard 1998 | Verified (DOI 10.1016/S0364-0213(99)80033-0) | Not checked | Load-bearing |
| B16 | Core | Data model | Antoniou 2021 | Verified (DOI) | Not checked | Load-bearing |
| B17 | Core | Data vs model | Leonelli 2019 | Verified (DOI) | Not checked | Load-bearing |
| B18 | Supporting | Data handling | Harris 2003 | Verified (DOI 10.1086/377426) | Not checked | Supporting |
| B19 | Supporting | Data/model/theory | Norelli et al. 2025 | Verified (DOI 10.1017/psa.2025.10161) | Not checked | Supporting |
| B20 | Supporting | Restricted revision | Long et al. 2022 | Verified (DOI) | Not checked | Supporting |
| B21 | Supporting | Belief change | Delgrande & Schaub 2003 | Verified (DOI) | Not checked | Supporting |
| C22 | Supporting | Worked example anchor | Futuyma & Kirkpatrick 2017 | Verified (ISBN) | N/A (book) | Supporting |
| C23 | Supporting | Worked example anchor | Sober 2008 | Verified (ISBN) | N/A (book) | Supporting |
| C24 | Supporting | Worked example anchor | Okasha 2002 | Verified (DOI) | N/A (book) | Supporting |

## Immediate cleanup TODOs (repo-only)

1) Putuskan apakah A9 dipertahankan sebagai flagged atau dikeluarkan.
2) Jika target jurnal minta, tambahkan bukti indexing (Scopus/WoS) per venue dari sumber resmi.
