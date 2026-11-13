---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_id: "participant-src-000014-settlement-agent"
title: "Settlement Agent"
source_labels: ["Settlement Agent"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Settlement Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Settlement Agent

Business context: Cash Management. Source classification: business role.

## Definition

National central bank or a private bank used to settle the cash leg of financial instruments: it provides the cash account to support the settlement of the transactions (trade, forex, securities) of another financial institution in central bank money.

Evidence: [T13](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0013.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000014-system-member.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 3, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Settlement Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000014](../../../evidence/omitted/335a400e27e5efca9fdafbb5.md).
