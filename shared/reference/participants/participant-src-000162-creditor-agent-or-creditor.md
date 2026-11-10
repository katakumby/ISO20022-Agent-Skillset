---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-creditor-agent-or-creditor"
title: "Creditor Agent or Creditor"
source_labels: ["Creditor Agent or Creditor"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct debit instruction "], "locator": "/w:document/w:body/w:tbl[25]/w:tr[2]", "paragraph_id": null, "table_id": "T25"}, {"source_id": "src-000162", "locator": "T25 row2"}]
flows: ["flow-src-000162-p154-direct-debit-instruction"]
process_sections: []
message_ids: []
message_families: ["pacs.010"]
search_terms: ["Creditor Agent or Creditor", "pacs.010"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
---



# Creditor Agent or Creditor

Business context: Payments Clearing and Settlement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Forward 1st/1off Direct Debit | The creditor agent (or creditor for financial institution direct debits) sends the message to the clearing system in line with the clearing cycle. The clearing system forwards the message to the debtor agent and processes the direct debit in accordance with the settlement cycle, to initiate the debit to the Debtor's account. | Initiator | [T25](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0025.md) row 2 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Direct debit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.010`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Creditor Agent or Creditor`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Alternative initiator in DD activity table: creditor agent, or creditor for financial-institution DD, sends instruction into clearing cycle. (T25 row2)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->
