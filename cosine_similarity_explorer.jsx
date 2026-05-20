import React, { useMemo, useState } from "react";

const commonVariables = [
  "Mengakui Allah sebagai Tuhan",
  "Mengakui Nabi Muhammad sebagai Rasul",
  "Mengakui Al-Qur'an sebagai kitab suci",
  "Mengakui hadis sebagai sumber ajaran Islam",
  "Mengakui keberadaan malaikat",
  "Mengakui adanya alam gaib",
  "Mengakui adanya hari akhir",
  "Mengakui adanya surga dan neraka",
  "Mengakui adanya alam kubur",
  "Mengakui pentingnya doa",
  "Mengakui pentingnya ibadah",
  "Mengakui pentingnya iman kepada Allah",
  "Mengakui kisah para nabi sebagai bagian dari ajaran Islam",
  "Mengakui Nabi Sulaiman sebagai nabi",
  "Mengakui Malaikat Jibril sebagai bagian dari ajaran Islam",
  "Mengakui Malaikat Munkar dan Nakir dalam keyakinan Islam",
  "Mengakui kematian sebagai ketetapan Allah",
  "Mengakui bahwa agama punya otoritas wahyu",
  "Mengakui bahwa ajaran Islam berkaitan dengan dunia dan akhirat",
  "Mengakui pertanggungjawaban manusia setelah mati",
];

const controversialVariables = [
  ["Mengaku video call dengan malaikat maut", "Tidak membuat klaim komunikasi gaib yang tidak berdasar", "MUI Pusat"],
  ["Mengaku video call dengan malaikat maut memakai bahasa Suryani", "Tidak mengklaim komunikasi gaib dengan malaikat maut memakai bahasa khusus", "Republika"],
  ["Mengaku melakukan panggilan video dengan Munkar dan Nakir", "Tidak mengklaim komunikasi langsung dengan malaikat kubur", "Kumparan"],
  ["Mengaku bisa mengatur pertanyaan kubur santrinya", "Tidak mengklaim bisa mengatur pertanyaan kubur bagi santri", "Kumparan"],
  ["Mengaku berbicara dengan malaikat Izrail", "Tidak mengklaim komunikasi langsung dengan malaikat Izrail", "Detik Jatim"],
  ["Mengaku bisa memanggil malaikat maut, Munkar-Nakir, dan semua malaikat", "Tidak mengklaim bisa memanggil malaikat", "Eramuslim"],
  ["Mengaku bisa menguji keaslian seseorang dengan malaikat", "Tidak memakai klaim malaikat untuk menguji keaslian seseorang", "Eramuslim"],
  ["Mengaku bisa berbahasa Suryani", "Tidak menjadikan klaim bahasa Suryani sebagai otoritas ajaran", "Detik/Republika"],
  ["Mengaku bisa berbahasa semut", "Tidak menjadikan klaim bahasa semut sebagai hujah agama", "Detik Jatim"],
  ["Mengucapkan kalimat yang diklaim sebagai bahasa semut", "Tidak membuat klaim bahasa semut yang tidak terverifikasi", "Eramuslim"],
  ["Mengaku bisa berbahasa jin", "Tidak menjadikan klaim bahasa jin sebagai otoritas agama", "Eramuslim"],
  ["Mengaku bisa berbahasa malaikat", "Tidak menjadikan klaim bahasa malaikat sebagai otoritas agama", "Eramuslim"],
  ["Mengucapkan istilah syududu", "Tidak menjadikan ucapan asing atau tidak terverifikasi sebagai legitimasi ajaran", "Kumparan"],
  ["Istilah syududu tidak punya makna linguistik jelas", "Tidak menghubungkan istilah tak bermakna dengan otoritas agama", "Kumparan"],
  ["Mengaku menjadi penjaga neraka", "Tidak mengklaim jabatan gaib dalam urusan neraka", "Republika/Detik"],
  ["Mengaku siap menjadi penjaga gawang neraka", "Tidak mengklaim menjadi penjaga gawang neraka", "Eramuslim"],
  ["Mengaku mengarang 500 kitab bahasa Suryani", "Tidak mengklaim otoritas kitab agama tanpa verifikasi", "Republika"],
  ["Mengklaim para nabi memakai bahasa Suryani", "Tidak membuat klaim sejarah kenabian tanpa dasar", "Republika"],
  ["Mengklaim manusia saat mati ditanya dengan bahasa Suryani", "Tidak memastikan detail alam kubur tanpa dalil", "Republika"],
  ["Mengaku sudah merilis 500 kitab bahasa Suryani", "Tidak mengklaim telah merilis kitab agama besar tanpa verifikasi", "tvOne"],
  ["Mengaku bisa mengubah air biasa menjadi air zamzam", "Tidak mengklaim bisa mengubah air biasa menjadi air zamzam", "Eramuslim"],
  ["Mengaitkan keyakinan jemaah dengan klaim air berubah jadi zamzam", "Tidak menjadikan keyakinan agama sebagai pembenar klaim metafisik tak terverifikasi", "Eramuslim"],
  ["Mengaku bisa mendatangkan Malaikat Jibril", "Tidak mengklaim bisa mendatangkan Malaikat Jibril", "Republika"],
  ["Mengaku bisa menyuruh menunda kiamat", "Tidak mengklaim bisa memengaruhi waktu kiamat", "Republika"],
  ["Mengaku mendapat tandangan dari Allah", "Tidak mengklaim pengalaman langsung dari Allah sebagai legitimasi ajaran", "Republika"],
  ["Mengaku belajar langsung kepada Allah selama 40 tahun", "Tidak mengklaim belajar agama langsung dari Allah sebagai otoritas pribadi", "Republika"],
  ["Mengaku mewakili Nabi Sulaiman untuk berbicara dengan semut", "Tidak mengklaim mewakili mukjizat Nabi Sulaiman", "Republika"],
  ["Mengaku bisa telepon Gusti Allah", "Tidak mengklaim komunikasi langsung dengan Allah sebagai otoritas ajaran", "Detik/PBNU"],
  ["Mengaku bisa telepon Malaikat Jibril", "Tidak mengklaim komunikasi langsung dengan Jibril sebagai otoritas ajaran", "Detik/PBNU"],
  ["Menafsirkan ayat Al-Qur'an tanpa kaidah tafsir", "Tidak menafsirkan Al-Qur'an tanpa kaidah tafsir", "Detik/MUI Malang"],
  ["Diberitakan mengeluarkan hadits baru memakai bahasa sendiri", "Tidak membuat atau menisbatkan hadis baru tanpa sanad dan verifikasi", "Tanya Islam Yuk"],
  ["Klaim hadits baru disebut memakai bahasa yang tidak dikenal", "Tidak menyebut ucapan tidak terverifikasi sebagai hadis", "Tanya Islam Yuk"],
  ["Mengucapkan syududu sebagai lafal viral yang dikaitkan dengan ceramahnya", "Tidak memakai lafal asing tidak bermakna sebagai legitimasi agama", "Kumparan"],
  ["Istilah Syududu dan Maqoli muncul dari potongan ceramah viral", "Tidak menjadikan lafal viral tidak jelas sebagai otoritas ajaran", "KabarJawa"],
  ["Mengucapkan Maqoli saat membela klaim 500 kitab bahasa Suryani", "Tidak memakai istilah tidak terverifikasi untuk membela klaim kitab agama", "tvOne"],
  ["Mengucapkan bahasa Arab oplosan saat ditantang menunjukkan 500 kitab", "Tidak mengganti verifikasi ilmiah dengan ucapan asing yang tidak jelas", "tvOne"],
  ["Dikritik karena cerita dan ajarannya disebut karangan sendiri", "Tidak membangun ajaran dari karangan personal yang tidak terverifikasi", "Tanya Islam Yuk"],
];

const initialVariables = [
  ...commonVariables.map((text, index) => ({
    id: 101 + index,
    sourceClaim: text,
    claimText: "Variabel umum untuk menangkap fondasi dasar keislaman yang sama-sama diakui.",
    variable: text,
    a: 1,
    b: 1,
    sourceName: "Variabel umum",
  })),
  ...controversialVariables.map(([sourceClaim, variable, sourceName], index) => ({
    id: index + 1,
    sourceClaim,
    claimText: "Klaim diberitakan oleh sumber publik dan dipetakan menjadi variabel biner untuk keperluan model.",
    variable,
    a: 1,
    b: 0,
    sourceName,
  })),
];

const simpleCompatibilityVariables = [
  { id: 201, variable: "Suka membaca buku", a: 1, b: 1 },
  { id: 202, variable: "Suka ngobrol panjang", a: 1, b: 1 },
  { id: 203, variable: "Suka film dokumenter", a: 1, b: 0 },
  { id: 204, variable: "Suka konser atau acara ramai", a: 0, b: 1 },
  { id: 205, variable: "Suka makanan pedas", a: 1, b: 1 },
  { id: 206, variable: "Lebih suka rencana spontan", a: 0, b: 1 },
  { id: 207, variable: "Suka jalan-jalan ke alam", a: 1, b: 0 },
  { id: 208, variable: "Suka kerja malam", a: 0, b: 0 },
  { id: 209, variable: "Suka diskusi ide dan konsep", a: 1, b: 1 },
  { id: 210, variable: "Suka olahraga ringan", a: 1, b: 0 },
];

const similarityBands = [
  { min: 0.9, label: "Sangat dekat" },
  { min: 0.75, label: "Cukup dekat" },
  { min: 0.6, label: "Bermasalah" },
  { min: 0.4, label: "Jauh" },
  { min: 0, label: "Sangat jauh" },
];

function clamp(n, min, max) {
  return Math.max(min, Math.min(max, n));
}

function getScoredVariables(items) {
  return items.filter((item) => item.b === 0 || item.b === 1);
}

function vectorFromVariables(items, key) {
  return items.map((item) => item[key]);
}

function cosineSimilarity(a, b) {
  if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) return 0;
  const dot = a.reduce((sum, value, index) => sum + value * b[index], 0);
  const normA = Math.sqrt(a.reduce((sum, value) => sum + value * value, 0));
  const normB = Math.sqrt(b.reduce((sum, value) => sum + value * value, 0));
  if (normA === 0 || normB === 0) return 0;
  return clamp(dot / (normA * normB), 0, 1);
}

function getCosineParts(items) {
  const scoredItems = getScoredVariables(items);
  const aVector = vectorFromVariables(scoredItems, "a");
  const bVector = vectorFromVariables(scoredItems, "b");
  const dot = aVector.reduce((sum, value, index) => sum + value * bVector[index], 0);
  const normASquared = aVector.reduce((sum, value) => sum + value * value, 0);
  const normBSquared = bVector.reduce((sum, value) => sum + value * value, 0);
  const normA = Math.sqrt(normASquared);
  const normB = Math.sqrt(normBSquared);
  const similarity = cosineSimilarity(aVector, bVector);
  const angleDeg = Math.acos(clamp(similarity, 0, 1)) * (180 / Math.PI);
  return { scoredItems, dot, normASquared, normBSquared, normA, normB, similarity, angleDeg };
}

function assertAlmostEqual(actual, expected, message) {
  console.assert(Math.abs(actual - expected) < 1e-9, `${message}. Expected ${expected}, got ${actual}`);
}

function runSelfTests() {
  assertAlmostEqual(getCosineParts([{ a: 1, b: 1 }, { a: 1, b: 1 }]).similarity, 1, "cosine test: identical vectors should equal 1");
  assertAlmostEqual(getCosineParts([{ a: 1, b: 0 }, { a: 1, b: 0 }]).similarity, 0, "cosine test: zero b vector should equal 0");
  assertAlmostEqual(getCosineParts([{ a: 1, b: 1 }, { a: 1, b: 0 }, { a: 1, b: 0 }, { a: 1, b: 0 }]).similarity, 0.5, "cosine test: one overlap among four a=1 and one b=1 should equal 0.5");
  assertAlmostEqual(getCosineParts([]).similarity, 0, "cosine test: empty vectors should equal 0");
  assertAlmostEqual(cosineSimilarity([1, 0, 1], [1, 0]), 0, "cosine test: mismatched vector lengths should equal 0");
  assertAlmostEqual(cosineSimilarity([1, 1, 1, 1], [1, 0, 0, 0]), 0.5, "cosine test: four baseline values with one overlap should equal 0.5");
}

runSelfTests();

function getSimilarityBand(similarity) {
  return similarityBands.find((band) => similarity >= band.min) || similarityBands[similarityBands.length - 1];
}

function countMatches(items) {
  return getScoredVariables(items).filter((item) => item.a === item.b).length;
}

function formatVariableId(item) {
  return item.id >= 100 ? `U${String(item.id - 100).padStart(2, "0")}` : `K${String(item.id).padStart(2, "0")}`;
}

function MetricCard({ label, value }) {
  return (
    <div className="rounded-2xl border border-slate-200/80 bg-white px-4 py-3 shadow-sm shadow-slate-200/70">
      <div className="text-[10px] font-semibold uppercase tracking-[0.18em] text-slate-400">{label}</div>
      <div className="mt-1 font-mono text-2xl font-black tracking-tight text-slate-950">{value}</div>
    </div>
  );
}

function TabButton({ children, active, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`rounded-full px-4 py-2 text-sm font-bold transition ${active ? "bg-slate-950 text-white shadow-sm ring-1 ring-slate-950" : "bg-white text-slate-500 ring-1 ring-slate-200 hover:bg-slate-50 hover:text-slate-900"}`}
    >
      {children}
    </button>
  );
}

function EthicalNote() {
  return (
    <div className="rounded-2xl border border-slate-200 bg-slate-50/80 p-4 text-sm leading-relaxed text-slate-600">
      <span className="font-bold text-slate-950">Catatan metodologis: </span>
      Ini model representasi, bukan fatwa dan bukan vonis personal. Dataset berisi klaim yang diberitakan dan dipetakan ke baseline secara eksplisit agar proses penilaian dapat diperiksa.
    </div>
  );
}

function FormulaBlock({ parts }) {
  return (
    <div className="rounded-[24px] border border-slate-200 bg-white p-4 shadow-sm shadow-slate-100/40">
      <div className="text-[11px] font-black uppercase tracking-[0.18em] text-blue-600">Rumus Cosine Similarity</div>
      <div className="mt-3 rounded-2xl bg-slate-50/60 p-4 text-center font-serif text-[21px] leading-relaxed text-slate-950">
        cos(θ) = Σᵢ aᵢbᵢ / √(Σᵢ aᵢ²) √(Σᵢ bᵢ²)
      </div>
      <div className="mt-3 rounded-2xl border border-slate-200 bg-slate-50/45 p-3">
        <div className="overflow-x-auto rounded-2xl bg-white px-3 py-3 text-center font-serif text-[18px] leading-relaxed text-slate-950">
          cos(θ) = {parts.dot} / √{parts.normASquared} √{parts.normBSquared} = {parts.dot} / ({parts.normA.toFixed(2)} × {parts.normB.toFixed(2)}) = <span className="font-black text-blue-800">{parts.similarity.toFixed(4)}</span>
        </div>
      </div>
    </div>
  );
}

function VariableTable({ variables, toggleVariable, compact = false }) {
  return (
    <div className="min-h-0 flex-1 overflow-x-auto overflow-y-auto rounded-2xl border border-slate-200/80 bg-slate-50/35">
      <table className="w-full min-w-[760px] text-left text-xs">
        <thead className="sticky top-0 z-20 border-b border-slate-200 bg-slate-50 text-[10px] uppercase tracking-wide text-slate-400 shadow-sm shadow-slate-200/40">
          <tr>
            {!compact && <th className="w-[58px] px-3 py-3">ID</th>}
            <th className="px-3 py-3">Variabel</th>
            {!compact && <th className="px-3 py-3">Klaim dari sumber</th>}
            <th className="px-3 py-3 text-center">a</th>
            <th className="px-3 py-3 text-center">b</th>
            <th className="px-3 py-3 text-center">Status</th>
            {!compact && <th className="px-3 py-3">Sumber</th>}
          </tr>
        </thead>
        <tbody>
          {variables.map((item) => {
            const same = item.a === item.b;
            return (
              <tr key={item.id} className="border-t border-slate-200/70 align-top">
                {!compact && <td className="px-3 py-3 font-mono font-black text-blue-950">{formatVariableId(item)}</td>}
                <td className="px-3 py-3 font-semibold leading-relaxed text-slate-700">{item.variable}</td>
                {!compact && (
                  <td className="px-3 py-3 leading-relaxed text-slate-600">
                    <div className="font-bold text-slate-800">{item.sourceClaim}</div>
                    <div className="mt-1 text-slate-500">{item.claimText}</div>
                  </td>
                )}
                <td className="px-3 py-3 text-center font-mono font-black text-slate-600">{item.a}</td>
                <td className="px-3 py-3 text-center">
                  {toggleVariable ? (
                    <button onClick={() => toggleVariable(item.id)} className={`h-7 w-7 rounded-lg font-mono text-sm font-black transition ${item.b === 1 ? "bg-sky-300 text-slate-950" : "bg-slate-200 text-slate-600"}`}>{item.b}</button>
                  ) : (
                    <span className="font-mono font-black text-slate-600">{item.b}</span>
                  )}
                </td>
                <td className="px-3 py-3 text-center">
                  <span className={`rounded-full px-2 py-1 text-[10px] font-bold ${same ? "bg-slate-200 text-blue-950" : "bg-white text-slate-500 ring-1 ring-slate-200"}`}>{same ? "Sama" : "Beda"}</span>
                </td>
                {!compact && <td className="px-3 py-3"><span className="inline-flex rounded-full bg-white px-2 py-1 text-[10px] font-bold text-blue-800 ring-1 ring-slate-200">{item.sourceName}</span></td>}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

function CosineVisual({ variables, caseName, aName = "Posisi Islam Mainstream", bName = caseName }) {
  const parts = getCosineParts(variables);
  const centerX = 18;
  const centerY = 66;
  const aLength = 42;
  const bLength = 50;
  const angle = -clamp(parts.angleDeg, 0, 90) * (Math.PI / 180);
  const aEnd = { x: centerX + aLength, y: centerY };
  const bEnd = { x: centerX + bLength * Math.cos(angle), y: centerY + bLength * Math.sin(angle) };

  return (
    <div className="rounded-[24px] bg-white">
      <div className="relative h-[320px] overflow-hidden rounded-[24px] bg-[radial-gradient(circle_at_25%_58%,rgba(125,211,252,.16),rgba(255,255,255,0)_60%)]">
        <svg className="absolute inset-0 h-full w-full" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
        <defs>
          <marker id="arrowA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#7dd3fc" /></marker>
          <marker id="arrowB" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" /></marker>
        </defs>
        <path d={`M ${centerX + 12} ${centerY} A 12 12 0 0 0 ${centerX + 12 * Math.cos(angle)} ${centerY + 12 * Math.sin(angle)}`} fill="none" stroke="rgba(37,99,235,.32)" strokeWidth="1" />
        <line x1={centerX} y1={centerY} x2={aEnd.x} y2={aEnd.y} stroke="#7dd3fc" strokeWidth="1.5" markerEnd="url(#arrowA)" />
        <line x1={centerX} y1={centerY} x2={bEnd.x} y2={bEnd.y} stroke="#2563eb" strokeWidth="1.5" markerEnd="url(#arrowB)" />
        <circle cx={centerX} cy={centerY} r="2" fill="#0f172a" />
      </svg>
      <div className="absolute left-[60%] top-[60%] whitespace-nowrap text-xs font-bold text-slate-600">a = {aName}</div>
      <div className="absolute left-[42%] top-[18%] whitespace-nowrap text-xs font-bold text-blue-800">b = {bName}</div>
      <div className="absolute left-[31%] top-[48%] rounded-full bg-white/80 px-2 py-1 font-mono text-xs font-black text-blue-800">θ = {parts.angleDeg.toFixed(1)}°</div>
      </div>
      <div className="mt-3 rounded-2xl border border-slate-200 bg-slate-50/80 px-4 py-3 text-xs leading-relaxed text-slate-500">
        Semakin kecil sudut antara vektor <span className="font-semibold text-slate-700">a</span> dan <span className="font-semibold text-slate-700">b</span>, semakin tinggi cosine similarity.
      </div>
    </div>
  );
}

function RadialDistanceMap({ variables, caseName }) {
  const parts = getCosineParts(variables);
  const similarity = parts.similarity;
  const band = getSimilarityBand(similarity);
  const matchCount = countMatches(variables);
  const total = parts.scoredItems.length;
  const distance = 1 - similarity;
  const radius = clamp(distance * 38 * 1.55, 0, 38);
  const angle = -28 * (Math.PI / 180);
  const pointX = 50 + radius * Math.cos(angle);
  const pointY = 50 + radius * Math.sin(angle);

  return (
    <div className="flex h-[720px] flex-col rounded-[24px] border border-slate-200 bg-white p-4 shadow-sm shadow-slate-100/40">
      <div className="mb-4 grid shrink-0 grid-cols-3 gap-3">
        <MetricCard label="Kemiripan" value={`${Math.round(similarity * 100)}%`} />
        <MetricCard label="Fitur sama" value={`${matchCount}/${total}`} />
        <MetricCard label="Posisi" value={band.label} />
      </div>

      <div className="min-h-0 flex-1 overflow-hidden rounded-[24px] bg-white">
        <div className="relative h-full w-full rounded-[24px] bg-[radial-gradient(circle_at_center,rgba(125,211,252,.18),rgba(248,250,252,.20)_38%,rgba(255,255,255,0)_78%)]">
          <svg className="absolute inset-0 h-full w-full" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
            {[7, 16, 25, 34, 42].map((r, index) => (
              <circle key={r} cx="50" cy="50" r={r} fill="none" stroke="rgba(14,165,233,.20)" strokeWidth="0.36" strokeDasharray={index === 4 ? "1.4 1.4" : ""} />
            ))}
            <line x1="50" y1="50" x2={pointX} y2={pointY} stroke="rgba(37,99,235,.42)" strokeWidth="0.7" strokeDasharray="1.6 1.4" />
            <circle cx="50" cy="50" r="3" fill="#7dd3fc" />
            <circle cx={pointX} cy={pointY} r="3.2" fill="#2563eb" />
            <text x="50" y="8" textAnchor="middle" fontSize="2.4" fontWeight="800" fill="rgba(71,85,105,.82)">SANGAT JAUH</text>
            <text x="50" y="20" textAnchor="middle" fontSize="2.2" fontWeight="800" fill="rgba(71,85,105,.72)">JAUH</text>
            <text x="50" y="32" textAnchor="middle" fontSize="2" fontWeight="800" fill="rgba(71,85,105,.62)">BERMASALAH</text>
            <text x="50" y="44" textAnchor="middle" fontSize="1.8" fontWeight="800" fill="rgba(71,85,105,.55)">CUKUP DEKAT</text>
          </svg>

          <div className="absolute bottom-5 left-5 text-[11px]">
            <div className="mb-2 font-black uppercase tracking-[0.16em] text-slate-400">Legenda</div>
            <div className="flex items-center gap-2 text-slate-600"><span className="h-2.5 w-2.5 rounded-full bg-sky-300" />a = Posisi Islam Mainstream</div>
            <div className="mt-1 flex items-center gap-2 text-slate-600"><span className="h-2.5 w-2.5 rounded-full bg-blue-700" />b = {caseName}</div>
          </div>
        </div>
      </div>

      <div className="mt-4 shrink-0 rounded-2xl bg-slate-50/60 p-4">
        <div className="mb-2 flex justify-between text-sm"><span className="font-semibold text-slate-700">Skor cosine similarity</span><span className="font-mono font-black text-blue-950">{similarity.toFixed(4)}</span></div>
        <div className="h-3 overflow-hidden rounded-full bg-slate-200"><div className="h-full rounded-full bg-sky-300 transition-all duration-300" style={{ width: `${similarity * 100}%` }} /></div>
        <div className="mt-2 text-xs text-slate-500">{matchCount} dari {total} variabel sejajar dengan baseline.</div>
      </div>
    </div>
  );
}

function SimpleIntroTab() {
  const parts = getCosineParts(simpleCompatibilityVariables);
  const matchCount = countMatches(simpleCompatibilityVariables);
  const total = parts.scoredItems.length;
  const band = getSimilarityBand(parts.similarity);
  return (
    <div className="grid gap-5 lg:grid-cols-[0.95fr_1.05fr] lg:items-start">
      <div className="flex h-[720px] flex-col rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm shadow-slate-100/40">
        <div className="mb-5">
          <div className="text-[11px] font-black uppercase tracking-[0.18em] text-blue-600">Contoh sederhana</div>
          <h2 className="mt-1 text-2xl font-black text-slate-950">Apakah X dan Y cocok?</h2>
          <p className="mt-2 text-sm leading-relaxed text-slate-500">Misalnya kita ingin melihat kedekatan selera dua orang. Setiap variabel diberi nilai 1 kalau iya, dan 0 kalau tidak.</p>
        </div>
        <div className="mb-4 grid grid-cols-3 gap-3">
          <MetricCard label="Kemiripan" value={`${Math.round(parts.similarity * 100)}%`} />
          <MetricCard label="Cocok" value={`${matchCount}/${total}`} />
          <MetricCard label="Posisi" value={band.label} />
        </div>
        <VariableTable variables={simpleCompatibilityVariables} compact />
        <div className="mt-4 shrink-0 rounded-2xl bg-slate-50/70 p-4 text-xs leading-relaxed text-slate-600">Cosine similarity membaca pola keseluruhan, bukan satu variabel saja.</div>
      </div>
      <div className="flex h-[720px] flex-col gap-4 rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm shadow-slate-100/40">
        <FormulaBlock parts={parts} />
        <div className="min-h-0 flex-1 overflow-hidden rounded-[24px] border border-slate-200/70 bg-white p-4"><h2 className="mb-2 text-xl font-black text-slate-950">Visual Cosine</h2><CosineVisual variables={simpleCompatibilityVariables} caseName="Y" aName="X" bName="Y" /></div>
      </div>
    </div>
  );
}

function DatasetTab({ variables, toggleVariable, caseName }) {
  return (
    <div className="flex h-[720px] flex-col rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm shadow-slate-100/40">
      <div className="mb-4 flex flex-col justify-between gap-3 md:flex-row md:items-end">
        <div>
          <div className="text-[11px] font-black uppercase tracking-[0.18em] text-blue-600">Dataset</div>
          <h2 className="mt-1 text-2xl font-black text-slate-950">Dataset {caseName}</h2>
          <p className="mt-1 text-sm text-slate-500">Klaim dari sumber digabung dalam satu kolom. Variabel cosine menjadi penentu langsung untuk nilai a dan b.</p>
        </div>
        <div className="rounded-full bg-slate-50 px-3 py-1 text-xs font-bold text-blue-950 ring-1 ring-slate-200">{variables.length} variabel</div>
      </div>
      <VariableTable variables={variables} toggleVariable={toggleVariable} />
    </div>
  );
}

function CosineTable({ variables, caseName }) {
  const parts = getCosineParts(variables);
  return (
    <div className="grid gap-5 lg:grid-cols-[1fr_0.9fr] lg:items-start">
      <div className="flex h-[720px] flex-col rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm shadow-slate-100/40">
        <div className="mb-5"><h2 className="text-2xl font-black text-slate-950">Tabel Perhitungan Cosine</h2><p className="mt-1 text-sm text-slate-500">a = Posisi Islam Mainstream, b = {caseName}</p></div>
        <div className="mb-4 grid grid-cols-4 gap-3"><MetricCard label="a · b" value={parts.dot} /><MetricCard label="||a||" value={parts.normA.toFixed(2)} /><MetricCard label="||b||" value={parts.normB.toFixed(2)} /><MetricCard label="Sudut" value={`${parts.angleDeg.toFixed(1)}°`} /></div>
        <div className="min-h-0 flex-1 overflow-x-auto overflow-y-auto rounded-2xl border border-slate-200/80 bg-slate-50/40">
          <table className="w-full text-left text-xs">
            <thead className="sticky top-0 z-20 border-b border-slate-200 bg-slate-50 text-[10px] uppercase tracking-wide text-slate-400 shadow-sm shadow-slate-200/40"><tr><th className="px-3 py-3">Variabel</th><th className="px-3 py-3 text-center">a</th><th className="px-3 py-3 text-center">b</th><th className="px-3 py-3 text-center">a×b</th><th className="px-3 py-3 text-center">a²</th><th className="px-3 py-3 text-center">b²</th></tr></thead>
            <tbody>
              {parts.scoredItems.map((item) => <tr key={item.id} className="border-t border-slate-200/70"><td className="px-3 py-2 font-semibold text-slate-700">{item.variable}</td><td className="px-3 py-2 text-center font-mono font-black text-slate-600">{item.a}</td><td className="px-3 py-2 text-center font-mono font-black text-slate-600">{item.b}</td><td className="px-3 py-2 text-center font-mono font-black text-blue-800">{item.a * item.b}</td><td className="px-3 py-2 text-center font-mono font-black text-slate-600">{item.a * item.a}</td><td className="px-3 py-2 text-center font-mono font-black text-slate-600">{item.b * item.b}</td></tr>)}
              <tr className="border-t border-slate-200 bg-slate-50"><td className="px-3 py-3 font-black text-slate-950">Total</td><td className="px-3 py-3 text-center font-mono font-black text-slate-400">—</td><td className="px-3 py-3 text-center font-mono font-black text-slate-400">—</td><td className="px-3 py-3 text-center font-mono font-black text-blue-800">{parts.dot}</td><td className="px-3 py-3 text-center font-mono font-black text-blue-800">{parts.normASquared}</td><td className="px-3 py-3 text-center font-mono font-black text-blue-800">{parts.normBSquared}</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div className="flex h-[720px] flex-col gap-4 rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm shadow-slate-100/40"><FormulaBlock parts={parts} /><div className="min-h-0 flex-1 overflow-hidden rounded-[24px] border border-slate-200/70 bg-white p-4"><h2 className="mb-2 text-xl font-black text-slate-950">Visual Cosine</h2><CosineVisual variables={variables} caseName={caseName} /></div></div>
    </div>
  );
}

function VariablePanel({ variables, toggleVariable, caseName }) {
  return (
    <div className="flex h-[720px] flex-col rounded-[24px] border border-slate-200 bg-white p-4 shadow-sm shadow-slate-100/40">
      <div className="mb-3 flex shrink-0 items-center justify-between gap-3">
        <div>
          <div className="text-xs font-black uppercase tracking-[0.2em] text-blue-600">Variabel</div>
          <div className="mt-0.5 text-[11px] text-slate-500">Klik nilai b untuk mengubah model.</div>
        </div>
        <div className="rounded-full bg-slate-50 px-3 py-1 text-xs font-bold text-blue-950 ring-1 ring-slate-200">{variables.length}</div>
      </div>

      <div className="mb-3 shrink-0 rounded-2xl border border-slate-200 bg-slate-50/60 p-3 text-xs leading-relaxed text-slate-600">
        <div><span className="font-mono font-black text-blue-950">a</span> = Posisi Islam Mainstream</div>
        <div><span className="font-mono font-black text-blue-950">b</span> = {caseName}</div>
      </div>

      <div className="min-h-0 flex-1 overflow-hidden rounded-2xl border border-slate-200/80 bg-slate-50/40">
        <div className="sticky top-0 z-20 grid grid-cols-[1fr_34px_34px_58px] gap-2 border-b border-slate-200 bg-slate-50 px-3 py-3 text-[9px] font-bold uppercase tracking-wide text-slate-400 shadow-sm shadow-slate-200/40">
          <div>Variabel</div>
          <div className="text-center">a</div>
          <div className="text-center">b</div>
          <div className="text-center">Status</div>
        </div>

        <div className="h-full overflow-y-auto p-2 pb-12">
          <div className="space-y-1.5">
            {variables.map((item) => {
              const isMatch = item.a === item.b;
              return (
                <div
                  key={item.id}
                  className={`grid grid-cols-[1fr_34px_34px_58px] items-center gap-2 rounded-xl border px-2.5 py-2 transition ${isMatch ? "border-transparent bg-white" : "border-slate-200 bg-white"}`}
                  title={item.sourceClaim}
                >
                  <div className="min-w-0 text-[12px] font-semibold leading-snug text-slate-700">{item.variable}</div>
                  <div className="text-center font-mono text-sm font-black text-slate-500">{item.a}</div>
                  <div className="text-center">
                    <button onClick={() => toggleVariable(item.id)} className={`h-7 w-7 rounded-lg font-mono text-sm font-black transition ${item.b === 1 ? "bg-sky-300 text-slate-950" : "bg-slate-200 text-slate-600"}`}>{item.b}</button>
                  </div>
                  <div className="text-center">
                    <span className={`inline-flex items-center justify-center rounded-full px-2 py-1 text-[9px] font-bold ${isMatch ? "bg-slate-100 text-slate-500" : "bg-sky-300 text-slate-950"}`}>{isMatch ? "Sama" : "Beda"}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default function App() {
  const [variables, setVariables] = useState(initialVariables);
  const [activeTab, setActiveTab] = useState("intro");
  const [variableFilter, setVariableFilter] = useState("all");
  const caseName = "Mama Ghufron";

  const toggleVariable = (id) => {
    setVariables((items) => items.map((item) => (item.id === id ? { ...item, b: item.b === 1 ? 0 : 1 } : item)));
  };

  const filteredVariables = useMemo(() => {
    return variableFilter === "controversial" ? variables.filter((item) => item.id < 100) : variables;
  }, [variables, variableFilter]);

  const mainView = useMemo(() => {
    if (activeTab === "intro") return <SimpleIntroTab />;
    if (activeTab === "dataset") return <DatasetTab variables={filteredVariables} toggleVariable={toggleVariable} caseName={caseName} />;
    if (activeTab === "table") return <CosineTable variables={filteredVariables} caseName={caseName} />;
    return <div className="grid gap-5 lg:grid-cols-[0.85fr_1.15fr] lg:items-start"><VariablePanel variables={filteredVariables} toggleVariable={toggleVariable} caseName={caseName} /><RadialDistanceMap variables={filteredVariables} caseName={caseName} /></div>;
  }, [activeTab, filteredVariables]);

  return (
    <div className="min-h-screen bg-[#f8fafc] bg-[radial-gradient(circle_at_top_left,rgba(14,165,233,.12),transparent_34%),linear-gradient(rgba(15,23,42,.035)_1px,transparent_1px),linear-gradient(90deg,rgba(15,23,42,.035)_1px,transparent_1px)] bg-[size:auto,32px_32px,32px_32px] p-4 text-slate-900 md:p-8">
      <div className="mx-auto max-w-7xl space-y-5">
        <div className="rounded-[32px] border border-slate-200/80 bg-white/90 shadow-xl shadow-slate-200/50 backdrop-blur">
          <div className="p-5 md:p-6">
            <div className="mb-5"><h1 className="text-3xl font-black tracking-tight text-slate-950 md:text-5xl">Cosine Similarity Explorer</h1></div>
            <div className="mb-5"><EthicalNote /></div>
            <div className="mb-5 flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
              <div className="flex flex-wrap gap-2">
                <TabButton active={activeTab === "intro"} onClick={() => setActiveTab("intro")}>Contoh sederhana</TabButton>
                <TabButton active={activeTab === "dataset"} onClick={() => setActiveTab("dataset")}>Dataset</TabButton>
                <TabButton active={activeTab === "table"} onClick={() => setActiveTab("table")}>Tabel cosine similarity</TabButton>
                <TabButton active={activeTab === "visual"} onClick={() => setActiveTab("visual")}>Lihat visual</TabButton>
              </div>
              <div className="flex flex-wrap gap-2 rounded-full border border-slate-200 bg-slate-50/60 p-1">
                <button onClick={() => setVariableFilter("all")} className={`rounded-full px-4 py-2 text-xs font-black transition ${variableFilter === "all" ? "bg-slate-950 text-white shadow-sm" : "bg-white text-slate-500 ring-1 ring-slate-200 hover:bg-slate-50 hover:text-slate-900"}`}>Semua variabel</button>
                <button onClick={() => setVariableFilter("controversial")} className={`rounded-full px-4 py-2 text-xs font-black transition ${variableFilter === "controversial" ? "bg-slate-950 text-white shadow-sm" : "bg-white text-slate-500 ring-1 ring-slate-200 hover:bg-slate-50 hover:text-slate-900"}`}>Kontroversial aja</button>
              </div>
            </div>
            {mainView}
          </div>
        </div>
      </div>
    </div>
  );
}
