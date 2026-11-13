---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p161-direct-debit-reversal"
title: "Direct Debit Reversal"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct Debit Reversal"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct Debit Reversal"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct Debit Reversal"]}]
participants: ["participant-src-000162-ach", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-instructed-agent-ach", "participant-src-000162-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Direct Debit Reversal", "Instructed Agent/ACH", "Settlement Agent", "Creditor Agent", "Debtor agent", "Creditor", "Debtor", "Party", "ACH"]
limitations: ["Lane containers preserve responsibilities; rounded source action boxes become rectangles. Final bullseye becomes a concentric open node; labelled source start/end outcomes are retained inside the reconstructed symbol. Original retains colour and precise routing.", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "Source P162 post-settlement reversal credits debtor if accepted. Clearing and settlement responsibilities are separate in this activity view. T26 defines initiating responsibilities and reversal rejection/correction; figure includes additional creditor/debtor reconciliation actions.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-ach", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-instructed-agent-ach", "participant-src-000162-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0011.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
table_review: "pass: exact cells, merges, complete Word table context"
---



# Direct Debit Reversal

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Reverse a settled direct debit.

Creditor identifies a paid instruction that should not have been processed; P162/T26.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [ach](../../../../../../../shared/reference/participants/participant-src-000162-ach.md) | Source narrative/table participant, possibly outside bounded picture. |
| [clearing agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [instructed agent ach](../../../../../../../shared/reference/participants/participant-src-000162-instructed-agent-ach.md) | Source narrative/table participant, possibly outside bounded picture. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

**P162** The creditor initiates a reversal instruction after settlement, when a paid Direct Debit should not have been processed. If the reversal instruction is accepted, consequently the Debtor will be credited back.

### fig-0011

[Source reconstruction and actual review](../diagrams/clearing/fig-0011.md); direct-body paragraph P163; Word page22.

| Step | From/action | To/action | Connection |
| --- | --- | --- | --- |
| 1 | Settled Direct Debit | Request Reversal of the Direct Debit Payment Order | directed source connector |
| 2 | Request Reversal of the Direct Debit Payment Order | accept request for reversal? | directed source connector |
| 3 | accept request for reversal? | Reject Request for Reversal | No |
| 4 | Reject Request for Reversal | Process Rejected Request for Reversal | directed source connector |
| 5 | Process Rejected Request for Reversal | correction possible? | directed source connector |
| 6 | correction possible? | Request Reversal of the Direct Debit Payment Order | Yes |
| 7 | correction possible? | Rejected request | No |
| 8 | accept request for reversal? | Process Request for Reversal and submit Reversal to the Clearing | Yes |
| 9 | Process Request for Reversal and submit Reversal to the Clearing | accept? | directed source connector |
| 10 | accept? | Reject Reversal | No |
| 11 | Reject Reversal | Process B2B Rejected Reversal | directed source connector |
| 12 | Process B2B Rejected Reversal | formatting error? | directed source connector |
| 13 | formatting error? | Process Request for Reversal and submit Reversal to the Clearing | Yes |
| 14 | formatting error? | Reject Request for Reversal | No |
| 15 | accept? | Clear Direct Debit Reversal | Yes |
| 16 | Clear Direct Debit Reversal | Settle DD Reversal Proceeds | directed source connector |
| 17 | Settle DD Reversal Proceeds | Reconcile Debit Entry and Inform Creditor | directed source connector |
| 18 | Reconcile Debit Entry and Inform Creditor | Reconcile Debit Entry | directed source connector |
| 19 | Reconcile Debit Entry | Reversed Direct Debit | directed source connector |
| 20 | Clear Direct Debit Reversal | accept? | directed source connector |
| 21 | accept? | Return DD Reversal | No |
| 22 | Return DD Reversal | Returned Credit | directed source connector |
| 23 | accept? | Process DD Reversal and Inform Debtor | Yes |
| 24 | Process DD Reversal and Inform Debtor | Reconcile Reversal | directed source connector |
| 25 | Reconcile Reversal | Reversed Direct Debit | directed source connector |
| 26 | Settle DD Reversal Proceeds | Reconcile DD Reversal Entry | directed source connector |
| 27 | Reconcile DD Reversal Entry | Reconciled Credit | directed source connector |



## Complete activity tables

- [T26: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0026.md)

## Outcomes, optional paths and source limitations

Accepted reversal credits debtor; creditor/creditor-agent/clearing rejection loops and debtor-agent return branch remain explicit.

- Lane containers preserve responsibilities; rounded source action boxes become rectangles. Final bullseye becomes a concentric open node; labelled source start/end outcomes are retained inside the reconstructed symbol. Original retains colour and precise routing.
- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- Source P162 post-settlement reversal credits debtor if accepted. Clearing and settlement responsibilities are separate in this activity view. T26 defines initiating responsibilities and reversal rejection/correction; figure includes additional creditor/debtor reconciliation actions.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

| Distinct process | Reference |
| --- | --- |
| Direct-debit return activity | [Direct-debit return activity](flow-src-000162-p157-return-direct-debit.md) |
| Debtor refund activity | [Debtor refund activity](flow-src-000162-p159-request-refund-direct-debit.md) |
| Reversal activity | [Reversal activity](flow-src-000162-p161-direct-debit-reversal.md) |
| PaymentReturn and debtor refund | [PaymentReturn and debtor refund](flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md) |
| Customer direct-debit reversal | [Customer direct-debit reversal](flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md) |
| FI direct-debit reversal | [FI direct-debit reversal](flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit.md) |


## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../evidence/archived/fa67d8621c20bf64aa62336b.md). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
