---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p138-credit-transfer"
title: "Credit Transfer"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "heading_path": ["Description of BusinessActivities", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "heading_path": ["Description of BusinessActivities", "Credit Transfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "heading_path": ["Description of BusinessActivities", "Credit Transfer"]}]
participants: ["participant-src-000162-payment-clearing-agent-a", "participant-src-000162-payment-clearing-agent-b", "participant-src-000162-payment-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Credit Transfer", "Payment Clearing Agent", "Intermediary Agent", "Settlement Agent", "Creditor Agent", "Debtor agent"]
limitations: ["Lane containers preserve responsibilities; rounded source action boxes become rectangles. Final bullseye becomes a concentric open node; labelled source start/end outcomes are retained inside the reconstructed symbol. Original retains colour and precise routing.", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P140 makes these generic roles: concrete flows may use debtor agent, creditor agent or intermediary. T24 blank descriptions remain blank; no source definition is manufactured. Positive business-validation connector has no source Yes label.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-payment-clearing-agent-a", "participant-src-000162-payment-clearing-agent-b", "participant-src-000162-payment-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0007.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
table_review: "pass: exact cells, merges, complete Word table context"
---



# Credit Transfer

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Purpose, trigger and preconditions

Validate, clear and settle a payment across generic clearing agents A/B and settlement agent.

A prepares and sends payment; B technically/business validates before settlement assessment.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [payment clearing agent a](../../../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent-a.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [payment clearing agent b](../../../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent-b.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [payment settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-payment-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

**P140** The agents in this activity diagram are called PaymentClearingAgent and PaymentSettlementAgent in generic terms. In more concrete examples, these will be replaced by the most relevant agents, for example, debtor agent, creditor agent and intermediary agent.

### fig-0007

[Source reconstruction and actual review](../diagrams/clearing/fig-0007.md); direct-body paragraph P139; Word page17.

| Step | From/action | To/action | Connection |
| --- | --- | --- | --- |
| 1 | start | Prepare onward interbank payment | directed source connector |
| 2 | Prepare onward interbank payment | Send payment | directed source connector |
| 3 | Send payment | Receive Payment Order | SingleCreditTransfer message |
| 4 | Receive Payment Order | Apply Technical Validation | directed source connector |
| 5 | Apply Technical Validation | Is payment order technically correct? | directed source connector |
| 6 | Is payment order technically correct? | Reject payment Order | No |
| 7 | Is payment order technically correct? | Apply Business Validation | Yes |
| 8 | Apply Business Validation | Is Payment Order valid? | directed source connector |
| 9 | Is Payment Order valid? | Reject payment Order | No |
| 10 | Is Payment Order valid? | Assess Interbank Payment Risk | directed source connector |
| 11 | Reject payment Order | Assess reject reason code | SingleCreditTransferReject message |
| 12 | Assess reject reason code | Is repair needed? | directed source connector |
| 13 | Is repair needed? | Repair payment order | Yes |
| 14 | Repair payment order | Send payment | directed source connector |
| 15 | Is repair needed? | Recycle payment order | No |
| 16 | Recycle payment order | end | directed source connector |
| 17 | Assess Interbank Payment Risk | Can Settlement take place? | directed source connector |
| 18 | Can Settlement take place? | Inform about Settlement | No |
| 19 | Can Settlement take place? | Settle Payment order | Yes |
| 20 | Settle Payment order | Inform about Settlement | directed source connector |
| 21 | Inform about Settlement | Reject payment Order | Settlement failure |
| 22 | Inform about Settlement | Sort interbank payment | Settlement passed |
| 23 | Sort interbank payment | Calculate settlement positions | directed source connector |
| 24 | Calculate settlement positions | Prepare onward interbank payment | directed source connector |
| 25 | Prepare onward interbank payment | end | directed source connector |



## Complete activity tables

- [T24: complete roles, trigger, conditions and activities](../documents/src-000162/tables/tbl-0024.md)

## Outcomes, optional paths and source limitations

Technical/business rejection, repair or recycle; settlement failure returns reject, passed settlement proceeds to sorting/positions/onward preparation.

- Lane containers preserve responsibilities; rounded source action boxes become rectangles. Final bullseye becomes a concentric open node; labelled source start/end outcomes are retained inside the reconstructed symbol. Original retains colour and precise routing.
- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P140 makes these generic roles: concrete flows may use debtor agent, creditor agent or intermediary. T24 blank descriptions remain blank; no source definition is manufactured. Positive business-validation connector has no source Yes label.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
