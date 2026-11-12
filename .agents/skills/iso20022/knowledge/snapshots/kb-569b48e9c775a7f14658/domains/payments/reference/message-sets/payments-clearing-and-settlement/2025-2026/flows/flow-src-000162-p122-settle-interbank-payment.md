---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p122-settle-interbank-payment"
title: "Settle Interbank Payment"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-settlement-agent", "participant-src-000162-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Settle Interbank Payment", "Financial Institution", "Settlement Agent", "Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Settle Interbank Payment

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Settlement agent performs the transfer of cash between the debit party and the credit party.

Evidence: [T17](../documents/src-000162/tables/tbl-0017.md), source row 2.

### Trigger

Payment execution date in the payment is reached.

Evidence: [T17](../documents/src-000162/tables/tbl-0017.md), source row 3.

### Pre-conditions

Instructed payment is executable (all information is there to process the payment and the payment validity has been checked) and the settlement agent is identified by the clearing agent.

Evidence: [T17](../documents/src-000162/tables/tbl-0017.md), source row 4.

### Post-conditions

Transfer of ownership is performed between the debit party and credit party.

Evidence: [T17](../documents/src-000162/tables/tbl-0017.md), source row 5.

### Role

Financial institution

Evidence: [T17](../documents/src-000162/tables/tbl-0017.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Settlement Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T17](../documents/src-000162/tables/tbl-0017.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T17, all rows](../documents/src-000162/tables/tbl-0017.md)

| Item | Description |
| --- | --- |
| Definition | Settlement agent performs the transfer of cash between the debit party and the credit party. |
| Trigger | Payment execution date in the payment is reached. |
| Pre-conditions | Instructed payment is executable (all information is there to process the payment and the payment validity has been checked) and the settlement agent is identified by the clearing agent. |
| Post-conditions | Transfer of ownership is performed between the debit party and credit party. |
| Role | Financial institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
