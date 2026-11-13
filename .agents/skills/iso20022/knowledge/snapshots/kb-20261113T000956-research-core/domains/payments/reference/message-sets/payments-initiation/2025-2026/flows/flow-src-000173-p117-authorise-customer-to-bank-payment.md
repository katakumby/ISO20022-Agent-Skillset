---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p117-authorise-customer-to-bank-payment"
title: "Authorise Customer-to-Bank Payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}]
participants: ["participant-src-000173-initiating-party", "participant-src-000173-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Authorise Customer-to-Bank Payment", "Initiating Party", "Debtor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Authorise Customer-to-Bank Payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The authorisation of a payment order by the initiating party. (An authorisation may be implicit if the system where the payment is generated has been approved to generate payments, as the preceding procedures are deemed satisfactory secure. The system will then generate a digital signature without manual intervention. An authorisation may be explicit, if procedures require human approval. The representation of this approval will be included in the payment order or sent to the forwarding or debtor agent as a separate message.)

Evidence: [T10](../documents/src-000173/tables/tbl-0010.md), source row 2.

### Trigger

A payment order has been created.

Evidence: [T10](../documents/src-000173/tables/tbl-0010.md), source row 3.

### Pre-conditions

The order payment process has completed and waits for authorisation.

Evidence: [T10](../documents/src-000173/tables/tbl-0010.md), source row 4.

### Post-conditions

The payment order is authorised.

Evidence: [T10](../documents/src-000173/tables/tbl-0010.md), source row 5.

### Role

Initiating party

Evidence: [T10](../documents/src-000173/tables/tbl-0010.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Initiating Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T10](../documents/src-000173/tables/tbl-0010.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T10, all rows](../documents/src-000173/tables/tbl-0010.md)

| Item | Description |
| --- | --- |
| Definition | The authorisation of a payment order by the initiating party. (An authorisation may be implicit if the system where the payment is generated has been approved to generate payments, as the preceding procedures are deemed satisfactory secure. The system will then generate a digital signature without manual intervention. An authorisation may be explicit, if procedures require human approval. The representation of this approval will be included in the payment order or sent to the forwarding or debtor agent as a separate message.) |
| Trigger | A payment order has been created. |
| Pre-conditions | The order payment process has completed and waits for authorisation. |
| Post-conditions | The payment order is authorised. |
| Role | Initiating party |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
