---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Deletion Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Deletion Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P248** Rejection Scenario

**P249** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P251** Party Deletion Request (reda.031)Modification processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTED

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

**P252** Party Deletion Request

**P253** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a Party. 

**P254** Party Status Advice

**P255** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P256** Rejected  
The instruction did not pass validation, some reasons could be:

**P257** the mandatory information is not present or incorrect;

**P258** the Instructing Party does not have the right to delete Party;

**P259** the instruction has already been received and is being processed;

**P260** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status  


**P261** Queued  
The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P263** Rejected after dequeuing  
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P264**  the mandatory information is not present or incorrect;

**P265**  the Party cannot be deleted;

**P266**  the Instructing Party does not have the right to delete Party;

**P267**  the instruction has already been received and is being processed;

**P268** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P269**   


