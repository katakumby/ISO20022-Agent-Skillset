---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Securities Audit Trail Query and Report Scenario"]
content_origin: "source-transcription"
---

# Securities Audit Trail Query and Report Scenario

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Securities Audit Trail Query and Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P303** Securities Audit Trail Query and Report Scenario

**P304** Securities Audit Trail Query (reda.033)Query/Response ProcessSecurities Audit Trail Report (reda.034): ERRORSecurities Audit Trail Report (reda.034)Securities Audit Trail Query (reda.033)Query/Response ProcessSecurities Audit Trail Report (reda.034): ERRORSecurities Audit Trail Report (reda.034)

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P305** Securities Audit Trail Query

**P306** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific security.

**P307** Securities Audit Trail Report

**P308** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P309** Securities Audit Trail Report

**P310** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

