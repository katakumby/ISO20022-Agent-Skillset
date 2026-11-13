---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p117-authorise-interbank-payment"
title: "Authorise Interbank Payment"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}]
participants: ["participant-src-000162-payment-clearing-agent", "participant-src-000162-financial-institution"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Authorise Interbank Payment", "Payment Clearing Agent", "Financial Institution"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Authorise Interbank Payment

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Authorisation of a payment order by the payment clearing agent. This is an extension of the sub-process of the 'Accept Interbank Payment' process.
An authorisation may be implicit if the system where the payment is generated has been approved to generate payments, as the preceding procedures are deemed satisfactory secure. The system will then generate a digital signature without manual intervention.
An authorisation may be explicit, if procedures require human approval.

Evidence: [T12](../documents/src-000162/tables/tbl-0012.md), source row 2.

### Trigger

A payment order has been created.

Evidence: [T12](../documents/src-000162/tables/tbl-0012.md), source row 3.

### Pre-conditions

Accept payment process is completed and waits for authorisation if required by the payment clearing agent.


Evidence: [T12](../documents/src-000162/tables/tbl-0012.md), source row 4.

### Post-conditions

Payment order is authorised.

Evidence: [T12](../documents/src-000162/tables/tbl-0012.md), source row 5.

### Role

Financial Institution

Evidence: [T12](../documents/src-000162/tables/tbl-0012.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Payment Clearing Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T12](../documents/src-000162/tables/tbl-0012.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T12, all rows](../documents/src-000162/tables/tbl-0012.md)

| Item | Description |
| --- | --- |
| Definition | Authorisation of a payment order by the payment clearing agent. This is an extension of the sub-process of the 'Accept Interbank Payment' process.<br>An authorisation may be implicit if the system where the payment is generated has been approved to generate payments, as the preceding procedures are deemed satisfactory secure. The system will then generate a digital signature without manual intervention.<br>An authorisation may be explicit, if procedures require human approval. |
| Trigger | A payment order has been created. |
| Pre-conditions | Accept payment process is completed and waits for authorisation if required by the payment clearing agent.<br> |
| Post-conditions | Payment order is authorised. |
| Role | Financial Institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../evidence/archived/fa67d8621c20bf64aa62336b.md). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
