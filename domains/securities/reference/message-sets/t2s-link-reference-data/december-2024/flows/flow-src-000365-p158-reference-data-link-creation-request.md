---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p158-reference-data-link-creation-request"
title: "Reference Data Link Creation Request:"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}]
participants: ["participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reference Data Link Creation Request:", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Reference Data Link Creation Request:

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P159** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new Reference Data Link. This instruction contains information that clearly identify the party. 

**P160** Reference Data Link Status Advice:

**P161** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P162** Rejected:
The instruction did not pass validation; some reasons could be:

**P163** the mandatory information is not present or incorrect,

**P164** the instruction is not a new occurrence,

**P165** the instruction has already been received and is being processed. 

**P166** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.


**P167** Queued:
The Executing/Servicing Party might inform the Instructing party that the processing of the Reference Data Link instruction has been delayed.  

**P169** Rejected after dequeuing:
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P170** the mandatory information is not present or incorrect,

**P171** the instruction is not a new occurrence,

**P172** the instruction has already been received and is being processed. 

**P174** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Rejection Scenario.

Reusable flows: [creation](flow-src-000365-p120-link-creation-process.md), [modification](flow-src-000365-p122-link-modification-process.md).
