---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P232** Rejection Scenario

**P233** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P235** Securities Account Modification Request (reda.023)Modification processSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020): REJECTED

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

**P236** Securities Account Maintenance Request

**P237** The Instruction Party sends an instruction to the Executing/Servicing Party to modify reference data for a securities account. 

**P238** Securities Account Status Advice

**P239** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P241** Rejected

**P242** The instruction did not pass validation, some reasons could be:

**P243** the mandatory information is not present or incorrect,

**P244** the data cannot be updated,

**P245** the instruction has already been received and is being processed 

**P246** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status

**P247** .

**P248** Queued

**P249** The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P251** Rejected

**P252** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P253** the mandatory information is not present or incorrect,

**P254** the data cannot be updated,

**P255** the Instructing Party does not have the right to block/unblock security account,

**P256** the instruction has already been received and is being processed. 

**P257** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

