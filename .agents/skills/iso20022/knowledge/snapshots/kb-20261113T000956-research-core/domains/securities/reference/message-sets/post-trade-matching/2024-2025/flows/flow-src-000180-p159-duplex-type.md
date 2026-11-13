---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p159-duplex-type"
title: "Duplex Type"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}]
participants: ["participant-src-000180-cash-settlement-agent", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-transfer-agent", "participant-src-000180-underwriter"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Duplex Type", "Central Matching Utility (JASDEC)", "Cash Settlement Agent", "Transfer Agent", "Underwriter"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---



# Duplex Type

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Matching Utility (JASDEC) | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-jasdec.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Cash Settlement Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-cash-settlement-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Underwriter | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P160** The Underwriter sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the Underwriter to the Transfer Agent. Should the trade detail on the confirmation agree with that of the Transfer Agent, it sends an affirmation message to the CMU. Upon receipt of the affirmation message from the Transfer Agent, the CMU forwards the confirmation received from the Underwriter to the Cash Settlement Agent. Should the trade detail on the confirmation agree with that of the Cash Settlement Agent, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU sends an affirmation status message to the Underwriter and the trade can move into the settlement process.

Source diagram evidence: [fig-0009](../documents/src-000180/diagrams/fig-0009.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T11](../documents/src-000180/tables/tbl-0011.md).

| Source column 1 | Source column 2 | Source column 3 | Source column 4 |
| --- | --- | --- | --- |
| Description of Activities |  |  |  |
| Underwriter | Central Matching Utility (JASDEC) | Transfer Agent | Cash Settlement Agent |
| Confirmation: The Underwriter sends a trade confirmation to JASDEC.  | Confirmation (Underwriter): JASDEC forwards the confirmation received from the Underwriter to the Transfer Agent. |  |  |
| Cancel Confirmation: Should the parties decide, for whatever reason, to cancel the trade a cancellation of the confirmation is sent from the Underwriter to JASDEC. A new confirmation may be sent.<br> | Disaffirmation Status Message: Upon receipt of the disaffirmation message, JASDEC sends a disaffirmation status message to the Underwriter which may lead to a new trade confirmation message from the Underwriter to JASDEC or a confirmation cancellation message from the Underwriter to JASDEC.     | Disaffirmation: The Transfer Agent compares the trade detail with its own trade detail and if there are irreconcilable differences, sends a disaffirmation message to JASDEC.  |  |
|  | Status Advice: JASDEC will send a cancellation status advice to the Underwriter and Transfer Agent |  |  |
|  | Confirmation (Underwriter): Upon receipt of the affirmation message from the Transfer Agent, JASDEC forwards the confirmation received from the Underwriter to the Cash Settlement Agent.   | Affirmation: Should the trade detail on the confirmation agree with that of the Transfer Agent, it sends an affirmation message to JASDEC.   |  |
|  | Disaffirmation Status Message: Upon receipt of the disaffirmation message from the Cash Settlement Agent, JASDEC sends a disaffirmation status message to the Underwriter which may lead to a trade confirmation cancellation or a new trade confirmation message from the Underwriter to JASDEC. |  | Disaffirmation: The Cash Settlement Agent compares the trade details of the confirmation (Underwriter) with its own trade detail and if there are irreconcilable differences sends a disaffirmation message to JASDEC. |
|  | Affirmation Status Message: JASDEC sends an affirmation status message to the Underwriter and the trade can move into the settlement process.   |  | Affirmation: Should the trade detail on the confirmation agree with that of the Cash Settlement Agent, it sends an affirmation message to JASDEC. The message will bind the parties to the trade details of the confirmation being affirmed. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: Description of BusinessActivities / BusinessProcess – Local Matching / Duplex Type.

## Curated process interpretation

Underwriter confirmation first goes through CMU to Transfer Agent. N.G. returns a disaffirmation status and rework/cancellation path to Underwriter. O.K. sends affirmation to CMU, which forwards the same underwriter confirmation to Cash Settlement Agent. Its N.G. and O.K. branches separately disaffirm or affirm. CMU sends the final status to Underwriter; accepted trade continues to settlement. The cancellation-status action has source arrows to Underwriter and Transfer Agent receipts; no additional cash-agent cancellation arrow is inserted in this activity diagram. P160 and T11 supply the corresponding responsibilities and conditions.

[Complete source diagram reconstruction](../diagrams/processes/fig-0009.md). The sequence figures use CashCorrespondent for a related fourth actor. The source labels remain distinct; the linked sequence preserves its own cancellation arrows.
