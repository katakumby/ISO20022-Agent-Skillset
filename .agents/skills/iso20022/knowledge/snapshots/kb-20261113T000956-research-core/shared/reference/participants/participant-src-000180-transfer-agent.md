---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-transfer-agent"
title: "Transfer Agent"
source_labels: ["Transfer Agent"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[6]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000180-p159-duplex-type", "flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
process_sections: ["flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.030.001.03"]
message_families: []
search_terms: ["Transfer Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Transfer Agent

Business context: Post-Trade Matching. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 4 | Disaffirmation: The Transfer Agent compares the trade detail with its own trade detail and if there are irreconcilable differences, sends a disaffirmation message to JASDEC.  | Transfer Agent | [T11](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0011.md) row 4 |
| Source activity row 6 | Affirmation: Should the trade detail on the confirmation agree with that of the Transfer Agent, it sends an affirmation message to JASDEC.   | Transfer Agent | [T11](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0011.md) row 6 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Transfer Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Post-trade matching scenario: [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0018.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0019.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0020.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Duplex local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md).
