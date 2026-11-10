---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Party Query/ Party Report Scenario"]
content_origin: "source-transcription"
---

# Party Query/ Party Report Scenario

Source: [src-000368](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Party Query/ Party Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P271** Party Query/ Party Report Scenario

**P273** Party Query (reda.015)Party Query/Report ProcessParty Report (reda.017): ERRORParty Report (reda.017)

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

**P275** Party query

**P276** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P277** Party Report 

**P278** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P279** Party Report 

**P280** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

**P281**   


