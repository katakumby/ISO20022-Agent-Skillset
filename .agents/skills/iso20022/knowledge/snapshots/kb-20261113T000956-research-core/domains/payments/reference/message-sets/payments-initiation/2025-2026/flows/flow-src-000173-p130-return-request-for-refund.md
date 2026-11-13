---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p130-return-request-for-refund"
title: "Return/Request for Refund"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:tbl[20]", "paragraph_id": null, "table_id": "T20"}]
participants: ["participant-src-000173-creditor", "participant-src-000173-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Return/Request for Refund", "Creditor", "Debtor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000044"]
table_review: "pass"
---





# Return/Request for Refund

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Returns are individual debits that have reached the debtor’s agent and have been settled at the inter-bank level, but the debtor’s agent is then unable to make the collection for one of a number of reasons, for example, account closed, no funds, customer dead, etc. 
The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction the debtor's account is credited by his bank and the debit is returned electronically through the clearing process to the creditor’s agent.

Evidence: [T20](../documents/src-000173/tables/tbl-0020.md), source row 2.

### Trigger

Return of a / request for refund.

Evidence: [T20](../documents/src-000173/tables/tbl-0020.md), source row 3.

### Pre-conditions

Settled instruction subject for return / refund.

Evidence: [T20](../documents/src-000173/tables/tbl-0020.md), source row 4.

### Post-conditions

Settled instruction / requested refund.

Evidence: [T20](../documents/src-000173/tables/tbl-0020.md), source row 5.

### Role

Debtor?

Evidence: [T20](../documents/src-000173/tables/tbl-0020.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T20](../documents/src-000173/tables/tbl-0020.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Direct Debit.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T20, all rows](../documents/src-000173/tables/tbl-0020.md)

| Item | Description |
| --- | --- |
| Definition | Returns are individual debits that have reached the debtor’s agent and have been settled at the inter-bank level, but the debtor’s agent is then unable to make the collection for one of a number of reasons, for example, account closed, no funds, customer dead, etc. <br>The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction the debtor's account is credited by his bank and the debit is returned electronically through the clearing process to the creditor’s agent. |
| Trigger | Return of a / request for refund. |
| Pre-conditions | Settled instruction subject for return / refund. |
| Post-conditions | Settled instruction / requested refund. |
| Role | Debtor? |


[Parent process and participant placement](flow-src-000173-p125-customer-to-bank-direct-debit.md)

Literal Role cell/figure or definition discrepancy remains issue-000044; no participant is silently substituted.
<!-- /INITIATION-ACTIVITY -->
