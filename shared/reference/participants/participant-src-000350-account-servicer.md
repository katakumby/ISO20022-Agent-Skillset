---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
participant_id: "participant-src-000350-account-servicer"
title: "Account Servicer"
source_labels: ["Account Servicer"]
role_type: "functional participant role (matrix label; definition not extracted)"
aliases: []
source_locations: []
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Account Servicer"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Account Servicer

Business context: T2S CashAccountQueryAndReport. Source classification: functional participant role (matrix label; definition not extracted).

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Collateral Management System](participant-src-000350-collateral-management-system.md) | [T7](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0007.md) row 2, column 2 |
| Business role listed for this functional participant | [National Central Bank](participant-src-000350-national-central-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [Payment Bank](participant-src-000350-payment-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Central Security Depository (CSD)](participant-src-000350-central-security-depository-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0007.md) row 5, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Account Servicer`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000350](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`.

Cash-account source context: [Cash account business-role context](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0001.md). .
