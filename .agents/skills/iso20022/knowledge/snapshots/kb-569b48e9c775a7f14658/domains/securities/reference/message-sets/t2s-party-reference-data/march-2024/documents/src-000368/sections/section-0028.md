---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Party Creation Request (reda.014)Creation processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTEDRejection Scenario"]
content_origin: "source-transcription"
---

# Party Creation Request (reda.014)Creation processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTEDRejection Scenario

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Party Creation Request (reda.014)Creation processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTEDRejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P167** Party Creation Request (reda.014)Creation processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTEDRejection Scenario

[fig-0013 - original figure evidence](../diagrams/fig-0013.md)

**P168** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P178** Party Creation Request:

**P179** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new party.  This instruction contains information that clearly identify the party. 

**P180** Party Status Advice:

**P181** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P182** Rejected:  
The instruction did not pass validation, some reasons could be:

**P183** the mandatory information is not present or incorrect,

**P184** the instruction is not a new occurrence,

**P185** the instruction has already been received and is being processed. 

**P186** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.  


**P187** Queued:  
The Executing/Servicing Party might inform the Instructing party that the processing of the Create Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P189** Rejected after dequeuing:  
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P190** the mandatory information is not present or incorrect,

**P191** the instruction is not a new occurrence,

**P192** the instruction has already been received and is being processed 

**P194** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

