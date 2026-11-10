---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[4]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000180-p120-business-process-diagram"]
process_sections: ["flow-src-000180-p120-business-process-diagram"]
message_ids: []
message_families: []
search_terms: ["Instructing Party"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---





# Instructing Party

Business context: Post-Trade Matching. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction. The party must own the account or have a power of attorney on the account.

Evidence: [T7](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0007.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Investment Manager](participant-src-000180-investment-manager.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 3, column 2 |
| Business role listed for this functional participant | [Confirmation Party](participant-src-000180-confirmation-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 6, column 2 |
| Business role listed for this functional participant | [Central Matching Utility (CMU)](participant-src-000180-central-matching-utility-cmu.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 8, column 2 |
| Business role listed for this functional participant | [Custodian](participant-src-000180-custodian.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 9, column 2 |
| Business role listed for this functional participant | [Order Giver](participant-src-000180-order-giver.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 11, column 2 |
| Business role listed for this functional participant | [Affirming Party](participant-src-000180-affirming-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 12, column 2 |
| Business role listed for this functional participant | [Prime Broker](participant-src-000180-prime-broker.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 13, column 2 |
| Business role listed for this functional participant | [Underwriter](participant-src-000180-underwriter.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 14, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [BusinessProcess Diagram](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p120-business-process-diagram.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Source context: [Trade lifecycle process overview](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0003.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p120-business-process-diagram.md).

Source context: [Trade lifecycle process overview](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0003.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p120-business-process-diagram.md).
