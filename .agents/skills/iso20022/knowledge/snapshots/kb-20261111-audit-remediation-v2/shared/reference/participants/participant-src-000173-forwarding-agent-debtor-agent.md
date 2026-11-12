---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-forwarding-agent-debtor-agent"
title: "Forwarding Agent / Debtor Agent"
source_labels: ["Forwarding Agent / Debtor Agent"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[3]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[4]", "paragraph_id": null, "table_id": "T23"}]
flows: ["flow-src-000173-p140-complex-scenario"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Forwarding Agent / Debtor Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Forwarding Agent / Debtor Agent

Business context: Payments Initiation. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Receive payment order and check authentication (2) | The forwarding agent, if present and debtor agent receive the payment orders from the previous party in the chain. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 3 |
| Technical Validation (3.1), risk assessment (3.2), apply business rules (3.3) and prepare payment orders for onward transmission (3.4). | Necessary checks before processing the payment order further include, for example, syntactical validation.<br>The debtor agent undertakes the necessary risk checks when the execution date is reached, in order to further process the payment. Examples of dynamic risk assessment are: is sufficient cash available, has cover been received, etc.<br>Examples of static risk assessment are: check limits, embargo, money laundering information, etc.<br>The forwarding agent (if any) or debtor agent will check business rules that he has logged for the initiating party sending the file. These business rules include information about the customer's profile: the type of transactions the customer is allowed to send, the authorisation procedures set up between customer and receiving agent, etc.<br>The forwarding agent rebuilds the payment order by:<br>subtracting the failed/invalid individual payment instructions from the payment orders he received<br>bulking, if relevant, of several payment orders coming from different initiating parties or agents acting as forwarding agents. The merge criteria are defined by the bank | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 4 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Forwarding Agent / Debtor Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).
