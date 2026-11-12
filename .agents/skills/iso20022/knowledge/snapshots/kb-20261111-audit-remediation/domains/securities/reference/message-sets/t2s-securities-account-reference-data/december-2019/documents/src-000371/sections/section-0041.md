---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Deletion Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P259** Confirmation Scenario

**P260** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P262** Securities Account Deletion Request (reda.032)Deletion processSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020):  COMPLETED

[fig-0016 - original figure evidence](../diagrams/fig-0016.md)

**P263** Securities Account Deletion Request

**P264** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a securities account. This instruction contains information that uniquely identifies the party and it is used when a party is no longer active.

**P265** Securities Account Status Advice

**P266** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P268** Queued:

**P269** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P271** Completed:

**P272** The Executing/Servicing Party informs the Instructing party that the Delete Securities Account instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the securities account that has been processed.

