---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p150-movement-preliminary-advice-final-entitlement-process"
title: "Movement Preliminary Advice / Final Entitlement process"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Movement Preliminary Advice / Final Entitlement process", "Account Servicer", "Account Owner"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Movement Preliminary Advice / Final Entitlement process

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process by which the account servicer pre-advises the account owner of upcoming postings to be made to its cash and/or securities account(s) as a result of a corporate action.

Evidence: [T15](../documents/src-000079/tables/tbl-0015.md), source row 2.

### Trigger

Account servicer has the required information about the postings to be made

Evidence: [T15](../documents/src-000079/tables/tbl-0015.md), source row 3.

### Pre-conditions

Postings of cash / securities have to be done the account owner’s account(s).

Evidence: [T15](../documents/src-000079/tables/tbl-0015.md), source row 4.

### Post-conditions

None

Evidence: [T15](../documents/src-000079/tables/tbl-0015.md), source row 5.

### Role

Account servicer

Evidence: [T15](../documents/src-000079/tables/tbl-0015.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P151** This process also includes the pre-advice of movement reversal (sent in order to give the account owner time to fund the reversal in its account). The process also includes the update/replacement of information previously provided.

Source table [T15](../documents/src-000079/tables/tbl-0015.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessProcess Description.

Related source activity diagram: [Movement preliminary advice activities](../diagrams/activities/fig-0017.md).
