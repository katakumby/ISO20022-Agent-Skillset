---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p155-status-reporting"
title: "Status Reporting"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[19]", "paragraph_id": null, "table_id": "T19"}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: []
message_families: ["seev.033"]
search_terms: ["Status Reporting", "Account Servicer", "Account Owner", "seev.033"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Status Reporting

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of:
providing the reason a corporate action event has not been completed by the announced payment dates
advising the status, or a change in status, of a corporate action-related transaction previously instructed by, or executed on behalf of, the account owner
advising the account owner of the processing status of a corporate action event 
acknowledging or rejecting a corporate action instruction or acknowledging or rejecting a request to cancel an outstanding instruction
providing the account owner with statements of its instructed and uninstructed balances for all its corporate action events for a safekeeping account

Evidence: [T19](../documents/src-000079/tables/tbl-0019.md), source row 2.

### Trigger

Execution of the various steps of the lifecycle of a corporate action event, when an account owner has sent an election instruction or requested the cancellation of a previously sent election instruction

Evidence: [T19](../documents/src-000079/tables/tbl-0019.md), source row 3.

### Pre-conditions

Corporate action event must be on-going or an election instruction has been received by the account servicer

Evidence: [T19](../documents/src-000079/tables/tbl-0019.md), source row 4.

### Post-conditions

None

Evidence: [T19](../documents/src-000079/tables/tbl-0019.md), source row 5.

### Role

Account servicer.

Evidence: [T19](../documents/src-000079/tables/tbl-0019.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T19](../documents/src-000079/tables/tbl-0019.md).

## Messages and alternative paths

Source-supported message family mentions: `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessProcess Description.

Related source activity diagram: [Instruction reporting activities](../diagrams/activities/fig-0016.md).
