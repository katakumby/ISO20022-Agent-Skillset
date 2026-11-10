---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p145-event-notification"
title: "Event Notification"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner", "participant-src-000079-sub-custodian", "participant-src-000079-csd-icsd"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Event Notification", "Account Servicer", "Account Owner", "Sub-Custodian", "CSD / ICSD"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Event Notification

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of notifying the account owner of an upcoming corporate action. It provides corporate action details including options (if any). The notification is validated by the account servicer who then passes on the information to the account owner. A notification can also provide notification of updates, remind or advise of the withdrawal of a corporate action that was announced previously.

Evidence: [T11](../documents/src-000079/tables/tbl-0011.md), source row 2.

### Trigger

new corporate action event is announced
details of a previously announced corporate action have been changed 
corporate action details were incorrect 
new corporate action details are known 
corporate action event has been withdrawn

Evidence: [T11](../documents/src-000079/tables/tbl-0011.md), source row 3.

### Pre-conditions

Account servicer has been notified of a corporate action event by an external source, for example, sub-custodian, CSD, ICSD, market data vendor and financial publication

Evidence: [T11](../documents/src-000079/tables/tbl-0011.md), source row 4.

### Post-conditions

Account owner is notified of the corporate action event

Evidence: [T11](../documents/src-000079/tables/tbl-0011.md), source row 5.

### Role

Account servicer

Evidence: [T11](../documents/src-000079/tables/tbl-0011.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Sub-Custodian | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-sub-custodian.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CSD / ICSD | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-csd-icsd.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T11](../documents/src-000079/tables/tbl-0011.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessProcess Description.

Related source activity diagram: [Event withdrawal activities](../diagrams/activities/fig-0019.md).
