# AISO Search and Corpus Construction Protocol v0.1

**African Information Systems Observatory (AISO)**  
**Document version:** 0.1  
**Coverage period:** 2000–2026  
**Status:** Pilot protocol

## 1. Purpose

This protocol defines the procedures used to discover, retrieve, document, deduplicate, and validate candidate publications for the AISO Core Collection.

The objective is to construct a transparent and reproducible scholarly corpus while minimizing dependence on any single journal list, bibliographic database, disciplinary tradition, or search vocabulary.

Corpus discovery is intentionally broader than final inclusion.

A publication retrieved during discovery becomes a **candidate record**. Inclusion in the AISO Core Collection is determined separately using the AISO Inclusion Protocol.

---

## 2. Coverage Period

The initial AISO Core Collection covers publications from:

**January 1, 2000 through December 31, 2026.**

Publications outside this period may be retained in the Discovery Index for future historical extensions but are outside the initial Core Collection.

---

## 3. Multi-Source Discovery Strategy

AISO uses multiple discovery strata to reduce source-specific coverage bias.

Each candidate record should retain information identifying the source or sources through which it was discovered.

### S1 — Premier Information Systems Journals

The initial search should include the journals recognized in the current AIS Senior Scholars' premier journal list.

The initial venue set includes:

- Decision Support Systems
- European Journal of Information Systems
- Information & Management
- Information and Organization
- Information Systems Journal
- Information Systems Research
- Journal of the Association for Information Systems
- Journal of Information Technology
- Journal of Management Information Systems
- Journal of Strategic Information Systems
- MIS Quarterly

The venue list should be versioned because disciplinary journal classifications may change over time.

### S2 — Broader Information Systems Journals

Candidate outlets include:

- Communications of the Association for Information Systems
- Information Systems Frontiers
- Information Systems Management
- Journal of Global Information Management
- Journal of Global Information Technology Management
- Journal of Computer Information Systems
- Government Information Quarterly
- International Journal of Information Management

Additional outlets may be added following pilot source-contribution analysis.

### S3 — Africa-Centered Information Systems Outlets

The initial set includes:

- African Journal of Information Systems

Additional Africa-centered IS outlets identified during discovery should be documented and evaluated for inclusion in this stratum.

### S4 — ICT4D and Digital Development Outlets

The initial set includes:

- Electronic Journal of Information Systems in Developing Countries
- Information Technology for Development

Additional outlets may be incorporated when they regularly publish work satisfying the AISO Information Systems inclusion criterion.

### S5 — Major Information Systems Conferences

The initial conference set includes:

- International Conference on Information Systems
- European Conference on Information Systems
- Americas Conference on Information Systems

### S6 — Africa-Centered Conferences

The initial set includes:

- African Conference on Information Systems and Technology

Other recurring African IS conferences should be documented as they are identified.

### S7 — Bibliographic Database Discovery

Database-wide discovery should be conducted using, where available:

- Scopus
- Web of Science

Supplementary bibliographic sources may include:

- OpenAlex
- Crossref
- Google Scholar

The role and limitations of each source should be documented.

### S8 — Citation Chaining

Backward and forward citation searches should be conducted for highly relevant publications, major reviews, and foundational African IS studies.

Citation chaining is intended to identify publications missed because of terminology, indexing, or venue differences.

### S9 — Existing Review Harvesting

Reference lists from systematic reviews, literature reviews, bibliometric studies, and scholarly syntheses concerning African Information Systems, ICT4D, digital transformation, and related domains may be used to identify candidate publications.

Records discovered this way remain subject to normal AISO eligibility screening.

### S10 — Community and Expert Submission

AISO may eventually allow scholars to nominate potentially missing publications.

Community submission does not establish eligibility.

Submitted records undergo the same screening process as records discovered through other sources.

---

## 4. Geographic Search Vocabulary

AISO geographic discovery should not rely on the keyword "Africa" alone.

The search vocabulary should contain:

1. Africa;
2. regional terms;
3. individual African country names;
4. recognized alternative country names;
5. relevant historical names where necessary for the coverage period;
6. common adjectival or geographic variants where they materially improve retrieval.

The canonical vocabulary will be maintained separately in:

`data/reference/AISO_Geography_Dictionary_v0.1.csv`

This allows geographic terminology to be versioned independently from the search protocol.

---

## 5. Regional Search Terms

Initial regional terminology should include phrases such as:

- Africa
- African
- Sub-Saharan Africa
- sub-Saharan Africa
- North Africa
- Northern Africa
- West Africa
- Western Africa
- East Africa
- Eastern Africa
- Central Africa
- Middle Africa
- Southern Africa

Additional regional terminology may be introduced following pilot retrieval analysis.

---

## 6. Information Systems and Digital Technology Vocabulary

For broad multidisciplinary databases, geographic terms should be combined with Information Systems and digital-technology terminology.

Initial concepts include:

- information system
- information systems
- information technology
- information and communication technology
- ICT
- digital technology
- digital technologies
- digital platform
- digital platforms
- digital transformation
- digitalization
- digitization
- mobile technology
- mobile phone
- mobile money
- fintech
- financial technology
- digital payment
- electronic commerce
- e-commerce
- e-government
- digital government
- digital identity
- health information system
- digital health
- enterprise system
- social media
- artificial intelligence
- data analytics
- digital labor
- platform labor
- cloud computing
- digital infrastructure
- cybersecurity
- knowledge management system
- agricultural information system

The vocabulary should be evaluated empirically during pilot discovery.

---

## 7. Search Logic

Search logic differs according to source type.

### 7.1 IS-Defined Venues

For journals and conferences whose disciplinary scope is already substantially Information Systems, searches should primarily use the geographic vocabulary.

Conceptually:

`AFRICA_GEOGRAPHY_BLOCK`

This reduces the risk of excluding relevant IS research because authors use unexpected technology terminology.

### 7.2 Multidisciplinary Databases

For Scopus, Web of Science, and similar broad databases, the initial conceptual query is:

`AFRICA_GEOGRAPHY_BLOCK AND IS_DIGITAL_BLOCK`

Exact syntax should be adapted to each database.

Database-specific queries must be preserved in the search log.

### 7.3 Country-Level Validation Searches

After broad discovery, country-by-country searches should be performed to identify geographic retrieval gaps.

Country-level searches are particularly important for countries whose publications may not use "Africa" or regional terminology in titles, abstracts, or keywords.

---

## 8. Author-Affiliation Discovery

Author institutional affiliation must not be used as a substitute for substantive African research context.

However, a separate search may identify scholarship produced by Africa-based IS researchers.

These records are relevant to the **Geography of Knowledge Production**.

Records discovered solely through African institutional affiliation should not enter the Core Collection unless they independently satisfy the substantive African relationship criterion.

This distinction permits AISO to analyze separately:

- research about or in Africa; and
- IS research produced from African institutions.

---

## 9. Search Logging

Every formal search should be recorded.

The search log should include at minimum:

- `Search_ID`
- `Search_Date`
- `Researcher`
- `Source`
- `Database_or_Venue`
- `Coverage_Years`
- `Exact_Query`
- `Filters`
- `Results_Returned`
- `Results_Exported`
- `Export_Format`
- `Export_File`
- `Notes`

The search log should eventually be stored in machine-readable form.

---

## 10. Raw Data Preservation

Original bibliographic exports should be preserved without manual alteration.

Raw files should be stored under:

`data/raw/`

Processed versions should never overwrite raw source files.

Where bibliographic database licensing restricts redistribution, raw exports should remain private even if AISO code and derived metadata are publicly released.

---

## 11. Record Provenance

Every candidate publication should retain its discovery provenance.

Suggested variables include:

- `Discovery_Scopus`
- `Discovery_WoS`
- `Discovery_OpenAlex`
- `Discovery_Crossref`
- `Discovery_GoogleScholar`
- `Discovery_PremierIS`
- `Discovery_BroaderIS`
- `Discovery_AfricaIS`
- `Discovery_ICT4D`
- `Discovery_Conference`
- `Discovery_Citation`
- `Discovery_Review`
- `Discovery_Community`

A publication may have multiple discovery sources.

---

## 12. Deduplication

Candidate records from different sources should be merged into a unified Discovery Index.

Deduplication should proceed using a hierarchy of evidence.

### Level 1 — DOI

Exact normalized DOI matches should generally be treated as duplicate bibliographic records.

### Level 2 — Exact Bibliographic Match

Where DOI is unavailable, exact or near-exact combinations of title, author, and publication year may identify duplicates.

### Level 3 — Fuzzy Title Matching

Normalized title similarity may be used to identify potential duplicate candidates.

Fuzzy matches should be reviewed before merging.

### Level 4 — Manual Resolution

Ambiguous records should be manually inspected.

Deduplication decisions should be reproducible and documented.

---

## 13. Conference and Journal Versions

Conference and journal publications derived from the same underlying project should not automatically be treated as simple duplicates.

Where a relationship is established:

- each publication may retain its own `AISO_Record_ID`;
- related publications should share an `AISO_Work_ID`;
- publication relationships should be documented.

This permits analyses at both publication and intellectual-work levels.

---

## 14. Screening

The deduplicated Discovery Index becomes the Screening Corpus.

Eligibility decisions must follow:

`docs/inclusion_protocol_v0.1.md`

Discovery source should not determine eligibility.

Records from premier journals, African journals, ICT4D journals, conferences, or community submissions are evaluated under the same substantive inclusion criteria.

---

## 15. Corpus Layers

AISO maintains distinct corpus layers.

### Discovery Index

All candidate publications identified through discovery.

### Screening Corpus

Deduplicated candidate records subjected to eligibility screening.

### Core Collection

Records satisfying AISO inclusion criteria.

### Extended Collection

Relevant scholarship outside one or more Core Collection boundaries.

### Exclusion Archive

Screened records excluded from the Core Collection with documented reasons.

---

## 16. Pilot Discovery

Before conducting the complete 2000–2026 search, AISO should run a pilot discovery exercise.

The pilot should evaluate approximately 100 candidate publications drawn from multiple discovery strata.

The pilot should assess:

- retrieval precision;
- number of records contributed by each source;
- number of unique records contributed by each source;
- country coverage;
- outlet coverage;
- temporal coverage;
- disciplinary coverage;
- frequency of false positives;
- frequency of duplicates;
- terminology responsible for successful retrieval;
- terminology responsible for false positives.

The pilot should inform Search Protocol v1.0.

---

## 17. Source-Contribution Analysis

For each discovery source, AISO should calculate:

- total candidate records contributed;
- eligible records contributed;
- unique eligible records contributed;
- overlap with other sources.

This analysis helps determine whether additional databases or venue strata materially improve coverage.

A source producing few records may still be valuable if those records are otherwise absent.

---

## 18. Coverage and Saturation Evaluation

AISO should not assume that corpus construction is complete merely because a large number of publications have been retrieved.

Coverage should be evaluated through multiple tests.

### Venue Saturation

Determine whether searching additional relevant outlets continues to yield unique eligible publications.

### Citation Saturation

Determine whether backward and forward citation chaining continues to identify previously undiscovered eligible publications.

### Geographic Validation

Conduct targeted searches for individual African countries and examine countries with unexpectedly low or zero representation.

### Temporal Validation

Inspect publication counts across years for suspicious gaps.

### Expert Validation

Ask knowledgeable scholars to identify important publications or research traditions absent from the candidate corpus.

### Phenomenon Validation

Examine whether known major African digital phenomena are represented in the corpus.

---

## 19. Multilingual Discovery

English-language indexing alone may produce systematic coverage limitations.

AISO should eventually evaluate supplementary discovery in at least:

- French;
- Portuguese.

Additional languages may be incorporated where evidence indicates meaningful scholarly coverage.

Language-specific search expansions should be documented and versioned.

The initial English-centered discovery process should therefore not be interpreted as evidence that English captures the complete African IS literature.

---

## 20. Reproducibility

Where permitted by database licensing, AISO should release:

- search dictionaries;
- exact search queries;
- search dates;
- source lists;
- discovery scripts;
- deduplication scripts;
- screening procedures;
- derived bibliographic metadata;
- exclusion reasons;
- methodological documentation.

Restricted raw bibliographic exports should not be redistributed when licensing prohibits it.

---

## 21. Analytical Universes

AISO distinguishes three related but non-equivalent analytical universes.

### Universe A — Information Systems Research About or In Africa

Research substantively investigating African empirical, digital, institutional, organizational, or social contexts.

### Universe B — Information Systems Research Produced From African Institutions

Research produced by scholars affiliated with African institutions, regardless of empirical context.

### Universe C — Information Systems Theory Emerging From African Contexts

Research in which African phenomena contribute to the development of constructs, mechanisms, boundary conditions, frameworks, or theoretical explanations.

A publication may belong to one, two, or all three universes.

The AISO Core Collection initially centers Universe A while collecting metadata necessary to investigate Universes B and C.

---

## 22. Scope of Claims

Until saturation and coverage validation have been completed, AISO should describe the Core Collection as:

> **A reproducibly constructed, multi-source scholarly corpus of Information Systems research from and about African contexts between 2000 and 2026.**

Terms such as "complete," "comprehensive," or "all African IS research" should not be used without supporting coverage evidence.

---

## 23. Versioning

This document is **AISO Search and Corpus Construction Protocol v0.1**.

Version 0.1 governs pilot discovery.

Changes arising from pilot searches should be documented in:

`docs/CHANGELOG.md`

Substantive modifications to sources, search logic, geographic scope, or corpus-construction procedures should result in a new protocol version.

---

## 24. Guiding Principle

AISO's corpus should not be defined by any single database, journal ranking, conference community, or disciplinary tradition.

The discovery strategy should be sufficiently broad to allow the empirical record to reveal where African Information Systems scholarship is produced, published, and theorized.


