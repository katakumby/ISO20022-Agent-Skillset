---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P185** Rejection Scenario

**P186** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P187** Creation ProcessSecurity Creation Status Advice (reda.008): QUEUEDSecurity Creation Status Advice (reda.008): REJECTEDCOMPLETEDSecurity Creation Request (reda.006)Creation ProcessSecurity Creation Status Advice (reda.008): QUEUEDSecurity Creation Status Advice (reda.008): REJECTEDCOMPLETEDSecurity Creation Request (reda.006)

[fig-0013 - original figure evidence](../diagrams/fig-0013.md)

**P189** Security Creation Request

**P190** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new security. This instruction contains information that clearly identify the security. 

**P191** Security Creation Status Advice

**P192** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P193** Rejected

**P194** The instruction did not pass validation, some reasons could be:

**P195** the mandatory information is not present or incorrect,

**P196** the instruction is not a new occurrence,

**P197** the instruction has already been received and is being processed. 

**P198** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P199** Queued

**P200** The Executing/Servicing Party might inform the Instructing party that the processing of the Create Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P201** Rejected

**P202** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P203** the mandatory information is not present or incorrect,

**P204** the instruction is not a new occurrence,

**P205** the instruction has already been received and is being processed 

**P206** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

