---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p165-end-of-process-report-for-listed-derivatives"
title: "End of Process Report for Listed Derivatives"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-investment-manager", "participant-src-000180-trust-bank", "participant-src-000180-trustee"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["End of Process Report for Listed Derivatives", "Central Matching Utility (JASDEC)", "Investment Manager", "Trust Bank", "Broker"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---



# End of Process Report for Listed Derivatives

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

**P166** The executing broker sends a confirmation of the trade to the CMU. The investment manager sends a confirmation of the trade to the CMU. The CMU will forward the two confirmations received to the trustee. After the executing broker sends all the trade confirmations on that day, the executing broker sends a delivery amount report to the CMU. The CMU forwards the delivery amount report to the trustee. The executing broker sends an end of process report of the confirmation to the CMU. After the investment manager sends all the trade confirmations on that day, the investment manager sends an end of process report of the confirmation to the CMU. The CMU forwards the end of day reports of the confirmation from both parties to the trustee.

Source diagram evidence: [fig-0010](../documents/src-000180/diagrams/fig-0010.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T12](../documents/src-000180/tables/tbl-0012.md).

| Source column 1 | Source column 2 | Source column 3 | Source column 4 |
| --- | --- | --- | --- |
| Description of Activities |  |  |  |
| Broker | Central Matching Utility (JASDEC) | Investment Manager | Trust Bank: |
| Confirmation The broker sends a confirmation of the trade to JASDEC . | JASDEC will compare the Confirmation details received from the broker and investment manager. | Confirmation: The investment manager sends a confirmation of the trade to JASDEC. |  |
|  | Confirmation (broker and IM): JASDEC will forward the confirmation received from both the broker and investment manager to the Trust Bank.   |  |  |
| Delivery Amount Report: The broker sends a delivery amount report to JASDEC. | Delivery Amount Report: JASDEC forwards the delivery amount report to the Trust bank |  |  |
| End of Day Report of Confirmation: The broker sends an end of day report of the confirmation to JASDEC. |  | End of Day Report of Confirmation: The investment manager sends an end of day report of the confirmation to JASDEC. |  |
|  | End of Day Report (IM): JASDEC forwards the end of day report of the confirmation of both parties to the Trust Bank and the trade can move to the NAV calculation process. |  |  |
| End of Day Report of Delivery Amount: The broker sends an end of day report of delivery amount to JASDEC. | End of Day Report of Delivery Amount: JASDEC forwards the end of day report of delivery amount to the Trust Bank and the trade can move into the settlement process.  |  |  |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: Description of BusinessActivities / BusinessProcess – Local Matching / End of Process Report for Listed Derivatives.

## Curated process interpretation

The source blue rounded area groups the initial through-type confirmation exchanges and delivery amount reporting. Broker and IM confirmations are forwarded separately to Trustee. Broker Delivery Amount Report is forwarded to Trustee as a separate exchange. After the respective daily confirmations, Broker and IM send End Of Day Report of Confirmation; CMU forwards both into one Trustee receipt marker leading to NAV calculation. Broker End Of Day Report of Delivery Amount Report is forwarded into a separate Trustee receipt leading to settlement. Broker settlement continuation receives dashed lines from both of its report actions. CMU has its own unlabelled end marker after delivery-report forwarding. P166 and T12 preserve timing and responsibilities.

[Complete source diagram reconstruction](../diagrams/processes/fig-0010.md). The original blue grouping and darker delivery row span several participant lanes. Mermaid describes this complete boundary in an explicit labelled note rather than duplicating the same node inside overlapping subgraphs. Source grouping, not additional process ordering, is intended. DeliveryAmountReport is explicitly proprietary in sequence figure21/P229; it is not merged with ISO SecuritiesEndOfProcessReport.
