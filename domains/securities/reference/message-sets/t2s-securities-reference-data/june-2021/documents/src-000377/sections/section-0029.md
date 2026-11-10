---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P211** Confirmation Scenario

**P212** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P214** Security Maintenance Request (reda.007)Modification processSecurity Maintenance Status Advice (reda.029): QUEUEDSecurity Maintenance Status Advice (reda.029):  COMPLETEDSecurity Maintenance Request (reda.007)Modification processSecurity Maintenance Status Advice (reda.029): QUEUEDSecurity Maintenance Status Advice (reda.029):  COMPLETED

[fig-0014 - original figure evidence](../diagrams/fig-0014.md)

**P215** Security Maintenance Request

**P216** The Instructing Party sends an instruction to the Executing/Servicing Party to modify data for a security. This instruction contains information that uniquely identify the security. 

**P217** In this case, this instruction contains details of the restriction like the restriction type and timeframe.

**P218** Security Maintenance Status Advice

**P219** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P220** Queued

**P221** The Executing/Servicing Party might informs the Instructing party that the processing of the Modify Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P222** Completed

**P223** The Executing/Servicing Party informs the Instructing party that the Modify Security instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the security that has been processed.

