---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Party Audit Trail Query/ Party Audit Trail Report Scenario"]
content_origin: "source-transcription"
---

# Party Audit Trail Query/ Party Audit Trail Report Scenario

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Party Audit Trail Query/ Party Audit Trail Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P282** Party Audit Trail Query/ Party Audit Trail Report Scenario

**P283** Party Audit Trail Query (reda.042)Query/Response ProcessParty Audit Trail Report (reda.043): ERRORParty Audit Trail Report (reda.043)

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P285** Party Audit Trail Query

**P286** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific party.

**P287** Party Audit Trail Report

**P288** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P289** Party Audit Trail Report

**P290** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

**P291**   


