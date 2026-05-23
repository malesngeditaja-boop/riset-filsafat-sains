# Agen Scopus Retrieval — Laporan (ETC)

## Status

Di branch ini belum ada output lane “Scopus Retrieval” yang benar-benar:
- narik metadata dari Scopus/OpenAlex/Crossref,
- memverifikasi venue/indexing,
- atau mencatat status akses full text secara sah.

Yang sudah ada baru: seed list + URL/DOI di `references/slr.md`.

## Kendala teknis di sesi ini

Di environment ini akses jaringan sempat terbatas; jadi retrieval otomatis (Crossref/OpenAlex/Scopus lookup) belum dijalankan sebagai batch job.

## Output wajib lane ini (minimum) untuk lolos gate Phase 0

Untuk tiap item di `references/slr.md`, buat tabel:
- Citation string (APA/Chicago sesuai target jurnal)
- DOI (kalau ada)
- Venue (jurnal/buku) + publisher
- Tahun
- Tipe (journal / book / thesis)
- Status indexing (Scopus? WoS? tidak?)
- Evidence-of-relevance: 1–2 kalimat “dipakai untuk klaim X di section Y”
- Akses: open / paywalled / belum tahu

## Handoff

Lane ini harus selesai sebelum drafting section yang mengandalkan klaim “peer-reviewed / indexed” supaya paper ETC tidak rapuh di audit sumber.

