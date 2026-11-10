---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
participant_id: "participant-src-000371-market-data-provider"
title: "Market Data Provider"
source_labels: ["Market Data Provider"]
role_type: "business role (matrix label; definition not extracted)"
aliases: []
source_locations: [{"source_id": "src-000371", "table_id": "T7", "row": 5, "rendered_file_page": 12}, {"source_id": "src-000371", "figure_id": "fig-0001", "paragraph_id": "P143", "rendered_file_page": 11}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Market Data Provider"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
issue_ids: ["issue-000050"]
---



# Market Data Provider

Business context: T2S SecuritiesAccountReferenceData. Source classification: business role (matrix label; definition not extracted).

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000371-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0007.md) row 5, column 2 |
| Can play the functional participant role in this source context | [Executing/Servicing Party](participant-src-000371-executing-servicing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0007.md) row 5, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Market Data Provider`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000371](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`.

Full-page inspection confirms T6 contains no definition for this label. T7 assigns both functional roles; figure1 shows only the executing/servicing connection. These claims remain separately scoped under issue-000050.
