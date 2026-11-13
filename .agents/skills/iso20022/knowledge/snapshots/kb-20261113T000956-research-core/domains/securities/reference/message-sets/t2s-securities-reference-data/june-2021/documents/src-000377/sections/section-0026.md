---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P172** Confirmation Scenario

**P173** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P175** Creation ProcessSecurity Creation Status Advice (reda.008): QUEUEDSecurity Creation Status Advice (reda.008): COMPLETEDCOMPLETEDSecurity Creation Request (reda.006)Creation ProcessSecurity Creation Status Advice (reda.008): QUEUEDSecurity Creation Status Advice (reda.008): COMPLETEDCOMPLETEDSecurity Creation Request (reda.006)

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

**P176** Security Creation Request

**P177** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new security. This instruction contains information that clearly identify the security. 

**P178** Security Creation Status Advice

**P179** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P180** Queued

**P181** The Executing/Servicing Party might inform the Instructing party that the processing of Security Creation Request has been delayed. In case of e.g. a night-time cycle is running.  

**P182** Completed

**P183** The Executing/Servicing Party informs the Instructing party that the Security Creation Request has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Security that has been processed.

