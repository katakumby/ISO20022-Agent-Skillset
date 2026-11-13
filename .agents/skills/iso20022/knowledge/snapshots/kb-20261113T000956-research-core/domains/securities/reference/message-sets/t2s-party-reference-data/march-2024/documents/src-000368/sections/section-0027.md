---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P155** Confirmation Scenario

**P156** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P158** Creation ProcessParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): COMPLETEDParty Creation Request (reda.014)

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

**P159** Party Creation Request

**P160** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new party.  This instruction contains information that clearly identify the party. 

**P161** Party Status Advice

**P162** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P163** Queued  
  
The Executing/Servicing Party might inform the Instructing party that the processing of  Party Creation Request  has been delayed. In case of e.g. a night-time cycle is running.  

**P165** Completed  
  
The Executing/Servicing Party informs the Instructing party that the Party Creation Request  has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Party that has been processed.

