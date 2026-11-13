---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
participant_id: "participant-src-000052-broker"
title: "Broker"
source_labels: ["Broker"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[9]", "paragraph_id": null, "table_id": "T10"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Broker"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Broker

Business context: CCP Clearing. Source classification: business role.

## Definition

The party that provides services to its members for the settlement of transactions and holding of assets.

Evidence: [T10](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0010.md), source row 9.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Clearing Member (G or I)](participant-src-000052-clearing-member-g-or-i.md) | [T11](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0011.md) row 5, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Broker`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000052](../../../evidence/omitted/b45c53bac2be08dee677b607.md).
