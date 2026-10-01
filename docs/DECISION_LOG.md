# AISO Decision Log

This document records methodological decisions arising during development and pilot testing of the African Information Systems Observatory.

---

## D001 — OpenAlex Generic Search Is Not Suitable for Controlled Geographic Discovery

**Date:** 2026-10-01  
**Stage:** Pilot Discovery  
**Status:** Adopted

### Issue

AISO requires geographic discovery procedures that identify publications containing substantive geographic signals while remaining reproducible and interpretable.

During pilot testing, the OpenAlex website returned two MIS Quarterly publications for a search of `Kenya` restricted to 2000–2026.

An API implementation using the OpenAlex generic `search=Kenya` parameter returned five publications under the same source and temporal restrictions.

### Investigation

The additional API records included publications such as:

- *Service Innovation in the Digital Age: Key Contributions and Future Directions*
- *Critical Realism in Information Systems Research*
- *Contextual Explanation: Alternative Approaches and Persistent Challenges*

Inspection showed that at least some additional records did not contain `Kenya` in their titles, indexed abstracts, or displayed keywords.

### Decision

The OpenAlex generic `search=` parameter will **not** be used as the primary geographic discovery mechanism for the AISO corpus.

AISO geographic discovery should use a retrieval procedure whose searchable fields and matching rules can be explicitly specified and documented.

### Rationale

A generic relevance search may incorporate indexed metadata or search signals that are not transparent enough for AISO's geographic inclusion workflow.

Using such retrieval as the primary discovery mechanism would make it difficult to explain why particular records were retrieved and could introduce uncontrolled false positives.

### Implication

The AISO OpenAlex discovery implementation will be revised before country-scale searching begins.

No 54-country automated discovery will be conducted using the current generic `search=` implementation.

The five-record Kenya API result is retained as pilot evidence and should not be treated as the AISO Kenya corpus.
