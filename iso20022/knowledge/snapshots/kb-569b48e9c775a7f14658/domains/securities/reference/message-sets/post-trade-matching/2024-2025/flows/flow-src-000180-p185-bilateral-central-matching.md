---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p185-bilateral-central-matching"
title: "Bilateral Central Matching"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[189]", "paragraph_id": "P189", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-investment-manager", "participant-src-000180-prime-broker"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Bilateral Central Matching", "Central Matching Utility (JASDEC)", "Investment Manager", "Prime Broker", "Broker"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
issue_ids: ["issue-000031"]
---





# Bilateral Central Matching

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Matching Utility (JASDEC) | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-jasdec.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Prime Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P186** The executing broker sends a confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The prime broker sends a confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties reflecting the outcome of the matching process. If the confirmations are matched, the trade can move into the settlement process.

Source diagram evidence: [fig-0013](../documents/src-000180/diagrams/fig-0013.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T15](../documents/src-000180/tables/tbl-0015.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Description of Activities |  |  |
| Broker | Central Matching Utility (JASDEC) | Broker |
| Confirmation: Broker 1 sends a confirmation to the CMU (JASDEC).  | Matching Status Messages: The CMU performs a matching process between the two confirmations and sends matching status messages to both parties reflecting the outcome of the matching process. If the confirmations are matched, the trade can move into the settlement process.  | Confirmation: Broker 2 sends a confirmation to the CMU (JASDEC).  |
| Cancel Confirmation: If the confirmation is unmatched, it may lead to the sending of a confirmation cancellation from the broker to the CMU or to the sending of a new confirmation from the broker to the CMU. |  | Cancel Confirmation: If the confirmation is unmatched, it may lead to the sending of a confirmation cancellation from the broker to the CMU or to the sending of a new confirmation from the broker to the CMU. |
|  | Status Advice: JASDEC will send a cancellation status advice to the broker and investment manager. |  |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: Description of BusinessActivities / BusinessProcess – Central Matching / Bilateral Central Matching.

## Curated process interpretation

The source activity labels both outer lanes Broker. Each submits a confirmation or cancellation to CMU. Cancellation status goes to the corresponding receipt marker; matching status goes to a local choice. N (Unmatched) loops to a new confirmation or cancellation; Y (Matched) continues toward settlement in both broker lanes and the CMU lane. P186 identifies the second narrative actor as Prime Broker. The reconstruction preserves the two identical artwork lane labels while linking the narrative-specific role separately.

[Complete source diagram reconstruction](../diagrams/processes/fig-0013.md). Both Broker lane instances remain distinct; the canonical business role may appear in more than one instance. The source does not specify an institution name.

## Source recipient inconsistency

The narrative on Word27 calls the second party the prime broker. The diagram and T15 label two brokers, with Broker1/Broker2 in activity cells. However, the final T15 Status Advice cell on Word28 names broker and investment manager as cancellation-status recipients. Preserve this unresolved source vocabulary in [issue-000031](../../../../../../../tracking/issues.md#issue-000031); do not silently replace either recipient.
