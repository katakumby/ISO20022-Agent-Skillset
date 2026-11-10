---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p132-link-modification-process"
title: "Link Modification Process"
source_locations: [{"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[134]", "paragraph_id": "P134", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[135]", "paragraph_id": "P135", "table_id": null}]
participants: ["participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Link Modification Process", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Link Modification Process

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000365/diagrams/fig-0008.md). Mermaid reconstruction and visual review are pending.

Source table [T12](../documents/src-000365/tables/tbl-0012.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a link. | Instructing Party |
| Validate: | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the link, the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after a specific event. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: Description of BusinessActivities / Link Reference Data / Link Modification Process.

Canonical reusable flow: [Link Modification Process](flow-src-000365-p122-link-modification-process.md).
