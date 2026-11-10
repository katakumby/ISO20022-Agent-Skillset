---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p149-return-direct-debit"
title: "Return Direct Debit"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "heading_path": ["Description of BusinessActivities", "Customer-to-bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "heading_path": ["Description of BusinessActivities", "Customer-to-bank Direct Debit"]}]
participants: ["participant-src-000173-clearing-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Return Direct Debit"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "All source lanes are retained, including the empty Debtor lane in figure11. Source clearing/settlement responsibilities are distinct from the combined participant in later sequence diagrams.", "Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.", "Mermaid collapses the empty Debtor lane to its label; the participant table and original preserve that empty source responsibility column.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0011.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Return Direct Debit

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Return a direct debit and reconcile returned funds.

Debtor agent initiates Return Direct Debit. The clearing agent accepts or rejects the return instruction.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [clearing agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-settlement-agent.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P149** Return Direct Debit

### fig-0011

[Source reconstruction and review](../diagrams/initiation/fig-0011.md); direct-body paragraph P150; Word file page22.

| Step | From/action | To/action | Source connection |
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



## Outcomes, alternatives and related processes

Rejected return is corrected/resubmitted; accepted return is cleared, settled, and reconciled by creditor, creditor agent and debtor agent.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- All source lanes are retained, including the empty Debtor lane in figure11. Source clearing/settlement responsibilities are distinct from the combined participant in later sequence diagrams.
- Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.
- Mermaid collapses the empty Debtor lane to its label; the participant table and original preserve that empty source responsibility column.
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
