---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p128-initiate-collection-of-direct-debit"
title: "Initiate Collection of Direct Debit"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:tbl[18]", "paragraph_id": null, "table_id": "T18"}]
participants: ["participant-src-000173-initiating-party", "participant-src-000173-creditor", "participant-src-000173-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Initiate Collection of Direct Debit", "Initiating Party", "Creditor", "Debtor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Initiate Collection of Direct Debit

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The creditor will create the first/one-off instruction and send it to its bank. This first/one-off will differ from subsequent (recurrent) transactions:
The first/one-off instruction may be sent a number of days (as defined in the operating rules) in advance of the settlement date.
In addition to the regular debiting information, which may include the unique mandate reference and the creditor identification, the first/one-off debit instruction may also include information that identifies it as a first under a new mandate or as a one-off transaction

Evidence: [T18](../documents/src-000173/tables/tbl-0018.md), source row 2.

### Trigger

Initiation of the collection.

Evidence: [T18](../documents/src-000173/tables/tbl-0018.md), source row 3.

### Pre-conditions

Consensus to use as payment method and debtor authorisation to be debited by the creditor, notification of the debtor.

Evidence: [T18](../documents/src-000173/tables/tbl-0018.md), source row 4.

### Post-conditions

Initiated collection of direct debit.

Evidence: [T18](../documents/src-000173/tables/tbl-0018.md), source row 5.

### Role

Initiating Party

Evidence: [T18](../documents/src-000173/tables/tbl-0018.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Initiating Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T18](../documents/src-000173/tables/tbl-0018.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Direct Debit.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T18, all rows](../documents/src-000173/tables/tbl-0018.md)

| Item | Description |
| --- | --- |
| Definition | The creditor will create the first/one-off instruction and send it to its bank. This first/one-off will differ from subsequent (recurrent) transactions:<br>The first/one-off instruction may be sent a number of days (as defined in the operating rules) in advance of the settlement date.<br>In addition to the regular debiting information, which may include the unique mandate reference and the creditor identification, the first/one-off debit instruction may also include information that identifies it as a first under a new mandate or as a one-off transaction |
| Trigger | Initiation of the collection. |
| Pre-conditions | Consensus to use as payment method and debtor authorisation to be debited by the creditor, notification of the debtor. |
| Post-conditions | Initiated collection of direct debit. |
| Role | Initiating Party |


[Parent process and participant placement](flow-src-000173-p125-customer-to-bank-direct-debit.md)

<!-- /INITIATION-ACTIVITY -->
