# Agen SLR — Laporan (ETC: Epistemic Type‑Constraint Model)

Laporan ini ditulis sebagai artefak yang bisa diaudit reviewer: jelas apa yang **sudah ada**, apa yang **masih kosong**, dan klaim apa yang **boleh**/tidak boleh ditopang oleh corpus saat ini.

Catatan anti-halu:
- Basis: `references/slr.md` (seed corpus) + `agent_reports/SLR_CORPUS_TABLE_ETC.md` + `agent_reports/SCOPUS_METADATA_ETC.md`.
- Jika sebuah item belum punya author/year/venue di seed, itu ditandai sebagai **metadata incomplete**, bukan diisi dengan tebakan.

## 0) Research question (ETC)

Bagaimana paper membedakan empat objek epistemik—`Q` (teks Qur’an), `Ti(Q)` (tafsir manusia), `D` (data empiris), `Mj(D)` (model ilmiah berbasis data)—ketika menilai klaim konflik “sains vs Qur’an”, dan bagaimana konflik itu harus diklasifikasikan sebelum upaya rekonsiliasi dilakukan?

## 1) Inclusion / exclusion (operasional)

Sebuah sumber masuk corpus ETC jika memenuhi minimal salah satu:
1) Langsung membahas **tafsir ilmī / Qur’an–science** (pro atau kontra) atau metodologinya, atau
2) Langsung menyediakan **mesin formal** yang ETC pakai (belief revision / restricted revision / constraint satisfaction), atau
3) Langsung membahas **pemisahan data–model–teori** (untuk membenarkan `D` vs `Mj(D)`).

Keluar jika:
- blog/polemik tanpa pijakan akademik,
- “serupa judul” tapi tidak menopang klaim inti,
- atau venue tak jelas dan tidak bisa diverifikasi.

## 2) Struktur corpus saat ini (apa yang sudah ada)

### 2.1. Cluster A — Qur’an–Science / tafsir ilmī / kritik

**A‑core (paling load‑bearing untuk framing constraint & anti‑concordism):**
- Ansari (2004) (DOI ada) → framing risiko *scientific exegesis* dan batas metodologis.
- Mir (2004) (URL ada) → challenge langsung “apakah proyek tafsir ilmī viable?”.
- Naguib (2019) (DOI ada) → kritik literer/hermeneutik yang kuat terhadap scientific exegesis.
- Mohd‑Noor (2013) (tesis; URL ada) → kritik mendalam pada contoh historis utama tafsir ilmī (al‑Jawāhir).

**A‑supporting (berguna untuk background/related work, tapi bukan tulang punggung tesis):**
- Ismail & Asnawi (2021) (URL ada) → ringkasan emergence/issues.
- Al‑Bayan comparative Malaysia–Indonesia (URL ada; metadata lengkap ada di `agent_reports/SCOPUS_METADATA_ETC.md`) → konteks komparatif.
- Bigliardi (2025) *Islam and Pseudoscience* (DOI ada; Cambridge Elements) → boundary‑setting terhadap pseudo‑science/concordism.
- Khalil (1991) (DOI ada) → metodologi: hati-hati klaim “Qur’an berisi sains” dan over-interpretation risk.
- Shaikh Mohd Saifuddeen & Baharuddin (2011) (URL ada; QURANICA) → background Islam–science (gunakan hanya sebagai framing umum).

**A‑optional / flagged (perlu audit venue sebelum dipakai untuk klaim kunci):**
- Journal of Positive School Psychology piece (2023) → scope/venue mismatch (positive psychology journal); treat sebagai **flagged** dan jangan dipakai untuk klaim inti ETC.
- “Journal of Religion and Society” pada domain `islamicreligious.com` → **name ambiguity** (berbeda dari Creighton’s *Journal of Religion & Society*, ISSN 1522-5658); treat sebagai **flagged** dan jangan dipakai untuk klaim sentral sebelum verifikasi.
- (Catatan) Item yang dulu metadata incomplete (Khalil 1991; QURANICA 2011; Bigliardi 2025) sekarang sudah dipaku di `references/slr.md` dan dicatat di `agent_reports/SCOPUS_METADATA_ETC.md`.

### 2.2. Cluster B — Formal apparatus (revision / constraints)

**B‑core (minimal ETC butuh ini supaya formal layer bukan slogan):**
- AGM 1985 (venue + DOI terverifikasi di `agent_reports/SCOPUS_METADATA_ETC.md`) → baseline revision operator.
- Gärdenfors 1988 (book; seed belum memuat publisher detail) → epistemic states & dynamics (butuh metadata lengkap).
- Thagard 1992 (URL ada) → coherence as constraint satisfaction.

**B‑supporting (opsional, tapi memperkuat restricted revision + belief change):**
- Long et al. 2022 “belief revision under restrictions” (DOI ada; metadata terverifikasi).
- Delgrande & Schaub 2003 “consistency‑based belief change” (DOI ada; metadata terverifikasi).
- Chandler & Booth 2022/23 (URL ada) → tightening operator account.

### 2.3. Cluster C — Philosophy of science: data/model/theory distinction

**C‑core (wajib untuk membenarkan klaim “jangan samakan D dengan Mj(D)”):**
- Leonelli 2019 “What distinguishes data from models?” (DOI; OA; metadata terverifikasi).
- Antoniou 2021 “What is a data model?” (DOI; metadata terverifikasi).

**C‑supporting (berguna untuk narasi “data processing / theory interplay”):**
- Philosophy of Science papers (Cambridge Core URLs ada di seed) — author/year perlu dilengkapi sebelum dipakai untuk klaim presisi.

## 3) Claim → Citation map (yang aman vs yang belum aman)

### 3.1. Klaim ETC yang sudah relatif aman ditopang (dengan corpus sekarang)

1) “Scientific exegesis butuh constraint; rawan over‑reading concordance” → Ansari 2004; Mir 2004; Naguib 2019; Mohd‑Noor 2013.
2) “Bedakan data dari model; model bukan ‘data’ dan tidak otomatis mewarisi derajat kepastian data” → Leonelli 2019; Antoniou 2021.
3) “Restricted revision itu sah sebagai model formal; revisi bisa dibatasi oleh constraint” → AGM 1985 (+ Long 2022 sebagai supporting modern).
4) “Constraint satisfaction dapat dipakai sebagai bahasa formal untuk diagnosis koherensi/ketegangan” → Thagard 1992.

### 3.2. Klaim yang **belum aman** (butuh lane Tafsir / lane Scopus Retrieval / tambahan sumber)

1) “Kapan sebuah `Ti(Q)` menjadi qath’i al‑dalalah” → butuh memo tafsir + sumber ushul/tafsir yang spesifik (belum ada di seed).
2) “Status indexing/Scopus untuk venue X” → butuh lookup resmi (lane Scopus Retrieval belum komplit).
3) “Threshold/zonasi konflik ETC” → butuh justifikasi metodologis (atau dinyatakan stipulatif).

## 4) Gaps yang akan bikin paper ETC ditolak jika tidak ditutup

1) **Worked example tunggal**: tanpa 1 kasus yang dieksekusi (type‑check → constraint → revision), ETC akan dibaca “framework‑only”.
2) **Lane Tafsir kosong** (di sisi substansi): tanpa rule & verdict yang bisa diaudit, klaim `Q` vs `Ti(Q)` hanya deklarasi.
3) **Lane Scopus Retrieval belum komplit**: beberapa item masih metadata incomplete; beberapa venue flagged.
4) **Formal layer belum dipaku**: istilah `constraint/revision/diagnosis` perlu operator minimal yang konsisten.

## 5) Output lane SLR berikutnya (yang benar‑benar bikin Phase 0 “lulus gate”)

1) `Core/Supporting/Optional` final (dikunci) + alasan 1 kalimat tiap item.
2) Metadata lengkap untuk semua item seed (author/year/venue/publisher) + status akses.
3) “Claim‑to‑citation ledger”: untuk tiap klaim kunci ETC (per section), sebut 1–2 sumber utama + 1 supporting.
4) Daftar “flagged sources” yang hanya boleh dipakai untuk background sampai lolos audit venue/indexing.
