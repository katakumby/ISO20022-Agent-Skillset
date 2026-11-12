---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000365](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P177** Confirmation Scenario

**P178** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P179** Security CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): COMPLETEDSecurity CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): COMPLETED

[fig-0011 - original figure evidence](../diagrams/fig-0011.md)

**P190** Reference Data Link Maintenance Request

**P191** The Instructing Party sends an instruction to the Executing/Servicing Party to modify data for a Reference Data Link. This instruction contains information that uniquely identify the Reference Data Link. 

**P192** Reference Data Link Status Advice

**P193** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P194** Queued:  
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Reference Data Link instruction has been delayed.  


**P195** Completed:  
The Executing/Servicing Party informs the Instructing party that the Modify Reference Data Link instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Reference Data Link that has been processed.

**P196**   


