---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-debtor-agent-creditor-agent"
title: "Debtor Agent / Creditor Agent"
source_labels: ["Debtor Agent / Creditor Agent"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[10]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[11]", "paragraph_id": null, "table_id": "T23"}]
flows: ["flow-src-000173-p140-complex-scenario"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Debtor Agent / Creditor Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Debtor Agent / Creditor Agent

Business context: Payments Initiation. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Internal bookkeeping (8) | The debtor agent debits the internal account where the provision for further processing of the payment order has been blocked. The creditor agent credits the creditor's account in its books. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 10 |
| Print Cheques (9) | If the initiating party has asked the debtor agent to issue a cheque to pay the creditor, the debtor agent or creditor agent will print a cheque. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 11 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Debtor Agent / Creditor Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx).
