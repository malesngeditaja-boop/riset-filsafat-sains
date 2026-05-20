# Riset Filsafat Sains: Epistemologi & Agama Islam

## Tentang Proyek Ini

Proyek riset tentang hubungan epistemologi dalam tradisi filsafat Islam dengan epistemologi sains modern.

## Struktur Folder

```
riset-filsafat-sains/
├── Imported Papers/     → Taruh file RIS, BibTeX, PubMed export di sini
├── Full Texts/          → Taruh PDF jurnal/buku di sini
├── Output/              → Hasil pemrosesan subagent (jangan edit manual)
│   ├── 01_deduplicated.csv
│   ├── 02_title_abstract_screen.csv
│   ├── 03_fulltext_screen.csv
│   └── 04_extraction_table.csv
├── protocol.md          → Kriteria inklusi/eksklusi riset
└── CLAUDE.md            → File ini
```

## Subagent yang Tersedia

Gunakan dengan perintah `/` di Claude Code:

| Subagent | Perintah | Fungsi |
|----------|----------|--------|
| Importer-Deduplicator | `/importer-deduplicator` | Gabung & deduplikasi file import |
| TA-Screener | `/ta-screener` | Saring paper berdasarkan judul & abstrak |
| Full-Text Screener | `/fulltext-screener` | Saring paper berdasarkan full text PDF |
| Data Extractor | `/data-extractor` | Ekstrak data dari paper yang lolos seleksi |

## Urutan Pipeline (Systematic Review)

```
Imported Papers/ → [Importer-Deduplicator] → 01_deduplicated.csv
                → [TA-Screener]           → 02_title_abstract_screen.csv
                → [Full-Text Screener]    → 03_fulltext_screen.csv
                → [Data Extractor]        → 04_extraction_table.csv
```

## Cara Menjalankan Pipeline Lengkap

Jalankan di Plan Mode terlebih dahulu:
```
Jalankan pipeline systematic review pada folder "Imported Papers" 
dengan urutan: Importer-Deduplicator, lalu TA-Screener. 
Berhenti setelah setiap tahap dan beri saya update.
```

## Aturan Penting

- Subagent TIDAK BOLEH mengubah file input — hanya membuat file output baru
- Test satu subagent dulu sebelum menjalankan pipeline penuh
- Commit Git setelah setiap sesi kerja yang signifikan
