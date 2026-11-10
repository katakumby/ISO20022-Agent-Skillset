---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
participant_id: "participant-src-000368-market-data-provider"
title: "Market Data Provider"
source_labels: ["Market Data Provider"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[7]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Market Data Provider"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Market Data Provider

Business context: T2S PartyReferenceData. Source classification: business role.

## Definition

An organization that provides data on financial instruments to other parties. Such as services provided by Thomson, Reuters, Bloomberg …

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0006.md), source row 7.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000368-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0007.md) row 5, column 2 |
| Can play the functional participant role in this source context | [Executing / Servicing Party](participant-src-000368-executing-servicing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0007.md) row 5, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Market Data Provider`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000368](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`.
