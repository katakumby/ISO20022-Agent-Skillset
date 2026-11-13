---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p123-clear-customer-to-bank-payment"
title: "Clear customer-to-bank payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[16]", "paragraph_id": null, "table_id": "T16"}]
participants: ["participant-src-000173-debtor-agent", "participant-src-000173-creditor", "participant-src-000173-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Clear customer-to-bank payment", "Debtor Agent", "Creditor", "Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Clear customer-to-bank payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The agent remits the payment and prepares the information for the next agent in the interbank chain by sorting it and releasing it for onward interbank payment processing.

Evidence: [T16](../documents/src-000173/tables/tbl-0016.md), source row 2.

### Trigger

Execution date.

Evidence: [T16](../documents/src-000173/tables/tbl-0016.md), source row 3.

### Pre-conditions

The payment is accepted, the next credit party is not the creditor and the next clearing agent is determined.

Evidence: [T16](../documents/src-000173/tables/tbl-0016.md), source row 4.

### Post-conditions

Onward interbank payment processing.

Evidence: [T16](../documents/src-000173/tables/tbl-0016.md), source row 5.

### Role

Debtor agent

Evidence: [T16](../documents/src-000173/tables/tbl-0016.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T16](../documents/src-000173/tables/tbl-0016.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T16, all rows](../documents/src-000173/tables/tbl-0016.md)

| Item | Description |
| --- | --- |
| Definition | The agent remits the payment and prepares the information for the next agent in the interbank chain by sorting it and releasing it for onward interbank payment processing. |
| Trigger | Execution date. |
| Pre-conditions | The payment is accepted, the next credit party is not the creditor and the next clearing agent is determined. |
| Post-conditions | Onward interbank payment processing. |
| Role | Debtor agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
