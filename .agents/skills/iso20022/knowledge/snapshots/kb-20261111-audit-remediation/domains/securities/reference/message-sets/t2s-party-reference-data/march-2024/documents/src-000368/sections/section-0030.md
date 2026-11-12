---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P197** Confirmation Scenario

**P198** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P200** Party Modification Request (reda.022)Modification processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): COMPLETED

[fig-0014 - original figure evidence](../diagrams/fig-0014.md)

**P201** Party Maintenance Request

**P202** The Instruction Party sends an instruction to the Executing/Servicing Party to modify data for a Party. This instruction contains information that uniquely identify the Party. 

**P203** In this instruction, the Instruction Party can also send to the Executing/Servicing Party the request to block/unblock a Party for settlement. 

**P204** In this case, this instruction contains details of the restriction like the restriction type and timeframe.

**P205** Party Status Advice

**P206** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P207** Queued:  
The Executing/Servicing Party might informs the Instructing party that the processing of the Modify Party instruction has been delayed. In case of e.g. a night-time cycle is running.    


**P208** Completed:  
The Executing/Servicing Party informs the Instructing party that the Modify Party instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Party that has been processed.

**P209**   


