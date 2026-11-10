---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
participant_id: "participant-src-000343-executing-servicing-party"
title: "Executing/Servicing Party"
source_labels: ["Executing/Servicing Party", "Executing / Servicing Party"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000343", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000343", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[7]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Executing/Servicing Party"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Executing/Servicing Party

Business context: T2S Administration. Source classification: business role.

## Definition

Party that processes, monitors and reports on transactions received from an instructing party.

Evidence: [T6](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0006.md), source row 3.

Party that processes, monitors and reports on transactions received from the Instructing party.

Evidence: [T6](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0006.md), source row 7.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000343-system-member.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 8, column 2 |
| Can play the functional participant role in this source context | [System Transaction Administrator](participant-src-000343-system-transaction-administrator.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 8, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing/Servicing Party`, `Executing / Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000343](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`.
