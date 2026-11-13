---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p191-business-process-trade-management"
title: "BusinessProcess - Trade Management"
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Trade Management"], "locator": "/w:document/w:body/w:p[191]", "paragraph_id": "P191", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Trade Management"], "locator": "/w:document/w:body/w:p[192]", "paragraph_id": "P192", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Trade Management"], "locator": "/w:document/w:body/w:p[193]", "paragraph_id": "P193", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Trade Management"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}]
participants: ["participant-src-000052-buyer", "participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-clearing-member-cm", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-seller", "participant-src-000052-trading-member-firm", "participant-src-000052-trading-venue"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess - Trade Management", "Central Counterparty (CCP)", "Clearing Member (CM)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# BusinessProcess - Trade Management

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in [the related source process](flow-src-000052-p113-trade-management-process.md).

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing Member (CM) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0006](../documents/src-000052/diagrams/fig-0006.md). The source reconstruction and actual review record are linked below.

Source table [T12](../documents/src-000052/tables/tbl-0012.md).

| Source column 1 | Source column 2 |
| --- | --- |
| Descriptions of the BusinessActivities |  |
| Central Counterparty (CCP) | Clearing Member (CM) |
| Accept trade: <br>After acceptance of a trade, the CCP splits the trade into two legs. The CCP becomes thus the counterparty of both the seller and the buyer.<br>Generally, the buyer and the seller become anonymous (depending on the markets).<br>At the end of the day (or during the day depending on each CCP’s internal process), the CCP reports a summary of all trades that occurred for a specific period in that day. This reporting can then be done intra-day or end of day.<br> | Process the trade information: <br>Technical and business validation of the transaction before further processing.<br>There are two cases:<br>1) The CM receives trades from the CCP and from its Trading Member Firm. If the CM does not pair or match the trade received from the CCP with a trade received from a trading member firm, the CM contacts this trading member firm (out of scope).<br>2) The CM only received trades from the CCP and in this case, the CM can never identify an incorrect trade (since the CM has not received the trade confirmation from the trading firm. No matching can be done). |
| Did the trading venue (Exchange or MTF) send a cancellation?<br>If NO, end of this process.<br>If YES, the CCP cancels the trade leg.<br>Note: Cancellations by the trading venue are very rare. However, arrangements between trading and clearing venues exist to send opposite trades instead of cancellation. In this case, it would then fall into the flow “Accept Trade” above. | Process cancellation: <br>Technical and business validation of the details of the cancellation. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: Description of BusinessActivities / BusinessProcess - Trade Management.

## Curated activity and relationship account

Two separate source start points represent the accepted-trade and cancellation paths. The negative cancellation decision ends immediately; the positive branch cancels the trade leg and the member processes the cancellation. Pink trading-venue notes provide out-of-scope trigger context, not additional message arrows. T12 preserves the independent trade-matching cases, contact with a trading member firm, and the opposite-trade alternative. Start/End words are explanatory marker labels added to the source circles.

[Source activity reconstruction](../diagrams/processes/fig-0006.md).

- [central counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- [individual or general clearing member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
- [trading venue](../../../../../../../shared/reference/participants/participant-src-000052-trading-venue.md).
- [trading member firm](../../../../../../../shared/reference/participants/participant-src-000052-trading-member-firm.md).
- [buyer](../../../../../../../shared/reference/participants/participant-src-000052-buyer.md).
- [seller](../../../../../../../shared/reference/participants/participant-src-000052-seller.md).
