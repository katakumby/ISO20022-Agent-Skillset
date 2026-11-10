---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Deletion Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P254** Confirmation Scenario

**P255** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P257** Security Deletion Request (reda.013)Deletion processSecurity Deletion Status Advice (reda.030): QUEUEDSecurity Deletion Status Advice (reda.030):  COMPLETEDSecurity Deletion Request (reda.013)Deletion processSecurity Deletion Status Advice (reda.030): QUEUEDSecurity Deletion Status Advice (reda.030):  COMPLETED

[fig-0016 - original figure evidence](../diagrams/fig-0016.md)

**P258** Security Deletion Request

**P259** The Instructing Party sends an instruction to the Executing/Servicing Party to delete a security. This instruction contains information that uniquely identifies the security and it is used when a security is no longer active.

**P260** Security Deletion Status Advice

**P261** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P262** Queued

**P263** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P264** Completed

**P265** The Executing/Servicing Party informs the Instructing party that the Delete Securiy instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the security that has been processed.

**P269**   


