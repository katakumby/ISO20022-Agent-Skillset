---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p124-direct-debit"
title: "Direct Debit"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "heading_path": ["BusinessProcess Description", "Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "heading_path": ["BusinessProcess Description", "Direct Debit"]}]
participants: ["participant-src-000162-clearing-system", "participant-src-000162-financial-institution", "participant-src-000162-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Direct Debit"]
limitations: ["Mandate-management use case is connected to the root in this source. Cancellation/revocation appears in overview but is outside the detailed scope (P131).", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "No actors or system boundary appear in these source process models. Colours distinguish source levels and remain in the original. Ordinary arrows are not automatically include/extend/generalization relationships.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-clearing-system", "participant-src-000162-financial-institution", "participant-src-000162-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0002.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
table_review: "pass: exact cells, merges, complete Word table context"
---



# Direct Debit

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Purpose, trigger and preconditions

Interbank direct-debit process breakdown.

Validated DD instruction is released to instructed agent (T19); rejection, return/refund and reversal have their own triggers.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [clearing system](../../../../../../../shared/reference/participants/participant-src-000162-clearing-system.md) | Source narrative/table participant, possibly outside bounded picture. |
| [financial institution](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Source narrative/table participant, possibly outside bounded picture. |
| [party](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Source narrative/table participant, possibly outside bounded picture. |


## Source-defined activities and conditions

**P125** This diagram pictures the high level BusinessProcesses for the direct debit.

**P127** Process direct debit

**P128** Process Reject

**P129** Process Return/Request for Refund

**P130** Process Reversal

**P131** The process cancellation/revocation is out of scope.

### fig-0002

[Source reconstruction and actual review](../diagrams/clearing/fig-0002.md); direct-body paragraph P126; Word page15.

| Step | From/action | To/action | Connection |
| --- | --- | --- | --- |
| 1 | Process Direct Debit end-to-end | Manage Direct Debit Mandate | plain directed source arrow |
| 2 | Process Direct Debit end-to-end | Process customer-to-bank Direct Debit | plain directed source arrow |
| 3 | Process Direct Debit end-to-end | Process interbank Direct Debit | plain directed source arrow |
| 4 | Process Direct Debit end-to-end | Report | plain directed source arrow |
| 5 | Process interbank Direct Debit | Process 1st/1-off Direct Debit | plain directed source arrow |
| 6 | Process interbank Direct Debit | Process recurrent Direct Debits | plain directed source arrow |
| 7 | Process interbank Direct Debit | Process reversals | plain directed source arrow |
| 8 | Process interbank Direct Debit | Process return/request for refund | plain directed source arrow |
| 9 | Process interbank Direct Debit | Process reject | plain directed source arrow |
| 10 | Process interbank Direct Debit | Process cancellation/Revocation | plain directed source arrow |



## Complete activity tables

- [T19: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0019.md)
- [T20: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0020.md)
- [T21: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0021.md)
- [T22: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0022.md)

## Outcomes, optional paths and source limitations

Collections forwarded, rejects reconciled, settled funds returned or reversal processed; cancellation/revocation is shown but outside detailed scope.

- Mandate-management use case is connected to the root in this source. Cancellation/revocation appears in overview but is outside the detailed scope (P131).
- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- No actors or system boundary appear in these source process models. Colours distinguish source levels and remain in the original. Ordinary arrows are not automatically include/extend/generalization relationships.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
