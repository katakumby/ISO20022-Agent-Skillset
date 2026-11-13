---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p151-request-refund-of-direct-debit"
title: "Request Refund of Direct Debit"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "heading_path": ["Description of BusinessActivities", "Customer-to-bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "heading_path": ["Description of BusinessActivities", "Customer-to-bank Direct Debit"]}]
participants: ["participant-src-000173-ach-system-transaction-administrator", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Request Refund of Direct Debit"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "All source lanes are retained, including the empty Debtor lane in figure11. Source clearing/settlement responsibilities are distinct from the combined participant in later sequence diagrams.", "Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-ach-system-transaction-administrator", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0012.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Request Refund of Direct Debit

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Handle debtor refund request and the resulting direct-debit return.

Debtor requests refund; debtor agent decides whether to accept.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [ach system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000173-ach-system-transaction-administrator.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-settlement-agent.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P151** Request Refund of Direct Debit

### fig-0012

[Source reconstruction and review](../diagrams/initiation/fig-0012.md); direct-body paragraph P152; Word file page23.

| Step | From/action | To/action | Source connection |
| --- | --- | --- | --- |
| 1 | Issue Direct Debit Return | accept? | directed |
| 2 | accept? | Reject Direct Debit Return Instruction | directed no |
| 3 | Reject Direct Debit Return Instruction | Correct and Resubmit Rejected Return Instruction | directed |
| 4 | Correct and Resubmit Rejected Return Instruction | Issue Direct Debit Return | directed |
| 5 | accept? | Clear Direct Debit Return | directed yes |
| 6 | Clear Direct Debit Return | Process Cleared Return | directed |
| 7 | Process Cleared Return | Reconcile Return Direct Debit | directed |
| 8 | Reconcile Return Direct Debit | Reconciled Direct Debit | directed |
| 9 | Clear Direct Debit Return | Settle Direct Debit Return Proceeds | directed |
| 10 | Settle Direct Debit Return Proceeds | Reconcile Debit Entry | directed |
| 11 | Reconcile Debit Entry | end | directed |
| 12 | Settle Direct Debit Return Proceeds | Reconcile Credit Entry | directed |
| 13 | Start | Request Refund (from Process Direct Debit) | directed |
| 14 | Request Refund (from Process Direct Debit) | accept request? | directed |
| 15 | accept request? | Reject Request for Refund | directed no |
| 16 | Reject Request for Refund | Insufficient information? | directed |
| 17 | Insufficient information? | Correct and Resubmit | directed yes |
| 18 | Insufficient information? | Rejected Request | directed no |
| 19 | Correct and Resubmit | Request Refund (from Process Direct Debit) | directed |
| 20 | accept request? | Dematerialise the Request for Refund | directed yes |
| 21 | Dematerialise the Request for Refund | Issue Direct Debit Return | directed |
| 22 | Reconcile Credit Entry | Inform Debtor | directed |
| 23 | Inform Debtor | Reconcile Credit Entry | directed |
| 24 | Reconcile Credit Entry | Reconciled Credit Entry | directed |



## Outcomes, alternatives and related processes

Rejected requests may be corrected for insufficient information or end rejected; accepted requests are dematerialised and returned through clearing/settlement, then debtor is informed and reconciles credit.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- All source lanes are retained, including the empty Debtor lane in figure11. Source clearing/settlement responsibilities are distinct from the combined participant in later sequence diagrams.
- Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.

| Process | Reference |
| --- | --- |
| Direct-debit return activity | [Direct-debit return activity](flow-src-000173-p149-return-direct-debit.md) |
| Debtor refund request | [Debtor refund request](flow-src-000173-p151-request-refund-of-direct-debit.md) |
| PaymentReturn exchange | [PaymentReturn exchange](flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md) |
| Post-settlement CustomerPaymentReversal | [Post-settlement CustomerPaymentReversal](flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md) |


## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
