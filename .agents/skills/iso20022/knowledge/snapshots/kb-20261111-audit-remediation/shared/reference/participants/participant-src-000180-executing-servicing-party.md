---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-executing-servicing-party"
title: "Executing/Servicing Party"
source_labels: ["Executing/Servicing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000180-p120-business-process-diagram"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Executing/Servicing Party"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---





# Executing/Servicing Party

Business context: Post-Trade Matching. Source classification: functional participant role.

## Definition

Party that processes, monitors and reports on transactions received from an instructing party.

Evidence: [T7](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0007.md), source row 5.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Broker/Executing Broker](participant-src-000180-broker-executing-broker.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 4, column 3 |
| Business role listed for this functional participant | [Central Counterparty](participant-src-000180-central-counterparty.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 5, column 3 |
| Business role listed for this functional participant | [Central Securities Depositories](participant-src-000180-central-securities-depositories.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 7, column 3 |
| Business role listed for this functional participant | [Central Matching Utility (CMU)](participant-src-000180-central-matching-utility-cmu.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 8, column 3 |
| Business role listed for this functional participant | [Custodian](participant-src-000180-custodian.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 9, column 3 |
| Business role listed for this functional participant | [Exchange](participant-src-000180-exchange.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 10, column 3 |
| Business role listed for this functional participant | [Prime Broker](participant-src-000180-prime-broker.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 13, column 3 |
| Business role listed for this functional participant | [Underwriter](participant-src-000180-underwriter.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 14, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing/Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Source context: [Trade lifecycle process overview](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0003.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p120-business-process-diagram.md).

Source context: [Trade lifecycle process overview](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0003.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p120-business-process-diagram.md).
