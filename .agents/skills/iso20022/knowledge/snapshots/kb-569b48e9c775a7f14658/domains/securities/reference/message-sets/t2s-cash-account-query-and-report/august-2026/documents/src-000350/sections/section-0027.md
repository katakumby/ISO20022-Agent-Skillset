---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"]
content_origin: "source-transcription"
---

# Cash Account Audit Trail Query/ Report Scenario

Source: [src-000350](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Cash Account Audit Trail Query/ Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P166** Cash Account Audit Trail Query/ Report Scenario

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

**P168** Cash Account Audit Trail Query

**P170** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific cash account.

**P172** Cash Account Audit Trail Report - Negative scenario

**P173** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P174**  

**P175** Cash Account  Audit Trail Report

**P176** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

