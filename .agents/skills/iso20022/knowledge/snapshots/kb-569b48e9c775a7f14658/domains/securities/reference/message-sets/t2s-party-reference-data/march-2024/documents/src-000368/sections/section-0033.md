---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Deletion Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P237** Confirmation Scenario

**P238** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party:

**P240** Party Deletion Request (reda.031)Modification processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): COMPLETED

[fig-0016 - original figure evidence](../diagrams/fig-0016.md)

**P241** Party Deletion Request

**P242** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a Party. This instruction contains information that uniquely identifies the party and it is used when a party is no longer active.

**P243** Party Status Advice

**P244** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P245** Queued  
The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Party instruction has been delayed. In case of e.g. a night-time cycle is running.    


**P246** Completed  
The Executing/Servicing Party informs the Instructing party that the Delete Party instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the party that has been processed.

**P247**   


