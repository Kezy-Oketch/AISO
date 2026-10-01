# AISO Inclusion Protocol v0.1

**African Information Systems Observatory (AISO)**  
**Document version:** 0.1  
**Coverage period:** 2000–2026  
**Status:** Pilot protocol

## 1. Purpose

This protocol defines the eligibility criteria for inclusion in the AISO Core Collection.

The AISO Core Collection is intended to provide a reproducibly constructed corpus of scholarly Information Systems research substantively involving African contexts.

Inclusion in the collection is based on the content and context of a publication rather than solely on author nationality, institutional affiliation, publication venue, or the presence of an African country name.

The protocol separates three dimensions that may otherwise be conflated:

1. **Geography of Evidence** — where the phenomena, populations, organizations, institutions, or empirical observations underlying the research are located.
2. **Geography of Knowledge Production** — where the scholars and institutions producing the research are located.
3. **Geography of Theorization** — the contextual origins of constructs, mechanisms, boundary conditions, and theoretical explanations developed through the research.

These dimensions are coded separately.

---

## 2. Unit of Inclusion

The primary unit of inclusion is a **scholarly publication**.

Each eligible publication receives a unique `AISO_Record_ID`.

Multiple publications originating from the same underlying research project remain separate publication records.

Different versions of substantially the same scholarly work, such as a conference paper followed by a journal article, should be linked using an `AISO_Work_ID` where the relationship can be established.

Versions should not be silently deleted or treated as independent intellectual contributions without documenting their relationship.

---

## 3. Temporal Scope

AISO Core Collection v0.1 covers publications from:

**January 1, 2000 through December 31, 2026.**

Earlier publications may eventually be incorporated into an AISO Historical Collection but are outside the initial Core Collection.

---

## 4. Inclusion Criteria

A publication must satisfy **all three** primary criteria below.

### Criterion A — Scholarly Status

The publication must constitute scholarly research.

Eligible publication types include:

- peer-reviewed journal articles;
- full peer-reviewed conference papers;
- scholarly review articles;
- scholarly conceptual or theoretical articles;
- peer-reviewed research articles published in relevant scholarly proceedings.

Publication types such as editorials, book reviews, news articles, teaching cases, presentation slides, abstracts without full papers, and non-scholarly commentary are not included in the Core Collection unless a later AISO protocol explicitly creates a separate collection for them.

### Criterion B — Substantive Information Systems Relevance

The publication must substantively examine an Information Systems phenomenon.

The research should involve digital or information technologies in relation to one or more human, organizational, societal, institutional, behavioral, managerial, economic, or sociotechnical phenomena.

Potential technologies and domains include, but are not limited to:

- information systems;
- information and communication technologies;
- digital platforms;
- mobile technologies;
- mobile money;
- financial technologies;
- digital payments;
- electronic commerce;
- digital government;
- digital identity;
- health information systems;
- digital health;
- enterprise systems;
- social media;
- artificial intelligence;
- data analytics;
- digital labor;
- digital marketplaces;
- agricultural information systems;
- cloud computing;
- digital infrastructure;
- cybersecurity;
- information and knowledge systems.

A publication is not included merely because it uses computers, software, statistical packages, machine learning, or digital data as research tools.

Technology must be substantively connected to the phenomenon being investigated.

### Criterion C — Substantive African Relationship

Africa must have a substantive role in the research.

At least one of the following must apply:

1. an African country, population, organization, community, institution, or setting provides empirical evidence;
2. an African digital phenomenon is substantively investigated;
3. an African context forms an explicit component of a comparative study;
4. the publication develops theoretical arguments concerning Information Systems phenomena in African contexts;
5. the publication synthesizes or reviews a body of Information Systems research concerning Africa.

A passing reference to Africa or an African country is insufficient.

---

## 5. What Does Not Establish Eligibility

The following characteristics alone do **not** qualify a publication for inclusion:

- an author is African;
- an author works at an African institution;
- the publication appears in an African journal;
- an African organization funded the research;
- Africa appears only in the introduction or discussion;
- an African country is mentioned incidentally;
- an African country occurs in a large global dataset but is not substantively represented in the analysis;
- the study uses a globally available dataset containing African observations without analytically engaging the African context;
- the publication discusses a technology that happens to operate in Africa without studying its African use or implications.

These characteristics may be recorded as metadata when relevant, but they do not independently determine inclusion.

---

## 6. Multi-Country and Global Studies

For studies containing both African and non-African countries, coders should assess the **analytical role of Africa**.

Use the following classification:

**0 — Incidental**

Africa or an African country appears in the dataset or text but receives no meaningful analytical role.

**1 — Included but pooled**

African observations are substantively part of the study but are pooled into a broader sample without Africa-specific analysis.

**2 — Explicitly analyzed**

African countries, populations, organizations, or observations receive identifiable analysis.

**3 — Central**

African contexts constitute a central empirical or theoretical component of the study.

Records classified as **0 — Incidental** are excluded from the AISO Core Collection.

Records classified as 1, 2, or 3 may be included when the other inclusion criteria are satisfied.

The distinction between categories 1 and 2 should be examined during the pilot because pooled global studies may require additional eligibility rules.

---

## 7. Relationship-to-Africa Metadata

Eligibility should not collapse different relationships to Africa into a single variable.

For included publications, AISO records separate indicators for:

- `Africa_Empirical_Context`
- `Africa_Theoretical_Context`
- `Africa_Digital_Phenomenon`
- `Africa_Focused_Review`
- `Africa_Based_Author`
- `Africa_Based_Institution`
- `Africa_Comparative_Component`

These variables permit later analysis of different forms of participation in African Information Systems scholarship.

---

## 8. Exclusion Codes

Every screened but excluded record should receive a documented exclusion reason.

Use the following preliminary codes:

**E01 — Outside temporal scope**  
Publication falls outside the designated collection period.

**E02 — Not scholarly research**  
Record does not constitute an eligible scholarly publication.

**E03 — Insufficient Information Systems relevance**  
Digital or information technology is not a substantive component of the research phenomenon.

**E04 — Incidental African reference**  
Africa is mentioned but does not play a substantive empirical, theoretical, or analytical role.

**E05 — African affiliation only**  
Connection to Africa arises solely from author or institutional affiliation.

**E06 — African venue only**  
Connection to Africa arises solely from the publication venue.

**E07 — Global dataset without substantive African analysis**  
African observations may exist but are not meaningfully incorporated into the study's analysis or argument.

**E08 — Duplicate record**  
The record duplicates another bibliographic record for the same publication.

**E09 — Ineligible publication type**  
Record is an abstract, editorial, book review, presentation, news item, or another publication type outside the Core Collection.

**E10 — Insufficient information for eligibility determination**  
Available metadata or text is insufficient to determine eligibility.

Records assigned E10 should be retained for later investigation rather than permanently discarded.

---

## 9. Borderline Cases

Ambiguous records should not be resolved through undocumented individual judgment.

Coders should:

1. assign the record a provisional eligibility decision;
2. document the reason for uncertainty;
3. identify the relevant protocol provision;
4. flag the record for adjudication;
5. record the final decision and rationale in the AISO Decision Log.

Recurring ambiguities should trigger clarification of the protocol.

Changes to the protocol should be versioned rather than silently introduced.

---

## 10. Screening Procedure

Screening should occur in stages.

### Stage 1 — Bibliographic Screening

Use title, abstract, keywords, venue, and available bibliographic metadata to identify clearly eligible or clearly ineligible records.

### Stage 2 — Full-Text Screening

When eligibility cannot be confidently determined from bibliographic information, examine the full text.

### Stage 3 — Adjudication

Records involving substantive uncertainty should be independently reviewed and adjudicated.

The final dataset should retain:

- initial screening decision;
- final screening decision;
- exclusion code where applicable;
- coder identifier;
- screening date;
- adjudication status;
- decision notes where necessary.

---

## 11. Pilot Validation

Before large-scale corpus construction, this protocol will be tested on a pilot set containing approximately 50 publications.

The pilot should intentionally contain:

- clearly eligible studies;
- clearly ineligible studies;
- African-author but non-African-context studies;
- African-context studies with non-African authors;
- multinational studies;
- global datasets containing African observations;
- conceptual papers;
- review papers;
- ICT4D research;
- adjacent non-IS research;
- difficult interdisciplinary cases.

At least two coders should independently screen the pilot.

The pilot will be used to assess:

- raw agreement;
- Cohen's kappa where appropriate;
- recurring sources of disagreement;
- ambiguous inclusion criteria;
- adequacy of exclusion codes.

The protocol will be revised based on documented pilot evidence before full screening begins.

---

## 12. Corpus Layers

AISO distinguishes among several corpus layers.

### Discovery Index

All candidate records identified through AISO discovery procedures.

### Screening Corpus

Deduplicated candidate records subjected to eligibility screening.

### AISO Core Collection

Publications satisfying the formal inclusion criteria.

### Extended Collection

Relevant scholarly work that may be valuable to AISO but falls outside one or more Core Collection boundaries.

### Exclusion Archive

Screened records excluded from the Core Collection, with documented exclusion reasons.

These layers should remain analytically distinguishable.

---

## 13. Scope of Claims

The AISO Core Collection should not initially be described as containing "all African Information Systems research."

Until coverage validation and saturation analyses have been completed, the preferred description is:

> **A reproducibly constructed, multi-source scholarly corpus of Information Systems research from and about African contexts between 2000 and 2026.**

Claims regarding comprehensiveness should be supported empirically through source-contribution analysis, citation saturation, country-level validation, venue coverage, and expert review.

---

## 14. Versioning

This document is **AISO Inclusion Protocol v0.1**.

Version 0.1 is intended for pilot testing.

Changes arising from pilot screening must be recorded in:

`docs/CHANGELOG.md`

Substantive modifications to eligibility rules should result in a new protocol version.

---

## 15. Foundational Principle

AISO distinguishes between:

**where evidence is observed,**

**where scholarly knowledge is produced,**

and

**where theoretical ideas originate.**

A publication's relationship to Africa cannot be adequately represented by any one of these dimensions alone.

Maintaining this distinction is foundational to the AISO research infrastructure.
