---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p146-eligibility-entitlement-notification"
title: "Eligibility / Entitlement Notification"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Eligibility / Entitlement Notification", "Account Servicer", "Account Owner"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source trigger and precondition conflict concerning withdrawn events; issue-000061 remains unresolved."]
manual_curated: true
issue_ids: ["issue-000061"]
rendered_file_pages: [14]
---



# Eligibility / Entitlement Notification

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of providing the account owner with the balance of holdings eligible for a corporate action event and the entitlement to outturn resources.

Evidence: [T12](../documents/src-000079/tables/tbl-0012.md), source row 2.

### Trigger

new corporate action event is announced
details of a previously announced corporate action have been changed
corporate action details were incorrect
new corporate action details are known
corporate action event has been withdrawn

Evidence: [T12](../documents/src-000079/tables/tbl-0012.md), source row 3.

### Pre-conditions

account owner has eligible holdings or pending transactions in the corporate action event’s underlying security
corporate action is not withdrawn

Evidence: [T12](../documents/src-000079/tables/tbl-0012.md), source row 4.

### Post-conditions

Account owner is informed of its eligible balance / entitlement

Evidence: [T12](../documents/src-000079/tables/tbl-0012.md), source row 5.

### Role

Account servicer

Evidence: [T12](../documents/src-000079/tables/tbl-0012.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T12](../documents/src-000079/tables/tbl-0012.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- T12 source text and complete Word14 visually compared2026-11-09. Source withdrawal conditions remain inconsistent (issue-000061).
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessProcess Description.

## Withdrawal-condition conflict

T12 row3 includes a withdrawn event as a trigger, while row4 requires the corporate action not to be withdrawn. Both statements are preserved from Word file/printed page14; no exception is inferred. See [issue-000061](../../../../../../../tracking/issues.md#issue-000061).
