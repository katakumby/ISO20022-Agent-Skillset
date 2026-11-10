---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p120-link-creation-process"
title: "Link Creation Process"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000365", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}]
participants: ["participant-src-000365-authorised-party", "participant-src-000365-authorised-user", "participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party", "participant-src-000365-investor-csd", "participant-src-000365-issuer-csd", "participant-src-000365-technical-issuer"]
message_mapping_evidence: []
message_ids: ["reda.045.001.01", "reda.047.001.01", "reda.049.001.01", "reda.051.001.01"]
message_families: ["reda.045", "reda.049", "reda.047", "reda.051"]
search_terms: ["Link Creation Process", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---









# Link Creation Process

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

When an Instructing Party would like to create a specific Reference Data Link that is not yet supported by the Executing/Servicing Party, an Instructing Party asks the Executing/Servicing Party to create the Reference Data Link in its system.

Evidence: [T8](../documents/src-000365/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends a Reference Data Link Creation Request message.

Evidence: [T8](../documents/src-000365/tables/tbl-0008.md), source row 3.

### Pre-conditions

The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the Reference Data Links coverage of the Executing/Servicing Party. The Instructing Party needs this Reference Data Link to be set-up at the Executing /Servicing Party to perform its activities.

Evidence: [T8](../documents/src-000365/tables/tbl-0008.md), source row 4.

### Post-conditions

The acknowledgement of the processing of the creation request.

Evidence: [T8](../documents/src-000365/tables/tbl-0008.md), source row 5.

### Role

Instructing Party

Evidence: [T8](../documents/src-000365/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000365/tables/tbl-0008.md).

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

Instruction passes from Instructing Party to Executing Party Validate. Accepted leads to Process and an Accepted status; No leads to Report and a Rejected status. Both return through a merge to Monitor. The instructing-side Accepted decision ends on Yes and follows the dashed No loop back to Instruction. The table separately defines QUEUED when a valid instruction cannot yet be processed: it is resubmitted to validation after a specific event. No QUEUED branch is drawn in this activity, and that narrative path is retained explicitly. T11 checks novelty and whether the instruction is already handled; successful timely creation produces COMPLETED.

[Complete source diagram](../diagrams/curated/fig-0007.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md), [authorised user](../../../../../../../shared/reference/participants/participant-src-000365-authorised-user.md), [authorised party](../../../../../../../shared/reference/participants/participant-src-000365-authorised-party.md), [issuer csd](../../../../../../../shared/reference/participants/participant-src-000365-issuer-csd.md), [investor csd](../../../../../../../shared/reference/participants/participant-src-000365-investor-csd.md), [technical issuer](../../../../../../../shared/reference/participants/participant-src-000365-technical-issuer.md).

## Ordered source activities

## Ordered activities and source narrative

Source diagram evidence: [fig-0007](../documents/src-000365/diagrams/fig-0007.md). Mermaid reconstruction and visual review are pending.

Source table [T11](../documents/src-000365/tables/tbl-0011.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party instructs the Executing/Servicing Party to create a link. | Instructing Party |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the creation of the link, the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after a specific event. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


Source scenario alternatives: [confirmation](flow-src-000365-p139-confirmation-scenario.md), [rejection](flow-src-000365-p153-rejection-scenario.md).

[Complete link business conditions and lifecycle statuses](../link-business-rules.md).
