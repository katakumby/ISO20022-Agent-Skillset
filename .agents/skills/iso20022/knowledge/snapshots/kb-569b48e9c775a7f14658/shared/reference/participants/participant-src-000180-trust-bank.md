---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-trust-bank"
title: "Trust Bank"
source_labels: ["Trust Bank", "Trust Bank:"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[7]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[8]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[7]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[8]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[7]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[8]", "paragraph_id": null, "table_id": "T14"}]
flows: ["flow-src-000180-p146-through-type", "flow-src-000180-p165-end-of-process-report-for-listed-derivatives", "flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Trust Bank"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Trust Bank

Business context: Post-Trade Matching. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 7 | Disaffirmation: Should the Trust Bank not agree with the details of the trade, it will send a disaffirmation message to JASDEC. | Trust Bank | [T9](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0009.md) row 7 |
| Source activity row 8 | Affirmation: The Trust Bank will send an affirmation message to JASDEC if it agrees with the detail of the trade.  The message will bind the parties to the trade details of the confirmation being affirmed.  | Trust Bank | [T9](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0009.md) row 8 |
| Source activity row 7 | Disaffirmation: Should the Trust Bank not agree with the details of the confirmations, it may send a disaffirmation message to the CMU (JASDEC).  | Trust Bank | [T13](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0013.md) row 7 |
| Source activity row 8 | Affirmation: If the Trust Bank agrees with the details of the confirmations, it may send an affirmation message to the CMU.  The message will bind the parties to the trade details of the confirmation being affirmed. | Trust Bank | [T13](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0013.md) row 8 |
| Source activity row 7 | Disaffirmation: If the Trust Bank does not agree with the details of the trade, it sends a disaffirmation message to the CMU. | Trust Bank | [T14](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0014.md) row 7 |
| Source activity row 8 | Affirmation: If the Trust Bank agrees with the details of the trade, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. | Trust Bank | [T14](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0014.md) row 8 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [End of Process Report for Listed Derivatives](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Trust Bank`, `Trust Bank:`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Source context: [Through-type local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md).

Source context: [Tripartite central matching without distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md).

Source context: [Tripartite central matching with distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0012.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md).

Source context: [Listed-derivatives end-of-process reporting activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md).
