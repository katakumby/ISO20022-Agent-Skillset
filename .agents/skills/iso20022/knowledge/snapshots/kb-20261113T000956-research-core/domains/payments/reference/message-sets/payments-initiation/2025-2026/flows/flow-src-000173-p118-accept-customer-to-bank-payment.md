---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p118-accept-customer-to-bank-payment"
title: "Accept Customer-to-Bank Payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}]
participants: ["participant-src-000173-debtor-agent-forwarding-agent", "participant-src-000173-creditor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Accept Customer-to-Bank Payment", "Debtor Agent / Forwarding Agent", "Creditor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Accept Customer-to-Bank Payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The payment acceptation includes the checking of the authorisation, the validation of the payment and the process risk assessment.

Evidence: [T11](../documents/src-000173/tables/tbl-0011.md), source row 2.

### Trigger

Receipt of a payment order.

Evidence: [T11](../documents/src-000173/tables/tbl-0011.md), source row 3.

### Pre-conditions

The Payment has been received

Evidence: [T11](../documents/src-000173/tables/tbl-0011.md), source row 4.

### Post-conditions

The payment order has been accepted or rejected.

Evidence: [T11](../documents/src-000173/tables/tbl-0011.md), source row 5.

### Role

Debtor agent, forwarding agent or creditor agent

Evidence: [T11](../documents/src-000173/tables/tbl-0011.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor Agent / Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T11](../documents/src-000173/tables/tbl-0011.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T11, all rows](../documents/src-000173/tables/tbl-0011.md)

| Item | Description |
| --- | --- |
| Definition | The payment acceptation includes the checking of the authorisation, the validation of the payment and the process risk assessment. |
| Trigger | Receipt of a payment order. |
| Pre-conditions | The Payment has been received |
| Post-conditions | The payment order has been accepted or rejected. |
| Role | Debtor agent, forwarding agent or creditor agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
