---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-cash-settlement-agent"
title: "Cash Settlement Agent"
source_labels: ["Cash Settlement Agent"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[7]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[8]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000180-p159-duplex-type", "flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
process_sections: ["flow-src-000180-p214-duplex-type", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
message_ids: []
message_families: []
search_terms: ["Cash Settlement Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Cash Settlement Agent

Business context: Post-Trade Matching. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 7 | Disaffirmation: The Cash Settlement Agent compares the trade details of the confirmation (Underwriter) with its own trade detail and if there are irreconcilable differences sends a disaffirmation message to JASDEC. | Cash Settlement Agent | [T11](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0011.md) row 7 |
| Source activity row 8 | Affirmation: Should the trade detail on the confirmation agree with that of the Cash Settlement Agent, it sends an affirmation message to JASDEC. The message will bind the parties to the trade details of the confirmation being affirmed. | Cash Settlement Agent | [T11](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0011.md) row 8 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Cash Settlement Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx).

Post-trade matching scenario: [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0018.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0019.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0020.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Source context: [Duplex local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md).
