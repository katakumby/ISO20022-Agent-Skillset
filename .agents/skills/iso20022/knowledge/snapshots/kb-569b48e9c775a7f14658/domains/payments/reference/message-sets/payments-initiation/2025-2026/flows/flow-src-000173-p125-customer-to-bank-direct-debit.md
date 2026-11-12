---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p125-customer-to-bank-direct-debit"
title: "Customer-to-Bank Direct Debit"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"]}]
participants: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Customer-to-Bank Direct Debit"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Manage Direct Debit Mandate is an unconnected source use case, retained without adding a parent edge.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "Participant pictograms sit below process groups without drawn connectors. Native actors remain unconnected; the explicit placement table preserves group membership without inventing association lines.", "Source arrows are ordinary filled arrows; no include/extend/generalization semantics are asserted. Source has no system boundary.", "Source colours distinguish process levels; original artwork preserves those colours and exact placement."]
manual_curated: true
participant_ids: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0002.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Customer-to-Bank Direct Debit

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Direct-debit process overview.

T18 requires consensus on payment method, debtor authorisation and notification for first/one-off collection.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P126** This diagram represents the high level BusinessProcesses for the direct debit.

**P128** Initiate Collection of Direct Debit

**P129** Reject

**P130** Return/Request for Refund

**P131** Reversal

## Complete source activity tables

- [T18: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0018.md)
- [T19: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0019.md)
- [T20: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0020.md)
- [T21: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0021.md)

### fig-0002

[Source reconstruction and review](../diagrams/initiation/fig-0002.md); direct-body paragraph P127; Word file page15.

| Step | From/action | To/action | Source connection |
| --- | --- | --- | --- |
| 1 | Process Direct Debit end-to-end | Process customer-to-bank Direct Debit | plain filled source arrow |
| 2 | Process Direct Debit end-to-end | Process interbank Direct Debit | plain filled source arrow |
| 3 | Process Direct Debit end-to-end | Report | plain filled source arrow |
| 4 | Process customer-to-bank Direct Debit | Initiate collection of 1st/1-off Direct Debit | plain filled source arrow |
| 5 | Process customer-to-bank Direct Debit | Initiate collection of recurrent Direct Debit | plain filled source arrow |
| 6 | Process customer-to-bank Direct Debit | Process reject | plain filled source arrow |
| 7 | Process customer-to-bank Direct Debit | Process return/request for refund | plain filled source arrow |
| 8 | Process customer-to-bank Direct Debit | Process reversal | plain filled source arrow |
| 9 | Process customer-to-bank Direct Debit | Process request for cancellation/Revocation | plain filled source arrow |



## Outcomes, alternatives and related processes

Collection, rejection, return/refund, reversal and cancellation/revocation remain separate processes. Mandate management is shown as unconnected.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Manage Direct Debit Mandate is an unconnected source use case, retained without adding a parent edge.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- Participant pictograms sit below process groups without drawn connectors. Native actors remain unconnected; the explicit placement table preserves group membership without inventing association lines.
- Source arrows are ordinary filled arrows; no include/extend/generalization semantics are asserted. Source has no system boundary.
- Source colours distinguish process levels; original artwork preserves those colours and exact placement.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. Full table review remains separate.
