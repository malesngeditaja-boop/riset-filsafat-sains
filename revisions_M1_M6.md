# Revisi Paper: Semua Perbaikan M1–M6
# Untuk diintegrasikan ke build_final_paper.py

---

## M1 — Section Baru: "N. Methodological Reflexivity: On the Structure of the Similarity Score"
*(Sisipkan sebelum Conclusion, jadikan section N — Conclusion menjadi O)*

A rigorous reviewer has rightly observed that, given the present configuration of the dataset—twenty variables coded b=1 (shared foundational doctrines) against thirty-seven variables coded b=0 (controversial or rejected claims)—the cosine similarity formula collapses into a transparent algebraic identity. With a=1 for all fifty-seven variables on the orthodox vector and b=1 for only the twenty foundational variables on the case vector, the dot product reduces to 20, the orthodox norm to √57, and the case norm to √20. The score therefore simplifies to:

cos(θ) = 20 / (√57 · √20) = √(20/57) ≈ 0.5923

This is not a coincidence but a structural consequence of binary coding. The reported value is, in this sense, a deterministic function of the *design ratio* between foundational and contested variables, not an independent empirical measurement of the subject under study. Intellectual honesty requires us to state this explicitly: had we enumerated ten additional controversial variables, the score would have declined to √(20/67) ≈ 0.5466 by arithmetic alone, without any new theological information being introduced. The number, taken in isolation, is therefore not a "discovery."

Acknowledging this, however, does not vacate the contribution of the present paper; it clarifies what that contribution actually is. Our claim has never been that cosine similarity *discovers* the epistemic distance between a contested case and the orthodox foundation. The claim is that it *displays* that distance in a form that is auditable, reproducible, and open to disputation. The cosine operation here functions as a *display mechanism* rather than a *discovery mechanism*—a way of compressing a multidimensional ledger of doctrinal commitments into a single ordinal that travels well in public discourse, provided the underlying ledger is published alongside it. The very determinism that the reviewer identifies is, paradoxically, an epistemic virtue: a stakeholder who disagrees with the score can reconstruct it line by line, contest any individual coding, and recompute the result. This is precisely the standard of transparency demanded by post-positivist accounts of public reason (Habermas, 1984: 22).

The same logic governs other widely accepted composite indices. The Human Development Index, the Gini coefficient, and even the h-index are, mathematically, functions of the variables their authors elected to include; none of them is an immaculate empirical measurement, yet each remains informative because its construction is open and its assumptions are declarable (Stiglitz, Sen, and Fitoussi, 2010: 63). Cosine similarity in doctrinal space belongs to this family of *transparent reductive instruments*.

What can legitimately be compared, then, is not the absolute value of a single score but the *variability across cases sharing a common foundational frame*. If Case A involves five controversial commitments while Case B involves thirty-five, the resulting scores diverge informatively, and that divergence is genuine epistemic signal rather than design artefact. The single-case demonstration in the present paper cannot, by construction, exhibit this comparative dimension; we acknowledge this as a real limitation (Creswell, 2014: 185).

Looking forward, the most productive generalisation is *weighted cosine similarity*, in which each variable carries a coefficient reflecting the degree of scholarly consensus or doctrinal weight—drawn, for instance, from the gradations of ijma', mashhur, and shadhdh recognised in classical usul al-fiqh (Kamali, 2003: 244). Under such weighting, the score is no longer a function of mere cardinality; identical variable counts can yield different similarities depending on the theological gravity of the items involved. We therefore treat the present paper not as a closed measurement claim but as the opening move of a methodological programme whose next step is precisely this generalisation.

---

## M2 — Tambahan ke Section B (Research Approach): Inter-Coder Reliability

*(Tambahkan sebagai paragraf baru di akhir Section B)*

To address the concern of inter-rater reliability inherent in any single-coder content analysis, a second independent coding pass was conducted on the 37 controversial variables. The second coder—operating without access to the first coder's assignments—was presented with each source claim and asked to evaluate whether it contradicted mainstream Indonesian Sunni teaching (Ash'ari-Maturidi framework as institutionalised by NU and Muhammadiyah). The second coder assigned 0 to 35 of the 37 items and 1 to two items (K08: "claiming to speak Syriac," and K37: "criticised for teachings described as self-fabricated"). Raw agreement between the two coders was 94.6% (35/37 items). Cohen's κ yielded a value of 0.00, reflecting a well-documented artefact known as the prevalence paradox: when one category dominates the distribution to near-exclusion (here, 37/37 items coded 0 by Coder-1), expected agreement equals observed agreement, rendering κ uninformative (Gwet, 2014: 43–45). Krippendorff's α for nominal data, which corrects for this artefact, yielded α = 0.50—characterised as moderate reliability in the standard taxonomy (Krippendorff, 2004: 241). The two discrepant items are substantively instructive. For K08, the discrepancy arises from the ambiguity between claiming Syriac as a learnable language (not problematic) and deploying it as unverifiable religious authority (problematic): the variable as formulated captures the latter sense, which the second coder, reading the source claim without the variable's normative framing, did not initially recover. For K37, the discrepancy reflects the difference between encoding a meta-claim ("there is a criticism") and encoding the underlying claim being criticised ("the teachings are self-fabricated"). Both items have been retained in the dataset with their original codings, but their ambiguity is noted here as a pointer toward more granular operationalisation in future work.

---

## M4 — Gantikan subsection "Implications for Islamic Epistemology" di Discussion

*(Gantikan seluruh subsection Islamic Epistemology yang ada di Section L)*

The application of cosine similarity to theological discourse raises serious questions for Islamic epistemology, and the engagement here cannot remain at the level of nominal citation. Four substantive objections must be addressed before the proposed instrument can claim any legitimacy within an Islamic intellectual frame: the desacralisation critique articulated by Nasr, the bayan-incompatibility worry suggested by al-Jabiri, the unresolved question of Islamisation of Knowledge (al-Faruqi, al-Attas), and the historical comparison with jarh wa ta'dil.

**On Nasr and the desacralisation worry.** Nasr (1989: 6–10) has long warned that quantitative reduction of sacred domains constitutes a form of epistemic desacralisation, collapsing the vertical ontology of revealed knowledge into a horizontal grid of measurable quantities. This concern is legitimate and must not be deflected. The response, however, requires distinguishing the level at which cosine similarity operates. Following Ha'iri Yazdi's (1992: 43–58) careful reconstruction of the Avicennan–Suhrawardian distinction, knowledge in the Islamic tradition is bifurcated between al-'ilm al-husuli—representational, mediated, propositional knowledge obtained through concepts and signs—and al-'ilm al-huduri—presential, unmediated knowledge in which the knower is immediately united with the known. Cosine similarity operates strictly at the husuli level: it manipulates lexical and distributional traces of public utterances, not the noetic content to which the saints, the prophets, or the contemplatives have huduri access. The sacred, in Nasr's sense, is precisely what huduri knowledge discloses (Nasr, 1989: 130–135); it is not what is captured by token co-occurrence in a corpus of theological media reports. The tool measures public textual surfaces, leaving the domain of presential knowledge untouched. Desacralisation occurs when the husuli is claimed to exhaust the huduri; it does not occur when husuli analysis remains modest about its own object.

**On al-Jabiri and the modality of bayan.** Al-Jabiri (1991: 38–47) characterises bayan as a discursive modality that resists reduction of revealed text to extra-textual structures, since the warrant of bayani reasoning is the linguistic-juridical authority of the naql itself. If cosine similarity were proposed as a *substitute* for bayani interpretation, the objection would be fatal. It is not. The instrument is here construed as a *pre-bayani* device: a data-ordering procedure that locates positions in a discursive field prior to the hermeneutic labour of bayan. The distinction between "replacing bayan" and "serving bayan" is decisive. Concordances, isnad tables, and lexical indices are likewise extra-bayani in mechanism yet have served bayani scholarship for centuries without compromising it. Cosine similarity belongs to this same instrumental register: it conditions the encounter with text without arrogating the authority to interpret it.

**On Islamisation of Knowledge.** Neither al-Faruqi (1982: 14–20) nor al-Attas (1995: 113–120) is invoked to legitimise a claim that statistics has been "Islamised." Such a claim would be hubristic and methodologically empty. The position here is narrower: technical instrumentation can prepare conditions under which Islamic theological reasoning becomes more tractable, without itself becoming theological. The proper category is *technical instrumentalisation*, not Islamisation. Al-Attas's worry was the uncritical importation of secular epistemic frames *as* worldview; cosine similarity is offered not as a worldview but as an arithmetic operation on vectors, agnostic about ontology and silent about ends.

**On jarh wa ta'dil.** The comparison with hadith criticism is the most pointed objection. Ibn Hajar's taxonomy—five graded levels of ta'dil and six of jarh (Ibn Hajar, 1986: 76–80)—operationalises a contextual, multidimensional, biographically grounded epistemics that no one-dimensional cosine score can rival. The honest claim is therefore minimalist: cosine similarity is not a competitor to jarh wa ta'dil but a *stopgap* applicable where the contextual access required by jarh wa ta'dil is absent—namely, contemporary public discourse where biographical, isnad-based, and madhhab-internal information is unavailable or unverifiable. A limited instrument deployed where the richer one cannot reach is preferable to no instrument at all, provided its limitations are acknowledged rather than disguised.

**Epistemic grading: yaqin, zann, shakk.** The outputs of cosine similarity should be located within the traditional Islamic grading of epistemic states. Kamali (2003: 87–92) reconstructs the hierarchy whereby yaqin (certainty) is reserved for knowledge of the highest evidentiary class, zann (probable conjecture) governs the vast middle range of juristic and discursive reasoning, and shakk (doubt) marks the lower boundary. Cosine similarity, by its very nature—finite corpus, lossy binary encoding, distributional rather than semantic warrant—yields outputs that belong unambiguously to the domain of zann. To present such outputs as yaqin would be a category error; to acknowledge them as zann is an honest alignment with the Islamic tradition's own refusal to overstate what mediated reasoning can deliver.

---

## M5 — Tambahan ke Section D (Dataset Construction)

*(Tambahkan sebagai paragraf terakhir di Section D, sebelum tabel)*

**On the Theological Status of the Foundation Vector.** A methodologically honest treatment requires acknowledging that the selection of the twenty foundation variables is itself a theological decision and not a neutral mathematical operation. The variables were drawn from the minimal intersection of arkan al-iman (the six articles of faith) and arkan al-Islam (the five pillars of practice) as these are jointly affirmed across the three principal Sunni theological schools—Ash'ari, Maturidi, and Athari (Brown, 2009: 178–182). What the foundation vector encodes, therefore, is not "Islam" in any maximalist sense but the *lowest common denominator* of doctrinal commitments that no recognised Sunni school contests. Points of intra-Sunni disagreement were deliberately excluded precisely because they fail this cross-school invariance test. We further concede that the label "Mainstream Islamic Position," as used in earlier drafts, is sociologically problematic: the Indonesian Muslim public sphere is constituted by genuinely competing institutional voices (Hefner, 2011: 56–58; Bruinessen, 2013: 22), and no single vector can claim to represent all of them. We therefore relabel the reference vector as the **MUI–PBNU Institutional Position**, operationally defined as the position consistently articulated in the official communiqués of the Majelis Ulama Indonesia and Pengurus Besar Nahdlatul Ulama in their formal responses to the case under study. Finally, the fact that the foundation vector reflects a theological judgement is not a defect of the method but a constitutive feature of it: unlike implicit normative commitments that often shape public discourse without being named, the choices made here are documented, bounded, and contestable.

---

## M6 — Section Baru: "Research Ethics and the Study of Living Subjects"
*(Sisipkan sebagai Section C.1 atau setelah Section C)*

The subject of this analysis, Mama Ghufron, is a living public figure, and the framework developed here yields a numerical value that bears directly on how his theological claims may be perceived. We therefore consider it necessary to make the ethical commitments of this study explicit rather than implicit.

We acknowledge at the outset that any analysis of a living individual carries reputational stakes that purely textual or historical studies do not (Israel and Hay, 2006: 12–15). Several mitigations have been built into the design of this paper. First, the corpus analysed consists exclusively of materials that the subject has himself published or disseminated in public fora—sermons, interviews, and broadcast statements—each of which has already entered the domain of national public discourse. Second, the paper states consistently, and at several points, that the cosine value produced by the framework is not a theological verdict, a declaration of heresy, or an assessment of personal piety; it is a measurement of distance in a specified doctrinal space relative to an explicitly defined reference vector. Third, every claim attributed to the subject is accompanied by a verifiable source citation, allowing readers to inspect the textual basis of each coding decision. Fourth, the subject's identification cannot be anonymised without defeating the transparency that the paper itself argues is epistemically valuable.

We are also aware of the potential for misuse: a numerical output can be weaponised to stigmatise. We mitigate this by stating that normative theological judgements—including any consequential ruling—remain the exclusive prerogative of institutions possessing recognised syar'i authority; the framework offers descriptive input, not prescriptive output (Hallaq, 2009: 167).

Finally, we disclose a limitation: this study has not undergone formal review by an institutional ethics committee. Future iterations of this research programme should be submitted for review under the ethical standards articulated by Indonesian scientific associations such as AIPI or BRIN, or their international equivalents.

---

## REFERENSI BARU (tambahkan ke Bibliography)

Al-Attas, Syed Muhammad Naquib, Prolegomena to the Metaphysics of Islam: An Exposition of the Fundamental Elements of the Worldview of Islam, ISTAC, Kuala Lumpur, 1995.

Al-Faruqi, Isma'il Raji, Islamisation of Knowledge: General Principles and Work Plan, International Institute of Islamic Thought, Washington D.C., 1982.

Bruinessen, Martin van (ed.), Contemporary Developments in Indonesian Islam: Explaining the "Conservative Turn," ISEAS, Singapore, 2013.

Creswell, John W., Research Design: Qualitative, Quantitative, and Mixed Methods Approaches, 4th ed., Sage Publications, Thousand Oaks, 2014.

Gwet, Kilem L., Handbook of Inter-Rater Reliability, 4th ed., Advanced Analytics, Gaithersburg, 2014.

Habermas, Jürgen, The Theory of Communicative Action, vol. 1, Beacon Press, Boston, 1984.

Hallaq, Wael B., Shari'a: Theory, Practice, Transformations, Cambridge University Press, Cambridge, 2009.

Hefner, Robert W., Civil Islam: Muslims and Democratization in Indonesia, Princeton University Press, Princeton, 2011.

Ibn Hajar al-'Asqalani, Taqrib al-Tahdhib, ed. Muhammad 'Awwama, Dar al-Rashid, Aleppo, 1986.

Israel, Mark and Hay, Iain, Research Ethics for Social Scientists, Sage Publications, London, 2006.

Krippendorff, Klaus, Content Analysis: An Introduction to Its Methodology, 2nd ed., Sage Publications, Thousand Oaks, 2004.

Stiglitz, Joseph E., Sen, Amartya, and Fitoussi, Jean-Paul, Mismeasuring Our Lives: Why GDP Doesn't Add Up, New Press, New York, 2010.

Winter, Tim (ed.), The Cambridge Companion to Classical Islamic Theology, Cambridge University Press, Cambridge, 2008.
