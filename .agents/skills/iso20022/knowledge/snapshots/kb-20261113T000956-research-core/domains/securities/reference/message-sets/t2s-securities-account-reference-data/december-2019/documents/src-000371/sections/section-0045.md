---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario"]
content_origin: "source-transcription"
---

# Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P311** Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario

**P312** Securities Account Audit Trail Query (reda.036)Query/Response ProcessSecurities Account Audit Trail Report (reda.037): ERRORSecurities Account Audit Trail Report (reda.037)

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P314** Securities Account Audit Trail Query

**P315** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific securities account.

**P316** Securities Account Audit Trail Report

**P317** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P318** Securities Account Audit Trail Report

**P319** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

