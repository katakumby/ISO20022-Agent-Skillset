---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p107-customer-to-bank-payment-order"
title: "Customer-to-Bank Payment Order"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[107]", "paragraph_id": "P107", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[108]", "paragraph_id": "P108", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[109]", "paragraph_id": "P109", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[110]", "paragraph_id": "P110", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[111]", "paragraph_id": "P111", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[112]", "paragraph_id": "P112", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[113]", "paragraph_id": "P113", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[114]", "paragraph_id": "P114", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"]}]
participants: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Customer-to-Bank Payment Order"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "Participant pictograms sit below process groups without drawn connectors. Native actors remain unconnected; the explicit placement table preserves group membership without inventing association lines.", "Source arrows are ordinary filled arrows; no include/extend/generalization semantics are asserted. Source has no system boundary.", "Source colours distinguish process levels; original artwork preserves those colours and exact placement.", "T15 names only Debtor agent for regulatory reporting; figure also shows Creditor Agent. Source discrepancy remains issue-000044."]
manual_curated: true
participant_ids: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-debtor"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0001.md"]
issue_ids: ["issue-000044"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Customer-to-Bank Payment Order

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

End-to-end customer-to-bank payment processes.

A decision to pay or collection request activates the applicable activity; T9–T17 supply precise activity triggers and conditions.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |
| [ultimate debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P108** This diagram represents the high level BusinessProcesses for the customer-to-bank payment.

**P110** Process Customer-to-bank Payment

**P111** This BusinessPprocess comprises all underlying sub-processes which are all related to the initiation and handling of customer-to-bank payments. The sub-processes are:

**P112** order customer-to-bank payment

**P113** accept customer-to-bank payment

**P114** clear customer-to-bank payment

**P115** settle customer-to-bank payment

## Complete source activity tables

- [T9: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0009.md)
- [T10: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0010.md)
- [T11: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0011.md)
- [T12: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0012.md)
- [T13: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0013.md)
- [T14: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0014.md)
- [T15: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0015.md)
- [T16: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0016.md)
- [T17: complete roles, conditions and activities](../documents/src-000173/tables/tbl-0017.md)

### fig-0001

[Source reconstruction and review](../diagrams/initiation/fig-0001.md); direct-body paragraph P109; Word file page11.

| Step | From/action | To/action | Source connection |
| --- | --- | --- | --- |
| 1 | Process end-to-end payment | Process customer-to-bank payment | plain filled source arrow |
| 2 | Process end-to-end payment | Process interbank payment | plain filled source arrow |
| 3 | Process end-to-end payment | Report | plain filled source arrow |
| 4 | Process customer-to-bank payment | Order customer-to-bank payment | plain filled source arrow |
| 5 | Process customer-to-bank payment | Accept customer-to-bank payment | plain filled source arrow |
| 6 | Process customer-to-bank payment | Clear customer-to-bank payment | plain filled source arrow |
| 7 | Process customer-to-bank payment | Settle customer-to-bank payment | plain filled source arrow |
| 8 | Order customer-to-bank payment | Authorise customer-to-bank payment | plain filled source arrow |
| 9 | Accept customer-to-bank payment | Check customer-to-bank Payment authorisation | plain filled source arrow |
| 10 | Accept customer-to-bank payment | Validate customer-to-bank payment | plain filled source arrow |
| 11 | Accept customer-to-bank payment | Assess customer-to-bank Payment risk | plain filled source arrow |
| 12 | Assess customer-to-bank Payment risk | Generate regulatory reporting information | plain filled source arrow |
| 13 | Clear customer-to-bank payment | Sort payment | plain filled source arrow |
| 14 | Clear customer-to-bank payment | Prepare onward interbank payment | plain filled source arrow |



## Outcomes, alternatives and related processes

Order/acceptance/clearing/settlement and regulatory reporting are distinct activities; source figure also locates out-of-scope interbank processing/reporting.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- Participant pictograms sit below process groups without drawn connectors. Native actors remain unconnected; the explicit placement table preserves group membership without inventing association lines.
- Source arrows are ordinary filled arrows; no include/extend/generalization semantics are asserted. Source has no system boundary.
- Source colours distinguish process levels; original artwork preserves those colours and exact placement.
- T15 names only Debtor agent for regulatory reporting; figure also shows Creditor Agent. Source discrepancy remains issue-000044.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. Unresolved source claims: issue-000044. Full table review remains separate.
