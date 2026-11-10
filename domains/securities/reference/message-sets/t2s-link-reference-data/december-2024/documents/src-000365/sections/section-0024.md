---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000365](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P153** Rejection Scenario

**P154** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

[fig-0010 - original figure evidence](../diagrams/fig-0010.md)

**P158** Reference Data Link Creation Request:

**P159** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new Reference Data Link. This instruction contains information that clearly identify the party. 

**P160** Reference Data Link Status Advice:

**P161** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P162** Rejected:  
The instruction did not pass validation; some reasons could be:

**P163** the mandatory information is not present or incorrect,

**P164** the instruction is not a new occurrence,

**P165** the instruction has already been received and is being processed. 

**P166** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.  


**P167** Queued:  
The Executing/Servicing Party might inform the Instructing party that the processing of the Reference Data Link instruction has been delayed.  

**P169** Rejected after dequeuing:  
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P170** the mandatory information is not present or incorrect,

**P171** the instruction is not a new occurrence,

**P172** the instruction has already been received and is being processed. 

**P174** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

