---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p146-through-type"
title: "Through Type"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-investment-manager", "participant-src-000180-trust-bank", "participant-src-000180-trustee"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Through Type", "Central Matching Utility (JASDEC)", "Investment Manager", "Trust Bank", "Broker"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---



# Through Type

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

**P147** The executing broker and the investment manager send a confirmation to the CMU. The CMU will forward the two confirmations received to the trustee. The trustee will send an affirmation message to the CMU if it agrees with the detail of the trade. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU will send an affirmation status message to the executing broker upon receipt of the affirmation message from the trustee. The trade will then move into the settlement process.

Source diagram evidence: [fig-0007](../documents/src-000180/diagrams/fig-0007.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T9](../documents/src-000180/tables/tbl-0009.md).

| Source column 1 | Source column 2 | Source column 3 | Source column 4 |
| --- | --- | --- | --- |
| Description of Activities |  |  |  |
| Broker | Central Matching Utility (JASDEC) | Investment Manager | Trust Bank |
| Confirmation: The broker sends a confirmation to JASDEC . | JASDEC will compare the Confirmation details received from the broker and investment manager. | Confirmation: The investment manager sends a confirmation of the trade to JASDEC. |  |
| Cancel Confirmation: The broker and investment manager may, for whatever reason, decide to cancel the confirmation and a new confirmation may be sent. Cancellation of the confirmation may also imply the cancellation of the trade, in which case a new confirmation will not be sent. |  | Cancel Confirmation: The investment manager and broker may decide to cancel the confirmation and a new confirmation may be sent. Cancellation of the confirmation may also imply the cancellation of the trade, in which case a new confirmation will not be sent. |  |
|  | Status Advice: JASDEC will send a cancellation status advice to the broker and investment manager.  |  |  |
|  | Confirmation (broker and IM): JASDEC will forward the confirmation received from both the broker and investment manager to the Trust Bank.   |  |  |
|  | Disaffirmation Status Message: JASDEC will send a disaffirmation status message to the broker upon receipt of the disaffirmation message from the Trust Bank. Once received it may lead to a cancellation of the confirmation or the sending of a new confirmation. |  | Disaffirmation: Should the Trust Bank not agree with the details of the trade, it will send a disaffirmation message to JASDEC. |
|  | Affirmation Status Message: JASDEC will send an affirmation status message to the broker upon receipt of the affirmation message from the Trust Bank. The trade will then move into the settlement process. |  | Affirmation: The Trust Bank will send an affirmation message to JASDEC if it agrees with the detail of the trade.  The message will bind the parties to the trade details of the confirmation being affirmed.  |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: Description of BusinessActivities / BusinessProcess – Local Matching / Through Type.

## Curated process interpretation

Broker and IM submit separate confirmations; CMU forwards each to Trustee. Trustee evaluates the details and follows N.G. to disaffirmation or O.K. to affirmation. CMU sends the corresponding status to Broker; disaffirmation loops to a new confirmation or cancellation, while affirmation continues toward settlement in the Broker, CMU and Trustee lanes. Cancellation inputs terminate at an unlabelled source endpoint within CMU; the separate cancellation-status action points to Broker and IM receipts. Two unconnected cancellation-choice diamonds remain as drawn. P147 says affirmation binds the trade details. T9 allows cancellation with a new confirmation, or cancellation of the trade without a new confirmation.

[Complete source diagram reconstruction](../diagrams/processes/fig-0007.md). The activity artwork says Trustee while T9 says Trust Bank. Both scoped records are linked; this local correspondence does not establish general institutional equivalence. Unlabelled endpoint symbols preserve source geometry without inventing a receiving activity.
