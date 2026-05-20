# REVIEW REPORT
**Paper:** Distance in Doctrinal Space: Cosine Similarity as an Epistemic Tool in Public Theological Discourse
**Target Journal:** Al-Jami'ah: Journal of Islamic Studies (Scopus Q1)
**Reviewer:** Anonymous Peer Reviewer
**Recommendation:** **Major Revision**

---

## Skor

| Kriteria | Skor | Maks |
|---|---|---|
| Originality & Contribution | 17 | 25 |
| Theoretical & Conceptual Framework | 12 | 20 |
| Methodology | 10 | 20 |
| Argument & Logic | 12 | 20 |
| Writing & Presentation | 11 | 15 |
| **Total** | **62** | **100** |

---

## Ringkasan Eksekutif

Paper ini mengajukan proposal yang secara konseptual menarik dan berani: menggunakan cosine similarity atas vektor biner sebagai *epistemic scaffold* untuk wacana teologi publik, dengan studi kasus Mama Ghufron (2024). Kekuatan utamanya terletak pada upaya jembatan interdisipliner yang jarang dilakukan — antara komputasi teks, filsafat sains pasca-positivis, dan epistemologi Islam klasik (bayan/burhan/'irfan; husuli/huduri). Penulis juga cukup self-aware: keterbatasan diakui secara eksplisit (bukan vonis teologis, snapshot bukan film, ketidakmampuan menangkap *Lebensform*), dan ini menyelamatkan paper dari klaim berlebihan yang biasa mencemari riset "computational humanities" awal.

Namun, dalam standar Al-Jami'ah (Scopus Q1), paper ini belum siap dipublikasikan dalam bentuk sekarang. Tiga masalah struktural perlu diatasi: (1) **validitas konstruk dataset belum terjustifikasi secara metodologis** — 57 variabel dirumuskan oleh penulis tunggal tanpa inter-coder reliability, padahal seluruh klaim epistemik paper bergantung pada konstruksi ini; (2) **angka 0.5923 secara matematis hampir trivial** — nilai sebenarnya hanya mencerminkan rasio variabel fondasi terhadap total variabel yang penulis pilih, bukan temuan empiris tentang subjek; (3) **kontribusi terhadap epistemologi Islam masih dangkal** — referensi ke Al-Jabiri, Nasr, Kartanegara, dan Al-Ghazali bersifat dekoratif, belum dialogis.

Rekomendasi: **Major Revision**. Ide intinya layak diselamatkan dan punya potensi orisinal, tapi memerlukan kerja ulang substansial pada metodologi, framing kontribusi, dan kedalaman engagement dengan literatur Islamic studies.

---

## Kekuatan Paper

1. **Premis orisinal**: Penerapan cosine similarity ke ranah wacana teologi publik adalah move yang segar — tidak ada presedennya di Al-Jami'ah, Studia Islamika, atau Zygon dalam 10 tahun terakhir.
2. **Self-reflexivity yang terpuji**: Section K (Limits of Approach) dan rumusan "epistemic scaffold, not theological verdict" menunjukkan kedewasaan metodologis.
3. **Trinitas interdisipliner yang ambisius**: Mengaitkan Popper-Lakatos-Quine dengan Al-Jabiri dan dengan Salton-Buckley adalah ambisi yang patut dihargai.
4. **Pengakuan eksplisit terhadap subjektivitas coding**: Section J mengakui formulasi variabel sebagai "rhetorical choice with mathematical consequences."
5. **Relevansi kontekstual**: Studi kasus Mama Ghufron relevan dengan diskursus literasi keagamaan digital Indonesia.
6. **Safeguards normatif Islami**: Invokasi musyawarah dan tabayyun (Q. 49:6) sebagai pengaman epistemis tepat untuk audiens jurnal.

---

## Kritik Mayor (Wajib Direvisi)

**M1. Validitas matematis nilai 0.5923 perlu diinterogasi ulang.**
Dengan a=1,b=1 untuk 20 variabel dan a=1,b=0 untuk 37 variabel, maka cos(θ) = 20/(√57·√20) = √(20/57) ≈ 0.5923. Artinya, **nilai cosine similarity adalah fungsi langsung dari rasio variabel fondasi terhadap total variabel yang penulis pilih**, bukan pengukuran empiris atas subjek. Jika ditambah 10 variabel kontroversial, nilainya turun otomatis. Ini bukan cacat fatal, tapi paper harus secara eksplisit mengakui struktur ini dan menjelaskan makna epistemiknya.

**M2. Tidak ada inter-coder reliability.**
57 variabel hanya dikoding oleh satu orang (penulis). Standar minimum content analysis menuntut: (a) dua coder independen, (b) pelaporan Cohen's κ atau Krippendorff's α, (c) protokol coding yang reproducible. Tanpa ini, klaim "transparansi dan intersubjektivitas" justru melemah.

**M3. Studi kasus tunggal tidak cukup untuk klaim metodologis.**
Klaim bahwa cosine similarity dapat berfungsi sebagai *epistemic scaffold* membutuhkan minimal 2-3 kasus kontras untuk menunjukkan variabilitas output. Saat ini terbaca sebagai *proof of concept* yang menarik tapi belum tegak sebagai kontribusi metodologis.

**M4. Engagement dengan epistemologi Islam masih superfisial.**
Pertanyaan kritis yang belum dijawab:
- Apakah formalisasi biner kompatibel dengan *bayan* yang menolak reduksi diskursus naqli ke struktur ekstra-tekstual?
- Bagaimana paper menjawab kritik Nasr bahwa kuantifikasi domain sakral adalah bentuk *desakralisasi*?
- Bagaimana posisi paper terhadap perdebatan *Islamisation of Knowledge* (al-Faruqi, al-Attas)?
- Tradisi *jarh wa ta'dil* punya kriteria sangat kaya (5 tingkat ta'dil, 6 tingkat jarh menurut Ibn Hajar). Cosine similarity 1-dimensi terlihat *lebih miskin* daripada presedennya.

**M5. Pemilihan 20 vs 37 variabel tidak dijustifikasi secara konseptual.**
"Mainstream Islamic Position" adalah konstruk yang sangat contested di Indonesia (NU vs Muhammadiyah vs MUI vs Salafi berbeda pada banyak titik). Pemilihan 20 variabel fondasi adalah keputusan teologis yang dibungkus matematika.

**M6. Etika penelitian terhadap subjek hidup.**
Mama Ghufron adalah figur hidup. Paper perlu: (a) section etika riset eksplisit, (b) diskusi tentang potential harm, (c) refleksi pemilihan kasus, (d) pertimbangan ethics committee.

**M7. Klaim kontribusi ke filsafat sains terlalu ambisius.**
"Formalisation of the non-scientific domain" adalah klaim besar. Ada slippage retoris antara "demarcation solution" dan "heuristic transparency tool" yang perlu diklarifikasi.

---

## Kritik Minor (Sebaiknya Direvisi)

1. Abstrak terlalu panjang menjelaskan metode, kurang menyatakan *finding* spesifik. Target 200-250 kata, gaya IMRAD.
2. Bibliografi 26 referensi kurang untuk Q1. Tambahkan: Hallaq, Anjum, El-Rouayheb (Islamic epistemology); Hefner, Bruinessen (Islam Indonesia); Choi et al. 2010 (kritik binary similarity).
3. Quine (1951) disitir tapi tidak dimanfaatkan — holisme Quinean justru *melawan* atomisme biner paper ini. Perlu dibahas.
4. Wittgenstein dan Lebensform hanya jadi disclaimer, padahal bisa memperkuat argumen jika digarap.
5. Section I (React implementation) tidak relevan untuk teks paper — pindahkan ke supplementary. Justifikasi threshold 5 zona perlu ditambahkan.
6. "Mainstream Islamic Position" (kapitalisasi) problematik. Pertimbangkan: "MUI-PBNU consensus position."
7. Sumber media (Eramuslim vs Republika) punya bias editorial berbeda — perlu didiskusikan.
8. Bahasa Inggris layak tapi perlu copy-editing native speaker.
9. Q. 49:6 (tabayyun) perlu teks ayat dan transliterasi sesuai konvensi Al-Jami'ah.
10. Notasi matematika tidak konsisten — standardisasi.

---

## Rekomendasi Spesifik untuk Penulis

1. Tambahkan **"Methodological Reflexivity" section** yang mengakui bahwa 0.5923 = √(20/57), sebuah fungsi desain dataset.
2. Lakukan **double-coding** minimal pada subset variabel, laporkan Krippendorff's α.
3. Tambahkan **satu kasus kontras** (figur lain dengan profil berbeda) untuk menunjukkan variabilitas metode.
4. **Tulis ulang Section L** dengan engagement substantif terhadap minimal 5 sumber Islamic studies per subsection (target ≥1500 kata total).
5. Pertimbangkan re-framing judul: "Cosine Similarity as Epistemic Scaffold" lebih jujur dari "Distance in Doctrinal Space."
6. Tambahkan **section etika riset**.
7. **Publish dataset di OSF/Zenodo** dengan codebook lengkap, cantumkan DOI di paper.
8. Diskusikan risiko **weaponization**: bagaimana mencegah metode dipakai untuk mendelegitimasi lawan teologis.
9. Pertimbangkan **weighted cosine similarity** sebagai bagian utama (bukan hanya future research).
10. Dialog eksplisit dengan tradisi **'aql-naql** di Section L.

---

## Rekomendasi Akhir

**Major Revision** — timeline realistis 4-6 bulan.

Paper punya potensi sebagai kontribusi yang dibicarakan di komunitas digital Islamic studies. Jika revisi menyentuh ketiga titik kritis (M1 refleksivitas matematis, M2 inter-coder reliability, M4 kedalaman Islamic studies), paper bisa naik ke level Q1.

Jika revisi mayor tidak memungkinkan, pertimbangkan re-targeting ke jurnal yang lebih sesuai untuk *exploratory conceptual papers*: **Ulumuna** (Q2), **Journal of Indonesian Islam** (Q2), atau **Method & Theory in the Study of Religion**.

---
*Review generated: 2026-05-20*
