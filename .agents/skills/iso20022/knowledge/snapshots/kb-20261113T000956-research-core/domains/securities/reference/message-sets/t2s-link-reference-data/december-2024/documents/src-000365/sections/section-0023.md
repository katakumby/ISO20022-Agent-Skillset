---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000365](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Creation Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P139** Confirmation Scenario

**P140** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

[fig-0009 - original figure evidence](../diagrams/fig-0009.md)

**P144** Reference Data Link Creation Request

**P145** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new Reference Data Link.  This instruction contains information that clearly identify the Reference Data Link.

**P146** Reference Data Link Status Advice

**P147** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P149** Queued  
  
The Executing/Servicing Party might inform the Instructing party that the processing of the Create Reference Data Link instruction has been delayed.

**P151** Completed  
  
The Executing/Servicing Party informs the Instructing party that the Create Reference Data Link instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Reference Data Link that has been processed.

