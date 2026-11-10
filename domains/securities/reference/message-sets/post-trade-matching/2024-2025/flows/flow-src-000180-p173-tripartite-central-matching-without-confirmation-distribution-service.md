---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service"
title: "Tripartite Central Matching Without Confirmation Distribution Service"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[176]", "paragraph_id": "P176", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[177]", "paragraph_id": "P177", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[178]", "paragraph_id": "P178", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-investment-manager", "participant-src-000180-trust-bank", "participant-src-000180-trustee"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Tripartite Central Matching Without Confirmation Distribution Service", "Central Matching Utility (JASDEC)", "Investment Manager", "Trust Bank", "Broker"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---



# Tripartite Central Matching Without Confirmation Distribution Service

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Matching Utility (JASDEC) | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-jasdec.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Trust Bank | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-trust-bank.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P174** The executing broker sends a trade confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The investment manager sends the corresponding trade confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. The CMU will forward the confirmation received from both the executing broker and investment manager to the trustee. If the trustee agrees with the details of the confirmations, it may send an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. Upon receipt of the affirmation message, the CMU will send an affirmation status message to the executing broker and the trade may move into the settlement process.

Source diagram evidence: [fig-0011](../documents/src-000180/diagrams/fig-0011.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T13](../documents/src-000180/tables/tbl-0013.md).

| Source column 1 | Source column 2 | Source column 3 | Source column 4 |
| --- | --- | --- | --- |
| Description of Activities |  |  |  |
| Broker | Central Matching Utility (JASDEC) | Investment Manager | Trust Bank |
| Confirmation: The broker sends a trade confirmation to the CMU (JASDEC).  | Matching Status Messages: The CMU (JASDEC) performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. | Confirmation: The investment manager sends a trade confirmation to the CMU (JASDEC). |  |
| Cancel Confirmation: If unmatched, the broker may send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. |  | Cancel Confirmation: If unmatched, the investment manager may send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. |  |
|  | Status Advice: JASDEC will send a cancellation status advice to the broker and investment manager. |  |  |
|  | Confirmation (IM & broker): If matched, the CMU forwards both confirmations to the Trust Bank.  |  |  |
|  | Disaffirmation Status Message: The CMU sends a disaffirmation status message to the broker, which may lead to a new confirmation being sent to the CMU of a confirmation cancellation being sent to the CMU. |  | Disaffirmation: Should the Trust Bank not agree with the details of the confirmations, it may send a disaffirmation message to the CMU (JASDEC).  |
|  | Affirmation Status Message: Upon receipt of the affirmation message, the CMU will send an affirmation status message to the broker and the trade may move into the settlement process.  |  | Affirmation: If the Trust Bank agrees with the details of the confirmations, it may send an affirmation message to the CMU.  The message will bind the parties to the trade details of the confirmation being affirmed. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: Description of BusinessActivities / BusinessProcess – Central Matching / Tripartite Central Matching Without Confirmation Distribution Service.

## Curated process interpretation

Without distribution, Broker and IM independently send confirmations to the matching process. The CMU matching process returns cancellation status to receipt circles and matching status to each party decision. N (Unmatched) returns toward a new confirmation or cancellation; Y (Matched) forwards both confirmations to Trustee. Trustee N.G. disaffirms and prompts Broker rework; O.K. affirms, produces status and permits settlement continuations. P174/P181 and T13/T14 preserve the timing, agreement and cancellation alternatives.

[Complete source diagram reconstruction](../diagrams/processes/fig-0011.md). The source matching process is a narrow orange ellipse; native Mermaid uses a labelled rounded node while preserving all associated arrows. Color and exact shape remain in the original. Cancellation receipt markers do not imply a settlement reversal.
