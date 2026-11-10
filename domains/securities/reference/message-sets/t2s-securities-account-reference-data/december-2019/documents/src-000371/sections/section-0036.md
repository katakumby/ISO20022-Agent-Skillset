---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000371](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P190** Rejection Scenario

**P191** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P192** Creation ProcessSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020): REJECTEDCOMPLETEDSecurities Account Creation Request (reda.018)

[fig-0013 - original figure evidence](../diagrams/fig-0013.md)

**P193** Securities Account Creation Request

**P194** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new securities account. This instruction contains information that clearly identify the securities account. 

**P195** Securities Account Status Advice

**P196** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P197** Rejected

**P198** The instruction did not pass validation, some reasons could be:

**P199** the mandatory information is not present or incorrect,

**P200** the instruction is not a new occurrence,

**P201** the instruction has already been received and is being processed. 

**P202** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P204** Queued  
The Executing/Servicing Party might inform the Instructing party that the processing of the Create Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P206** Rejected

**P207** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P208** the mandatory information is not present or incorrect,

**P209** the instruction is not a new occurrence,

**P210** the instruction has already been received and is being processed 

**P211** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

