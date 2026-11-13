---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p111-credit-transfer"
title: "Credit Transfer"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[111]", "paragraph_id": "P111", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[112]", "paragraph_id": "P112", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[113]", "paragraph_id": "P113", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[114]", "paragraph_id": "P114", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[119]", "paragraph_id": "P119", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "heading_path": ["BusinessProcess Description", "Credit Transfer"]}]
participants: ["participant-src-000162-clearing-system", "participant-src-000162-financial-institution"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Credit Transfer"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "No actors or system boundary appear in these source process models. Colours distinguish source levels and remain in the original. Ordinary arrows are not automatically include/extend/generalization relationships.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.", "T12 calls authorisation an extension of acceptance. Picture directs dashed arrow from Accept to Authorise without an extend label; that literal direction/style is preserved, without inventing UML semantics."]
manual_curated: true
participant_ids: ["participant-src-000162-clearing-system", "participant-src-000162-financial-institution"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0001.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
table_review: "pass: exact cells, merges, complete Word table context"
---



# Credit Transfer

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Interbank credit-transfer process breakdown.

Receipt/execution date activates acceptance, clearing or settlement per T9–T18; each table preserves its exact preconditions.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [clearing system](../../../../../../../shared/reference/participants/participant-src-000162-clearing-system.md) | Source narrative/table participant, possibly outside bounded picture. |
| [financial institution](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Source narrative/table participant, possibly outside bounded picture. |


## Source-defined activities and conditions

**P112** This diagram pictures the high level end-to-end payments BusinessProcesses for the credit transfer.

**P114** Accept Inter-Bank Payment

**P115** Asses Interbank Payment Risk

**P116** Validate Interbank Payment

**P117** Authorise Interbank Payment

**P118** Clear Interbank Payment

**P119** Sort Interbank Payment

**P120** Calculate the Settlement Positions

**P121** Prepare Onward Interbank Payment

**P122** Settle Interbank Payment

**P123** Generate Regulatory Reporting Information

### fig-0001

[Source reconstruction and actual review](../diagrams/clearing/fig-0001.md); direct-body paragraph P113; Word page11.

| Step | From/action | To/action | Connection |
| --- | --- | --- | --- |
| 1 | Process end-to-end payment | Process customer-to-bank payment | plain directed source arrow |
| 2 | Process end-to-end payment | Process interbank payment | plain directed source arrow |
| 3 | Process end-to-end payment | Report | plain directed source arrow |
| 4 | Process interbank payment | Accept interbank payment | plain directed source arrow |
| 5 | Process interbank payment | Clear interbank payment | plain directed source arrow |
| 6 | Process interbank payment | Settle interbank payment | plain directed source arrow |
| 7 | Accept interbank payment | Assess interbank Payment risk | plain directed source arrow |
| 8 | Accept interbank payment | Validate interbank payment | plain directed source arrow |
| 9 | Accept interbank payment | Authorise interbank payment | unlabelled dashed directed source arrow |
| 10 | Clear interbank payment | Sort interbank payment | plain directed source arrow |
| 11 | Clear interbank payment | Calculate the settlement positions | plain directed source arrow |
| 12 | Clear interbank payment | Prepare onward interbank payment | plain directed source arrow |
| 13 | Prepare onward interbank payment | Generate regulatory reporting information | unlabelled dashed directed source arrow |



## Complete activity tables

- [T9: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0009.md)
- [T10: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0010.md)
- [T11: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0011.md)
- [T12: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0012.md)
- [T13: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0013.md)
- [T14: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0014.md)
- [T15: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0015.md)
- [T16: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0016.md)
- [T17: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0017.md)
- [T18: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0018.md)

## Outcomes, optional paths and source limitations

Accepted/rejected instructions, onward routing/positions, transfer of ownership and applicable regulatory information remain distinct outcomes.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- No actors or system boundary appear in these source process models. Colours distinguish source levels and remain in the original. Ordinary arrows are not automatically include/extend/generalization relationships.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.
- T12 calls authorisation an extension of acceptance. Picture directs dashed arrow from Accept to Authorise without an extend label; that literal direction/style is preserved, without inventing UML semantics.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../evidence/archived/fa67d8621c20bf64aa62336b.md). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
