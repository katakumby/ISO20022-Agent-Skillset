---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
participant_id: "participant-src-000079-global-custodian"
title: "Global Custodian"
source_labels: ["Global Custodian"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[2]", "paragraph_id": null, "table_id": "T9"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Global Custodian"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Global Custodian

Business context: Corporate Actions. Source classification: business role.

## Definition

Party that safekeeps and administers assets on behalf of the owner and that has a network of sub-custodians.

Evidence: [T9](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/tables/tbl-0009.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Account Servicer](participant-src-000079-account-servicer.md) | [T10](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/tables/tbl-0010.md) row 2, column 2 |
| Can play the functional participant role in this source context | [Account Owner](participant-src-000079-account-owner.md) | [T10](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/tables/tbl-0010.md) row 2, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Global Custodian`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000079](../../../evidence/omitted/2628a9d179f54e089e8f29f3.md).

Source diagram: [Corporate Actions business roles and functional participants](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/diagrams/overview/fig-0001.md).
