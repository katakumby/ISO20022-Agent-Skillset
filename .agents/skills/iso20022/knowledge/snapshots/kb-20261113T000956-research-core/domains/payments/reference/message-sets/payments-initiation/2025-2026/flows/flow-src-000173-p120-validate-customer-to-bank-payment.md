---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p120-validate-customer-to-bank-payment"
title: "Validate Customer-to-Bank-payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}]
participants: ["participant-src-000173-forwarding-agent", "participant-src-000173-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Validate Customer-to-Bank-payment", "Forwarding Agent", "Debtor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Validate Customer-to-Bank-payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Syntactical check in order to process the payment further.

Evidence: [T13](../documents/src-000173/tables/tbl-0013.md), source row 2.

### Trigger

Receipt of payment order, positive authorisation check.

Evidence: [T13](../documents/src-000173/tables/tbl-0013.md), source row 3.

### Pre-conditions

The agent has received the payment order and performed the necessary. Authorisation checks. Validation procedures have been established.

Evidence: [T13](../documents/src-000173/tables/tbl-0013.md), source row 4.

### Post-conditions

The payment will be accepted for risk assessment, if necessary, or is executable.

Evidence: [T13](../documents/src-000173/tables/tbl-0013.md), source row 5.

### Role

Debtor agent or forwarding agent

Evidence: [T13](../documents/src-000173/tables/tbl-0013.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T13](../documents/src-000173/tables/tbl-0013.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T13, all rows](../documents/src-000173/tables/tbl-0013.md)

| Item | Description |
| --- | --- |
| Definition | Syntactical check in order to process the payment further. |
| Trigger | Receipt of payment order, positive authorisation check. |
| Pre-conditions | The agent has received the payment order and performed the necessary. Authorisation checks. Validation procedures have been established. |
| Post-conditions | The payment will be accepted for risk assessment, if necessary, or is executable. |
| Role | Debtor agent or forwarding agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
