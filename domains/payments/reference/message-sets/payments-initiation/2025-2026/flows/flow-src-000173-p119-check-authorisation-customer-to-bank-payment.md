---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p119-check-authorisation-customer-to-bank-payment"
title: "Check Authorisation Customer-to-Bank Payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[119]", "paragraph_id": "P119", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}]
participants: ["participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-debtor-agent", "participant-src-000173-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Check Authorisation Customer-to-Bank Payment", "Forwarding Agent", "Initiating Party", "Debtor Agent", "Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Check Authorisation Customer-to-Bank Payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The forwarding or debtor agent checks if initiating party is allowed or entitled to do so as included in the authorisation specifications of the customer profile and the type of payment is in scope. (Authorisation procedures are in some countries required for legal reasons.)
(The result of these authorisation procedures can, depending on the authorisation scenario defined, be included in the payment initiation order (for example, one or more signatures included in the payment initiation order), or can result in a dissociated authorisation message, sent by another party than the initiating party, which is referring to the payment initiation message.)

Evidence: [T12](../documents/src-000173/tables/tbl-0012.md), source row 2.

### Trigger

Established authorisation procedures.

Evidence: [T12](../documents/src-000173/tables/tbl-0012.md), source row 3.

### Pre-conditions



Evidence: [T12](../documents/src-000173/tables/tbl-0012.md), source row 4.

### Post-conditions

The payment will be accepted or rejected for validation and, when applicable, risk assessment.

Evidence: [T12](../documents/src-000173/tables/tbl-0012.md), source row 5.

### Role

Debtor agent or forwarding agent

Evidence: [T12](../documents/src-000173/tables/tbl-0012.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Initiating Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T12](../documents/src-000173/tables/tbl-0012.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T12, all rows](../documents/src-000173/tables/tbl-0012.md)

| Item | Description |
| --- | --- |
| Definition | The forwarding or debtor agent checks if initiating party is allowed or entitled to do so as included in the authorisation specifications of the customer profile and the type of payment is in scope. (Authorisation procedures are in some countries required for legal reasons.)<br>(The result of these authorisation procedures can, depending on the authorisation scenario defined, be included in the payment initiation order (for example, one or more signatures included in the payment initiation order), or can result in a dissociated authorisation message, sent by another party than the initiating party, which is referring to the payment initiation message.) |
| Trigger | Established authorisation procedures. |
| Pre-conditions |  |
| Post-conditions | The payment will be accepted or rejected for validation and, when applicable, risk assessment. |
| Role | Debtor agent or forwarding agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
