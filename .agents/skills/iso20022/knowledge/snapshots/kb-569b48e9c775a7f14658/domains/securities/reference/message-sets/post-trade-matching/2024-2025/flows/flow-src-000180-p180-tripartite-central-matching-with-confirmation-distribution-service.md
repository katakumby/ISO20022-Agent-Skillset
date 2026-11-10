---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service"
title: "Tripartite Central Matching With Confirmation Distribution Service"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[182]", "paragraph_id": "P182", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[183]", "paragraph_id": "P183", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:p[184]", "paragraph_id": "P184", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-investment-manager", "participant-src-000180-trust-bank", "participant-src-000180-trustee"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Tripartite Central Matching With Confirmation Distribution Service", "Central Matching Utility (JASDEC)", "Investment Manager", "Trust Bank", "Broker"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---



# Tripartite Central Matching With Confirmation Distribution Service

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

**P181** The executing broker sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the broker to the investment manager. The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU. The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process. If matched, the CMU sends both the confirmations received from the investment manager and from the executing broker to the trustee. If the trustee agrees with the details of the trade, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. Upon receipt of the affirmation message from the trustee, the CMU sends an affirmation status message to the executing broker and the trade can move into the settlement process.

Source diagram evidence: [fig-0012](../documents/src-000180/diagrams/fig-0012.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T14](../documents/src-000180/tables/tbl-0014.md).

| Source column 1 | Source column 2 | Source column 3 | Source column 4 |
| --- | --- | --- | --- |
| Description of Activities |  |  |  |
| Broker | Central Matching Utility (JASDEC) | Investment Manager | Trust Bank |
| Confirmation: The broker sends a trade confirmation to the CMU (JASDEC). | Confirmation (IM): The CMU (JASDEC) forwards the confirmation received from the broker to the investment manager. | Confirmation: The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU.  |  |
| Cancel Confirmation: If unmatched, the broker may send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. | Matching Status Messages: The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process.  | Cancel Confirmation: If unmatched, the investment manager may send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. |  |
|  | Status Advice: JASDEC will send a cancellation status advice to the broker and investment manager. |  |  |
|  | Confirmation (IM & broker): If matched, the CMU sends both the confirmations received from the investment manager and from the broker to the Trust Bank.  |  |  |
|  | Disaffirmation Status Message: Upon receipt of the disaffirmation message from the Trust Bank, the CMU sends a disaffirmation status message to the broker, which may lead to the broker sending a new confirmation to the CMU or a confirmation cancellation. |  | Disaffirmation: If the Trust Bank does not agree with the details of the trade, it sends a disaffirmation message to the CMU. |
|  | Affirmation Status Message: Upon receipt of the affirmation message from the Trust Bank, the CMU sends an affirmation status message to the  and the trade can move into the settlement process.  |  | Affirmation: If the Trust Bank agrees with the details of the trade, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: Description of BusinessActivities / BusinessProcess – Central Matching / Tripartite Central Matching With Confirmation Distribution Service.

## Curated process interpretation

With distribution, Broker confirmation is first forwarded by CMU to IM; the initial IM O.K. comparison leads to its own confirmation. The top CMU forwarding box is labelled Send Confirmation (IM) in the source, although P181 describes forwarding Broker data; that exact box label is retained. The CMU matching process returns cancellation status to receipt circles and matching status to each party decision. N (Unmatched) returns toward a new confirmation or cancellation; Y (Matched) forwards both confirmations to Trustee. Trustee N.G. disaffirms and prompts Broker rework; O.K. affirms, produces status and permits settlement continuations. P174/P181 and T13/T14 preserve the timing, agreement and cancellation alternatives.

[Complete source diagram reconstruction](../diagrams/processes/fig-0012.md). The source matching process is a narrow orange ellipse; native Mermaid uses a labelled rounded node while preserving all associated arrows. Color and exact shape remain in the original. Cancellation receipt markers do not imply a settlement reversal.
