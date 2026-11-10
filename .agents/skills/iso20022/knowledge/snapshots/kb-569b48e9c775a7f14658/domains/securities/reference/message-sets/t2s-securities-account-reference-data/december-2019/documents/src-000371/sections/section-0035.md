---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P178** Confirmation Scenario

**P179** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P181** Creation ProcessSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020): COMPLETEDCOMPLETEDSecurities Account Creation Request (reda.018)

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

**P182** Securities Account Creation Request

**P183** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new securities account. This instruction contains information that clearly identify the securities account. 

**P184** Securities Account Status Advice

**P185** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P187** Queued  
The Executing/Servicing Party might inform the Instructing party that the processing of Securities Account Creation Request has been delayed. In case of e.g. a night-time cycle is running.

**P189** Completed  
The Executing/Servicing Party informs the Instructing party that the Securities Account Creation Request has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Securities Account that has been processed.

