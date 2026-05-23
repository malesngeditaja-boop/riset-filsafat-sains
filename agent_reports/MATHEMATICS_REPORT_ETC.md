# Agen Matematika — Laporan (ETC: Epistemic Type-Constraint Model)

## Status

Lane matematika untuk ETC (yang dibutuhkan outline) adalah **formalisasi minimal yang usable**, bukan notasi dekoratif.

Di branch ini sudah ada:
- Daftar objek yang ingin diformalisasi di `PAPER_OUTLINE.md`.

Yang belum ada (dan ini output lane matematika ETC):
- definisi formal `Conflict`, `Type`, `constraint`, `revision`, `diagnosis` + aturan eksekusinya.

## Formalisasi minimal yang disarankan (usable)

### 1) Tipe epistemik
Definisikan type universe:
- `Text` untuk `Q`
- `Interpretation` untuk `Ti(Q)`
- `Data` untuk `D`
- `Model` untuk `Mj(D)`

### 2) Relasi dasar
- `interprets(Ti, Q)` : sebuah interpretasi ditujukan pada teks.
- `supported_by(Mj, D)` : model didukung oleh data.

### 3) Konflik
Definisikan predikat konflik sebagai relasi hanya antar entitas bertipe sama / kompatibel:
- `Conflict(x, y)` hanya well-typed jika `type(x)=type(y)` atau ada *bridge rule* yang eksplisit.

Inti tesis ETC bisa ditulis sebagai:
- Banyak klaim “Conflict(Mj(D), Q)” adalah **ill-typed**, dan yang meaningful biasanya “Conflict(Mj(D), Ti(Q))”.

### 4) Constraint set
Constraint bukan “mencegah revisi”, tapi **membatasi ruang revisi**.
Contoh constraint minimal:
- `C_text`: `Q` immutable.
- `C_tafsir`: revisi pada `Ti(Q)` harus memenuhi rule hermeneutik (bukti lughawi/ushuli).
- `C_science`: revisi pada `Mj(D)` mengikuti evidential support (jika D berubah / M kalah kompetisi).

### 5) Revision operator (restricted)
Gunakan operator revisi terbatas (skema):
- `Rev( Ti(Q), φ | C_tafsir )` menghasilkan `Ti'(Q)` yang paling dekat konsisten dengan constraint.
- `Rev( Mj(D), ψ | C_science )` menghasilkan `Mj'`.

Konsep “paling dekat” boleh diambil dari AGM atau coherence-as-constraint-satisfaction, tapi harus dinyatakan secara minimal (tanpa mengklaim logika penuh).

### 6) Diagnosis
`diagnose(claim)` mengembalikan:
- `type_error` jika conflict statement ill-typed,
- `interpretive_conflict` jika `Conflict(Mj, Ti(Q))`,
- `scientific_conflict` jika `Conflict(Mj1, Mj2)`,
- `textual_conflict` (harus sangat jarang & dibatasi) jika ada argumen bahwa dalalah qath’i bersentuhan langsung.

## Output lane matematika berikutnya

- File definisi formal 1–2 halaman (notasi + contoh instansiasi).
- 1 worked example yang dieksekusi: input → type-check → constraint → revision/don’t revise.

