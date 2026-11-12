---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Rejection Scenario"]
content_origin: "source-transcription"
---

# Rejection Scenario

Source: [src-000365](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Rejection Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P197** Rejection Scenario

**P198** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P200** Security CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): REJECTEDSecurity CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): REJECTED

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

**P212** Reference Data Link Maintenance Request

**P213** The Instructing Party sends an instruction to the Executing/Servicing Party to modify reference data for a link. 

**P214** Reference Data Link Status Advice

**P215** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:  


**P216** Rejected:  
The instruction did not pass validation; some reasons could be:

**P217** the mandatory information is not present or incorrect,

**P218** the data cannot be updated,

**P219** the instruction has already been received and is being processed. 

**P220** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.  


**P221** Queued:  
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Reference Data Link instruction has been delayed.

**P223** Rejected:  
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P224** the mandatory information is not present or incorrect,

**P225** the data cannot be updated,

**P226** the instruction has already been received and is being processed. 

**P227** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

