---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p154-cancellation"
title: "Cancellation"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[18]", "paragraph_id": null, "table_id": "T18"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: []
message_families: ["seev.035"]
search_terms: ["Cancellation", "Account Servicer", "Account Owner", "seev.035"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---







# Cancellation

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Process by which the account servicer can advise the cancellation of a previously announced corporate action event or advise the cancellation of a previously sent corporate action movement preliminary advice, or by which the account owner can request the cancellation of an instruction.

Evidence: [T18](../documents/src-000079/tables/tbl-0018.md), source row 2.

### Trigger

Previous communication is identified as inaccurate or void

Evidence: [T18](../documents/src-000079/tables/tbl-0018.md), source row 3.

### Pre-conditions

Previous communication must have taken place

Evidence: [T18](../documents/src-000079/tables/tbl-0018.md), source row 4.

### Post-conditions

None

Evidence: [T18](../documents/src-000079/tables/tbl-0018.md), source row 5.

### Role

Account servicer / account owner

Evidence: [T18](../documents/src-000079/tables/tbl-0018.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T18](../documents/src-000079/tables/tbl-0018.md).

## Messages and alternative paths

Source-supported message family mentions: `seev.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessProcess Description.

Source activity diagram: [Corporate action instruction cancellation activities](../diagrams/overview/fig-0003.md). The conditional use of parallel bars remains ambiguous (issue-000020).

Related source activity diagram: [Movement preliminary advice cancellation activities](../diagrams/activities/fig-0018.md).
