---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
participant_id: "participant-src-000347-account-owner"
title: "Account Owner"
source_labels: ["Account Owner"]
role_type: "functional participant role (matrix label; definition not extracted)"
aliases: []
source_locations: []
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Account Owner"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Account Owner

Business context: T2S Billing. Source classification: functional participant role (matrix label; definition not extracted).

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Market Infrastructure](participant-src-000347-market-infrastructure.md) | [T7](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0007.md) row 6, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Account Owner`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000347](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`.

Billing source context: [Billing business roles and functional participants](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0001.md). Source role-matrix inconsistency remains open under issue-000038.
