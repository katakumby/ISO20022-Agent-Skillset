---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_id: "participant-src-000014-market-infrastructure"
title: "Market Infrastructure"
source_labels: ["Market Infrastructure"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[5]", "paragraph_id": null, "table_id": "T13"}]
flows: []
process_sections: ["flow-src-000014-p111-selecting-the-appropriate-get-return-messages"]
message_ids: []
message_families: []
search_terms: ["Market Infrastructure"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Market Infrastructure

Business context: Cash Management. Source classification: business role.

## Definition

A multilateral system among participating financial institutions, including the operator of the system, used for the purposes of recording, clearing, or settling payments, securities, derivatives, or other financial transactions

Evidence: [T13](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0013.md), source row 5.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000014-system-member.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 5, column 2 |
| Can play the functional participant role in this source context | [Transaction Administrator/System](participant-src-000014-transaction-administrator-system.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 5, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Selecting the appropriate Get/Return Messages](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p111-selecting-the-appropriate-get-return-messages.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Market Infrastructure`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000014](../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx).
