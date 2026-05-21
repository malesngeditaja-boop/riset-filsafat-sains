"""
Builds the final integrated paper docx for Al-Jami'ah journal.
Run: python3 build_final_paper.py
All revisions M1–M6 and minor rounds 1–3 integrated.
"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# Page setup: A4, 2.54 cm margins
section = doc.sections[0]
section.page_height = Cm(29.7)
section.page_width  = Cm(21.0)
section.top_margin    = Cm(2.54)
section.bottom_margin = Cm(2.54)
section.left_margin   = Cm(2.54)
section.right_margin  = Cm(2.54)

# Default style: Times New Roman 12 pt
style = doc.styles['Normal']
font  = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

def set_spacing(para, before=0, after=6, line=360):
    pf = para.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after  = Pt(after)
    pPr = para._p.get_or_add_pPr()
    lnSpc = OxmlElement('w:lnSpc')
    lnSpcVal = OxmlElement('w:lnSpcVal')
    lnSpcVal.set(qn('w:line'), str(line))
    lnSpcVal.set(qn('w:lineRule'), 'auto')
    lnSpc.append(lnSpcVal)
    existing = pPr.find(qn('w:lnSpc'))
    if existing is not None:
        pPr.remove(existing)
    pPr.append(lnSpc)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(14)
    run.font.name = 'Times New Roman'
    set_spacing(p, before=0, after=12)
    return p

def add_heading(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    set_spacing(p, before=12, after=6)
    return p

def add_subheading(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.italic = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    set_spacing(p, before=8, after=4)
    return p

def add_para(text, italic=False, bold=False, indent=False):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Cm(0.75)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.italic = italic
    run.bold = bold
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    set_spacing(p)
    return p

def add_para_mixed(parts, indent=True):
    """parts = list of (text, bold, italic)"""
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Cm(0.75)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for text, bold, italic in parts:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
    set_spacing(p)
    return p

def add_small(text, italic=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.italic = italic
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'
    set_spacing(p, before=0, after=4)
    return p

def add_small_mixed(parts):
    """Abstract-level text at Pt(11) with mixed formatting."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for text, bold, italic in parts:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(11)
        run.font.name = 'Times New Roman'
    set_spacing(p, before=0, after=4)
    return p

def add_ref(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-1.0)
    run = p.add_run(text)
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'
    set_spacing(p, before=0, after=4)
    return p

def add_formula(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(12)
    set_spacing(p, before=4, after=4)
    return p

# =============================================================
# TITLE
# =============================================================
add_title("DISTANCE IN DOCTRINAL SPACE: COSINE SIMILARITY AS AN\nEPISTEMIC TOOL IN PUBLIC THEOLOGICAL DISCOURSE")
doc.add_paragraph()

# =============================================================
# ABSTRACT (EN) — IMRAD, revised (ISU 4, Minor Round 3)
# =============================================================
add_heading("Abstract")
add_small_mixed([
    ("Public theological discourse in Indonesia frequently proceeds in the absence of a shared, "
     "intersubjectively examinable reference frame, with the result that debates over orthodoxy "
     "and heterodoxy circulate without productive resolution. This article addresses that absence "
     "by demonstrating a transparent reductive instrument for locating contested doctrinal profiles "
     "within an explicitly stipulated reference space. The instrument applies cosine similarity to "
     "a fifty-seven-variable binary dataset comprising twenty foundational doctrines jointly affirmed "
     "across the principal Sunni schools and thirty-seven controversial claims drawn from verified "
     "Indonesian media coverage and the official communiqués of the Majelis Ulama Indonesia and "
     "Pengurus Besar Nahdlatul Ulama. The 2024 case of the preacher Mama Ghufron is treated as an "
     "illustrative vehicle, not as the substantive object of inquiry. The computed value of 0.5923 "
     "is presented not as an empirical discovery but as a ", False, False),
    ("display mechanism", False, True),
    (": a deterministic compression of a publicly auditable ledger into an ordinal that travels "
     "intelligibly through public debate. Located within classical Islamic grades of epistemic states, "
     "the output belongs unambiguously to the register of ", False, False),
    ("zann", False, True),
    (" rather than ", False, False),
    ("yaqin", False, True),
    (". The article's contribution is methodological: it offers a transparent reductive instrument "
     "that can serve as an epistemic scaffold for public theological discourse, equipping rather than "
     "displacing the deliberative practices of ", False, False),
    ("musyawarah", False, True),
    (" and ", False, False),
    ("tabayyun", False, True),
    (".", False, False),
])

# ABSTRACT (ID) — updated terminology (ISU 5)
add_small(
    "Wacana keagamaan publik di Indonesia kerap berlangsung tanpa titik referensi bersama yang dapat diperiksa "
    "secara intersubjektif, sehingga menghasilkan perdebatan yang berputar-putar tanpa resolusi yang produktif. "
    "Artikel ini mengajukan cosine similarity atas vektor biner klaim keagamaan sebagai epistemic scaffold—"
    "sebuah perancah epistemik yang membuat premis-premis perdebatan teologis menjadi eksplisit, terbuka, dan "
    "dapat diverifikasi. Dengan menggunakan kasus viral penceramah Mama Ghufron (2024) sebagai studi kasus, "
    "dataset 57 variabel biner dikonstruksi dari laporan media terverifikasi dan respons resmi lembaga "
    "keagamaan. Hasil perhitungan menunjukkan cosine similarity sebesar 0,5923 antara profil klaim subjek dan "
    "Posisi Institusional MUI–PBNU. Artikel ini berargumen bahwa nilai tersebut bukan vonis teologis, "
    "melainkan instrumen transparansi yang memungkinkan diskusi publik dimulai dari fakta yang sama. Implikasi "
    "dibahas dari tiga sudut: filsafat sains (formalisasi domain non-ilmiah), matematika terapan (perluasan "
    "cosine similarity ke luar domain komputasi teks), dan epistemologi Islam (naql dan ʻaql sebagai basis "
    "evaluasi klaim).", italic=True
)
add_small("Keywords: cosine similarity, binary vector, Islamic epistemology, philosophy of science, theological discourse.")
doc.add_paragraph()

# =============================================================
# A. INTRODUCTION
# =============================================================
add_heading("A.\tIntroduction")

add_para(
    "One of the fundamental challenges in public religious discourse is the absence of a common reference "
    "system that can be examined intersubjectively. When a religious figure is claimed to be deviant, the "
    "debate that arises often runs on two separate tracks: opponents cite certain claims as evidence of "
    "deviance, while proponents respond with arguments of character or community loyalty. There is no equally "
    "held map, no agreed variables, and no way to check how far the differences actually exist in a structured "
    "manner.", indent=False
)

add_para(
    "The absence of this common reference system is not just a communication problem. It is an epistemological "
    "problem. Without a transparent and verifiable framework, discussions about orthodoxy and heterodoxy are "
    "vulnerable to rhetorical manipulation from all directions. Supporters can blur substantive differences "
    "with emotional arguments, while opponents can exaggerate distance by selectively highlighting the most "
    "controversial claims while ignoring the common foundations that remain.", indent=True
)

add_para(
    "Mathematics, especially the cosine similarity technique commonly used in natural language processing and "
    "information retrieval, offers a possibility that has not been explored much before: borrowing an "
    "inter-vector distance measuring tool to map the distance between two doctrinal positions. Not as a "
    "determinant of truth, but as an epistemic scaffold that makes the premises of the debate explicit and "
    "auditable.", indent=True
)

add_para(
    "This article asks the question: To what extent can cosine similarity over binary representations of "
    "religious claims serve as a valid epistemic tool in public theological discourse, and what are its "
    "legitimate limits? To answer this question, the article uses the viral case of a preacher from East Java "
    "known as Mama Ghufron, who in mid-2024 became a national focus due to a series of religious claims "
    "reported by the media and officially responded to by the Indonesian Ulema Council (MUI) and the Executive "
    "Board of Nahdlatul Ulama (PBNU).", indent=True
)

add_para(
    "The purpose of this article is threefold. First, to demonstrate how cosine similarity works in the "
    "context of religious claim representation. Second, to interpret the results of the calculation within "
    "the framework of Islamic philosophy of science and epistemology. Third, to honestly map the boundaries "
    "of this approach so that it is not misused as a substitute for true theological judgement.", indent=True
)

add_para(
    "Cosine similarity was first introduced as a measure of similarity in vector space models by Salton and "
    "colleagues in order to build an automated information retrieval system (Salton and Buckley, 1988). In its "
    "original context, it is used to measure how similar two text documents are based on the frequency with "
    "which words appear. Mathematically, it is defined as the angular cosine between two vectors in "
    "multidimensional space, resulting in values between 0 (no resemblance) and 1 (identical).", indent=True
)

add_para(
    "Further developments show that cosine similarity has special advantages for binary and sparse data: it "
    "does not count absent-feature matches as evidence of similarity, but only calculates the convergence of "
    "positive values. This makes it fairer than simple similarity measures based on percentage matches, "
    "especially when the data has many zero values (Manning, Raghavan, and Schütze, 2008). In computational "
    "social science, cosine similarity has been used to measure the similarity of political positions between "
    "parties based on voting patterns (Poole and Rosenthal, 1985), to classify sentiment in social media texts "
    "(Liu, 2012; Grimmer and Stewart, 2013), and to map ideological closeness in policy documents. However, "
    "its application to map the distance between religious doctrinal positions and an orthodoxy baseline—"
    "particularly with datasets constructed explicitly from verified sources—has not received systematic "
    "attention in the literature.", indent=True
)

add_para(
    "The question of whether religious claims can or should be mathematically formalised touches on one of the "
    "longest-running debates in the philosophy of science: the demarcation problem—the boundary between "
    "science and non-science. Karl Popper (2005) proposed falsifiability as a demarcation criterion: a "
    "statement is scientific only if it can in principle be refuted by empirical evidence. Religious claims, "
    "in Popper’s framework, are generally outside the domain of science not because they are wrong, but "
    "because their structure does not allow for falsification. Lakatos (1978) refined this position with the "
    "concept of a research programme: every research programme has a hard core protected from falsification, "
    "and a protective belt that can be modified. In a religious context, the core beliefs function similarly "
    "to the hard core, while the fringe interpretations are more flexible. Quine (1951) adds a relevant "
    "perspective through the web-of-beliefs argument: beliefs do not stand alone but are interconnected in a "
    "network, and the revision of one belief has implications for others.", indent=True
)

add_para(
    "It is important to note that this article does not claim that cosine similarity turns religious claims "
    "into scientific statements in the Popperian sense. Instead, it borrows the structure of transparency from "
    "science—the explicitness of the premise, the verifiability of sources, the reproducibility of "
    "calculations—to apply to the domain of public discourse that has been running without such a structure.",
    indent=True
)

add_para(
    "In the Islamic scientific tradition, the debate on the role of reason (ʻaql) vis-à-vis the text "
    "of revelation (naql) has been ongoing since the Middle Ages. Al-Ghazali in Tahafut al-Falasifa criticises "
    "philosophers who give reason excessive authority in the domains of metaphysics and theology, while Ibn "
    "Rushd (Averroes) in Tahafut al-Tahafut argues that reason and revelation, if understood correctly, are "
    "not in conflict with each other (Leaman, 1998). In the modern context, Amin Abdullah (2006) proposes an "
    "integration-interconnection paradigm in Islamic science: religious sciences and general sciences do not "
    "need to be opposed, but can reinforce each other within the framework of honest methodological dialogue.",
    indent=True
)

add_para(
    "The Islamic philosophical resources for thinking about epistemic verification extend considerably beyond "
    "this classical disputation, and a fuller engagement with these resources clarifies the position the "
    "present article seeks to occupy. Mulyadhi Kartanegara, among the most systematic of contemporary "
    "Indonesian Muslim philosophers, has argued for a non-dichotomous model of the relation between religious "
    "and scientific knowledge, in which the two are understood as complementary modes of access to a unitary "
    "reality (Kartanegara, 2003: 21–34; 2005: 87–104). On Kartanegara’s account, the project "
    "of integration does not require dissolving the methodological autonomy of the empirical sciences, but "
    "rather acknowledging that each domain of inquiry possesses its own appropriate instruments.", indent=True
)

add_para(
    "Seyyed Hossein Nasr’s enduring critique of modern science must also be engaged seriously. Nasr "
    "(1989: 1–18; 1996: 96–119) maintains that modern science, having severed itself from the "
    "sacred, produces a knowledge that is technically powerful but metaphysically impoverished. From this "
    "vantage, any importation of formal techniques into theological discourse risks reproducing the very "
    "reductionism that the scientia sacra tradition resists. The present article takes this warning to heart "
    "by restricting the scope of the technique it proposes: cosine similarity is not deployed to evaluate "
    "the truth of doctrinal claims, only to display their structural relations under an explicitly stipulated "
    "coding.", indent=True
)

add_para(
    "Mohammed Abed Al-Jabiri’s tripartite classification of epistemic modalities in the Arab-Islamic "
    "intellectual tradition—bayan (exegetical-juridical reasoning anchored in textual sources), burhan "
    "(demonstrative reasoning in the Aristotelian sense), and ʻirfan (gnostic or illuminative "
    "knowledge)—provides a particularly useful map for situating the contribution of the present article "
    "(Al-Jabiri, 1991: 383–415). The cosine similarity procedure does not pretend to operate in the "
    "register of ʻirfan, which by its nature resists formal representation, and it is not itself a form "
    "of bayan, since it does not generate juridical rulings. It functions instead as an auxiliary within the "
    "burhani register: a formal, demonstrative operation upon explicitly represented premises, whose output "
    "is then returned to the bayani community for interpretation.", indent=True
)

add_para(
    "A further distinction internal to the Isyraqi tradition refines this placement. Suhrawardi and his "
    "commentators differentiate al-ʻildm al-husuli, knowledge acquired through the mediation of concepts "
    "and representations, from al-ʻildm al-huduri, knowledge present to the knower without mediation "
    "(Ha’iri Yazdi, 1992: 43–67). Cosine similarity is, by construction, an operation upon "
    "representations; it is therefore intelligible only within the domain of al-ʻildm al-husuli and has "
    "no purchase whatsoever upon al-ʻildm al-huduri. Recognising this limit is not a concession but a "
    "clarification.", indent=True
)

add_para(
    "In the tradition of usul al-fiqh, the evaluation of claims—including claims about spiritual "
    "capacity—requires structured verification. The concept of jarh wa taʿdil in hadith science, "
    "for example, is a systematic assessment of the credibility of narrators based on explicit criteria that "
    "can be audited (Brown, 2009). In the same spirit, albeit with a different medium, cosine similarity "
    "offers an explicit variable-based scoring system that anyone can examine.", indent=True
)

add_para(
    "The emergence of social media platforms has significantly changed the ecosystem of religious discourse. "
    "Religious claims now circulate as video clips, screenshots, and infographics cut off from their original "
    "context, reaching millions of people in hours without institutional filters (Bunt, 2018). Some research "
    "suggests that repeated exposure to certain claims, even inaccurate ones, can improve their perceived "
    "accuracy—an effect known as the illusory truth effect (Pennycook, Cannon, and Rand, 2018). In this "
    "context, a tool that can help the public visualise differences systematically, based on verifiable "
    "sources, has epistemic and social value that goes beyond mere academic interest.", indent=True
)

# =============================================================
# B. RESEARCH APPROACH (+ M2 inter-coder + ISU 1 instrument demo)
# =============================================================
add_heading("B.\tResearch Approach")

add_para(
    "This article uses a descriptive-analytical approach grounded in a single case study. The choice of a "
    "single case study is methodologically deliberate rather than incidental. As Yin (2018: 49–53) "
    "argues, the single-case design is particularly justified when the case functions as a representative or "
    "paradigmatic instance through which a broader methodological proposition can be tested in concrete terms. "
    "Flyvbjerg (2006: 219–229) further demonstrates that the conventional bias against the explanatory "
    "power of single cases rests on a misreading of how knowledge is actually produced in the social sciences: "
    "paradigmatic cases are often more generative of theoretical insight than large-N studies because they "
    "expose the inner workings of a phenomenon under examination. The case of Mama Ghufron in 2024 satisfies "
    "both criteria. It is representative of a broader pattern of contested theological claims circulating in "
    "Indonesian digital public space, and it is paradigmatic insofar as it crystallises the very "
    "ambiguity—between unorthodoxy and outright heresy—that motivates the construction of an "
    "epistemic scaffold in the first place.", indent=False
)

add_para(
    "The descriptive-analytical mode is preferred over experimental or survey-based designs for several "
    "interrelated reasons. First, the object of inquiry is not a measurable behavioural variable across a "
    "population, but a structural relation between a discursive profile and a doctrinal reference position. "
    "Such relations are not amenable to randomised manipulation in any ethically or epistemically meaningful "
    "way. Second, the unit of analysis is a corpus of theological propositions, not a sample of human "
    "respondents; survey instruments would therefore mistake the locus of evidence. Third, the article’s "
    "ambition is to exhibit a method—to show how cosine similarity can be operationalised on binary "
    "representations of religious claims and what such operationalisation does and does not yield—rather "
    "than to estimate parameters or test hypotheses in the inferential-statistical sense.", indent=True
)

add_para(
    "The approach carries inherent limitations that must be acknowledged. A single case cannot, on its own, "
    "licence generalisations about the distribution of doctrinal deviance in Indonesian preaching, nor can it "
    "adjudicate the substantive theological merits of any particular claim. The construction of the "
    "57-variable binary dataset, moreover, encodes interpretive choices that other researchers might contest. "
    "The article addresses these limitations not by claiming to overcome them but by foregrounding them: all "
    "coding decisions are documented, the reference position is explicitly stipulated rather than assumed, and "
    "the resulting similarity score is presented as a diagnostic prompt for further deliberation rather than "
    "as a final verdict. The article should therefore be read as a conceptual-methodological demonstration—"
    "a proof of concept for a transparent epistemic tool—rather than as an empirical generalisation "
    "about the state of public preaching in Indonesia.", indent=True
)

# M2 — Inter-coder reliability paragraph
add_para(
    "To address the concern of inter-rater reliability inherent in any single-coder content analysis, a "
    "second independent coding pass was conducted on the 37 controversial variables. The second coder—"
    "operating without access to the first coder’s assignments—was presented with each source "
    "claim and asked to evaluate whether it contradicted mainstream Indonesian Sunni teaching (Ashʿari–"
    "Maturidi framework as institutionalised by NU and Muhammadiyah). The second coder assigned 0 to 35 of "
    "the 37 items and 1 to two items (K08: ‘claiming to speak Syriac,’ and K37: ‘criticised "
    "for teachings described as self-fabricated’). Raw agreement between the two coders was 94.6% "
    "(35/37 items). Cohen’s κ yielded a value of 0.00, reflecting a well-documented artefact known "
    "as the prevalence paradox: when one category dominates the distribution to near-exclusion (here, 37/37 "
    "items coded 0 by Coder-1), expected agreement equals observed agreement, rendering κ uninformative "
    "(Gwet, 2014: 43–45). Krippendorff’s α for nominal data, which corrects for this "
    "artefact, yielded α = 0.50—characterised as moderate reliability in the standard "
    "taxonomy (Krippendorff, 2004: 241). The two discrepant items are substantively instructive. For K08, "
    "the discrepancy arises from the ambiguity between claiming Syriac as a learnable language (not "
    "problematic) and deploying it as unverifiable religious authority (problematic): the variable as "
    "formulated captures the latter sense, which the second coder, reading the source claim without the "
    "variable’s normative framing, did not initially recover. For K37, the discrepancy reflects the "
    "difference between encoding a meta-claim (‘there is a criticism’) and encoding the underlying "
    "claim being criticised (‘the teachings are self-fabricated’). Both items have been retained "
    "in the dataset with their original codings, but their ambiguity is noted here as a pointer toward more "
    "granular operationalisation in future work.", indent=True
)

# ISU 1 — Instrument demonstration clarification (closing para Section B)
add_para_mixed([
    ("A clarification of the article’s argumentative architecture is warranted at this juncture. "
     "The Mama Ghufron case is invoked not as the substantive object whose properties the analysis aims "
     "to characterise, but as an ", False, False),
    ("illustrative vehicle", False, True),
    (" through which the operation of a transparent epistemic instrument can be exhibited under realistic "
     "conditions. The article is, in this sense, an ", False, False),
    ("instrument demonstration", False, True),
    (" rather than a single case study in the conventional sense (Yin, 2018: 51). The epistemic load it "
     "carries lies in the architecture of the procedure—dataset construction, binary coding, cosine "
     "computation, zone interpretation, and reflexive audit—not in any conclusion about the subject "
     "himself. Were the case substituted by another comparably documented controversy, the procedure would "
     "remain intact, and the diagnostic value of the demonstration would be substantially preserved.",
     False, False),
], indent=True)

# =============================================================
# C. DATA SOURCES
# =============================================================
add_heading("C.\tData Sources")

add_para(
    "The data in this article is sourced from two layers. The first layer is news reports from verified "
    "national media covering claims attributed to the subject of the case study, including Republika, "
    "Detik.com, Kumparan, tvOne, and Eramuslim, published between April and October 2024. The second layer "
    "is official statements from religious institutions, especially the MUI Malang (10 points of "
    "irregularity that were officially released) and comments from PBNU.", indent=False
)

add_para(
    "The selection of these sources is based on two criteria: (1) the source is publicly accessible with a "
    "verifiable URL, and (2) the source has explicitly responded to the reported claims. This is important "
    "to ensure that the constructed variables do not come from assumptions or speculation, but rather from a "
    "record of real public discourse.", indent=True
)

# =============================================================
# C.1 RESEARCH ETHICS (M6)
# =============================================================
add_heading("C.1\tResearch Ethics and the Study of Living Subjects")

add_para(
    "The subject of this analysis, Mama Ghufron, is a living public figure, and the framework developed "
    "here yields a numerical value that bears directly on how his theological claims may be perceived. We "
    "therefore consider it necessary to make the ethical commitments of this study explicit rather than "
    "implicit.", indent=False
)

add_para(
    "We acknowledge at the outset that any analysis of a living individual carries reputational stakes that "
    "purely textual or historical studies do not (Israel and Hay, 2006: 12–15). Several mitigations "
    "have been built into the design of this paper. First, the corpus analysed consists exclusively of "
    "materials that the subject has himself published or disseminated in public fora—sermons, "
    "interviews, and broadcast statements—each of which has already entered the domain of national "
    "public discourse. Second, the paper states consistently, and at several points, that the cosine value "
    "produced by the framework is not a theological verdict, a declaration of heresy, or an assessment of "
    "personal piety; it is a measurement of distance in a specified doctrinal space relative to an "
    "explicitly defined reference vector. Third, every claim attributed to the subject is accompanied by a "
    "verifiable source citation, allowing readers to inspect the textual basis of each coding decision. "
    "Fourth, the subject’s identification cannot be anonymised without defeating the transparency that "
    "the paper itself argues is epistemically valuable.", indent=True
)

add_para(
    "We are also aware of the potential for misuse: a numerical output can be weaponised to stigmatise. We "
    "mitigate this by stating that normative theological judgements—including any consequential "
    "ruling—remain the exclusive prerogative of institutions possessing recognised syarʿi "
    "authority; the framework offers descriptive input, not prescriptive output (Hallaq, 2009: 167).", indent=True
)

add_para(
    "Finally, we disclose a limitation: this study has not undergone formal review by an institutional "
    "ethics committee. Future iterations of this research programme should be submitted for review under "
    "the ethical standards articulated by Indonesian scientific associations such as AIPI or BRIN, or their "
    "international equivalents.", indent=True
)

# =============================================================
# D. DATASET CONSTRUCTION
# =============================================================
add_heading("D.\tDataset Construction")

add_para(
    "The dataset is constructed in two structurally distinct layers that reflect the comparative "
    "architecture of the model.", indent=False
)

add_para(
    "Layer 1: Common Foundation (20 variables, U01–U20). The first layer consists of twenty variables "
    "representing fundamental Islamic beliefs that are overwhelmingly shared across the full spectrum of "
    "Indonesian Muslim expression, including by the subject of this case study. Both vectors receive a "
    "score of 1 on this layer. The decision to include this foundational layer carries significant "
    "epistemological weight: it ensures that the model does not begin from the premise that the subject "
    "occupies the position of an outsider or non-Muslim. Rather, it acknowledges a substantial shared "
    "ground before the analysis proceeds to examine areas of reported divergence. Without this layer, the "
    "similarity score would collapse to zero—a result that would be both arithmetically predictable "
    "and epistemologically dishonest. The twenty foundation variables cover the core affirmations of "
    "Islamic faith (usul al-din): monotheism, prophethood, revealed scripture, the authority of hadith, "
    "the existence of angels and the unseen realm, eschatological beliefs (the Day of Judgement, paradise, "
    "and hellfire), the reality of the grave (alam kubur), the obligatory nature of worship, and the "
    "principle of post-mortem accountability. Their inclusion as a shared baseline is not a rhetorical "
    "concession; it is a structural requirement for a model that aspires to be fair.", indent=True
)

add_para(
    "Layer 2: Controversial Claims (37 variables, K01–K37). The second layer consists of "
    "thirty-seven variables derived from specific claims attributed to the subject and reported by "
    "verified Indonesian media outlets between April and October 2024. These claims were systematically "
    "gathered from six primary sources: Republika, Detik.com (including Detik Jatim), Kumparan, tvOne, "
    "Eramuslim, and Tanya Islam Yuk, supplemented by official institutional responses from MUI Pusat, "
    "MUI Malang, PBNU, and KabarJawa.", indent=True
)

# ISU 5 — updated "position" description
add_para(
    "Each raw claim from the media was transformed into a normative variable—a statement of the "
    "position consistently articulated in the official communiqués of MUI and PBNU in response to "
    "the case under study. Because the variable represents this institutional norm, the MUI–PBNU "
    "Institutional Position vector (a) is uniformly valued at 1 across all 37 variables, while the "
    "subject’s claim profile (b) receives 0 on each, since the reported claim contradicts the norm. "
    "This asymmetry is precisely what drives the cosine calculation.", indent=True
)

add_para(
    "The 37 controversial variables cluster into five thematic groups: (1) claims of supernatural "
    "communication (K01–K07), including alleged video calls with the Angel of Death and direct "
    "conversation with Munkar, Nakir, and Izrail; (2) claims of extraordinary linguistic capacity "
    "(K08–K14), including alleged command of Syriac, the language of ants, the language of jinn, "
    "and the language of angels; (3) claims of cosmological authority (K15–K16, K23–K27), "
    "including alleged capacity to guard hellfire, summon Angel Jibril, postpone the Day of Judgement, "
    "and serve as Nabi Sulaiman’s representative; (4) claims of unverified textual authority "
    "(K17–K20, K30–K37), including alleged authorship of 500 Syriac-language religious texts, "
    "unauthorised Qurʼanic interpretation, and self-composed hadith; and (5) claims of direct divine "
    "access (K21–K22, K25–K26, K28–K29), including alleged ability to transform ordinary "
    "water into zamzam water and direct learning from Allah over forty years.", indent=True
)

# M5 — theological status of foundation vector + relabeling justification
add_para_mixed([
    ("On the Theological Status of the Foundation Vector. ", True, False),
    ("A methodologically honest treatment requires acknowledging that the selection of the twenty "
     "foundation variables is itself a theological decision and not a neutral mathematical operation. "
     "The variables were drawn from the minimal intersection of arkan al-iman (the six articles of "
     "faith) and arkan al-Islam (the five pillars of practice) as these are jointly affirmed across "
     "the three principal Sunni theological schools—Ashʿari, Maturidi, and Athari (Brown, "
     "2009: 178–182). What the foundation vector encodes, therefore, is not ‘Islam’ in "
     "any maximalist sense but the ", False, False),
    ("lowest common denominator", False, True),
    (" of doctrinal commitments that no recognised Sunni school contests. Points of intra-Sunni "
     "disagreement were deliberately excluded precisely because they fail this cross-school invariance "
     "test. We further concede that the label ‘Mainstream Islamic Position,’ as used in "
     "earlier drafts, is sociologically problematic: the Indonesian Muslim public sphere is constituted "
     "by genuinely competing institutional voices (Hefner, 2011: 56–58; Bruinessen, 2013: 22), "
     "and no single vector can claim to represent all of them. We therefore relabel the reference vector "
     "as the ", False, False),
    ("MUI–PBNU Institutional Position", True, False),
    (", operationally defined as the position consistently articulated in the official communiqués "
     "of the Majelis Ulama Indonesia and Pengurus Besar Nahdlatul Ulama in their formal responses to "
     "the case under study. Finally, the fact that the foundation vector reflects a theological judgement "
     "is not a defect of the method but a constitutive feature of it: unlike implicit normative "
     "commitments that often shape public discourse without being named, the choices made here are "
     "documented, bounded, and contestable.", False, False),
], indent=True)

add_para(
    "Every variable in the dataset is linked to at least one publicly verifiable source. The complete "
    "dataset is presented in Table 1 (common foundation) and Table 2 (controversial claims) below.",
    indent=True
)

# --- TABLE 1 ---
doc.add_paragraph()
t1_header = doc.add_paragraph()
t1_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t1_header.add_run("Table 1. Common Foundation Variables (a = 1, b = 1 for both vectors)")
r.bold = True; r.font.size = Pt(11); r.font.name = 'Times New Roman'

table1 = doc.add_table(rows=1, cols=4)
table1.style = 'Table Grid'
table1.alignment = WD_TABLE_ALIGNMENT.CENTER
for cell, txt in zip(table1.rows[0].cells, ["ID", "Variable", "a", "b"]):
    cell.text = txt
    cell.paragraphs[0].runs[0].bold = True
    cell.paragraphs[0].runs[0].font.size = Pt(10)

common_vars = [
    "Mengakui Allah sebagai Tuhan",
    "Mengakui Nabi Muhammad sebagai Rasul",
    "Mengakui Al-Qurʼan sebagai kitab suci",
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
]
for i, v in enumerate(common_vars, 1):
    row = table1.add_row().cells
    row[0].text = f"U{i:02d}"; row[1].text = v; row[2].text = "1"; row[3].text = "1"
    for cell in row:
        cell.paragraphs[0].runs[0].font.size = Pt(10)

doc.add_paragraph()

# --- TABLE 2 --- (header caption updated: ISU 5)
t2_header = doc.add_paragraph()
t2_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = t2_header.add_run(
    "Table 2. Controversial Claims Variables "
    "(a = MUI–PBNU Institutional Position = 1, b = subject’s claim profile = 0)"
)
r2.bold = True; r2.font.size = Pt(11); r2.font.name = 'Times New Roman'

table2 = doc.add_table(rows=1, cols=5)
table2.style = 'Table Grid'
table2.alignment = WD_TABLE_ALIGNMENT.CENTER
for cell, txt in zip(table2.rows[0].cells,
                     ["ID", "Source Claim", "Variable (Institutional Norm)", "Source", "b"]):
    cell.text = txt
    cell.paragraphs[0].runs[0].bold = True
    cell.paragraphs[0].runs[0].font.size = Pt(9)

controversial = [
    ("Mengaku video call dengan malaikat maut", "Tidak membuat klaim komunikasi gaib yang tidak berdasar", "MUI Pusat"),
    ("Mengaku video call dengan malaikat maut memakai bahasa Suryani", "Tidak mengklaim komunikasi gaib dengan malaikat maut memakai bahasa khusus", "Republika"),
    ("Mengaku melakukan panggilan video dengan Munkar dan Nakir", "Tidak mengklaim komunikasi langsung dengan malaikat kubur", "Kumparan"),
    ("Mengaku bisa mengatur pertanyaan kubur santrinya", "Tidak mengklaim bisa mengatur pertanyaan kubur bagi santri", "Kumparan"),
    ("Mengaku berbicara dengan malaikat Izrail", "Tidak mengklaim komunikasi langsung dengan malaikat Izrail", "Detik Jatim"),
    ("Mengaku bisa memanggil malaikat maut, Munkar-Nakir, dan semua malaikat", "Tidak mengklaim bisa memanggil malaikat", "Eramuslim"),
    ("Mengaku bisa menguji keaslian seseorang dengan malaikat", "Tidak memakai klaim malaikat untuk menguji keaslian seseorang", "Eramuslim"),
    ("Mengaku bisa berbahasa Suryani", "Tidak menjadikan klaim bahasa Suryani sebagai otoritas ajaran", "Detik/Republika"),
    ("Mengaku bisa berbahasa semut", "Tidak menjadikan klaim bahasa semut sebagai hujah agama", "Detik Jatim"),
    ("Mengucapkan kalimat yang diklaim sebagai bahasa semut", "Tidak membuat klaim bahasa semut yang tidak terverifikasi", "Eramuslim"),
    ("Mengaku bisa berbahasa jin", "Tidak menjadikan klaim bahasa jin sebagai otoritas agama", "Eramuslim"),
    ("Mengaku bisa berbahasa malaikat", "Tidak menjadikan klaim bahasa malaikat sebagai otoritas agama", "Eramuslim"),
    ("Mengucapkan istilah syududu", "Tidak menjadikan ucapan asing atau tidak terverifikasi sebagai legitimasi ajaran", "Kumparan"),
    ("Istilah syududu tidak punya makna linguistik jelas", "Tidak menghubungkan istilah tak bermakna dengan otoritas agama", "Kumparan"),
    ("Mengaku menjadi penjaga neraka", "Tidak mengklaim jabatan gaib dalam urusan neraka", "Republika/Detik"),
    ("Mengaku siap menjadi penjaga gawang neraka", "Tidak mengklaim menjadi penjaga gawang neraka", "Eramuslim"),
    ("Mengaku mengarang 500 kitab bahasa Suryani", "Tidak mengklaim otoritas kitab agama tanpa verifikasi", "Republika"),
    ("Mengklaim para nabi memakai bahasa Suryani", "Tidak membuat klaim sejarah kenabian tanpa dasar", "Republika"),
    ("Mengklaim manusia saat mati ditanya dengan bahasa Suryani", "Tidak memastikan detail alam kubur tanpa dalil", "Republika"),
    ("Mengaku sudah merilis 500 kitab bahasa Suryani", "Tidak mengklaim telah merilis kitab agama besar tanpa verifikasi", "tvOne"),
    ("Mengaku bisa mengubah air biasa menjadi air zamzam", "Tidak mengklaim bisa mengubah air biasa menjadi air zamzam", "Eramuslim"),
    ("Mengaitkan keyakinan jemaah dengan klaim air berubah jadi zamzam", "Tidak menjadikan keyakinan agama sebagai pembenar klaim metafisik tak terverifikasi", "Eramuslim"),
    ("Mengaku bisa mendatangkan Malaikat Jibril", "Tidak mengklaim bisa mendatangkan Malaikat Jibril", "Republika"),
    ("Mengaku bisa menyuruh menunda kiamat", "Tidak mengklaim bisa memengaruhi waktu kiamat", "Republika"),
    ("Mengaku mendapat tandangan dari Allah", "Tidak mengklaim pengalaman langsung dari Allah sebagai legitimasi ajaran", "Republika"),
    ("Mengaku belajar langsung kepada Allah selama 40 tahun", "Tidak mengklaim belajar agama langsung dari Allah sebagai otoritas pribadi", "Republika"),
    ("Mengaku mewakili Nabi Sulaiman untuk berbicara dengan semut", "Tidak mengklaim mewakili mukjizat Nabi Sulaiman", "Republika"),
    ("Mengaku bisa telepon Gusti Allah", "Tidak mengklaim komunikasi langsung dengan Allah sebagai otoritas ajaran", "Detik/PBNU"),
    ("Mengaku bisa telepon Malaikat Jibril", "Tidak mengklaim komunikasi langsung dengan Jibril sebagai otoritas ajaran", "Detik/PBNU"),
    ("Menafsirkan ayat Al-Qurʼān tanpa kaidah tafsir", "Tidak menafsirkan Al-Qurʼān tanpa kaidah tafsir", "Detik/MUI Malang"),
    ("Diberitakan mengeluarkan hadits baru memakai bahasa sendiri", "Tidak membuat atau menisbatkan hadis baru tanpa sanad dan verifikasi", "Tanya Islam Yuk"),
    ("Klaim hadits baru disebut memakai bahasa yang tidak dikenal", "Tidak menyebut ucapan tidak terverifikasi sebagai hadis", "Tanya Islam Yuk"),
    ("Mengucapkan syududu sebagai lafal viral yang dikaitkan dengan ceramahnya", "Tidak memakai lafal asing tidak bermakna sebagai legitimasi agama", "Kumparan"),
    ("Istilah Syududu dan Maqoli muncul dari potongan ceramah viral", "Tidak menjadikan lafal viral tidak jelas sebagai otoritas ajaran", "KabarJawa"),
    ("Mengucapkan Maqoli saat membela klaim 500 kitab bahasa Suryani", "Tidak memakai istilah tidak terverifikasi untuk membela klaim kitab agama", "tvOne"),
    ("Mengucapkan bahasa Arab oplosan saat ditantang menunjukkan 500 kitab", "Tidak mengganti verifikasi ilmiah dengan ucapan asing yang tidak jelas", "tvOne"),
    ("Dikritik karena cerita dan ajarannya disebut karangan sendiri", "Tidak membangun ajaran dari karangan personal yang tidak terverifikasi", "Tanya Islam Yuk"),
]
for i, (src, var, source) in enumerate(controversial, 1):
    row = table2.add_row().cells
    row[0].text = f"K{i:02d}"; row[1].text = src; row[2].text = var
    row[3].text = source; row[4].text = "0"
    for cell in row:
        cell.paragraphs[0].runs[0].font.size = Pt(9)

doc.add_paragraph()

# =============================================================
# E. BINARY REPRESENTATIONS
# =============================================================
add_heading("E.\tBinary Representations and Their Justifications")

add_para(
    "The use of binary values 0 and 1 is a conscious simplification. It abstracts the nuances, contexts, "
    "and gradations that exist in each claim. The justifications for its use are pragmatic and "
    "epistemological: pragmatic because it allows for reproducible cosine similarity calculations, and "
    "epistemological because it forces dataset creators to make explicit decisions about each variable "
    "rather than leaving them ambiguous. In this sense, binary limitation is precisely a methodological "
    "strength: any ambiguity must be resolved explicitly and arguably.", indent=False
)

# =============================================================
# F. MATHEMATICAL FOUNDATIONS
# =============================================================
add_heading("F.\tMathematical Foundations: Why Cosine Similarity")

add_para(
    "Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle "
    "between them. For two vectors a and b in n-dimensional space, the formula is:", indent=False
)

add_formula("cos(θ) = (Σᵢ aᵢbᵢ) / (√(Σᵢ aᵢ²) · √(Σᵢ bᵢ²))")

add_para(
    "where a·b is the dot product of the two vectors, and ‖a‖ and ‖b‖ are their "
    "Euclidean norms.", indent=False
)

add_para(
    "For binary data, the dot product produces a positive value only when both corresponding elements are "
    "valued at 1. When either or both are 0, the contribution to the dot product is zero. This means that "
    "cosine similarity does not count zero-zero matches as evidence of similarity—a property that is "
    "crucial for this context. Two subjects who both lack a belief should not be considered more alike "
    "simply because of that absence. This property distinguishes cosine similarity from simple distance "
    "metrics such as the simple matching coefficient, which treats a null-value match equal to a one-value "
    "match (Manning, Raghavan, and Schütze, 2008).", indent=True
)

# =============================================================
# G. CALCULATIONS (ISU 5: vector a label updated)
# =============================================================
add_heading("G.\tCalculations for Mama Ghufron’s Case")

add_para(
    "With the dataset of 57 variables constructed across Table 1 and Table 2, the calculation proceeds "
    "as follows.", indent=False
)

add_para(
    "Dot product (a·b): The dot product produces a positive value only where both vectors are valued "
    "at 1. This occurs exclusively on the 20 common foundation variables. In the 37 controversial claim "
    "variables, vector a is valued at 1 but vector b is valued at 0, so the contribution is zero. "
    "Thus: a·b = 20.", indent=True
)

add_para(
    "Vector norm ‖a‖: Vector a (MUI–PBNU Institutional Position) is valued at 1 on all "
    "57 variables: ‖a‖ = √57 ≈ 7.5498.", indent=True
)

add_para(
    "Vector norm ‖b‖: Vector b (subject’s claim profile) is valued at 1 on only the 20 "
    "foundation variables: ‖b‖ = √20 ≈ 4.4721.", indent=True
)

add_formula("cos(θ) = 20 / (7.5498 × 4.4721) = 20 / 33.7639 ≈ 0.5923")
add_formula("θ = arccos(0.5923) ≈ 53.66°")

add_para(
    "This result places the subject’s claim profile in the ‘Far’ zone on the "
    "interpretation scale used, where zones are defined as: Very Close (≥0.90), Fairly Close "
    "(≥0.75), Problematic (≥0.60), Far (≥0.40), and Very Far (<0.40).", indent=True
)

# =============================================================
# H. READING THE NUMBERS
# =============================================================
add_heading("H.\tReading the Numbers: What It Says")

add_para(
    "The value of 0.5923 communicates two things simultaneously. First, it confirms the existence of a "
    "substantial common foundation: the 20 variables with full match represent a significant proportion "
    "of the total 57 variables. Second, it shows that in the 37 variables born from specific claims "
    "reported by the media, there are systematic differences large enough to lower the similarity score "
    "to the ‘Far’ zone.", indent=False
)

add_para(
    "What is important to attend to is the information hidden behind this single number. The difference "
    "between a score of 0.59 and a score of 0.20 is not just a matter of magnitude—it reflects a "
    "completely different structure of differences. The score of 0.59 in this case arises from a large "
    "common foundation (20 variables) that is offset by an equally large set of differences (37 "
    "variables). The same score in another hypothetical case could arise from an entirely different "
    "pattern. The same number does not necessarily tell the same story.", indent=True
)

# =============================================================
# I. VISUALISATION (ISU 5: MUI-PBNU label updated)
# =============================================================
add_heading("I.\tVisualisation as a Complement to Calculation")

add_para(
    "To support more intuitive reading, the project on which this article is based also provides an "
    "interactive radial map built as an open-source React application. The radial map places the "
    "MUI–PBNU Institutional Position at the central point, and visualises the subject’s "
    "position as a point in two-dimensional space whose distance from the centre represents the cosine "
    "distance. Five concentric zones (Very Close to Very Far) provide instantly readable visual context "
    "without requiring the reader to inspect the underlying numbers.", indent=False
)

add_para(
    "This visualisation is not decorative. It is part of the epistemological argument of this article: "
    "transparency requires not only data openness, but also accessibility of presentation. A map that "
    "can be read by journalists, students, and ordinary citizens has a different epistemic value than a "
    "table of numbers accessible only to statisticians. The tool further allows users to toggle "
    "individual variable values interactively, enabling readers to test how the similarity score changes "
    "when specific coding decisions are revised—an affordance that directly operationalises the "
    "article’s commitment to auditability.", indent=True
)

# =============================================================
# J. CONSTRUCT OF VARIABLES
# =============================================================
add_heading("J.\tConstruct of Variables as Epistemic Decisions")

add_para(
    "The most important—and most often overlooked—part of this whole approach is the process "
    "of constructing the variables themselves. Each variable in the dataset is the result of a human "
    "decision: decisions about which claims are sufficiently documented to include, how to formulate "
    "variables neutrally, and from which sources those claims are drawn.", indent=False
)

add_para(
    "These decisions cannot be completely free from subjective considerations. The choice to formulate "
    "the variable as a positive norm (‘Not claiming direct communication with the angel of "
    "death’) rather than a negative statement (‘Claiming direct communication with the angel "
    "of death’) is a rhetorical choice with mathematical consequences: it determines which side is "
    "by default valued at 1 and which at 0. Precisely because these limitations are inherent and cannot "
    "be eliminated, the openness of the process becomes the main accountability mechanism. Because each "
    "variable is explicitly recorded along with its source, anyone can question the decision to include "
    "it, propose an alternative formulation, or dispute the reliability of a source. Open debates about "
    "variables are far more epistemologically productive than debates whose assumptions are never "
    "disclosed.", indent=True
)

# =============================================================
# K. LIMITS
# =============================================================
add_heading("K.\tThe Limits of the Approach: What Numbers Cannot Tell")

add_para(
    "This section is the most crucial in this article, and at the same time the most frequently missed "
    "in discussions of formal methods applied to humanistic domains.", indent=False
)

add_para(
    "First, this figure is not a theological verdict. The value of 0.5923 measures the distance between "
    "two sets of positions encoded in 57 binary variables based on selected sources at a given point in "
    "time. It does not state whether the subject is misguided, not misguided, worthy of criticism, or "
    "worthy of defending. These are theological questions requiring expertise in tafsir, hadith, kalam, "
    "and usul al-fiqh—domains that binary vectors simply cannot address.", indent=True
)

add_para(
    "Second, variables are human decisions. If the dataset were constructed with a different choice of "
    "variables—for example, by including variables that support the subject, or with different "
    "weights for different types of claims—the results would differ. This is not a fatal flaw of "
    "the methodology but rather because every methodology has assumptions. What sets this approach apart "
    "is that these assumptions are explicit and debatable.", indent=True
)

add_para(
    "Third, it is a snapshot, not a film. The dataset records the claims in circulation and reported "
    "over a given period. If the subject subsequently substantially retracts or revises those claims, "
    "the dataset should be updated and the numbers will change. Cosine similarity does not record "
    "history; it takes a picture of a moment.", indent=True
)

add_para(
    "Fourth, humans cannot be reduced to vectors. This is the most fundamental limitation. Every "
    "individual—including anyone who is the subject of this kind of analysis—is a complex "
    "human being with life journeys, social contexts, intentions, and dimensions of humanity that no "
    "number can capture. Wittgenstein (2010) reminds us that the meaning of a statement cannot be "
    "separated from the context of its use (Lebensform). The binary representation of a claim abstracts "
    "that context, and that abstraction is always a partial loss of meaning.", indent=True
)

add_para(
    "Acknowledging these limitations is not a sign of methodological weakness, but of methodological "
    "integrity. A tool that knows the limits of its capabilities can be used responsibly. A tool that "
    "claims to be all-purpose is genuinely dangerous.", indent=True
)

# =============================================================
# L. DISCUSSION
# =============================================================
add_heading("L.\tDiscussion")

# ISU 2 — Opening disclaimer paragraph (before Implications for Philosophy of Science)
add_para_mixed([
    ("Before proceeding, the scope of the engagement that follows must be stated precisely. The "
     "discussion appropriates selected idioms from twentieth-century philosophy of science—"
     "Popper’s demarcation criterion, Lakatos’s research-programme architecture, and "
     "Quine’s web-of-belief image—as ", False, False),
    ("heuristic analogies", False, True),
    (" through which the structural transparency afforded by the present instrument can be made "
     "intelligible to a reader trained in those traditions (Popper, 2005: 18; Lakatos, 1978: 47; "
     "Quine, 1951: 39). No claim of original contribution to the philosophy of science is advanced "
     "or intended. The argument moves in the opposite direction: it borrows vocabulary from a mature "
     "discipline to clarify a modest methodological proposal in an adjacent domain, and the burden of "
     "proof carried by that proposal is correspondingly local rather than disciplinary.", False, False),
], indent=False)

add_subheading("Implications for the Philosophy of Science")

add_para(
    "The procedure demonstrated in this article borrows a structural feature of scientific "
    "practice—the explicit, auditable representation of premises and the calculable relation among "
    "them—and transposes it onto a domain that is, on any reasonable construal, not itself a "
    "science. This transposition requires careful qualification. The article does not claim, in the "
    "Popperian register, that theological propositions are or ought to be falsifiable in the strict "
    "sense, nor that the cosine score between two doctrinal profiles is itself a truth-functional "
    "verdict. The demarcation problem, as Popper (2005) framed it and as Lakatos subsequently refined "
    "it, concerns the conditions under which a body of propositions counts as scientific; the present "
    "article sidesteps that question by appropriating not the content of scientific reasoning but its "
    "epistemic virtues: the explicitness of assumptions, the reproducibility of operations, and the "
    "verifiability of intermediate steps.", indent=False
)

add_para(
    "This appropriation finds support in recent work in the social epistemology of science. Longino "
    "(2002: 128–135) argues that the criteria for genuine knowledge—publicly recognised venues "
    "for criticism, uptake of criticism, public standards, and tempered equality of intellectual "
    "authority—are not the exclusive property of natural science but generalise to any community "
    "engaged in the cooperative production of warranted belief. Kitcher’s (2001: 117–135) "
    "notion of well-ordered science points in the same direction: what makes an inquiry well-ordered is "
    "not its subject matter but the institutional and procedural transparency through which its claims "
    "are produced and contested. Cosine similarity, deployed as an epistemic scaffold, contributes "
    "precisely such procedural transparency to a discourse that has historically been mediated by "
    "charismatic authority and rhetorical performance.", indent=True
)

add_para(
    "For the long-running debate over the Islamisation of Knowledge, this reframing matters. Rather "
    "than asking whether religious commitments can constitute a science in their own right, the present "
    "approach asks a narrower and more tractable question: which formal techniques of representation and "
    "comparison, drawn from contemporary information science, can be reflectively appropriated to render "
    "public theological discourse more accountable to its own stated premises? Posed this way, the "
    "question avoids the polemical impasse between sacralisation and secularisation of knowledge and "
    "opens a pragmatic middle path.", indent=True
)

# M4 — Deep engagement with Islamic Epistemology (replaces old subsection)
add_subheading("Implications for Islamic Epistemology")

add_para(
    "The application of cosine similarity to theological discourse raises serious questions for Islamic "
    "epistemology, and the engagement here cannot remain at the level of nominal citation. Four "
    "substantive objections must be addressed before the proposed instrument can claim any legitimacy "
    "within an Islamic intellectual frame: the desacralisation critique articulated by Nasr, the "
    "bayan-incompatibility worry suggested by al-Jabiri, the unresolved question of Islamisation of "
    "Knowledge (al-Faruqi, al-Attas), and the historical comparison with jarh wa taʿdil.", indent=False
)

add_para_mixed([
    ("On Nasr and the desacralisation worry. ", True, False),
    ("Nasr (1989: 6–10) has long warned that quantitative reduction of sacred domains constitutes "
     "a form of epistemic desacralisation, collapsing the vertical ontology of revealed knowledge into "
     "a horizontal grid of measurable quantities. This concern is legitimate and must not be deflected. "
     "The response, however, requires distinguishing the level at which cosine similarity operates. "
     "Following Ha’iri Yazdi’s (1992: 43–58) careful reconstruction of the Avicennan–"
     "Suhrawardian distinction, knowledge in the Islamic tradition is bifurcated between "
     "al-ʻildm al-husuli—representational, mediated, propositional knowledge obtained through "
     "concepts and signs—and al-ʻildm al-huduri—presential, unmediated knowledge in which "
     "the knower is immediately united with the known. Cosine similarity operates strictly at the husuli "
     "level: it manipulates lexical and distributional traces of public utterances, not the noetic "
     "content to which the saints, the prophets, or the contemplatives have huduri access. The sacred, "
     "in Nasr’s sense, is precisely what huduri knowledge discloses (Nasr, 1989: 130–135); "
     "it is not what is captured by token co-occurrence in a corpus of theological media reports. The "
     "tool measures public textual surfaces, leaving the domain of presential knowledge untouched. "
     "Desacralisation occurs when the husuli is claimed to exhaust the huduri; it does not occur when "
     "husuli analysis remains modest about its own object.", False, False),
], indent=True)

add_para_mixed([
    ("On al-Jabiri and the modality of bayan. ", True, False),
    ("Al-Jabiri (1991: 38–47) characterises bayan as a discursive modality that resists reduction "
     "of revealed text to extra-textual structures, since the warrant of bayani reasoning is the "
     "linguistic-juridical authority of the naql itself. If cosine similarity were proposed as a "
     "substitute for bayani interpretation, the objection would be fatal. It is not. The instrument "
     "is here construed as a ", False, False),
    ("pre-bayani", False, True),
    (" device: a data-ordering procedure that locates positions in a discursive field prior to the "
     "hermeneutic labour of bayan. The distinction between ‘replacing bayan’ and "
     "‘serving bayan’ is decisive. Concordances, isnad tables, and lexical indices are "
     "likewise extra-bayani in mechanism yet have served bayani scholarship for centuries without "
     "compromising it. Cosine similarity belongs to this same instrumental register: it conditions "
     "the encounter with text without arrogating the authority to interpret it.", False, False),
], indent=True)

add_para_mixed([
    ("On Islamisation of Knowledge. ", True, False),
    ("Neither al-Faruqi (1982: 14–20) nor al-Attas (1995: 113–120) is invoked to legitimise "
     "a claim that statistics has been ‘Islamised.’ Such a claim would be hubristic and "
     "methodologically empty. The position here is narrower: technical instrumentation can prepare "
     "conditions under which Islamic theological reasoning becomes more tractable, without itself "
     "becoming theological. The proper category is ", False, False),
    ("technical instrumentalisation", False, True),
    (", not Islamisation. Al-Attas’s worry was the uncritical importation of secular epistemic "
     "frames ", False, False),
    ("as", False, True),
    (" worldview; cosine similarity is offered not as a worldview but as an arithmetic operation on "
     "vectors, agnostic about ontology and silent about ends.", False, False),
], indent=True)

add_para_mixed([
    ("On jarh wa taʿdil. ", True, False),
    ("The comparison with hadith criticism is the most pointed objection. Ibn Hajar’s taxonomy—"
     "five graded levels of taʿdil and six of jarh (Ibn Hajar, 1986: 76–80)—"
     "operationalises a contextual, multidimensional, biographically grounded epistemics that no "
     "one-dimensional cosine score can rival. The honest claim is therefore minimalist: cosine "
     "similarity is not a competitor to jarh wa taʿdil but a ", False, False),
    ("stopgap", False, True),
    (" applicable where the contextual access required by jarh wa taʿdil is absent—namely, "
     "contemporary public discourse where biographical, isnad-based, and madhhab-internal information "
     "is unavailable or unverifiable. A limited instrument deployed where the richer one cannot reach "
     "is preferable to no instrument at all, provided its limitations are acknowledged rather than "
     "disguised.", False, False),
], indent=True)

add_para_mixed([
    ("Epistemic grading: yaqin, zann, shakk. ", True, False),
    ("The outputs of cosine similarity should be located within the traditional Islamic grading of "
     "epistemic states. Kamali (2003: 87–92) reconstructs the hierarchy whereby ", False, False),
    ("yaqin", False, True),
    (" (certainty) is reserved for knowledge of the highest evidentiary class, ", False, False),
    ("zann", False, True),
    (" (probable conjecture) governs the vast middle range of juristic and discursive reasoning, and ",
     False, False),
    ("shakk", False, True),
    (" (doubt) marks the lower boundary. Cosine similarity, by its very nature—finite corpus, "
     "lossy binary encoding, distributional rather than semantic warrant—yields outputs that "
     "belong unambiguously to the domain of ", False, False),
    ("zann", False, True),
    (". To present such outputs as ", False, False),
    ("yaqin", False, True),
    (" would be a category error; to acknowledge them as ", False, False),
    ("zann", False, True),
    (" is an honest alignment with the Islamic tradition’s own refusal to overstate what mediated "
     "reasoning can deliver.", False, False),
], indent=True)

add_subheading("Implications for Public Discourse in Indonesia")

add_para(
    "The Indonesian religious public sphere is now mediated, to an unprecedented degree, by short-form "
    "digital content whose virality often outruns its theological scrutiny (Bunt, 2018). Cases analogous "
    "to Mama Ghufron’s recur with increasing frequency, each generating a familiar cycle of viral "
    "outrage, denominational rebuttal, and inconclusive debate. A transparent epistemic scaffold of the "
    "kind demonstrated here offers practical value to several stakeholders: to journalists seeking a "
    "defensible basis for reporting on doctrinal controversies, to authoritative bodies such as MUI, "
    "Nahdlatul Ulama, and Muhammadiyah seeking to articulate the structural location of a contested "
    "claim, and to the general public seeking literacy in the criteria by which such judgements are made.",
    indent=False
)

add_para(
    "The risks of misuse are real and must be confronted. The construction of the binary dataset is "
    "itself an exercise of interpretive authority: whoever defines the 57 variables and stipulates the "
    "reference position effectively constrains the space of permissible answers. A tool of this kind "
    "could be weaponised for sectarian disqualification or for politically motivated discrediting of "
    "preachers whose appeal is inconvenient to incumbent authorities. Mitigating these risks requires "
    "institutional safeguards: the public documentation of coding decisions, the involvement of plural "
    "scholarly voices in dataset construction, and an explicit norm that similarity scores function as "
    "discussion-opening evidence rather than as discussion-closing verdicts.", indent=True
)

add_para(
    "These safeguards align naturally with two cardinal values of Indonesian Islamic civic culture: "
    "musyawarah, the deliberative consultation through which contested matters are collectively "
    "adjudicated, and tabayyun, the Qurʼanic injunction (Q. 49:6) to verify reports before acting "
    "upon them. Cosine similarity, properly deployed, does not displace these practices; it equips them "
    "with a more disciplined evidentiary base.", indent=True
)

# =============================================================
# N. METHODOLOGICAL REFLEXIVITY (M1 + ISU 3)
# =============================================================
add_heading("N.\tMethodological Reflexivity: On the Structure of the Similarity Score")

add_para(
    "A rigorous reviewer has rightly observed that, given the present configuration of the dataset—"
    "twenty variables coded b=1 (shared foundational doctrines) against thirty-seven variables coded "
    "b=0 (controversial or rejected claims)—the cosine similarity formula collapses into a "
    "transparent algebraic identity. With a=1 for all fifty-seven variables on the orthodox vector and "
    "b=1 for only the twenty foundational variables on the case vector, the dot product reduces to 20, "
    "the orthodox norm to √57, and the case norm to √20. The score therefore simplifies to:",
    indent=False
)

add_formula("cos(θ) = 20 / (√57 · √20) = √(20/57) ≈ 0.5923")

add_para_mixed([
    ("This is not a coincidence but a structural consequence of binary coding. The reported value is, "
     "in this sense, a deterministic function of the ", False, False),
    ("design ratio", False, True),
    (" between foundational and contested variables, not an independent empirical measurement of the "
     "subject under study. Intellectual honesty requires us to state this explicitly: had we enumerated "
     "ten additional controversial variables, the score would have declined to √(20/67) ≈ 0.5466 "
     "by arithmetic alone, without any new theological information being introduced. The number, taken "
     "in isolation, is therefore not a ‘discovery.’", False, False),
], indent=True)

# Paragraph 2 of Section N with ISU 3 sentences inserted at correct position
add_para_mixed([
    ("Acknowledging this, however, does not vacate the contribution of the present paper; it clarifies "
     "what that contribution actually is. Our claim has never been that cosine similarity ", False, False),
    ("discovers", False, True),
    (" the epistemic distance between a contested case and the orthodox foundation. The claim is that "
     "it ", False, False),
    ("displays", False, True),
    (" that distance in a form that is auditable, reproducible, and open to disputation. What the "
     "procedure guarantees, however, is ", False, False),
    ("transparency of mechanism", False, True),
    ("—the auditability of every step from source citation through coding decision to final "
     "computation—rather than ", False, False),
    ("transparency of outcome", False, True),
    (", since the outcome itself remains conditioned by coding choices whose reliability, as reported "
     "above, is no higher than moderate (Krippendorff, 2004: 241). The score travels into public "
     "discourse as a ", False, False),
    ("contestable artefact", False, True),
    (" whose construction is open to inspection, not as a frictionless number whose magnitude has been "
     "laundered of the interpretive labour that produced it. The cosine operation here functions as a ",
     False, False),
    ("display mechanism", False, True),
    (" rather than a ", False, False),
    ("discovery mechanism", False, True),
    ("—a way of compressing a multidimensional ledger of doctrinal commitments into a single "
     "ordinal that travels well in public discourse, provided the underlying ledger is published "
     "alongside it. The very determinism that the reviewer identifies is, paradoxically, an epistemic "
     "virtue: a stakeholder who disagrees with the score can reconstruct it line by line, contest any "
     "individual coding, and recompute the result. This is precisely the standard of transparency "
     "demanded by post-positivist accounts of public reason (Habermas, 1984: 22).", False, False),
], indent=True)

add_para_mixed([
    ("The same logic governs other widely accepted composite indices. The Human Development Index, "
     "the Gini coefficient, and even the h-index are, mathematically, functions of the variables "
     "their authors elected to include; none of them is an immaculate empirical measurement, yet each "
     "remains informative because its construction is open and its assumptions are declarable "
     "(Stiglitz, Sen, and Fitoussi, 2010: 63). Cosine similarity in doctrinal space belongs to this "
     "family of ", False, False),
    ("transparent reductive instruments", False, True),
    (".", False, False),
], indent=True)

add_para_mixed([
    ("What can legitimately be compared, then, is not the absolute value of a single score but the ",
     False, False),
    ("variability across cases sharing a common foundational frame", False, True),
    (". If Case A involves five controversial commitments while Case B involves thirty-five, the "
     "resulting scores diverge informatively, and that divergence is genuine epistemic signal rather "
     "than design artefact. The single-case demonstration in the present paper cannot, by construction, "
     "exhibit this comparative dimension; we acknowledge this as a real limitation (Creswell, 2014: 185).",
     False, False),
], indent=True)

add_para_mixed([
    ("Looking forward, the most productive generalisation is ", False, False),
    ("weighted cosine similarity", False, True),
    (", in which each variable carries a coefficient reflecting the degree of scholarly consensus or "
     "doctrinal weight—drawn, for instance, from the gradations of ijmaʼ, mashhur, and "
     "shadhdh recognised in classical usul al-fiqh (Kamali, 2003: 244). Under such weighting, the "
     "score is no longer a function of mere cardinality; identical variable counts can yield different "
     "similarities depending on the theological gravity of the items involved. We therefore treat the "
     "present paper not as a closed measurement claim but as the opening move of a methodological "
     "programme whose next step is precisely this generalisation.", False, False),
], indent=True)

# =============================================================
# O. CONCLUSION (was M)
# =============================================================
add_heading("O.\tConclusion")

add_para(
    "This article has demonstrated that cosine similarity applied to the binary representation of "
    "religious claims can serve as a valid epistemic scaffold in public theological "
    "discourse—provided it is understood and used within its proper limits. It is not a substitute "
    "for theological judgement, but a complement that offers something rarely present in religious "
    "discourse: transparency of premises, reproducibility of calculations, and accessibility of "
    "interpretation.", indent=False
)

add_para(
    "From the point of view of the philosophy of science, this article contributes to the understanding "
    "that mathematical formalisation can be applied to the non-scientific domain not to convert it into "
    "a science in the Popperian sense, but rather to borrow the structure of scientific "
    "transparency—the explicitness of assumptions, the verifiability of sources, the "
    "reproducibility of procedures—into a domain that requires it.", indent=True
)

add_para(
    "From the point of view of applied mathematics, this article shows that cosine similarity has uses "
    "that go beyond the domain of text computing. Its property of not counting zero-zero matches makes "
    "it an inherently precise tool for binary data with asymmetric meanings, such as the representation "
    "of doctrinal positions.", indent=True
)

add_para(
    "From the point of view of Islamic epistemology, this article shows that the spirit of jarh wa "
    "taʿdil—systematic assessment based on explicit criteria—can be continued with a "
    "different medium in the context of modern public discourse. Mathematics here is not a threat to "
    "the naql authority, but a form of operationalisation of ʻaql in the task of helping the "
    "public think more clearly.", indent=True
)

add_para(
    "Further research can expand this approach in several directions: (1) the development of variable "
    "weighting schemes based on scholarly consensus (weighted cosine similarity); (2) multicase "
    "comparisons to validate the usefulness of radial maps as a comparative instrument; and (3) a more "
    "in-depth epistemological study of the legitimacy of formalisation in classical and contemporary "
    "Islamic scientific traditions.", indent=True
)

add_para(
    "Most importantly, this article wants to emphasise that a good tool does not claim more than it "
    "can provide. Cosine similarity provides structure. The interpretation of that structure, and what "
    "decisions to make from it, remains the responsibility of human beings—especially those who "
    "have the scholarly depth to do so fairly.", indent=True
)

# =============================================================
# BIBLIOGRAPHY (complete, alphabetical, including all new refs)
# =============================================================
add_heading("Bibliography")

refs = [
    "Abdullah, M. Amin, Islamic Studies di Perguruan Tinggi: Pendekatan Integratif-Interkonektif, Pustaka Pelajar, Yogyakarta, 2006.",
    "Al-Attas, Syed Muhammad Naquib, Prolegomena to the Metaphysics of Islam: An Exposition of the Fundamental Elements of the Worldview of Islam, ISTAC, Kuala Lumpur, 1995.",
    "Al-Faruqi, Ismaʼil Raji, Islamisation of Knowledge: General Principles and Work Plan, International Institute of Islamic Thought, Washington D.C., 1982.",
    "Al-Jabiri, Mohammed Abed, Bunyat al-ʿAql al-ʿArabi: Dirasah Tahliliyyah Naqdiyyah li-Nuzum al-Maʿrifah fi al-Thaqafah al-ʿArabiyyah, Markaz Dirasat al-Wahdah al-ʿArabiyyah, Beirut, 1991.",
    "Brown, Jonathan A.C., Hadith: Muhammad’s Legacy in the Medieval and Modern World, Oneworld, Oxford, 2009.",
    "Bruinessen, Martin van (ed.), Contemporary Developments in Indonesian Islam: Explaining the ‘Conservative Turn,’ ISEAS, Singapore, 2013.",
    "Bunt, Gary R., Hashtag Islam: How Cyber-Islamic Environments Are Transforming Religious Authority, University of North Carolina Press, Chapel Hill, 2018.",
    "Creswell, John W., Research Design: Qualitative, Quantitative, and Mixed Methods Approaches, 4th ed., Sage Publications, Thousand Oaks, 2014.",
    "Flyvbjerg, Bent, ‘Five Misunderstandings About Case-Study Research’, Qualitative Inquiry, vol. 12, no. 2, 2006, pp. 219–245.",
    "Grimmer, Justin and Stewart, Brandon M., ‘Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts’, Political Analysis, vol. 21, no. 3, 2013, pp. 267–297.",
    "Gwet, Kilem L., Handbook of Inter-Rater Reliability, 4th ed., Advanced Analytics, Gaithersburg, 2014.",
    "Ha’iri Yazdi, Mehdi, The Principles of Epistemology in Islamic Philosophy: Knowledge by Presence, State University of New York Press, Albany, 1992.",
    "Habermas, Jürgen, The Theory of Communicative Action, vol. 1, Beacon Press, Boston, 1984.",
    "Hallaq, Wael B., Shariʼa: Theory, Practice, Transformations, Cambridge University Press, Cambridge, 2009.",
    "Hefner, Robert W., Civil Islam: Muslims and Democratization in Indonesia, Princeton University Press, Princeton, 2011.",
    "Ibn Hajar al-ʿAsqalani, Taqrib al-Tahdhib, ed. Muhammad ʿAwwama, Dar al-Rashid, Aleppo, 1986.",
    "Israel, Mark and Hay, Iain, Research Ethics for Social Scientists, Sage Publications, London, 2006.",
    "Kamali, Mohammad Hashim, Principles of Islamic Jurisprudence, 3rd ed., Islamic Texts Society, Cambridge, 2003.",
    "Kartanegara, Mulyadhi, Menyibak Tirai Kejahilan: Pengantar Epistemologi Islam, Mizan, Bandung, 2003.",
    "Kartanegara, Mulyadhi, Integrasi Ilmu: Sebuah Rekonstruksi Holistik, Arasy Mizan, Bandung, 2005.",
    "Kitcher, Philip, Science, Truth, and Democracy, Oxford University Press, Oxford, 2001.",
    "Krippendorff, Klaus, Content Analysis: An Introduction to Its Methodology, 2nd ed., Sage Publications, Thousand Oaks, 2004.",
    "Lakatos, Imre, The Methodology of Scientific Research Programmes: Philosophical Papers, vol. 1, ed. by John Worrall and Gregory Currie, Cambridge University Press, Cambridge, 1978.",
    "Leaman, Oliver, Averroes and His Philosophy, Psychology Press, London, 1998.",
    "Liu, Bing, Sentiment Analysis and Opinion Mining, Morgan & Claypool Publishers, San Rafael, 2012.",
    "Longino, Helen E., The Fate of Knowledge, Princeton University Press, Princeton, 2002.",
    "Manning, Christopher D., Raghavan, Prabhakar, and Schütze, Hinrich, Introduction to Information Retrieval, Cambridge University Press, Cambridge, 2008.",
    "Nasr, Seyyed Hossein, Knowledge and the Sacred, State University of New York Press, Albany, 1989.",
    "Nasr, Seyyed Hossein, Religion and the Order of Nature, Oxford University Press, Oxford, 1996.",
    "Pennycook, Gordon, Cannon, Tyrone D., and Rand, David G., ‘Prior Exposure Increases Perceived Accuracy of Fake News’, Journal of Experimental Psychology: General, vol. 147, no. 12, 2018, pp. 1865–1880.",
    "Poole, Keith T. and Rosenthal, Howard, ‘A Spatial Model for Legislative Roll Call Analysis’, American Journal of Political Science, vol. 29, no. 2, 1985, pp. 357–384.",
    "Popper, Karl, The Logic of Scientific Discovery, Routledge, London, 2005.",
    "Quine, W.V., ‘Two Dogmas of Empiricism’, The Philosophical Review, vol. 60, no. 1, 1951, pp. 20–43.",
    "Rahman, Fazlur, Islam and Modernity: Transformation of an Intellectual Tradition, University of Chicago Press, Chicago, 1982.",
    "Salton, Gerard and Buckley, Christopher, ‘Term-Weighting Approaches in Automatic Text Retrieval’, Information Processing and Management, vol. 24, no. 5, 1988, pp. 513–523.",
    "Stiglitz, Joseph E., Sen, Amartya, and Fitoussi, Jean-Paul, Mismeasuring Our Lives: Why GDP Doesn’t Add Up, New Press, New York, 2010.",
    "Winter, Tim (ed.), The Cambridge Companion to Classical Islamic Theology, Cambridge University Press, Cambridge, 2008.",
    "Wittgenstein, Ludwig, Philosophical Investigations, ed. by P.M.S. Hacker and Joachim Schulte, Wiley-Blackwell, Chichester, 2010.",
    "Yin, Robert K., Case Study Research and Applications: Design and Methods, 6th ed., Sage Publications, Thousand Oaks, 2018.",
]

for ref in refs:
    add_ref(ref)

# =============================================================
# SAVE
# =============================================================
output_path = "/home/user/riset-filsafat-sains/DISTANCE_IN_DOCTRINAL_SPACE_final.docx"
doc.save(output_path)
print(f"Saved: {output_path}")

# Word count (paragraphs + tables)
para_words = sum(len(p.text.split()) for p in doc.paragraphs)
table_words = sum(
    len(cell.text.split())
    for table in doc.tables
    for row in table.rows
    for cell in row.cells
)
total = para_words + table_words
print(f"Estimated word count: {total:,} words (paragraphs: {para_words:,}, tables: {table_words:,})")
print(f"References: {len(refs)}")
