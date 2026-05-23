# Agen Tafsir — Boundary Memo (ETC)

Tujuan memo ini: memberi **aturan kerja** yang bisa diaudit untuk membedakan `Q` vs `Ti(Q)` dan menetapkan batas revisi yang sah di model ETC.

Catatan anti-halu:
- Memo ini **belum** menilai kasus tertentu (worked example belum dipilih).
- Semua klaim di sini bersifat **operasional untuk paper**, bukan fatwa.

---

## 1) Definisi operasional objek

### `Q` (Qur’anic text)
- `Q` = lafaz Al-Qur’an sebagaimana termaktub dalam mushaf standar (qirā’āt mutawātirah), diperlakukan sebagai **fixed** dalam ETC.
- Di level model: `Q` bukan target revisi.

### `Ti(Q)` (human interpretation)
- `Ti(Q)` = semua proposisi interpretif yang menghubungkan lafaz `Q` dengan makna tertentu, termasuk:
  - pilihan makna leksikal,
  - analisis gramatikal,
  - klaim sebab turun (asbāb al-nuzūl),
  - klaim referensi empiris/alamiah,
  - klaim “ini maksud ayat tentang fenomena X”.
- Di level model: `Ti(Q)` default-nya **revisable (nazhari)**, kecuali dibuktikan lain.

---

## 2) Rule minimal: kapan `Ti(Q)` boleh dianggap “kuat”

ETC butuh rule yang sederhana tapi defensible:

### 2.1. `Ti(Q)` sebagai **nazhari (revisable)** bila
- bergantung pada asumsi eksternal (mis. teori ilmiah kontemporer) agar terasa “pas”,
- tidak ada qarinah kuat di teks (siyaq/struktur),
- multi-tafsir yang sama-sama mungkin secara bahasa,
- atau makna yang diambil adalah “spesialisasi modern” dari kata yang secara bahasa lebih umum.

### 2.2. `Ti(Q)` bisa disebut **qath’i terbatas** bila (semua/nyaris semua terpenuhi)
- bahasa Arabnya jelas (tidak multi-tafsir yang selevel),
- disokong siyaq/qarinah internal ayat,
- tidak memerlukan “bridge” ilmiah untuk membuatnya masuk akal,
- dan (idealnya) ada penguatan dari tradisi tafsir/ushul yang kuat.

Catatan: ETC tidak wajib mengklaim “qath’i al-dalalah” untuk banyak ayat; justru lebih aman memposisikan sebagian besar konflik populer sebagai konflik terhadap `Ti(Q)` (interpretasi), bukan terhadap `Q`.

---

## 3) Constraint anti-cocoklogi (tafsir-side)

Ini constraint yang dipakai lane matematika sebagai `C_tafsir`.

### `C_tafsir` (minimal)
Sebuah revisi pada `Ti(Q)` **hanya sah** jika:
1) Tidak melanggar kaidah bahasa Arab dasar (makna kata/nahwu/balaghah yang relevan),
2) Konsisten dengan siyaq/qarinah yang paling langsung,
3) Tidak menggunakan teori ilmiah sebagai *driver* utama makna (teori ilmiah hanya boleh sebagai *compatibility check* setelah makna tekstual plausible),
4) Bila pembacaan mengklaim spesifikasi ilmiah, harus ada justifikasi hermeneutik kenapa spesifikasi itu tidak arbitrer.

### Output yang harus terlihat di worked example
Saat contoh dikerjakan, pembaca harus bisa melihat:
- Di titik mana interpretasi masuk sebagai `Ti(Q)`,
- Constraint mana yang dipakai untuk menolak/menerima revisi,
- Dan kenapa itu bukan “sekadar cocoklogi”.

---

## 4) Interface ke lane Science

Agar konflik tidak salah level:
- `Q` tidak pernah “berhadapan langsung” dengan `Mj(D)` tanpa perantara `Ti(Q)`.
- Jadi setiap klaim “sains vs Qur’an” harus di-decompose menjadi:
  - `Mj(D)` vs **proposisi interpretif** tertentu (`Ti(Q)`), bukan vs lafaz `Q`.

---

## 5) Checklist untuk drafting (biar nggak halu)

- Jangan tulis “ayat ini pasti maksudnya X (fenomena modern)” kecuali rule 2.2 terpenuhi.
- Kalau tidak terpenuhi, tulis secara jujur: “sebuah pembacaan yang mengaitkan ayat dengan X adalah `Ti(Q)` (nazhari) dan karenanya revisable.”
- Selalu pisahkan “lafaz ayat” (Q) vs “paraphrase interpretif” (Ti(Q)).

