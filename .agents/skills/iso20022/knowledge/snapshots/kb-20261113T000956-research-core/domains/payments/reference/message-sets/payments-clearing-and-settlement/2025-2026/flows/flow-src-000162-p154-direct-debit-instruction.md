---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p154-direct-debit-instruction"
title: "Direct debit instruction"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "heading_path": ["Description of BusinessActivities", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct debit instruction "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct debit instruction "]}]
participants: ["participant-src-000162-ach", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: []
search_terms: ["Direct debit instruction", "Creditor Agent or Creditor", "Financial Institution", "Settlement Agent", "Clearing System", "Creditor Agent", "Debtor agent", "Debtor", "ACH", "pacs.010"]
limitations: ["Byte-identical source artwork; source162 P154 context and complete Word page checked. Responsibilities retain separate source162 participant scope.", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-ach", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0008.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
table_review: "pass: exact cells, merges, complete Word table context"
---



# Direct debit instruction

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Collect a direct debit, including notification, rejection and reconciliation.

Signed mandate in place; pre-notification and participant acceptance decisions govern branches.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [ach](../../../../../../../shared/reference/participants/participant-src-000162-ach.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

**P143** Some base definitions of direct debit terms:

**P144** Direct Debit: Direct Debit(s) results in cash transfers between debtors and creditors through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

**P145** Mandate: This is the authorisation / expression of consent given by the Debtor allowing a specified creditor to originate Direct Debit instructions for debiting the specified Debtor’s account in accordance with the relevant Direct Debit scheme rules and, if applicable,  the mandate details.

**P146** Reject: Rejects are individual debits or files of debits that are rejected due to technical reasons, e.g. invalid format, wrong IBAN check digit. Rejects take place prior to interbank settlement if the creditor’s agent, the debtor’s agent or any other agent in the chain is not able to process the individual debit or files of debits.

**P147** Request for Cancellation: A request by the creditor to cancel a Direct Debit instruction prior to the interbank settlement

**P148** Revocation: A request by the creditor to revoke a Direct Debit Payment order prior to the acceptance by the creditor’s Agent.

**P149** Reversal: The creditor initiates a reversal instruction after settlement, when a paid Direct Debit should not have been processed. Consequently, the debtor will be credited back.

**P150** Refusal by the Debtor: One of the Debtor’s right to refuse either any Direct Debit transaction to be debited on its account, or one Direct Debit, once pre-noticed by a creditor.

**P151** Return: Returns are individual debits that have reached the Debtor’s Agent and have been settled at the interbank level, but the Debtor’s Agent is then unable to make the collection for one of a number of reasons e.g. account closed, no funds, customer dead, account does not accept Direct Debit, etc.

**P152** Refund: Refund is the process to claim for reimbursement of a Direct Debit for any reason after settlement and within a defined period ("n" days). A refund instruction is initiated by the Debtor.

### fig-0008

[Source reconstruction and actual review](../diagrams/clearing/fig-0008.md); direct-body paragraph P155; Word page20.

| Step | From/action | To/action | Connection |
| --- | --- | --- | --- |
| 1 | Signed mandate in place | Pre-Notification sent? | directed |
| 2 | Pre-Notification sent? | Pre-Notification of the Debtor (from Process 1st/1-off Direct Debit) | directed no |
| 3 | Pre-Notification sent? | Initiate Collection of the Direct Debit | directed yes |
| 4 | Pre-Notification of the Debtor (from Process 1st/1-off Direct Debit) | Initiate Collection of the Direct Debit | directed |
| 5 | Pre-Notification of the Debtor (from Process 1st/1-off Direct Debit) | Reconcile Pre-Notification | directed |
| 6 | Reconcile Pre-Notification | accept? | directed |
| 7 | accept? | Refused Direct Debit | directed no |
| 8 | accept? | Reconciled Pre-Notification | directed yes |
| 9 | Initiate Collection of the Direct Debit | accept request for initiation of a direct debit / creditor registered for the DD scheme? | directed |
| 10 | accept request for initiation of a direct debit / creditor registered for the DD scheme? | Reject Direct Debit Instruction | directed no |
| 11 | accept request for initiation of a direct debit / creditor registered for the DD scheme? | Forward DD Instruction | directed yes |
| 12 | Forward DD Instruction | accept direct debit transaction? | directed |
| 13 | accept direct debit transaction? | Reject Direct Debit Instruction | directed no |
| 14 | accept direct debit transaction? | Clear Direct Debit | directed yes |
| 15 | Reject Direct Debit Instruction | Process B2B Reject | directed |
| 16 | Process B2B Reject | format error? | directed |
| 17 | format error? | Correct and resubmit | directed yes |
| 18 | format error? | Reject Direct Debit Instruction | directed no |
| 19 | Correct and resubmit | Forward DD Instruction | directed |
| 20 | Reject Direct Debit Instruction | Process Reject | directed |
| 21 | Process Reject | correction? | directed |
| 22 | correction? | Rejected DD | directed no |
| 23 | correction? | Initiate Collection of the Direct Debit | directed yes |
| 24 | Clear Direct Debit | Settle Direct Debit Proceeds | directed |
| 25 | Clear Direct Debit | accept? | directed |
| 26 | accept? | before due date? | directed no |
| 27 | before due date? | Reject Direct Debit Instruction | directed yes |
| 28 | before due date? | Return Direct Debit Instruction | directed no |
| 29 | Reject Direct Debit Instruction | Reject Direct Debit Instruction | directed |
| 30 | accept? | Provide Value Added Services | directed yes |
| 31 | Provide Value Added Services | Reconcile Debit Entry | directed |
| 32 | Reconcile Debit Entry | Refund requested? | directed |
| 33 | Refund requested? | Reconciled Direct Debit | directed no |
| 34 | Refund requested? | Request Refund | directed yes |
| 35 | Settle Direct Debit Proceeds | Reconcile Debit | directed report |
| 36 | Reconcile Debit | Reconciled Debit Entry | directed |
| 37 | Settle Direct Debit Proceeds | Reconcile Credit Entry and Inform Creditor | directed |
| 38 | Reconcile Credit Entry and Inform Creditor | Reconcile Collected Direct Debit | directed |
| 39 | Reconcile Collected Direct Debit | Reconciled Direct Debit | directed |



## Complete activity tables

- [T25: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0025.md)

## Outcomes, optional paths and source limitations

Accepted DD clears/settles; rejection may be repaired; before-due rejection and post-settlement return remain distinct; debtor may request refund.

- Byte-identical source artwork; source162 P154 context and complete Word page checked. Responsibilities retain separate source162 participant scope.
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
