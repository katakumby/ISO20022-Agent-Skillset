---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Deletion Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Deletion Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P270** Rejection Scenario

**P271** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P273** Security Deletion Request (reda.013)Deletion processSecurity Deletion Status Advice (reda.030): QUEUEDSecurity Deletion Status Advice (reda.030):  REJECTEDSecurity Deletion Request (reda.013)Deletion processSecurity Deletion Status Advice (reda.030): QUEUEDSecurity Deletion Status Advice (reda.030):  REJECTED

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

**P274** Security Deletion Request

**P275** The Instructing Party sends an instruction to the Executing/Servicing Party to delete a security. 

**P276** Security Status Advice

**P277** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P278** Rejected

**P279** The instruction did not pass validation, some reasons could be:

**P280** the mandatory information is not present or incorrect,

**P281** the Instructing Party does not have the right to delete security,

**P282** the instruction has already been received and is being processed. 

**P283** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P284** Queued

**P285** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P286** Rejected

**P287** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P288** the mandatory information is not present or incorrect,

**P289** the security cannot be deleted,

**P290** the Instructing Party does not have the right to delete security,

**P291** the instruction has already been received and is being processed 

**P292** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

