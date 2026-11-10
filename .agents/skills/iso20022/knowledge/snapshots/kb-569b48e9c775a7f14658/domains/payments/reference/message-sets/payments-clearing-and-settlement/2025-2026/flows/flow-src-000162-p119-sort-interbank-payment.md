---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p119-sort-interbank-payment"
title: "Sort Interbank Payment"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[119]", "paragraph_id": "P119", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-account-servicer", "participant-src-000162-creditor", "participant-src-000162-debtor", "participant-src-000162-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Sort Interbank Payment", "Financial Institution", "Account Servicer", "Creditor", "Debtor", "Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Sort Interbank Payment

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Clearing agent determines the next clearing agent or creditor/debtor for the payment.  The clearing agent identification is done by the previous party or selected by the current agent (tables). The last clearing agent is determined by the creditor/debtor's account servicer.

Evidence: [T14](../documents/src-000162/tables/tbl-0014.md), source row 2.

### Trigger

The payment must be instructed to the next party .

Evidence: [T14](../documents/src-000162/tables/tbl-0014.md), source row 3.

### Pre-conditions

Payment is accepted.

Evidence: [T14](../documents/src-000162/tables/tbl-0014.md), source row 4.

### Post-conditions

Next clearing agent is determined.

Evidence: [T14](../documents/src-000162/tables/tbl-0014.md), source row 5.

### Role

Financial institution

Evidence: [T14](../documents/src-000162/tables/tbl-0014.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T14](../documents/src-000162/tables/tbl-0014.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T14, all rows](../documents/src-000162/tables/tbl-0014.md)

| Item | Description |
| --- | --- |
| Definition | Clearing agent determines the next clearing agent or creditor/debtor for the payment.  The clearing agent identification is done by the previous party or selected by the current agent (tables). The last clearing agent is determined by the creditor/debtor's account servicer. |
| Trigger | The payment must be instructed to the next party . |
| Pre-conditions | Payment is accepted. |
| Post-conditions | Next clearing agent is determined. |
| Role | Financial institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
