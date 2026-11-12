---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p129-reject"
title: "Reject"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:tbl[19]", "paragraph_id": null, "table_id": "T19"}]
participants: ["participant-src-000173-creditor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reject", "Creditor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Reject

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Reconciles reject with the original instructions and identifies the reason for rejection. If the reject results from a formatting error, correct the data and resubmit for processing. 

Evidence: [T19](../documents/src-000173/tables/tbl-0019.md), source row 2.

### Trigger

Reconciliation of the reject.

Evidence: [T19](../documents/src-000173/tables/tbl-0019.md), source row 3.

### Pre-conditions

Reject received.

Evidence: [T19](../documents/src-000173/tables/tbl-0019.md), source row 4.

### Post-conditions

Reconciled reject. 

Evidence: [T19](../documents/src-000173/tables/tbl-0019.md), source row 5.

### Role

Creditor agent

Evidence: [T19](../documents/src-000173/tables/tbl-0019.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T19](../documents/src-000173/tables/tbl-0019.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Direct Debit.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T19, all rows](../documents/src-000173/tables/tbl-0019.md)

| Item | Description |
| --- | --- |
| Definition | Reconciles reject with the original instructions and identifies the reason for rejection. If the reject results from a formatting error, correct the data and resubmit for processing.  |
| Trigger | Reconciliation of the reject. |
| Pre-conditions | Reject received. |
| Post-conditions | Reconciled reject.  |
| Role | Creditor agent |


[Parent process and participant placement](flow-src-000173-p125-customer-to-bank-direct-debit.md)

<!-- /INITIATION-ACTIVITY -->
