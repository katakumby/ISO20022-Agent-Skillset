---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p122-link-modification-process"
title: "Link Modification Process"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000365", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[134]", "paragraph_id": "P134", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:p[135]", "paragraph_id": "P135", "table_id": null}]
participants: ["participant-src-000365-authorised-party", "participant-src-000365-authorised-user", "participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party", "participant-src-000365-investor-csd"]
message_mapping_evidence: []
message_ids: ["reda.046.001.01", "reda.047.001.01", "reda.050.001.01", "reda.051.001.01"]
message_families: ["reda.046", "reda.050", "reda.047", "reda.051"]
search_terms: ["Link Modification Process", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---









# Link Modification Process

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

When an Instructing Party is in charge of the modification of a specific Reference Data Link already supported by the Executing/Servicing Party system, the Instructing Party asks the Executing/Servicing Party to modify the Reference Data Link in the Executing/Servicing Party system. 

Evidence: [T9](../documents/src-000365/tables/tbl-0009.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends a Reference Data
Link Modification Request message.

Evidence: [T9](../documents/src-000365/tables/tbl-0009.md), source row 3.

### Pre-conditions

The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. An attribute of the Reference Data Link has changed which requires a modification of the Reference Data Link in the Executing/Servicing Party system.

Evidence: [T9](../documents/src-000365/tables/tbl-0009.md), source row 4.

### Post-conditions

The acknowledgement of the processing of the modification request.

Evidence: [T9](../documents/src-000365/tables/tbl-0009.md), source row 5.

### Role

Instructing Party

Evidence: [T9](../documents/src-000365/tables/tbl-0009.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T9](../documents/src-000365/tables/tbl-0009.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessProcess Description.

## Curated source flow

A single start branches to Link Creation and Link Modification, which converge at an end point. The source does not draw an exclusive-choice diamond or a parallel bar, so neither execution constraint is inferred. P110 says the overview is not exhaustive. T8/T9 supply distinct known-party/privilege preconditions and acknowledgment postconditions for creation versus modification.

[Complete source diagram](../diagrams/curated/fig-0002.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md), [authorised user](../../../../../../../shared/reference/participants/participant-src-000365-authorised-user.md), [authorised party](../../../../../../../shared/reference/participants/participant-src-000365-authorised-party.md).

## Curated source flow

Instruction passes from Instructing Party to Executing Party Validate. Accepted leads to Process and an Accepted status; No leads to Report and a Rejected status. Both return through a merge to Monitor. The instructing-side Accepted decision ends on Yes and follows the dashed No loop back to Instruction. The table separately defines QUEUED when a valid instruction cannot yet be processed: it is resubmitted to validation after a specific event. No QUEUED branch is drawn in this activity, and that narrative path is retained explicitly. T12 checks existence and whether the data can be updated; successful timely update produces COMPLETED.

[Complete source diagram](../diagrams/curated/fig-0007.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md), [authorised user](../../../../../../../shared/reference/participants/participant-src-000365-authorised-user.md), [authorised party](../../../../../../../shared/reference/participants/participant-src-000365-authorised-party.md), [investor csd](../../../../../../../shared/reference/participants/participant-src-000365-investor-csd.md).

## Ordered source activities

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


Source scenario alternatives: [confirmation](flow-src-000365-p177-confirmation-scenario.md), [rejection](flow-src-000365-p197-rejection-scenario.md).

[Complete link business conditions and lifecycle statuses](../link-business-rules.md).
