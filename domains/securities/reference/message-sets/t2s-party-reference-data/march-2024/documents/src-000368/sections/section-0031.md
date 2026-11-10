---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000368](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P210** Rejection Scenario

**P211** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P213** Party Modification Request (reda.022)Modification processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTED

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

**P214** Party Maintenance Request

**P215** The Instruction Party sends an instruction to the Executing/Servicing Party to modify reference data for a party. 

**P216** Party Status Advice

**P217** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P218** Rejected:  
The instruction did not pass validation, some reasons could be:

**P219** the mandatory information is not present or incorrect,

**P220** the data cannot be updated,

**P221** the party cannot be blocked/unblocked,

**P222** the Instructing Party does not have the right to (un)block party

**P223** the instruction has already been received and is being processed 

**P224** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.  


**P225** Queued:  
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P227** Rejected after dequeuing:  
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P228** the mandatory information is not present or incorrect,

**P229** the data cannot be updated,

**P230** the party cannot be blocked,

**P231** the Instructing Party does not have the right to block/unblock Party

**P232** the instruction has already been received and is being processed 

**P234** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P235**   


