---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p136-customer-to-bank-payment-order"
title: "Customer to Bank Payment Order"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[136]", "paragraph_id": "P136", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}]
participants: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Customer to Bank Payment Order"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Four separate forwarding-agent status nodes and the separate payment-order/authorisation arrows are preserved. Source green communications and grey internal control are listed together without equating them to schema message types.", "Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "T23 activity definitions, including repair/rebuild conditions and non-final execution statuses, govern this view. The source Cheques connector from Debtor Agent reaches both initiating-party and creditor receive-cheque nodes.", "Yellow source note: Either the Payment Autorisations are sent separately or with the payment order(s). Literal spelling retained."]
manual_curated: true
participant_ids: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0009.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Customer to Bank Payment Order

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Initiate, validate, route and reconcile customer-to-bank payment orders.

T23 begins with initiating-party preparation/authorisation; authorisation may accompany the order or be separate.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P137** In the customer-to-bank payment order(s), multiple participants can be present.

**P138** Simple scenario:

**P140** Complex scenario:

## Complete source activity tables

- [T23: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0023.md)

### fig-0009

[Source reconstruction and review](../diagrams/initiation/fig-0009.md); direct-body paragraph P145; Word file page18.

| Step | From/action | To/action | Source connection |
| --- | --- | --- | --- |
| 1 | start | 1 Prepare, authorise and send payment order(s) | directed |
| 2 | 1 Prepare, authorise and send payment order(s) | 2 Receive and check authentication | directed Authorisation |
| 3 | 1 Prepare, authorise and send payment order(s) | 2 Receive and check authentication | directed Payment order |
| 4 | 2 Receive and check authentication | 3.1 Technical validation | directed |
| 5 | 3.1 Technical validation | 3.3 Apply business rules | directed |
| 6 | 3.3 Apply business rules | 3.2 Assess static/dynamic risk | directed |
| 7 | 3.2 Assess static/dynamic risk | 3.4 Rebuild and forward payment order(s) | directed |
| 8 | 3.4 Rebuild and forward payment order(s) | Receive and check authentication | directed Payment order |
| 9 | 4 Receive Status Report | Is repair possible? | directed |
| 10 | Is repair possible? | Repair Payment Order(s) | directed Yes |
| 11 | Is repair possible? | Recycle Payment Order(s) | directed No |
| 12 | Repair Payment Order(s) | 1 Prepare, authorise and send payment order(s) | directed |
| 13 | Recycle Payment Order(s) | 1 Prepare, authorise and send payment order(s) | directed |
| 14 | 4 Receive Status Report | 6 Reconcile and track Payment | directed |
| 15 | 6 Reconcile and track Payment | Reconciliation/tracking OK? | directed |
| 16 | Reconciliation/tracking OK? | end | directed Yes |
| 17 | Reconciliation/tracking OK? | Investigation/claim and resolve | directed No |
| 18 | Investigation/claim and resolve | end | directed |
| 19 | 9.1 Receive cheque | end | directed |
| 20 | Receive and check authentication | 3.1 Technical validation | directed |
| 21 | 3.1 Technical validation | 3.3 Apply business rules | directed |
| 22 | 3.3 Apply business rules | 3.2 Assess static/dynamic risk | directed |
| 23 | 3.2 Assess static/dynamic risk | 5.1 Confirm acceptance | directed |
| 24 | 5.1 Confirm acceptance | 5.2 Send acceptance acknowledgement | directed |
| 25 | 5.2 Send acceptance acknowledgement | 5.3 Receive and forward acceptance acknowledgement | directed |
| 26 | 5.3 Receive and forward acceptance acknowledgement | 6 Reconcile and track Payment | directed |
| 27 | 5.1 Confirm acceptance | 7 Debit Customer Account and credit internal account | directed |
| 28 | 7 Debit Customer Account and credit internal account | 7.1 Prepare and send Debit Advice(s) | directed |
| 29 | 7.1 Prepare and send Debit Advice(s) | 7.1 Receive and forward Debit advices | directed |
| 30 | 7.1 Receive and forward Debit advices | 6 Reconcile and track Payment | directed |
| 31 | 7.1 Prepare and send Debit Advice(s) | Payment Routing | directed |
| 32 | Payment Routing | 8 Internal book keeping | directed On us |
| 33 | Payment Routing | 9 Print Cheques | directed Cheque |
| 34 | Payment Routing | 10 Rebuild Payments Order(s) | directed Not on us |
| 35 | 8 Internal book keeping | 11 Execution Status | directed |
| 36 | 9 Print Cheques | 11 Execution Status | directed |
| 37 | 10 Rebuild Payments Order(s) | 11 Execution Status | directed |
| 38 | 11 Execution Status | 11.1 Receive and forward Execution status | directed |
| 39 | 11.1 Receive and forward Execution status | 6 Reconcile and track Payment | directed |
| 40 | 9 Print Cheques | 9.1 Receive cheque | directed Cheques |
| 41 | 9 Print Cheques | 9.1 Receive cheques | directed Cheques |
| 42 | 10 Rebuild Payments Order(s) | Sort cheque(s) and credit transfers | directed Payment order |
| 43 | Sort cheque(s) and credit transfers | 8 Internal book keeping | directed |
| 44 | Sort cheque(s) and credit transfers | 9 Print cheques | directed |
| 45 | 8 Internal book keeping | Receive account information | directed Account information |
| 46 | 9 Print cheques | 9.1 Receive cheques | directed Cheques |
| 47 | 9.1 Receive cheques | Reconciliation | directed |
| 48 | Receive account information | Reconciliation | directed |
| 49 | Reconciliation | end | directed |
| 50 | 3.1 Technical validation | 4 Receive Status Report | directed |
| 51 | 3.3 Apply business rules | 4 Receive Status Report | directed |
| 52 | 3.2 Assess static/dynamic risk | 4 Receive Status Report | directed |
| 53 | 3.4 Rebuild and forward payment order(s) | 4 Receive Status Report | directed |
| 54 | 3.1 Technical validation | 4 Receive and forward Status Report | directed |
| 55 | 4 Receive and forward Status Report | 4 Receive Status Report | directed |
| 56 | 3.3 Apply business rules | 4 Receive and forward Status Report | directed |
| 57 | 4 Receive and forward Status Report | 4 Receive Status Report | directed |
| 58 | 3.2 Assess static/dynamic risk | 4 Receive and forward Status Report | directed |
| 59 | 4 Receive and forward Status Report | 4 Receive Status Report | directed |
| 60 | 7 Debit Customer Account and credit internal account | 4 Receive and forward Status Report | directed |
| 61 | 4 Receive and forward Status Report | 4 Receive Status Report | directed |



## Outcomes, alternatives and related processes

Repair/recycle and investigation loops, on-us/cheque/not-on-us branches and final/non-final execution status distinctions remain explicit in T23.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Four separate forwarding-agent status nodes and the separate payment-order/authorisation arrows are preserved. Source green communications and grey internal control are listed together without equating them to schema message types.
- Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- T23 activity definitions, including repair/rebuild conditions and non-final execution statuses, govern this view. The source Cheques connector from Debtor Agent reaches both initiating-party and creditor receive-cheque nodes.
- Yellow source note: Either the Payment Autorisations are sent separately or with the payment order(s). Literal spelling retained.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. T23 complete source-cell, merge and Word visual-table review passed.
