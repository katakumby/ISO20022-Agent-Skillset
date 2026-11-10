---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
participant_id: "participant-src-000350-market-infrastructure"
title: "Market Infrastructure"
source_labels: ["Market Infrastructure"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[7]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Market Infrastructure"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Market Infrastructure

Business context: T2S CashAccountQueryAndReport. Source classification: business role.

## Definition

The party that provides, through common membership, services to create a fair and open process for the execution of transactions between trading parties, and the creation of settlement obligations. Example include an exchange.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0006.md), source row 7.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Account Owner](participant-src-000350-account-owner.md) | [T7](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0007.md) row 6, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Market Infrastructure`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000350](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`.

Cash-account source context: [Cash account business-role context](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0001.md). .
