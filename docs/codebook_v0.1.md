# AISO Metadata and Coding Codebook v0.1

**African Information Systems Observatory (AISO)**  
**Document version:** 0.1  
**Coverage period:** 2000–2026  
**Status:** Pilot codebook

## 1. Purpose

This codebook defines the metadata fields and analytical variables used to characterize publications in the AISO Core Collection.

The codebook supports three goals:

1. creation of a reusable scholarly information infrastructure;
2. descriptive mapping of Information Systems scholarship concerning Africa; and
3. investigation of how empirical context relates to knowledge production and theorization.

AISO distinguishes three dimensions throughout the coding process:

**Geography of Evidence** — where empirical phenomena and observations are located.

**Geography of Knowledge Production** — where the scholars and institutions producing the research are located.

**Geography of Theorization** — the contextual origins of constructs, mechanisms, boundary conditions, and theoretical explanations.

These dimensions must not be inferred from one another.

---

# PART I — CODING PRINCIPLES

## 2. Unit of Analysis

The primary unit is the scholarly publication.

Each publication receives a unique:

`AISO_Record_ID`

Related publications arising from substantially the same underlying scholarly work may additionally share:

`AISO_Work_ID`

The relationship between conference and journal versions should be documented rather than resolved through silent deletion.

---

## 3. Metadata Levels

AISO distinguishes three levels of metadata.

### Level 1 — Factual Metadata

Information that can generally be extracted with limited interpretive judgment.

Examples:

- title;
- year;
- journal;
- DOI;
- author;
- institutional affiliation;
- country;
- methodology stated by authors.

### Level 2 — Analytical Metadata

Variables requiring classification but ordinarily based on observable characteristics.

Examples:

- technology category;
- phenomenon category;
- research setting;
- data type;
- collaboration structure.

### Level 3 — Theoretical Metadata

Variables requiring substantive interpretation of the publication's argument.

Examples:

- theory role;
- African-context theory role;
- new construct development;
- mechanism development;
- theoretical boundary conditions.

Level 3 variables should receive the greatest validation attention.

---

## 4. Missing and Uncertain Information

Do not infer information without sufficient evidence.

Use:

`NA` — information is not applicable.

`NR` — information is not reported or cannot be established.

`UNCERTAIN` — evidence exists but coding remains ambiguous.

Uncertainty should be accompanied by a coder note.

---

# PART II — RECORD IDENTIFICATION

## 5. AISO Record ID

**Variable:** `AISO_Record_ID`

Unique identifier assigned to every publication.

Recommended format:

`AISO-000001`

IDs should remain stable across later dataset releases.

---

## 6. AISO Work ID

**Variable:** `AISO_Work_ID`

Identifier linking publications representing substantially related versions of the same scholarly work.

Example:

```text
AISO_Record_ID      AISO_Work_ID
AISO-000041         WORK-000019
AISO-000267         WORK-000019
```

Use only when a relationship can be established with reasonable confidence.

---

# PART III — BIBLIOGRAPHIC METADATA

## 7. Title

`Title`

Record the publication title as published.

---

## 8. Publication Year

`Publication_Year`

Four-digit year.

---

## 9. Publication Type

`Publication_Type`

Allowed values:

- Journal Article
- Conference Paper
- Review Article
- Conceptual/Theoretical Article
- Other Eligible Scholarly Publication

---

## 10. Venue

`Venue`

Full journal, conference, or proceedings name.

---

## 11. Volume

`Volume`

Record where applicable.

---

## 12. Issue

`Issue`

Record where applicable.

---

## 13. Pages

`Pages`

Record article or proceedings page range where available.

---

## 14. DOI

`DOI`

Store normalized DOI without URL prefix where possible.

Example:

`10.xxxx/xxxxx`

---

## 15. Abstract

`Abstract`

Store where licensing permits.

---

## 16. Author Keywords

`Author_Keywords`

Preserve original author-provided keywords where available.

---

# PART IV — AUTHOR AND INSTITUTION METADATA

## 17. Author Count

`Author_Count`

Total number of publication authors.

---

## 18. Author Names

Author-level information should eventually be stored relationally rather than as a single publication-level string.

For pilot coding, preserve ordered author names.

---

## 19. Author Position

For each author record:

`Author_Position`

Values:

1, 2, 3, etc.

---

## 20. Corresponding Author

`Corresponding_Author`

Values:

- Yes
- No
- NR

---

## 21. Institutional Affiliation

`Institution_Name`

Record institutional affiliation at the time of publication where available.

Do not substitute current affiliation for publication-time affiliation.

---

## 22. Institution Country

`Institution_Country`

Use standardized AISO geography terminology.

---

## 23. Africa-Based Institution

`Africa_Based_Institution`

Values:

- Yes
- No
- NR

Determined from publication-time institutional location.

---

## 24. Africa-Based First Author

`Africa_Based_First_Author`

Values:

- Yes
- No
- NR

This refers to institutional affiliation, not nationality or ethnicity.

---

## 25. Africa-Based Corresponding Author

`Africa_Based_Corresponding_Author`

Values:

- Yes
- No
- NR

---

## 26. Africa-Based Last Author

`Africa_Based_Last_Author`

Values:

- Yes
- No
- NR

Use where author order is meaningful.

---

## 27. All Authors Africa-Based

`All_Authors_Africa_Based`

Values:

- Yes
- No
- NR

---

## 28. Africa/Non-Africa Collaboration

`Africa_International_Collaboration`

Values:

- Yes
- No
- NR

Code Yes when the author team contains at least one Africa-based institution and at least one institution outside Africa.

---

## 29. Local Institutional Participation

`Local_Institutional_Coauthor`

Values:

- Yes
- No
- NR

Code Yes when at least one author is affiliated with an institution located in an African country serving as a substantive empirical setting for the study.

For multi-country research, document the relationship carefully.

---

# PART V — GEOGRAPHY OF EVIDENCE

## 30. African Empirical Context

`Africa_Empirical_Context`

Values:

- Yes
- No

Code Yes when African populations, organizations, communities, institutions, countries, or observations provide substantive empirical evidence.

---

## 31. Study Country

`Study_Country`

Record every African country substantively represented in the empirical research.

Use a relational table or delimited values for multi-country studies.

Do not code countries mentioned only incidentally.

---

## 32. Study Region

`Study_Region`

Use standardized regional categories from the AISO Geography Dictionary.

---

## 33. Multi-Country Study

`Multi_Country_Study`

Values:

- Yes
- No

---

## 34. Africa Analytical Role

`Africa_Analytical_Role`

Values:

**1 — Included but pooled**

African observations substantively contribute to the analysis but are pooled within a broader sample.

**2 — Explicitly analyzed**

African observations or contexts receive identifiable analysis.

**3 — Central**

African contexts constitute a central empirical or theoretical component.

Records with an incidental role should have been excluded during screening.

---

## 35. Comparative Component

`Africa_Comparative_Component`

Values:

- Yes
- No

Code Yes when African and non-African settings are explicitly compared.

---

## 36. Unit of Observation

`Unit_of_Observation`

Examples:

- Individual
- Household
- Organization
- Team
- Community
- Platform
- Transaction
- Government Agency
- Health Facility
- Country
- Publication
- Digital Trace
- Other

Multiple values may be used when appropriate.

---

## 37. Research Setting

`Research_Setting`

Examples:

- Urban
- Rural
- Mixed
- National
- Organizational
- Community
- Online
- Platform-mediated
- Other
- NR

Do not infer rurality or urbanity from country alone.

---

# PART VI — GEOGRAPHY OF KNOWLEDGE PRODUCTION

## 38. Africa-Based Author Present

`Africa_Based_Author`

Values:

- Yes
- No
- NR

---

## 39. Number of Africa-Based Authors

`Africa_Based_Author_Count`

Integer where affiliation data permit.

---

## 40. Number of Africa-Based Institutions

`Africa_Based_Institution_Count`

Integer.

---

## 41. Knowledge Production Countries

`Knowledge_Production_Countries`

Countries represented by author institutional affiliations.

These countries must remain analytically distinct from study countries.

---

## 42. Knowledge Production Configuration

`Knowledge_Production_Configuration`

Preliminary values:

- Africa Only
- Africa + Non-Africa
- Non-Africa Only
- Unclear

---

# PART VII — TECHNOLOGY

## 43. Technology Present

`Technology_Present`

The primary digital or information technology examined in the publication.

---

## 44. Technology Category

`Technology_Category`

Preliminary controlled vocabulary:

- Information Systems
- Information and Communication Technologies
- Mobile Technologies
- Mobile Money
- Financial Technology
- Digital Payments
- E-Commerce
- Digital Platforms
- Social Media
- E-Government
- Digital Government
- Digital Identity
- Health Information Systems
- Digital Health
- Enterprise Systems
- Artificial Intelligence
- Data Analytics
- Cloud Computing
- Digital Infrastructure
- Cybersecurity
- Knowledge Management Systems
- Agricultural Information Systems
- Digital Labor Platforms
- Other

Multiple categories may be assigned when substantively necessary.

---

## 45. Named Technology or Platform

`Named_Technology`

Examples might include a particular platform, system, service, application, or infrastructure.

Record only when explicitly identified.

---

# PART VIII — PHENOMENON

## 46. Primary Phenomenon

`Primary_Phenomenon`

Describe the central IS phenomenon investigated.

This field should initially permit inductive coding.

Examples may include:

- technology adoption;
- digital financial inclusion;
- digital entrepreneurship;
- platform work;
- information-system implementation;
- digital government transformation;
- technology-enabled corruption reduction;
- digital health implementation;
- social media use;
- ICT-enabled development.

---

## 47. Secondary Phenomena

`Secondary_Phenomena`

Record additional substantive phenomena where useful.

---

## 48. Phenomenon Category

`Phenomenon_Category`

A controlled vocabulary should be developed inductively from pilot coding rather than fully imposed in advance.

---

## 49. African Digital Phenomenon

`Africa_Digital_Phenomenon`

Values:

- Yes
- No
- Uncertain

Code Yes when the publication investigates a digital phenomenon whose empirical manifestation in an African context is substantively central to the research.

This variable does not imply that the phenomenon is unique to Africa.

---

# PART IX — METHODOLOGY

## 50. Research Approach

`Research_Approach`

Values may include:

- Quantitative
- Qualitative
- Mixed Methods
- Conceptual
- Review
- Computational
- Design Science
- Other

Multiple categories may be used where justified.

---

## 51. Research Design

`Research_Design`

Examples:

- Survey
- Case Study
- Multiple Case Study
- Experiment
- Field Experiment
- Interview Study
- Ethnography
- Observation
- Archival Study
- Panel Study
- Cross-Sectional Study
- Longitudinal Study
- Bibliometric Study
- Systematic Review
- Conceptual Analysis
- Design and Evaluation
- Other

---

## 52. Data Source

`Data_Source`

Examples:

- Survey
- Interview
- Focus Group
- Administrative Data
- Platform Data
- Transaction Data
- Digital Trace
- Documents
- Archival Data
- Observation
- Experiment
- Secondary Dataset
- Literature
- Other

---

## 53. Sample Size

`Sample_Size`

Record where meaningful and reported.

Do not force a sample-size representation onto conceptual or qualitative designs for which a single numeric sample is inappropriate.

---

## 54. Longitudinal

`Longitudinal`

Values:

- Yes
- No
- NR

---

# PART X — LANGUAGE

## 55. Research Language

`Research_Language`

Language or languages used in data collection or empirical materials where reported.

---

## 56. Publication Language

`Publication_Language`

Language in which the scholarly publication is written.

---

## 57. African Language Used

`African_Language_Used`

Values:

- Yes
- No
- NR

When Yes, record the specific language separately.

---

## 58. African Languages

`African_Languages`

Record named languages used in data collection, interaction, analysis, or substantive empirical material.

Do not infer language from country.

---

# PART XI — THEORY METADATA

## 59. Explicit Theory Present

`Explicit_Theory_Present`

Values:

- Yes
- No
- Uncertain

Code Yes when the publication explicitly invokes a named theory, theoretical framework, theoretical perspective, or clearly articulated theoretical explanation.

---

## 60. Named Theory

`Named_Theory`

Record the theory or theories explicitly used.

Examples:

- Technology Acceptance Model
- Unified Theory of Acceptance and Use of Technology
- Institutional Theory
- Structuration Theory
- Capability Approach
- Actor-Network Theory
- Resource-Based View

Do not infer theories that authors do not invoke.

---

## 61. Theory Role

`Theory_Role`

This variable captures what the publication does with theory.

### T0 — No Explicit Theory

No identifiable theory or theoretical framework plays a substantive role.

### T1 — Background / Reference

Theory is discussed or cited but does not substantially organize the empirical analysis or theoretical contribution.

### T2 — Applied / Tested

An existing theory is used to explain, organize, predict, or test the focal phenomenon without substantial modification to the theory.

### T3 — Extended

The publication adds constructs, relationships, boundary conditions, mechanisms, or conceptual modifications to an existing theory.

### T4 — Challenged / Revised

The findings identify substantive limitations in an existing theoretical explanation and motivate revision, qualification, or reconsideration.

### T5 — New Theoretical Framework / Explanation

The publication develops a substantially new theoretical framework, model, mechanism, conceptual explanation, or theoretical account.

Coding should be based on the publication's actual contribution rather than rhetorical claims alone.

---

## 62. Theory Role Evidence

`Theory_Role_Evidence`

Record a concise explanation of why the Theory Role was assigned.

Where possible, record page number or section.

---

## 63. Theory Evidence Page

`Theory_Evidence_Page`

Page or pages containing the strongest evidence supporting the theoretical coding.

---

# PART XII — GEOGRAPHY OF THEORIZATION

## 64. African Context Theory Role

`African_Context_Theory_Role`

This variable captures how the African empirical or contextual setting participates in theorization.

### A0 — Not Applicable

The publication does not provide a basis for assessing an African-context theoretical role.

### A1 — Site of Application

An existing theory is applied or tested in an African context, but the context does not materially alter the theoretical explanation.

### A2 — Contextual Qualification

The African context reveals boundary conditions, contextual contingencies, moderators, or qualifications affecting an existing theoretical explanation.

### A3 — Mechanism Discovery

The African empirical context contributes to identifying a mechanism, process, relationship, or explanatory logic that is not merely imported from the prior theory.

### A4 — Theory Generation

African phenomena or contextual conditions materially contribute to generating new constructs, frameworks, mechanisms, propositions, or theoretical explanations.

The coder must identify evidence linking the theoretical contribution to the African empirical or contextual setting.

---

## 65. African Context Theory Evidence

`African_Context_Theory_Evidence`

Provide a concise justification for the assigned A0–A4 code.

---

## 66. African Context Theory Evidence Page

`African_Context_Theory_Evidence_Page`

Record page or section.

---

## 67. Context Necessary for Contribution

`Context_Necessary_For_Contribution`

Pilot variable.

Values:

- Yes
- No
- Uncertain

Question:

> Would the central theoretical contribution remain essentially unchanged if the African context were replaced with a generic empirical setting?

Code cautiously.

This variable is exploratory and should not enter substantive analysis until reliability has been established.

---

# PART XIII — CONSTRUCTS AND MECHANISMS

## 68. New Construct Introduced

`New_Construct_Introduced`

Values:

- Yes
- No
- Uncertain

---

## 69. New Construct Name

`New_Construct_Name`

Record the construct using the authors' terminology.

---

## 70. Construct Definition

`Construct_Definition`

Record or closely paraphrase the authors' definition.

Direct quotations should be clearly marked and handled according to applicable copyright restrictions.

---

## 71. Construct Origin Context

`Construct_Origin_Context`

Describe the empirical or conceptual context from which the construct emerges.

---

## 72. New Mechanism Proposed

`New_Mechanism_Proposed`

Values:

- Yes
- No
- Uncertain

---

## 73. Mechanism Description

`Mechanism_Description`

Concise description of the mechanism.

---

## 74. Boundary Condition Proposed

`Boundary_Condition_Proposed`

Values:

- Yes
- No
- Uncertain

---

## 75. Boundary Condition Description

`Boundary_Condition_Description`

Record the proposed condition and relevant theoretical relationship.

---

# PART XIV — CONTEXTUAL FEATURES

## 76. Contextual Features

`Contextual_Features`

Record contextual characteristics that authors explicitly identify as relevant to the phenomenon or explanation.

Potential examples include:

- institutional arrangements;
- infrastructure constraints;
- linguistic diversity;
- informal economic structures;
- community relationships;
- kinship structures;
- regulatory environments;
- resource constraints;
- trust arrangements;
- social norms;
- political structures;
- historical conditions.

These categories should be developed inductively.

Do not impose stereotypical contextual attributes on a country or population.

---

## 77. Contextual Feature Evidence

`Contextual_Feature_Evidence`

Record the textual or analytical basis for the contextual feature coding.

---

# PART XV — CONTRIBUTION

## 78. Claimed Contribution Type

`Claimed_Contribution_Type`

Preliminary categories:

- Empirical
- Theoretical
- Methodological
- Design/Artifact
- Practical
- Policy
- Review/Synthesis
- Multiple

This variable represents authors' stated contribution.

---

## 79. AISO-Assessed Theoretical Contribution

`AISO_Theoretical_Contribution`

Values:

- None Identified
- Theory Application
- Theory Extension
- Theory Challenge/Revision
- New Theoretical Explanation
- Uncertain

This should correspond closely to `Theory_Role` and primarily exists as a human-readable analytical field during pilot development.

It may be removed if redundant.

---

# PART XVI — OPEN SCIENCE AND DATA

## 80. Data Availability Statement

`Data_Availability_Statement`

Values:

- Yes
- No
- NR

---

## 81. Data Publicly Available

`Data_Publicly_Available`

Values:

- Yes
- No
- Partial
- Unclear

---

## 82. Code Publicly Available

`Code_Publicly_Available`

Values:

- Yes
- No
- Partial
- Unclear

---

## 83. Repository URL

`Repository_URL`

Record where publicly reported.

---

# PART XVII — PHENOMENA REGISTRY

## 84. Phenomena Registry Candidate

`Phenomena_Registry_Candidate`

Values:

- Yes
- No
- Uncertain

A publication may become a candidate when it documents a substantively important digital phenomenon that should be represented in the AISO Digital Phenomena Registry.

---

## 85. Phenomenon Registry Name

`Phenomenon_Registry_Name`

Provisional standardized name.

---

## 86. Phenomenon Geography

`Phenomenon_Geography`

Country or countries in which the phenomenon is documented.

---

# PART XVIII — THEORY REGISTRY

## 87. Theory Registry Candidate

`Theory_Registry_Candidate`

Values:

- Yes
- No
- Uncertain

A publication may become a candidate when it introduces or substantially develops a construct, mechanism, theoretical framework, or contextual theoretical explanation emerging from African evidence.

---

## 88. Theory Registry Contribution

`Theory_Registry_Contribution`

Describe the construct, mechanism, framework, or theoretical contribution.

---

## 89. Theory Registry Origin Evidence

`Theory_Registry_Origin_Evidence`

Document how the African phenomenon or context contributed to the theoretical development.

---

# PART XIX — CODER INFORMATION

## 90. Coder ID

`Coder_ID`

Unique identifier for the coder.

---

## 91. Coding Date

`Coding_Date`

ISO format recommended:

`YYYY-MM-DD`

---

## 92. Coding Confidence

`Coding_Confidence`

Values:

- High
- Moderate
- Low

This field reflects coder confidence, not publication quality.

---

## 93. Coding Notes

`Coding_Notes`

Free-text notes concerning ambiguity, unusual cases, or adjudication needs.

---

## 94. Requires Adjudication

`Requires_Adjudication`

Values:

- Yes
- No

---

## 95. Adjudication Decision

`Adjudication_Decision`

Record final decision where applicable.

---

## 96. Adjudication Notes

`Adjudication_Notes`

Document rationale for the final decision.

---

# PART XX — PILOT RELIABILITY

## 97. Pilot Sample

Approximately 50 eligible publications should initially be independently coded by at least two coders.

The pilot should maximize variation in:

- publication year;
- country;
- venue type;
- methodology;
- technology;
- phenomenon;
- author institutional geography;
- theoretical orientation.

---

## 98. Reliability Priorities

Reliability analysis should focus particularly on interpretive variables including:

- `Technology_Category`
- `Primary_Phenomenon`
- `Phenomenon_Category`
- `Theory_Role`
- `African_Context_Theory_Role`
- `New_Construct_Introduced`
- `New_Mechanism_Proposed`
- `Boundary_Condition_Proposed`
- `Contextual_Features`
- `Theory_Registry_Candidate`

Raw agreement should be reported.

Appropriate chance-corrected agreement statistics should also be considered depending on variable structure and prevalence.

---

## 99. Decision Log

Recurring coding disagreements should be documented in a separate AISO Decision Log.

The Decision Log should record:

- issue;
- example;
- competing interpretations;
- adjudicated decision;
- rationale;
- affected codebook provision;
- date;
- resulting codebook revision where applicable.

The purpose is to transform difficult cases into explicit methodological rules.

---

# PART XXI — MINIMUM DATASET FOR AISO v0.1

## 100. Minimum Fields

The first operational dataset does not need all variables in this codebook.

The minimum AISO v0.1 publication dataset should include:

1. `AISO_Record_ID`
2. `AISO_Work_ID`
3. `Title`
4. `Publication_Year`
5. `Publication_Type`
6. `Venue`
7. `DOI`
8. `Study_Country`
9. `Study_Region`
10. `Africa_Empirical_Context`
11. `Africa_Analytical_Role`
12. `Africa_Based_Author`
13. `Africa_Based_First_Author`
14. `Africa_Based_Corresponding_Author`
15. `Africa_International_Collaboration`
16. `Knowledge_Production_Countries`
17. `Technology_Category`
18. `Primary_Phenomenon`
19. `Research_Approach`
20. `Research_Design`
21. `Research_Language`
22. `Explicit_Theory_Present`
23. `Named_Theory`
24. `Theory_Role`
25. `African_Context_Theory_Role`
26. `Coder_ID`
27. `Coding_Confidence`

More advanced variables can be added after pilot validation.

---

# PART XXII — FOUNDATIONAL ANALYTICAL DISTINCTION

## 101. Geography of Evidence

Answers:

> Where does the empirical phenomenon occur?

This should be established from the research design and empirical setting.

---

## 102. Geography of Knowledge Production

Answers:

> Where are the institutions producing the scholarly knowledge located?

This should be established from publication-time author affiliations.

---

## 103. Geography of Theorization

Answers:

> From which contextual phenomena do theoretical constructs, mechanisms, boundary conditions, or explanations emerge?

This requires substantive interpretation of the theoretical contribution.

It cannot be determined merely from:

- author affiliation;
- study country;
- journal;
- theory name;
- abstract keywords.

---

## 104. Why the Distinction Matters

Consider two hypothetical studies.

**Study A**

- empirical evidence from Kenya;
- authors based outside Africa;
- existing theory tested without modification.

Its geography of evidence includes Kenya, while its theoretical contribution may remain primarily an application of existing theory.

**Study B**

- empirical evidence from Nigeria;
- collaborative authorship;
- a local digital phenomenon reveals a mechanism that changes the theoretical explanation.

Its geography of evidence includes Nigeria, and the Nigerian empirical context may also participate in the geography of theorization.

Both publications concern Africa.

They do not occupy the same epistemic position.

AISO is designed to make that distinction observable.

---

# PART XXIII — VERSIONING

## 105. Version Status

This document is **AISO Metadata and Coding Codebook v0.1**.

It is a pilot instrument.

The categories in this document should not be treated as finalized before empirical pilot testing.

Changes arising from coding disagreements, construct ambiguity, empirical distributions, or methodological review must be recorded in:

`docs/CHANGELOG.md`

Following pilot validation, a revised Codebook v1.0 should be released.

---

# PART XXIV — GUIDING PRINCIPLE

AISO should allow the evidence to determine whether African contexts primarily function as sites of data collection, sites of knowledge production, sources of contextual qualification, sources of mechanism discovery, sources of theory generation, or some combination of these roles.

The coding framework must therefore remain capable of producing findings that contradict the expectations motivating the Observatory.




