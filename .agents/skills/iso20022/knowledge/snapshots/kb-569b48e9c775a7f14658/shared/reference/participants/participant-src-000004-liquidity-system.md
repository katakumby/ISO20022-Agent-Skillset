---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-liquidity-system"
title: "Liquidity System"
source_labels: ["Liquidity System"]
role_type: "functional system role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[6]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[7]", "paragraph_id": null, "table_id": "T14"}]
flows: ["flow-src-000004-p115-cash-positioning"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Liquidity System"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---





# Liquidity System

Business context: Bank-to-Customer Cash Management. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Collect available funds for investing/funding | All available liquidity is collected throughout the different systems. | Initiator | [T14](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0014.md) row 6 |
| Provide investment/funding final amount | Available liquidity is made available to the cash position system. | Initiator | [T14](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0014.md) row 7 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Liquidity System`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../evidence/omitted/52f543e2b58f688bc16fa140.md).

Bank-to-customer source context: [Cash positioning across internal systems and account servicer](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0007.md). [flow Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md).
