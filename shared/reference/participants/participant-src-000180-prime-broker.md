---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-prime-broker"
title: "Prime Broker"
source_labels: ["Prime Broker"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[17]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000180-p185-bilateral-central-matching", "flow-src-000180-p274-bilateral-central-matching", "flow-src-000180-p278-bilateral-central-matching-cancellation"]
process_sections: ["flow-src-000180-p274-bilateral-central-matching", "flow-src-000180-p278-bilateral-central-matching-cancellation"]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.044.001.04"]
message_families: []
search_terms: ["Prime Broker"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---











# Prime Broker

Business context: Post-Trade Matching. Source classification: business role.

## Definition

A broker which acts as settlement agent, provides custody for assets, provides financing for leverage, and prepares daily account statements for its clients, who are money managers, hedge funds, market makers, arbitrageurs, specialists and other professional investors.

Evidence: [T7](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0007.md), source row 17.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000180-instructing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 13, column 2 |
| Can play the functional participant role in this source context | [Executing/Servicing Party](participant-src-000180-executing-servicing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 13, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p274-bilateral-central-matching.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bilateral Central Matching Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p278-bilateral-central-matching-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Prime Broker`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx).

Post-trade matching scenario: [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p274-bilateral-central-matching.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0031.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Bilateral Central Matching Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p278-bilateral-central-matching-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0032.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Post-trade business-actor context](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0002.md).

Source context: [Bilateral central matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0013.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md).
