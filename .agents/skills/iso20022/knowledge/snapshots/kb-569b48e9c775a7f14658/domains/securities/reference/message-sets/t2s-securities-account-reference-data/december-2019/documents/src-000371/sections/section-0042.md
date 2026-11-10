---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Deletion Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Deletion Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P274** Rejection Scenario

**P275** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P276** Securities Account Deletion Request (reda.032)Deletion processSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020):  REJECTED

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

**P277** Securities Account Deletion Request

**P278** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a securities account. 

**P279** Securities Account Status Advice

**P280** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P282** Rejected

**P283** The instruction did not pass validation, some reasons could be:

**P284** the mandatory information is not present or incorrect,

**P285** the Instructing Party does not have the right to delete securities account,

**P286** the instruction has already been received and is being processed. 

**P287** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P289** Queued

**P290** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P292** Rejected

**P293** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P294** the mandatory information is not present or incorrect,

**P295** the securities account cannot be deleted,

**P296** the Instructing Party does not have the right to delete securities account,

**P297** the instruction has already been received and is being processed 

**P298** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

