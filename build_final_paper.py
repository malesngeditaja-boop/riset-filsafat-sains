"""
Builds the final integrated paper docx for Al-Jami'ah journal.
Run: python3 build_final_paper.py
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# --- Page setup: A4, margins ---
section = doc.sections[0]
section.page_height = Cm(29.7)
section.page_width  = Cm(21.0)
section.top_margin    = Cm(2.54)
section.bottom_margin = Cm(2.54)
section.left_margin   = Cm(2.54)
section.right_margin  = Cm(2.54)

# --- Default paragraph style: Times New Roman 12pt, 1.5 spacing ---
style = doc.styles['Normal']
font  = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
from docx.oxml.ns import qn
style.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

def set_spacing(para, before=0, after=6, line=276):
    from docx.shared import Pt as _Pt
    from docx.oxml.ns import qn as _qn
    pf = para.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after  = Pt(after)
    # Set 1.5 line spacing via XML directly
    pPr = para._p.get_or_add_pPr()
    lnSpc = OxmlElement('w:lnSpc')
    lnSpcVal = OxmlElement('w:lnSpcVal')
    lnSpcVal.set(_qn('w:line'), '360')  # 360 = 1.5 * 240
    lnSpcVal.set(_qn('w:lineRule'), 'auto')
    lnSpc.append(lnSpcVal)
    existing = pPr.find(_qn('w:lnSpc'))
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

def add_label(text):
    """For 'Keywords:', 'Abstract:' labels."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'
    set_spacing(p, before=0, after=3)
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

# ============================================================
# TITLE
# ============================================================
add_title("DISTANCE IN DOCTRINAL SPACE: COSINE SIMILARITY AS AN\nEPISTEMIC TOOL IN PUBLIC THEOLOGICAL DISCOURSE")

doc.add_paragraph()  # spacer

# ============================================================
# ABSTRACT (EN)
# ============================================================
add_heading("Abstract")
add_small(
    "Public religious discourse in Indonesia often takes place without a common reference point that can be "
    "examined intersubjectively, resulting in debate that goes around without a productive resolution. This "
    "article proposes cosine similarity applied to binary vectors of religious claims as an epistemic scaffold—"
    "a structure that makes the premises of theological debate explicit, open, and verifiable. Using the viral "
    "case of preacher Mama Ghufron (2024) as a case study, a dataset of 57 binary variables was constructed "
    "from verified media reports and official responses from religious institutions. The results of the "
    "calculation showed a cosine similarity of 0.5923 between the profile of the subject's claims and the "
    "Mainstream Islamic Position. This article argues that this value is not a theological verdict, but rather "
    "an instrument of transparency that allows public discussion to start from the same facts. Implications are "
    "discussed from three angles: philosophy of science (formalisation of the non-scientific domain), applied "
    "mathematics (extension of cosine similarity beyond text computing), and Islamic epistemology (naql and "
    "'aql as the basis for evaluating claims)."
)

# ABSTRACT (ID)
add_small(
    "Wacana keagamaan publik di Indonesia kerap berlangsung tanpa titik referensi bersama yang dapat diperiksa "
    "secara intersubjektif, sehingga menghasilkan perdebatan yang berputar-putar tanpa resolusi yang produktif. "
    "Artikel ini mengajukan cosine similarity atas vektor biner klaim keagamaan sebagai epistemic scaffold—"
    "sebuah perancah epistemik yang membuat premis-premis perdebatan teologis menjadi eksplisit, terbuka, dan "
    "dapat diverifikasi. Dengan menggunakan kasus viral penceramah Mama Ghufron (2024) sebagai studi kasus, "
    "dataset 57 variabel biner dikonstruksi dari laporan media terverifikasi dan respons resmi lembaga "
    "keagamaan. Hasil perhitungan menunjukkan cosine similarity sebesar 0,5923 antara profil klaim subjek dan "
    "Posisi Islam Mainstream. Artikel ini berargumen bahwa nilai tersebut bukan vonis teologis, melainkan "
    "instrumen transparansi yang memungkinkan diskusi publik dimulai dari fakta yang sama. Implikasi dibahas "
    "dari tiga sudut: filsafat sains (formalisasi domain non-ilmiah), matematika terapan (perluasan cosine "
    "similarity ke luar domain komputasi teks), dan epistemologi Islam (naql dan 'aql sebagai basis evaluasi "
    "klaim).", italic=True
)

add_small("Keywords: cosine similarity, binary vector, Islamic epistemology, philosophy of science, theological discourse.")

doc.add_paragraph()

# ============================================================
# A. INTRODUCTION
# ============================================================
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
    "longest-running debates in the philosophy of science: the demarcation problem—the boundary between science "
    "and non-science. Karl Popper (2005) proposed falsifiability as a demarcation criterion: a statement is "
    "scientific only if it can in principle be refuted by empirical evidence. Religious claims, in Popper's "
    "framework, are generally outside the domain of science not because they are wrong, but because their "
    "structure does not allow for falsification. Lakatos (1978) refined this position with the concept of a "
    "research programme: every research programme has a hard core protected from falsification, and a "
    "protective belt that can be modified. In a religious context, the core beliefs function similarly to the "
    "hard core, while the fringe interpretations are more flexible. Quine (1951) adds a relevant perspective "
    "through the web-of-beliefs argument: beliefs do not stand alone but are interconnected in a network, and "
    "the revision of one belief has implications for others.", indent=True
)

add_para(
    "It is important to note that this article does not claim that cosine similarity turns religious claims "
    "into scientific statements in the Popperian sense. Instead, it borrows the structure of transparency from "
    "science—the explicitness of the premise, the verifiability of sources, the reproducibility of "
    "calculations—to apply to the domain of public discourse that has been running without such a structure.", indent=True
)

add_para(
    "In the Islamic scientific tradition, the debate on the role of reason ('aql) vis-à-vis the text of "
    "revelation (naql) has been ongoing since the Middle Ages. Al-Ghazali in Tahafut al-Falasifa criticises "
    "philosophers who give reason excessive authority in the domains of metaphysics and theology, while Ibn "
    "Rushd (Averroes) in Tahafut al-Tahafut argues that reason and revelation, if understood correctly, are "
    "not in conflict with each other (Leaman, 1998). In the modern context, Amin Abdullah (2006) proposes an "
    "integration-interconnection paradigm in Islamic science: religious sciences and general sciences do not "
    "need to be opposed, but can reinforce each other within the framework of honest methodological dialogue.", indent=True
)

# --- NEW: Literature review addition (Kartanegara, Nasr, Al-Jabiri) ---
add_para(
    "The Islamic philosophical resources for thinking about epistemic verification extend considerably beyond "
    "this classical disputation, and a fuller engagement with these resources clarifies the position the "
    "present article seeks to occupy. Mulyadhi Kartanegara, among the most systematic of contemporary "
    "Indonesian Muslim philosophers, has argued for a non-dichotomous model of the relation between religious "
    "and scientific knowledge, in which the two are understood as complementary modes of access to a unitary "
    "reality (Kartanegara, 2003: 21–34; 2005: 87–104). On Kartanegara's account, the project of integration "
    "does not require dissolving the methodological autonomy of the empirical sciences, but rather "
    "acknowledging that each domain of inquiry possesses its own appropriate instruments.", indent=True
)

add_para(
    "Seyyed Hossein Nasr's enduring critique of modern science must also be engaged seriously. Nasr (1989: "
    "1–18; 1996: 96–119) maintains that modern science, having severed itself from the sacred, produces a "
    "knowledge that is technically powerful but metaphysically impoverished. From this vantage, any "
    "importation of formal techniques into theological discourse risks reproducing the very reductionism that "
    "the scientia sacra tradition resists. The present article takes this warning to heart by restricting the "
    "scope of the technique it proposes: cosine similarity is not deployed to evaluate the truth of doctrinal "
    "claims, only to display their structural relations under an explicitly stipulated coding.", indent=True
)

add_para(
    "Mohammed Abed Al-Jabiri's tripartite classification of epistemic modalities in the Arab-Islamic "
    "intellectual tradition—bayan (exegetical-juridical reasoning anchored in textual sources), burhan "
    "(demonstrative reasoning in the Aristotelian sense), and 'irfan (gnostic or illuminative knowledge)—"
    "provides a particularly useful map for situating the contribution of the present article (Al-Jabiri, "
    "1991: 383–415). The cosine similarity procedure does not pretend to operate in the register of 'irfan, "
    "which by its nature resists formal representation, and it is not itself a form of bayan, since it does "
    "not generate juridical rulings. It functions instead as an auxiliary within the burhani register: a "
    "formal, demonstrative operation upon explicitly represented premises, whose output is then returned to "
    "the bayani community for interpretation.", indent=True
)

add_para(
    "A further distinction internal to the Isyraqi tradition refines this placement. Suhrawardi and his "
    "commentators differentiate al-'ilm al-husuli, knowledge acquired through the mediation of concepts and "
    "representations, from al-'ilm al-huduri, knowledge present to the knower without mediation (Ha'iri Yazdi, "
    "1992: 43–67). Cosine similarity is, by construction, an operation upon representations; it is therefore "
    "intelligible only within the domain of al-'ilm al-husuli and has no purchase whatsoever upon al-'ilm "
    "al-huduri. Recognising this limit is not a concession but a clarification.", indent=True
)

add_para(
    "In the tradition of usul al-fiqh, the evaluation of claims—including claims about spiritual capacity—"
    "requires structured verification. The concept of jarh wa ta'dil in hadith science, for example, is a "
    "systematic assessment of the credibility of narrators based on explicit criteria that can be audited "
    "(Brown, 2009). In the same spirit, albeit with a different medium, cosine similarity offers an explicit "
    "variable-based scoring system that anyone can examine.", indent=True
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

# ============================================================
# B. RESEARCH APPROACH
# ============================================================
add_heading("B.\tResearch Approach")

add_para(
    "This article uses a descriptive-analytical approach grounded in a single case study. The choice of a "
    "single case study is methodologically deliberate rather than incidental. As Yin (2018: 49–53) argues, "
    "the single-case design is particularly justified when the case functions as a representative or "
    "paradigmatic instance through which a broader methodological proposition can be tested in concrete terms. "
    "Flyvbjerg (2006: 219–229) further demonstrates that the conventional bias against the explanatory power "
    "of single cases rests on a misreading of how knowledge is actually produced in the social sciences: "
    "paradigmatic cases are often more generative of theoretical insight than large-N studies because they "
    "expose the inner workings of a phenomenon under examination. The case of Mama Ghufron in 2024 satisfies "
    "both criteria. It is representative of a broader pattern of contested theological claims circulating in "
    "Indonesian digital public space, and it is paradigmatic insofar as it crystallises the very ambiguity—"
    "between unorthodoxy and outright heresy—that motivates the construction of an epistemic scaffold in the "
    "first place.", indent=False
)

add_para(
    "The descriptive-analytical mode is preferred over experimental or survey-based designs for several "
    "interrelated reasons. First, the object of inquiry is not a measurable behavioural variable across a "
    "population, but a structural relation between a discursive profile and a doctrinal reference position. "
    "Such relations are not amenable to randomised manipulation in any ethically or epistemically meaningful "
    "way. Second, the unit of analysis is a corpus of theological propositions, not a sample of human "
    "respondents; survey instruments would therefore mistake the locus of evidence. Third, the article's "
    "ambition is to exhibit a method—to show how cosine similarity can be operationalised on binary "
    "representations of religious claims and what such operationalisation does and does not yield—rather than "
    "to estimate parameters or test hypotheses in the inferential-statistical sense.", indent=True
)

add_para(
    "The approach carries inherent limitations that must be acknowledged. A single case cannot, on its own, "
    "licence generalisations about the distribution of doctrinal deviance in Indonesian preaching, nor can it "
    "adjudicate the substantive theological merits of any particular claim. The construction of the "
    "57-variable binary dataset, moreover, encodes interpretive choices that other researchers might contest. "
    "The article addresses these limitations not by claiming to overcome them but by foregrounding them: all "
    "coding decisions are documented, the reference position is explicitly stipulated rather than assumed, and "
    "the resulting similarity score is presented as a diagnostic prompt for further deliberation rather than "
    "as a final verdict. The article should therefore be read as a conceptual-methodological demonstration—a "
    "proof of concept for a transparent epistemic tool—rather than as an empirical generalisation about the "
    "state of public preaching in Indonesia.", indent=True
)

# ============================================================
# C. DATA SOURCES
# ============================================================
add_heading("C.\tData Sources")

add_para(
    "The data in this article is sourced from two layers. The first layer is news reports from verified "
    "national media covering claims attributed to the subject of the case study, including Republika, "
    "Detik.com, Kumparan, tvOne, and Eramuslim, published between April and October 2024. The second layer "
    "is official statements from religious institutions, especially the MUI Malang (10 points of irregularity "
    "that were officially released) and comments from PBNU.", indent=False
)

add_para(
    "The selection of these sources is based on two criteria: (1) the source is publicly accessible with a "
    "verifiable URL, and (2) the source has explicitly responded to the reported claims. This is important to "
    "ensure that the constructed variables do not come from assumptions or speculation, but rather from a "
    "record of real public discourse.", indent=True
)

# ============================================================
# D. DATASET CONSTRUCTION
# ============================================================
add_heading("D.\tDataset Construction")

add_para(
    "The dataset is constructed in two structurally distinct layers that reflect the comparative architecture "
    "of the model.", indent=False
)

add_para(
    "Layer 1: Common Foundation (20 variables, U01–U20). The first layer consists of twenty variables "
    "representing fundamental Islamic beliefs that are overwhelmingly shared across the full spectrum of "
    "Indonesian Muslim expression, including by the subject of this case study. Both vectors receive a score "
    "of 1 on this layer. The decision to include this foundational layer carries significant epistemological "
    "weight: it ensures that the model does not begin from the premise that the subject occupies the position "
    "of an outsider or non-Muslim. Rather, it acknowledges a substantial shared ground before the analysis "
    "proceeds to examine areas of reported divergence. Without this layer, the similarity score would collapse "
    "to zero—a result that would be both arithmetically predictable and epistemologically dishonest. The "
    "twenty foundation variables cover the core affirmations of Islamic faith (usul al-din): monotheism, "
    "prophethood, revealed scripture, the authority of hadith, the existence of angels and the unseen realm, "
    "eschatological beliefs (the Day of Judgement, paradise, and hellfire), the reality of the grave (alam "
    "kubur), the obligatory nature of worship, and the principle of post-mortem accountability. Their "
    "inclusion as a shared baseline is not a rhetorical concession; it is a structural requirement for a "
    "model that aspires to be fair.", indent=True
)

add_para(
    "Layer 2: Controversial Claims (37 variables, K01–K37). The second layer consists of thirty-seven "
    "variables derived from specific claims attributed to the subject and reported by verified Indonesian "
    "media outlets between April and October 2024. These claims were systematically gathered from six primary "
    "sources: Republika, Detik.com (including Detik Jatim), Kumparan, tvOne, Eramuslim, and Tanya Islam Yuk, "
    "supplemented by official institutional responses from MUI Pusat, MUI Malang, PBNU, and KabarJawa.", indent=True
)

add_para(
    "Each raw claim from the media was transformed into a normative variable—a statement of the position that "
    "a person aligned with mainstream Indonesian Islamic teaching would be expected to hold. Because the "
    "variable represents the mainstream norm, the Mainstream Islamic Position vector (a) is uniformly valued "
    "at 1 across all 37 variables, while the subject's claim profile (b) receives 0 on each, since the "
    "reported claim contradicts the norm. This asymmetry is precisely what drives the cosine calculation.", indent=True
)

add_para(
    "The 37 controversial variables cluster into five thematic groups: (1) claims of supernatural "
    "communication (K01–K07), including alleged video calls with the Angel of Death and direct conversation "
    "with Munkar, Nakir, and Izrail; (2) claims of extraordinary linguistic capacity (K08–K14), including "
    "alleged command of Syriac, the language of ants, the language of jinn, and the language of angels; "
    "(3) claims of cosmological authority (K15–K16, K23–K27), including alleged capacity to guard hellfire, "
    "summon Angel Jibril, postpone the Day of Judgement, and serve as Nabi Sulaiman's representative; "
    "(4) claims of unverified textual authority (K17–K20, K30–K37), including alleged authorship of 500 "
    "Syriac-language religious texts, unauthorised Qur'anic interpretation, and self-composed hadith; and "
    "(5) claims of direct divine access (K21–K22, K25–K26, K28–K29), including alleged ability to transform "
    "ordinary water into zamzam water and direct learning from Allah over forty years.", indent=True
)

add_para(
    "Every variable in the dataset is linked to at least one publicly verifiable source. The complete dataset "
    "is presented in Table 1 (common foundation) and Table 2 (controversial claims) below.", indent=True
)

# --- TABLE 1 ---
doc.add_paragraph()
t1_header = doc.add_paragraph()
t1_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t1_header.add_run("Table 1. Common Foundation Variables (a = 1, b = 1 for both vectors)")
r.bold = True
r.font.size = Pt(11)
r.font.name = 'Times New Roman'

table1 = doc.add_table(rows=1, cols=4)
table1.style = 'Table Grid'
table1.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = table1.rows[0].cells
for cell, txt in zip(hdr, ["ID", "Variable", "a", "b"]):
    cell.text = txt
    cell.paragraphs[0].runs[0].bold = True
    cell.paragraphs[0].runs[0].font.size = Pt(10)

common_vars = [
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
]
for i, v in enumerate(common_vars, 1):
    row = table1.add_row().cells
    row[0].text = f"U{i:02d}"
    row[1].text = v
    row[2].text = "1"
    row[3].text = "1"
    for cell in row:
        cell.paragraphs[0].runs[0].font.size = Pt(10)

doc.add_paragraph()

# --- TABLE 2 ---
t2_header = doc.add_paragraph()
t2_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = t2_header.add_run("Table 2. Controversial Claims Variables (a = 1, b = 0)")
r2.bold = True
r2.font.size = Pt(11)
r2.font.name = 'Times New Roman'

table2 = doc.add_table(rows=1, cols=5)
table2.style = 'Table Grid'
table2.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr2 = table2.rows[0].cells
for cell, txt in zip(hdr2, ["ID", "Source Claim", "Variable (Mainstream Norm)", "Source", "b"]):
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
    ("Menafsirkan ayat Al-Qur'an tanpa kaidah tafsir", "Tidak menafsirkan Al-Qur'an tanpa kaidah tafsir", "Detik/MUI Malang"),
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
    row[0].text = f"K{i:02d}"
    row[1].text = src
    row[2].text = var
    row[3].text = source
    row[4].text = "0"
    for cell in row:
        cell.paragraphs[0].runs[0].font.size = Pt(9)

doc.add_paragraph()

# ============================================================
# E. BINARY REPRESENTATIONS
# ============================================================
add_heading("E.\tBinary Representations and Their Justifications")

add_para(
    "The use of binary values 0 and 1 is a conscious simplification. It abstracts the nuances, contexts, and "
    "gradations that exist in each claim. The justifications for its use are pragmatic and epistemological: "
    "pragmatic because it allows for reproducible cosine similarity calculations, and epistemological because "
    "it forces dataset creators to make explicit decisions about each variable rather than leaving them "
    "ambiguous. In this sense, binary limitation is precisely a methodological strength: any ambiguity must "
    "be resolved explicitly and arguably.", indent=False
)

# ============================================================
# F. MATHEMATICAL FOUNDATIONS
# ============================================================
add_heading("F.\tMathematical Foundations: Why Cosine Similarity")

add_para(
    "Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle "
    "between them. For two vectors a and b in n-dimensional space, the formula is:", indent=False
)

# Formula as centred paragraph
fp = doc.add_paragraph()
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = fp.add_run("cos(θ) = (Σᵢ aᵢbᵢ) / (√(Σᵢ aᵢ²) · √(Σᵢ bᵢ²))")
fr.font.name = 'Courier New'
fr.font.size = Pt(12)
set_spacing(fp, before=6, after=6)

add_para(
    "where a · b is the dot product of the two vectors, and ‖a‖ and ‖b‖ are their Euclidean norms.", indent=False
)

add_para(
    "For binary data, the dot product produces a positive value only when both corresponding elements are "
    "valued at 1. When either or both are 0, the contribution to the dot product is zero. This means that "
    "cosine similarity does not count zero-zero matches as evidence of similarity—a property that is crucial "
    "for this context. Two subjects who both lack a belief should not be considered more alike simply because "
    "of that absence. This property distinguishes cosine similarity from simple distance metrics such as the "
    "simple matching coefficient, which treats a null-value match equal to a one-value match (Manning, "
    "Raghavan, and Schütze, 2008).", indent=True
)

# ============================================================
# G. CALCULATIONS
# ============================================================
add_heading("G.\tCalculations for Mama Ghufron's Case")

add_para(
    "With the dataset of 57 variables constructed across Table 1 and Table 2, the calculation proceeds as "
    "follows.", indent=False
)

add_para(
    "Dot product (a · b): The dot product produces a positive value only where both vectors are valued at 1. "
    "This occurs exclusively on the 20 common foundation variables. In the 37 controversial claim variables, "
    "vector a is valued at 1 but vector b is valued at 0, so the contribution is zero. Thus: a · b = 20.", indent=True
)

add_para(
    "Vector norm ‖a‖: Vector a (Mainstream Islamic Position) is valued at 1 on all 57 variables: "
    "‖a‖ = √57 ≈ 7.5498.", indent=True
)

add_para(
    "Vector norm ‖b‖: Vector b (subject claim profile) is valued at 1 on only the 20 foundation variables: "
    "‖b‖ = √20 ≈ 4.4721.", indent=True
)

# Calculation formula
cp = doc.add_paragraph()
cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
cr = cp.add_run("cos(θ) = 20 / (7.5498 × 4.4721) = 20 / 33.7639 ≈ 0.5923")
cr.font.name = 'Courier New'
cr.font.size = Pt(12)
set_spacing(cp, before=4, after=4)

ap = doc.add_paragraph()
ap.alignment = WD_ALIGN_PARAGRAPH.CENTER
ar = ap.add_run("θ = arccos(0.5923) ≈ 53.66°")
ar.font.name = 'Courier New'
ar.font.size = Pt(12)
set_spacing(ap, before=4, after=6)

add_para(
    "This result places the subject's claim profile in the 'Far' zone on the interpretation scale used, "
    "where zones are defined as: Very Close (≥0.90), Fairly Close (≥0.75), Problematic (≥0.60), "
    "Far (≥0.40), and Very Far (<0.40).", indent=True
)

# ============================================================
# H. READING THE NUMBERS
# ============================================================
add_heading("H.\tReading the Numbers: What It Says")

add_para(
    "The value of 0.5923 communicates two things simultaneously. First, it confirms the existence of a "
    "substantial common foundation: the 20 variables with full match represent a significant proportion of "
    "the total 57 variables. Second, it shows that in the 37 variables born from specific claims reported "
    "by the media, there are systematic differences large enough to lower the similarity score to the 'Far' "
    "zone.", indent=False
)

add_para(
    "What is important to attend to is the information hidden behind this single number. The difference "
    "between a score of 0.59 and a score of 0.20 is not just a matter of magnitude—it reflects a completely "
    "different structure of differences. The score of 0.59 in this case arises from a large common foundation "
    "(20 variables) that is offset by an equally large set of differences (37 variables). The same score in "
    "another hypothetical case could arise from an entirely different pattern. The same number does not "
    "necessarily tell the same story.", indent=True
)

# ============================================================
# I. VISUALIZATION
# ============================================================
add_heading("I.\tVisualisation as a Complement to Calculation")

add_para(
    "To support more intuitive reading, the project on which this article is based also provides an "
    "interactive radial map built as an open-source React application. The radial map places the Mainstream "
    "Islamic Position at the central point, and visualises the subject's position as a point in "
    "two-dimensional space whose distance from the centre represents the cosine distance. Five concentric "
    "zones (Very Close to Very Far) provide instantly readable visual context without requiring the reader "
    "to inspect the underlying numbers.", indent=False
)

add_para(
    "This visualisation is not decorative. It is part of the epistemological argument of this article: "
    "transparency requires not only data openness, but also accessibility of presentation. A map that can "
    "be read by journalists, students, and ordinary citizens has a different epistemic value than a table "
    "of numbers accessible only to statisticians. The tool further allows users to toggle individual "
    "variable values interactively, enabling readers to test how the similarity score changes when specific "
    "coding decisions are revised—an affordance that directly operationalises the article's commitment to "
    "auditability.", indent=True
)

# ============================================================
# J. CONSTRUCT OF VARIABLES
# ============================================================
add_heading("J.\tConstruct of Variables as Epistemic Decisions")

add_para(
    "The most important—and most often overlooked—part of this whole approach is the process of constructing "
    "the variables themselves. Each variable in the dataset is the result of a human decision: decisions "
    "about which claims are sufficiently documented to include, how to formulate variables neutrally, and "
    "from which sources those claims are drawn.", indent=False
)

add_para(
    "These decisions cannot be completely free from subjective considerations. The choice to formulate the "
    "variable as a positive norm ('Not claiming direct communication with the angel of death') rather than "
    "a negative statement ('Claiming direct communication with the angel of death') is a rhetorical choice "
    "with mathematical consequences: it determines which side is by default valued at 1 and which at 0. "
    "Precisely because these limitations are inherent and cannot be eliminated, the openness of the process "
    "becomes the main accountability mechanism. Because each variable is explicitly recorded along with its "
    "source, anyone can question the decision to include it, propose an alternative formulation, or dispute "
    "the reliability of a source. Open debates about variables are far more epistemologically productive "
    "than debates whose assumptions are never disclosed.", indent=True
)

# ============================================================
# K. LIMITS OF APPROACH
# ============================================================
add_heading("K.\tThe Limits of the Approach: What Numbers Cannot Tell")

add_para(
    "This section is the most crucial in this article, and at the same time the most frequently missed in "
    "discussions of formal methods applied to humanistic domains.", indent=False
)

add_para(
    "First, this figure is not a theological verdict. The value of 0.5923 measures the distance between two "
    "sets of positions encoded in 57 binary variables based on selected sources at a given point in time. "
    "It does not state whether the subject is misguided, not misguided, worthy of criticism, or worthy of "
    "defending. These are theological questions requiring expertise in tafsir, hadith, kalam, and usul "
    "al-fiqh—domains that binary vectors simply cannot address.", indent=True
)

add_para(
    "Second, variables are human decisions. If the dataset were constructed with a different choice of "
    "variables—for example, by including variables that support the subject, or with different weights for "
    "different types of claims—the results would differ. This is not a fatal flaw of the methodology but "
    "rather because every methodology has assumptions. What sets this approach apart is that these "
    "assumptions are explicit and debatable.", indent=True
)

add_para(
    "Third, it is a snapshot, not a film. The dataset records the claims in circulation and reported over "
    "a given period. If the subject subsequently substantially retracts or revises those claims, the dataset "
    "should be updated and the numbers will change. Cosine similarity does not record history; it takes a "
    "picture of a moment.", indent=True
)

add_para(
    "Fourth, humans cannot be reduced to vectors. This is the most fundamental limitation. Every "
    "individual—including anyone who is the subject of this kind of analysis—is a complex human being with "
    "life journeys, social contexts, intentions, and dimensions of humanity that no number can capture. "
    "Wittgenstein (2010) reminds us that the meaning of a statement cannot be separated from the context "
    "of its use (Lebensform). The binary representation of a claim abstracts that context, and that "
    "abstraction is always a partial loss of meaning.", indent=True
)

add_para(
    "Acknowledging these limitations is not a sign of methodological weakness, but of methodological "
    "integrity. A tool that knows the limits of its capabilities can be used responsibly. A tool that "
    "claims to be all-purpose is genuinely dangerous.", indent=True
)

# ============================================================
# L. DISCUSSION  (NEW SECTION)
# ============================================================
add_heading("L.\tDiscussion")

add_subheading("Implications for the Philosophy of Science")

add_para(
    "The procedure demonstrated in this article borrows a structural feature of scientific practice—the "
    "explicit, auditable representation of premises and the calculable relation among them—and transposes "
    "it onto a domain that is, on any reasonable construal, not itself a science. This transposition "
    "requires careful qualification. The article does not claim, in the Popperian register, that theological "
    "propositions are or ought to be falsifiable in the strict sense, nor that the cosine score between two "
    "doctrinal profiles is itself a truth-functional verdict. The demarcation problem, as Popper (2005) "
    "framed it and as Lakatos subsequently refined it, concerns the conditions under which a body of "
    "propositions counts as scientific; the present article sidesteps that question by appropriating not the "
    "content of scientific reasoning but its epistemic virtues: the explicitness of assumptions, the "
    "reproducibility of operations, and the verifiability of intermediate steps.", indent=False
)

add_para(
    "This appropriation finds support in recent work in the social epistemology of science. Longino (2002: "
    "128–135) argues that the criteria for genuine knowledge—publicly recognised venues for criticism, "
    "uptake of criticism, public standards, and tempered equality of intellectual authority—are not the "
    "exclusive property of natural science but generalise to any community engaged in the cooperative "
    "production of warranted belief. Kitcher's (2001: 117–135) notion of well-ordered science points in the "
    "same direction: what makes an inquiry well-ordered is not its subject matter but the institutional and "
    "procedural transparency through which its claims are produced and contested. Cosine similarity, "
    "deployed as an epistemic scaffold, contributes precisely such procedural transparency to a discourse "
    "that has historically been mediated by charismatic authority and rhetorical performance.", indent=True
)

add_para(
    "For the long-running debate over the Islamisation of Knowledge, this reframing matters. Rather than "
    "asking whether religious commitments can constitute a science in their own right, the present approach "
    "asks a narrower and more tractable question: which formal techniques of representation and comparison, "
    "drawn from contemporary information science, can be reflectively appropriated to render public "
    "theological discourse more accountable to its own stated premises? Posed this way, the question avoids "
    "the polemical impasse between sacralisation and secularisation of knowledge and opens a pragmatic "
    "middle path.", indent=True
)

add_subheading("Implications for Islamic Epistemology")

add_para(
    "The article's deeper resonance lies with the long Islamic tradition of grading epistemic states. The "
    "classical usul al-fiqh distinction among yaqin (certainty), zann (probable conjecture), and shakk "
    "(suspended doubt) already encodes a graded epistemology in which the same proposition may, under "
    "different evidentiary conditions, occupy different epistemic ranks (Kamali, 2003: 87–93). A cosine "
    "similarity score of 0.5923 sits naturally within such a graded framework: it does not pronounce a "
    "verdict of disbelief but situates a discursive profile within a continuum of proximity to a stipulated "
    "reference, leaving the normative adjudication to the appropriate scholarly community.", indent=False
)

add_para(
    "Nasr's critique of modern science warns against the reduction of all knowledge to quantifiable, "
    "instrumental form (Nasr, 1989: 130–159). The procedure proposed here must answer that critique "
    "honestly. It does so by limiting its own scope: the cosine score is not offered as a substitute for "
    "hermeneutic, juridical, or spiritual discernment but as a propaedeutic—an aid to the prior stage of "
    "clarifying what is at stake before deeper interpretive labour begins. The instrument is silent on the "
    "meaning of doctrinal commitments; it speaks only to the structural relation among their explicit forms.", indent=True
)

add_para(
    "Fazlur Rahman's call for a renewed Islamic methodology, willing to use the tools of contemporary "
    "scholarship (Rahman, 1982: 1–11), aligns with rather than opposes this proposal. Most pointedly, the "
    "procedure can be read as a modernisation of the spirit of jarh wa ta'dil in the hadith tradition: the "
    "systematic, auditable evaluation of testimony against explicit criteria, conducted in public and open "
    "to revision. What classical critics did for chains of transmission, a transparent similarity calculus "
    "can do, in a limited and propaedeutic way, for the doctrinal content of contemporary public preaching.", indent=True
)

add_para(
    "The limits of the technique must, however, be stated plainly. Cosine similarity cannot weigh the "
    "relative gravity of doctrinal claims; it treats all 57 variables as equally weighted unless otherwise "
    "stipulated. It cannot detect rhetorical irony, pedagogical hyperbole, or contextual accommodation. It "
    "cannot, finally, replace the judgement of qualified scholars; it can only make the antecedents of that "
    "judgement more visible.", indent=True
)

add_subheading("Implications for Public Discourse in Indonesia")

add_para(
    "The Indonesian religious public sphere is now mediated, to an unprecedented degree, by short-form "
    "digital content whose virality often outruns its theological scrutiny (Bunt, 2018). Cases analogous "
    "to Mama Ghufron's recur with increasing frequency, each generating a familiar cycle of viral outrage, "
    "denominational rebuttal, and inconclusive debate. A transparent epistemic scaffold of the kind "
    "demonstrated here offers practical value to several stakeholders: to journalists seeking a defensible "
    "basis for reporting on doctrinal controversies, to authoritative bodies such as MUI, Nahdlatul Ulama, "
    "and Muhammadiyah seeking to articulate the structural location of a contested claim, and to the general "
    "public seeking literacy in the criteria by which such judgements are made.", indent=False
)

add_para(
    "The risks of misuse are real and must be confronted. The construction of the binary dataset is itself "
    "an exercise of interpretive authority: whoever defines the 57 variables and stipulates the reference "
    "position effectively constrains the space of permissible answers. A tool of this kind could be "
    "weaponised for sectarian disqualification or for politically motivated discrediting of preachers whose "
    "appeal is inconvenient to incumbent authorities. Mitigating these risks requires institutional "
    "safeguards: the public documentation of coding decisions, the involvement of plural scholarly voices "
    "in dataset construction, and an explicit norm that similarity scores function as discussion-opening "
    "evidence rather than as discussion-closing verdicts.", indent=True
)

add_para(
    "These safeguards align naturally with two cardinal values of Indonesian Islamic civic culture: "
    "musyawarah, the deliberative consultation through which contested matters are collectively adjudicated, "
    "and tabayyun, the Qur'anic injunction (Q. 49:6) to verify reports before acting upon them. Cosine "
    "similarity, properly deployed, does not displace these practices; it equips them with a more disciplined "
    "evidentiary base.", indent=True
)

# ============================================================
# M. CONCLUSION
# ============================================================
add_heading("M.\tConclusion")

add_para(
    "This article has demonstrated that cosine similarity applied to the binary representation of religious "
    "claims can serve as a valid epistemic scaffold in public theological discourse—provided it is understood "
    "and used within its proper limits. It is not a substitute for theological judgement, but a complement "
    "that offers something rarely present in religious discourse: transparency of premises, reproducibility "
    "of calculations, and accessibility of interpretation.", indent=False
)

add_para(
    "From the point of view of the philosophy of science, this article contributes to the understanding that "
    "mathematical formalisation can be applied to the non-scientific domain not to convert it into a science "
    "in the Popperian sense, but rather to borrow the structure of scientific transparency—the explicitness "
    "of assumptions, the verifiability of sources, the reproducibility of procedures—into a domain that "
    "requires it.", indent=True
)

add_para(
    "From the point of view of applied mathematics, this article shows that cosine similarity has uses that "
    "go beyond the domain of text computing. Its property of not counting zero-zero matches makes it an "
    "inherently precise tool for binary data with asymmetric meanings, such as the representation of "
    "doctrinal positions.", indent=True
)

add_para(
    "From the point of view of Islamic epistemology, this article shows that the spirit of jarh wa ta'dil—"
    "systematic assessment based on explicit criteria—can be continued with a different medium in the "
    "context of modern public discourse. Mathematics here is not a threat to the naql authority, but a form "
    "of operationalisation of 'aql in the task of helping the public think more clearly.", indent=True
)

add_para(
    "Further research can expand this approach in several directions: (1) the development of variable "
    "weighting schemes based on scholarly consensus (weighted cosine similarity); (2) multicase comparisons "
    "to validate the usefulness of radial maps as a comparative instrument; and (3) a more in-depth "
    "epistemological study of the legitimacy of formalisation in classical and contemporary Islamic "
    "scientific traditions.", indent=True
)

add_para(
    "Most importantly, this article wants to emphasise that a good tool does not claim more than it can "
    "provide. Cosine similarity provides structure. The interpretation of that structure, and what decisions "
    "to make from it, remains the responsibility of human beings—especially those who have the scholarly "
    "depth to do so fairly.", indent=True
)

# ============================================================
# BIBLIOGRAPHY
# ============================================================
add_heading("Bibliography")

refs = [
    "Abdullah, M. Amin, Islamic Studies di Perguruan Tinggi: Pendekatan Integratif-Interkonektif, Pustaka Pelajar, Yogyakarta, 2006.",
    "Al-Jabiri, Mohammed Abed, Bunyat al-'Aql al-'Arabi: Dirasah Tahliliyyah Naqdiyyah li-Nuzum al-Ma'rifah fi al-Thaqafah al-'Arabiyyah, Markaz Dirasat al-Wahdah al-'Arabiyyah, Beirut, 1991.",
    "Brown, Jonathan A.C., Hadith: Muhammad's Legacy in the Medieval and Modern World, Oneworld, Oxford, 2009.",
    "Bunt, Gary R., Hashtag Islam: How Cyber-Islamic Environments Are Transforming Religious Authority, University of North Carolina Press, Chapel Hill, 2018.",
    "Flyvbjerg, Bent, 'Five Misunderstandings About Case-Study Research', Qualitative Inquiry, vol. 12, no. 2, 2006, pp. 219–245.",
    "Grimmer, Justin and Stewart, Brandon M., 'Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts', Political Analysis, vol. 21, no. 3, 2013, pp. 267–297.",
    "Ha'iri Yazdi, Mehdi, The Principles of Epistemology in Islamic Philosophy: Knowledge by Presence, State University of New York Press, Albany, 1992.",
    "Kamali, Mohammad Hashim, Principles of Islamic Jurisprudence, 3rd ed., Islamic Texts Society, Cambridge, 2003.",
    "Kartanegara, Mulyadhi, Menyibak Tirai Kejahilan: Pengantar Epistemologi Islam, Mizan, Bandung, 2003.",
    "Kartanegara, Mulyadhi, Integrasi Ilmu: Sebuah Rekonstruksi Holistik, Arasy Mizan, Bandung, 2005.",
    "Kitcher, Philip, Science, Truth, and Democracy, Oxford University Press, Oxford, 2001.",
    "Lakatos, Imre, The Methodology of Scientific Research Programmes: Philosophical Papers, vol. 1, ed. by John Worrall and Gregory Currie, Cambridge University Press, Cambridge, 1978.",
    "Leaman, Oliver, Averroes and His Philosophy, Psychology Press, London, 1998.",
    "Liu, Bing, Sentiment Analysis and Opinion Mining, Morgan & Claypool Publishers, San Rafael, 2012.",
    "Longino, Helen E., The Fate of Knowledge, Princeton University Press, Princeton, 2002.",
    "Manning, Christopher D., Raghavan, Prabhakar, and Schütze, Hinrich, Introduction to Information Retrieval, Cambridge University Press, Cambridge, 2008.",
    "Nasr, Seyyed Hossein, Knowledge and the Sacred, State University of New York Press, Albany, 1989.",
    "Nasr, Seyyed Hossein, Religion and the Order of Nature, Oxford University Press, Oxford, 1996.",
    "Pennycook, Gordon, Cannon, Tyrone D., and Rand, David G., 'Prior Exposure Increases Perceived Accuracy of Fake News', Journal of Experimental Psychology: General, vol. 147, no. 12, 2018, pp. 1865–1880.",
    "Poole, Keith T. and Rosenthal, Howard, 'A Spatial Model for Legislative Roll Call Analysis', American Journal of Political Science, vol. 29, no. 2, 1985, pp. 357–384.",
    "Popper, Karl, The Logic of Scientific Discovery, Routledge, London, 2005.",
    "Quine, W.V., 'Two Dogmas of Empiricism', The Philosophical Review, vol. 60, no. 1, 1951, pp. 20–43.",
    "Rahman, Fazlur, Islam and Modernity: Transformation of an Intellectual Tradition, University of Chicago Press, Chicago, 1982.",
    "Salton, Gerard and Buckley, Christopher, 'Term-Weighting Approaches in Automatic Text Retrieval', Information Processing and Management, vol. 24, no. 5, 1988, pp. 513–523.",
    "Wittgenstein, Ludwig, Philosophical Investigations, ed. by P.M.S. Hacker and Joachim Schulte, Wiley-Blackwell, Chichester, 2010.",
    "Yin, Robert K., Case Study Research and Applications: Design and Methods, 6th ed., Sage Publications, Thousand Oaks, 2018.",
]

for ref in refs:
    add_ref(ref)

# ============================================================
# SAVE
# ============================================================
output_path = "/home/user/riset-filsafat-sains/DISTANCE_IN_DOCTRINAL_SPACE_final.docx"
doc.save(output_path)
print(f"Saved: {output_path}")

# Word count estimate
total_text = " ".join([p.text for p in doc.paragraphs])
word_count = len(total_text.split())
print(f"Estimated word count: {word_count:,} words")
