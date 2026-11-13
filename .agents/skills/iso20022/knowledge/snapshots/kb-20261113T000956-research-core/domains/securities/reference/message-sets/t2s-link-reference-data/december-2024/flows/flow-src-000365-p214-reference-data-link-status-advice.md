---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p214-reference-data-link-status-advice"
title: "Reference Data Link Status Advice"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[222]", "paragraph_id": "P222", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}]
participants: ["participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reference Data Link Status Advice", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Reference Data Link Status Advice

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

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

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.

Reusable flows: [creation](flow-src-000365-p120-link-creation-process.md), [modification](flow-src-000365-p122-link-modification-process.md).
