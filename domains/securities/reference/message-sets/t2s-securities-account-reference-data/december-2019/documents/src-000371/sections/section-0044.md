---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Query/Response Process", "Securities Account Query/Securities Account Report Scenario"]
content_origin: "source-transcription"
---

# Securities Account Query/Securities Account Report Scenario

Source: [src-000371](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Query/Response Process / Securities Account Query/Securities Account Report Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P301** Securities Account Query/Securities Account Report Scenario

**P303** Securities Account Query (reda.019)Query/Report ProcessSecurities Account Report (reda.021): ERRORSecurities Account Report (reda.021)

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

**P305** Securities Account Query

**P306** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P307** Securities Account Report 

**P308** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P309** Securities Account Report 

**P310** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

