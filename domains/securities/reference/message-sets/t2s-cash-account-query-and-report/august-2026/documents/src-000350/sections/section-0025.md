---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"]
content_origin: "source-transcription"
---

# Account Query List/Report Scenario

Source: [src-000350](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Account Query List/Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P148** Account Query List/Report Scenario

[fig-0010 - original figure evidence](../diagrams/fig-0010.md)

**P152** Account Query List

**P153** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P155** Account List Report - Negative Scenario

**P156** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P158** Account List Report

**P159** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

