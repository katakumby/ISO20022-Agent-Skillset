---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p201-business-process-settlement-management-settlement-netting-process"
title: "BusinessProcess - Settlement Management – Settlement Netting Process"
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:p[202]", "paragraph_id": "P202", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:tbl[16]", "paragraph_id": null, "table_id": "T16"}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-central-securities-depository-csd", "participant-src-000052-clearing-member-cm", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-paying-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess - Settlement Management – Settlement Netting Process", "Central Securities Depository (CSD)", "Central Counterparty (CCP)", "Central Counterparty", "Clearing Member (CM)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# BusinessProcess - Settlement Management – Settlement Netting Process

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in [the related source process](flow-src-000052-p155-settlement-netting-process.md).

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Securities Depository (CSD) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-securities-depository-csd.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Central Counterparty | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing Member (CM) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000052/diagrams/fig-0010.md). The source reconstruction and actual review record are linked below.

Source table [T16](../documents/src-000052/tables/tbl-0016.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Descriptions of the BusinessActivities |  |  |
| Central Securities Depository (CSD) | Central Counterparty (CCP) | Clearing Member (CM) |
| Report the settlement results:<br>The CSD sends the settlement result to the CCP (either the confirmation or pending or failed settlement). | OPTIONAL<br>Positions/Instructions update:<br>Based on the settlement result received from the CSD, the CCP updates the positions/instructions. |  |
|  | OPTIONAL<br>(some CCPs settle gross transactions) <br>CCP does trade netting |  |
| Report the list of Corporate Events: <br>The CSD sends the list of all corporate events (CEs) that are announced. | OPTIONAL<br>Based on the list of corporate events received from the CSD, the CCP selects those related to the positions/instructions. <br>The CCP will also apply these CEs to the impacted positions/instructions. |  |
|  | Settlement Instructions:<br>The CCP builds and sends all settlement instructions to the CSD and settlement obligations to clearing members. |  |
| Process the instruction:<br>The CSD processes the settlement instructions.<br> |  | Process the information:<br>The CMs will send the settlement instructions to their paying agent unless they have signed a power of attorney with the central counterparty.<br>In the latter case, the CCP is responsible for sending the settlement instructions to the CSD on behalf of the CM. |
| Failed Trades:<br>The CSD sends a report with all failed trades and the CCPs will also report these failed trades if the GCM is not part of the settlement chain. |  |  |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: Description of BusinessActivities / BusinessProcess - Settlement Management – Settlement Netting Process.

## Curated activity and relationship account

Three source lanes assign CSD reporting/processing, CCP updates/netting/event application/instruction building, and clearing-member information processing. The three CCP optional activities remain individually labeled; CNS-only applies to position/instruction update. Both CSD event input and settlement results are preserved, as are all three final paths. T16 additionally describes clearing-member instructions to a paying agent, the power-of-attorney exception, and failed-trade reporting when the general clearing member is absent from the settlement chain.

[Source activity reconstruction](../diagrams/processes/fig-0010.md).

- [central counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- [individual or general clearing member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
- [paying agent](../../../../../../../shared/reference/participants/participant-src-000052-paying-agent.md).
- [central securities depository csd](../../../../../../../shared/reference/participants/participant-src-000052-central-securities-depository-csd.md).
