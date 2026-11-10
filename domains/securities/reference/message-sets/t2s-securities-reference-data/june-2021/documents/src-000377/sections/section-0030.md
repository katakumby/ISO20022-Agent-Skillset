---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P231** Rejection Scenario

**P232** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P234** Security Maintenance Request (reda.007)Modification processSecurity Maintenance Status Advice (reda.029): QUEUEDSecurity Maintenance Status Advice (reda.029): REJECTEDSecurity Maintenance Request (reda.007)Modification processSecurity Maintenance Status Advice (reda.029): QUEUEDSecurity Maintenance Status Advice (reda.029): REJECTED

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

**P235** Security Maintenance Request

**P236** The Instructing Party sends an instruction to the Executing/Servicing Party to modify reference data for a Security. 

**P237** Security Maintenance Status Advice

**P238** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P239** Rejected

**P240** The instruction did not pass validation, some reasons could be:

**P241** the mandatory information is not present or incorrect,

**P242** the data cannot be updated,

**P243** the instruction has already been received and is being processed. 

**P244** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P245** Queued

**P246** The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P247** Rejected

**P248** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P249** the mandatory information is not present or incorrect,

**P250** the data cannot be updated,

**P251** the instruction has already been received and is being processed. 

**P252** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

