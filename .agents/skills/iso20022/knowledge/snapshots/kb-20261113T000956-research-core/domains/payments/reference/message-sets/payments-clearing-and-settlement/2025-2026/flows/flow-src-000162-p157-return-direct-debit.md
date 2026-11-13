---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p157-return-direct-debit"
title: "Return Direct Debit"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Return Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Return Direct Debit"]}]
participants: ["participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Return Direct Debit"]
limitations: ["Byte-identical source artwork; source162 P157 context and complete Word page checked. Responsibilities retain separate source162 participant scope.", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0009.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
table_review: "pass: exact cells, merges, complete Word table context"
---



# Return Direct Debit

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Return a direct debit through clearing and settlement.

Debtor agent initiates return; clearing accepts or rejects return instruction.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [clearing agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

### fig-0009

[Source reconstruction and actual review](../diagrams/clearing/fig-0009.md); direct-body paragraph P158; Word page21.

| Step | From/action | To/action | Connection |
| --- | --- | --- | --- |
| 1 | Return Direct Debit | accept? | directed |
| 2 | accept? | Reject Direct Debit Return Instruction | directed no |
| 3 | Reject Direct Debit Return Instruction | Correct and Resubmit Rejected Return Instruction | directed |
| 4 | Correct and Resubmit Rejected Return Instruction | Return Direct Debit | directed |
| 5 | accept? | Clear Direct Debit Return | directed yes |
| 6 | Clear Direct Debit Return | Process Cleared Return | directed |
| 7 | Process Cleared Return | Reconcile Return Direct Debit | directed |
| 8 | Reconcile Return Direct Debit | Reconciled Returned Direct Debit | directed |
| 9 | Clear Direct Debit Return | Settle Direct Debit Return Proceeds | directed |
| 10 | Settle Direct Debit Return Proceeds | Reconcile Debit Entry | directed |
| 11 | Reconcile Debit Entry | Reconciled Debit Entry | directed |
| 12 | Settle Direct Debit Return Proceeds | Reconcile Credit Entry | directed |
| 13 | Start | Return Direct Debit | directed |
| 14 | Reconcile Credit Entry | Reconciled Credit Entry | directed |



## Outcomes, optional paths and source limitations

Correction/resubmission on rejection; accepted return settles and participants reconcile returned funds.

- Byte-identical source artwork; source162 P157 context and complete Word page checked. Responsibilities retain separate source162 participant scope.
- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
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
