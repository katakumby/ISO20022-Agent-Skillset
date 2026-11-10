---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p115-collateral-reference-data-deletion"
title: "Collateral Reference Data deletion"
source_locations: [{"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data deletion"], "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "table_id": null}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data deletion"], "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "table_id": null}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data deletion"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data deletion"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}]
participants: ["participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party"]
message_mapping_evidence: []
message_ids: ["reda.028.001.01", "reda.075.001.01", "reda.077.001.01"]
message_families: ["reda.075", "reda.077", "reda.028"]
search_terms: ["Collateral Reference Data deletion", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
issue_ids: ["issue-000043"]
disputed_message_ids: ["reda.044.001.01"]
---







# Collateral Reference Data deletion

Source context: T2S CollateralManagementReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000353/diagrams/fig-0008.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T12](../documents/src-000353/tables/tbl-0012.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instruct the Executing/Servicing Party to delete: <br>• an Auto-Collateralisation Eligibility Link<br>• a Close Link | Instructing Party  |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the creation of the object, the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after a specific event. | Executing/Servicing Party  |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: Description of BusinessActivities / Collateral Management Reference Data / Collateral Reference Data deletion.

## Curated source flow

The identical artwork is used for creation at P112 and deletion at P116. Instruction crosses to Validate. An accepted instruction goes to Process and returns Status <<Accepted>>; a rejected instruction goes to Report and returns Status <<Rejected>>. A merge diamond leads to Monitor, then the second Accepted decision ends on Yes or follows a dashed No loop back to Instruction. T11/T12 add a substantive QUEUED case absent from the artwork: if valid but timing does not permit processing, QUEUED is sent and the instruction is resubmitted to validation after a specific event. This narrative participant responsibility is preserved without inventing a diagram branch. T12 still says time permits creation in its deletion validation row; issue-000043 records that wording.

[Complete source diagram](../diagrams/curated/fig-0007.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md).

Exact confirmed bindings for this process: [reda.028.001.01](../../../../messages/reda.028.001.01/index.md), [reda.075.001.01](../../../../messages/reda.075.001.01/index.md), [reda.077.001.01](../../../../messages/reda.077.001.01/index.md). Source response family044 in deletion sequences remains disputed under issue-000043.
