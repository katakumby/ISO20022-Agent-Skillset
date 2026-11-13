---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p153-movement-reversal"
title: "Movement Reversal"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000079", "locator": "BusinessTransactions / Confirmation and Reversal, P262–P281"}, {"source_id": "src-000080", "locator": "file pages360,540,665,813; §§7.1,8.1,9.1,15.1 MessageDefinition Functionality"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner", "participant-corporate-actions-designated-agent"]
message_mapping_evidence: []
message_ids: ["seev.035.001.17", "seev.036.001.17", "seev.037.001.17", "seev.044.001.13"]
message_families: ["seev.035", "seev.036", "seev.037", "seev.044"]
search_terms: ["corporate action movement reversal", "cancellation of reversal pre-advice", "account servicer", "account owner", "designated agent", "seev.037", "seev.044"]
limitations: ["Source table T7 row4 has a contradictory seev.037 message name; issue-000016 retains it. Exact message identity is established separately by MDR2 §9 p665.", "The two source sequence reconstructions have passed rendering and visual comparison. Broader source-wide table/diagram reconciliation remains pending."]
manual_curated: true
related_message_ids: ["seev.040.001.13"]
---

# Corporate action movement reversal

The account servicer reverses previously confirmed cash or securities postings and sends the account owner or its designated agent a reversal advice. The process table permits only a full movement reversal. Cancelling a previously announced reversal pre-advice is a different path: the movements will not be reversed. Evidence: src-000079 T17, P272–P279; src-000080 p665 §9.1 and p813 §15.1.

## Reusable flow and participant responsibilities

| Stage | Responsible participant / direction | Message or action | Source evidence |
| --- | --- | --- | --- |
| Context | Account Servicer → Account Owner | A movement confirmation has already been sent and cash/securities postings have been applied. | src-000079 T17 preconditions; P272 |
| Optional pre-advice | Account Servicer → Account Owner | CorporateActionMovementPreliminaryAdvice, seev.035.001.17, may pre-advise the impending reversal and may give its reason. | src-000079 P272; src-000080 p360 §7.1 exact identity |
| Reversal advice | Account Servicer → Account Owner or designated agent | CorporateActionMovementReversalAdvice, seev.037.001.17, confirms the reversal. P273 requires sending it; the process table lists already reversed postings as a precondition. | src-000079 T17,P273; src-000080 p665 §9.1 |
| Alternative after pre-advice | Account Servicer → Account Owner or designated agent | If the movements will not be reversed, cancel the reversal pre-advice with seev.044.001.13. This cancels the announcement, not an executed movement reversal. | src-000079 P278–P279; src-000080 p813 §15.1 |


The source table states postconditions as “None”; this is retained as a source assertion. The process and its notification must not be flattened into a schema rule. The designated-agent receiver is included from the functionality narrative even though the illustrated two-actor sequences show only Account Servicer and Account Owner.

## Cancellation and reversal navigation

| Purpose | Direction | Canonical message |
| --- | --- | --- |
| Reverse a confirmed posting | Account Servicer → Account Owner/designated agent | [seev.037.001.17](../../../../messages/seev.037.001.17/index.md) |
| Cancel a preliminary movement advice, including a reversal pre-advice | Account Servicer → Account Owner/designated agent | [seev.044.001.13](../../../../messages/seev.044.001.13/index.md) |
| Request cancellation of an election instruction | Account Owner → Account Servicer | [seev.040.001.13](../../../../messages/seev.040.001.13/index.md) |

The instruction-cancellation direction and purpose are established by src-000080 file p719 §12.1.

## Diagrams and source context

[Reviewed reversal sequence](../diagrams/reversal/fig-0001.md); [Reviewed reversal pre-advice cancellation sequence](../diagrams/reversal/fig-0002.md).

[Narrative-only designated agent](../../../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md). Source-name conflict: [issue-000016](../../../../../../../tracking/issues.md).

## Full process-table evidence

## Purpose, trigger and conditions

### Definition

The process of reversing the postings (cash and/or securities) made to the account owner’s safekeeping and /or cash accounts. It is to be noted that only full movement reversal can be done.

Evidence: [T17](../documents/src-000079/tables/tbl-0017.md), source row 2.

### Trigger

previous communication (notification or confirmation) due to calculation updates on the corporate action event (changes or updates in rates)
updates due to tax components that result in changes in confirmed distribution amounts as well as calculation errors

Evidence: [T17](../documents/src-000079/tables/tbl-0017.md), source row 3.

### Pre-conditions

previous movement confirmation must have been sent. 
cash and/or securities postings are reversed in the account owner’s account(s)

Evidence: [T17](../documents/src-000079/tables/tbl-0017.md), source row 4.

### Post-conditions

None

Evidence: [T17](../documents/src-000079/tables/tbl-0017.md), source row 5.

### Role

Account servicer

Evidence: [T17](../documents/src-000079/tables/tbl-0017.md), source row 6.


## Provenance

[Complete T17 process table](../documents/src-000079/tables/tbl-0017.md); [P270–P275 reversal narrative](flow-src-000079-p270-reversal.md); [P276–P281 alternative narrative](flow-src-000079-p276-reversal-pre-advice-cancellation.md).
