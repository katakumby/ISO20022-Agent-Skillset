---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p115-asses-interbank-payment-risk"
title: "Asses Interbank Payment Risk"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Asses Interbank Payment Risk", "Financial Institution", "Settlement Agent"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Asses Interbank Payment Risk

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Settlement agent undertakes the necessary risk checks in order to process the payment further, for example, embargo, sufficient credit, cover received, system limits.

Evidence: [T10](../documents/src-000162/tables/tbl-0010.md), source row 2.

### Trigger

Receipt of the payment order.

Evidence: [T10](../documents/src-000162/tables/tbl-0010.md), source row 3.

### Pre-conditions

The settlement agent has received the payment order.

Evidence: [T10](../documents/src-000162/tables/tbl-0010.md), source row 4.

### Post-conditions

Payment has been accepted or rejected.

Evidence: [T10](../documents/src-000162/tables/tbl-0010.md), source row 5.

### Role

Financial Institution

Evidence: [T10](../documents/src-000162/tables/tbl-0010.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Settlement Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T10](../documents/src-000162/tables/tbl-0010.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T10, all rows](../documents/src-000162/tables/tbl-0010.md)

| Item | Description |
| --- | --- |
| Definition | Settlement agent undertakes the necessary risk checks in order to process the payment further, for example, embargo, sufficient credit, cover received, system limits. |
| Trigger | Receipt of the payment order. |
| Pre-conditions | The settlement agent has received the payment order. |
| Post-conditions | Payment has been accepted or rejected. |
| Role | Financial Institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../evidence/archived/fa67d8621c20bf64aa62336b.md). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
