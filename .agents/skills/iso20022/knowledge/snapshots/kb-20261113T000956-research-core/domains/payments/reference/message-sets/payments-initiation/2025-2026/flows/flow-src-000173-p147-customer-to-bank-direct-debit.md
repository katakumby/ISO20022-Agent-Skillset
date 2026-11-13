---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p147-customer-to-bank-direct-debit"
title: "Customer-to-bank Direct Debit"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "heading_path": ["Description of BusinessActivities", "Customer-to-bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "heading_path": ["Description of BusinessActivities", "Customer-to-bank Direct Debit"]}]
participants: ["participant-src-000173-ach-system-transaction-administrator", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Customer-to-bank Direct Debit"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "Purple activity-reference notes link Return Direct Debit Instruction to figure11 and Request Refund to figure12; they are not extra process activities.", "Source initial state includes Signed mandate in place. Separate debtor pre-notification acceptance/refusal does not have a connector back to creditor collection. No such connector is invented."]
manual_curated: true
participant_ids: ["participant-src-000173-ach-system-transaction-administrator", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0010.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Customer-to-bank Direct Debit

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Collect a direct debit, including pre-notification and rejection.

Source starts Signed mandate in place and tests whether pre-notification was sent.

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

### fig-0010

[Source reconstruction and review](../diagrams/initiation/fig-0010.md); direct-body paragraph P148; Word file page22.

| Step | From/action | To/action | Source connection |
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



## Outcomes, alternatives and related processes

Accepted clearing leads to settlement/reconciliation; rejection may be corrected; debtor-agent rejection before due date and return afterward are separate paths, while debtor refund branches to its reusable flow.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- Purple activity-reference notes link Return Direct Debit Instruction to figure11 and Request Refund to figure12; they are not extra process activities.
- Source initial state includes Signed mandate in place. Separate debtor pre-notification acceptance/refusal does not have a connector back to creditor collection. No such connector is invented.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
