---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-reconciliation-system"
title: "Reconciliation System"
source_labels: ["Reconciliation System", "Reconciliation system"]
role_type: "functional system role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[11]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[8]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[9]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[6]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[9]", "paragraph_id": null, "table_id": "T17"}]
flows: ["flow-src-000004-p115-cash-positioning", "flow-src-000004-p119-transaction-reconciliation-1", "flow-src-000004-p122-transaction-reconciliation-2"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Reconciliation System"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Reconciliation System

Business context: Bank-to-Customer Cash Management. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Provide todays reconciled balance | Forecasted balance is reconciled with actual balance information received from the bank. | Initiator | [T14](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0014.md) row 11 |
| Receive cash movement information | The account owner's reconciliation system receives the cash movement information, both from the external feed, that is, the account servicer, and the internal accounting system. | Initiator | [T16](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0016.md) row 8 |
| Reconcile | The account owner's reconciliation system matches the information from the internal accounting system with the information received from the external feed (that is the account servicer). It identifies items which are not matched. These mismatched items may trigger an investigation process. | Initiator | [T16](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0016.md) row 9 |
| Receive information | The account owner's reconciliation system receives the cash movement information from the external feed (that is the account servicer) and receives information on the liabilities/claims from the internal accounting system. | Initiator | [T17](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0017.md) row 6 |
| Reconcile | The account owner's reconciliation system matches the information from the internal accounting system with the information received from the external feed, that is, the account servicer. It identifies items which are not matched. These mismatched items may trigger an investigation process. | Initiator | [T17](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0017.md) row 9 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Reconciliation System`, `Reconciliation system`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../evidence/omitted/52f543e2b58f688bc16fa140.md).

Bank-to-customer source context: [Cash positioning across internal systems and account servicer](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0007.md). [flow Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md).

Bank-to-customer source context: [Transaction reconciliation initiated by the account owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0009.md). [flow Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md).

Bank-to-customer source context: [Transaction reconciliation initiated by a counterparty](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0010.md). [flow Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md).
