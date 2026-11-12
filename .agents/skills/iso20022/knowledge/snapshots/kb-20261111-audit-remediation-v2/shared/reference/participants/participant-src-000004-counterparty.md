---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-counterparty"
title: "Counterparty"
source_labels: ["Counterparty"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[2]", "paragraph_id": null, "table_id": "T17"}]
flows: ["flow-src-000004-p117-notification-to-account-owner", "flow-src-000004-p119-transaction-reconciliation-1", "flow-src-000004-p122-transaction-reconciliation-2"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Counterparty"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---







# Counterparty

Business context: Bank-to-Customer Cash Management. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Initiate transaction | The counterparty initiates a transaction with the account owner. This can be any type of transaction (such as securities, trade, purchase of goods, etc.). The counterparty will also initiate the financial leg of the transaction with its account servicer. The counterparty's account servicer may be or may not be equal to the account servicer of the account owner. | Initiator | [T17](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0017.md) row 2 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Notification to Account Owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p117-notification-to-account-owner.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Counterparty`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../evidence/omitted/52f543e2b58f688bc16fa140.md).

Bank-to-customer source context: [Transaction reconciliation initiated by the account owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0009.md). [flow Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md).

Bank-to-customer source context: [Transaction reconciliation initiated by a counterparty](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0010.md). [flow Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md).
