---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p116-order-customer-to-bank-payment"
title: "Order Customer-to-bank payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}]
participants: ["participant-src-000173-financial-institution", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-debtor-agent", "participant-src-000173-party"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["pain.001"]
search_terms: ["Order Customer-to-bank payment", "Financial Institution", "Forwarding Agent", "Initiating Party", "Debtor Agent", "Party", "pain.001"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Order Customer-to-bank payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

An initiating party orders to financial institution (debtor agent or forwarding agent) a payment related instruction. This may refer to an underlying business transaction (for example, an invoice).

Evidence: [T9](../documents/src-000173/tables/tbl-0009.md), source row 2.

### Trigger

Decision has been made to make a payment (either by a person or a system).

Evidence: [T9](../documents/src-000173/tables/tbl-0009.md), source row 3.

### Pre-conditions

The required (identifying) information is available to make a payment.

Evidence: [T9](../documents/src-000173/tables/tbl-0009.md), source row 4.

### Post-conditions

The initiation party sends a CustomerCreditTransferInitiation message to the forwarding agent or debtor agent. 

Evidence: [T9](../documents/src-000173/tables/tbl-0009.md), source row 5.

### Role

Initiating party

Evidence: [T9](../documents/src-000173/tables/tbl-0009.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Initiating Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T9](../documents/src-000173/tables/tbl-0009.md).

## Messages and alternative paths

Source-supported message family mentions: `pain.001`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T9, all rows](../documents/src-000173/tables/tbl-0009.md)

| Item | Description |
| --- | --- |
| Definition | An initiating party orders to financial institution (debtor agent or forwarding agent) a payment related instruction. This may refer to an underlying business transaction (for example, an invoice). |
| Trigger | Decision has been made to make a payment (either by a person or a system). |
| Pre-conditions | The required (identifying) information is available to make a payment. |
| Post-conditions | The initiation party sends a CustomerCreditTransferInitiation message to the forwarding agent or debtor agent.  |
| Role | Initiating party |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
