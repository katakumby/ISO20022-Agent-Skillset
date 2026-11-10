---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p217-trade-leg-notification-business-transaction"
title: "Trade Leg Notification BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification BusinessTransaction"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification BusinessTransaction"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification BusinessTransaction"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification BusinessTransaction"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}]
participants: ["participant-src-000052-buyer", "participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-seller", "participant-src-000052-trading-member-firm", "participant-src-000052-trading-venue"]
message_mapping_evidence: [{"source_label": "TradeLegNotification", "message_id": "secl.001.001.05", "source_id": "src-000053", "locator": "file pages 6-63; 2 MX secl.001.001.05 TradeLegNotificationV05"}, {"source_label": "TradeLegStatement", "message_id": "secl.003.001.05", "source_id": "src-000053", "locator": "file pages 124-190; 4 MX secl.003.001.05 TradeLegStatementV05"}]
message_ids: ["secl.001.001.05", "secl.003.001.05"]
message_families: ["secl.001", "secl.003"]
search_terms: ["Trade Leg Notification BusinessTransaction", "Central Counterparty (CCP)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000030"]
---







# Trade Leg Notification BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The CCP reports the executed trade after novation and then reports a summary for a period during or at the end of the day. P218 describes both trade sides from the clearing member perspective; P219 makes reporting timing dependent on CCP processes.

The related [source process](flow-src-000052-p113-trade-management-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P218** The TradeLegNotification message is sent by the central counterparty (CCP) to a clearing member to report the trade that has been executed by the trading platform. Through novation the original contract between the buyer and seller is extinguished and replaced by two new contracts, one between the CCP and the buyer and one between the CCP and the seller. The CCP reports both sides of the trade from the clearing member perspective. 

**P219** At the end of the day (or during the day depending on each CCP’s internal process), the CCP reports a summary of all trades that occurred for a specific period in that day, that is, the CCP sends the TradeLegStatement message to the clearing member.

Source diagram evidence: [fig-0012](../documents/src-000052/diagrams/fig-0012.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessTransactions / Trade Leg Notification BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0012.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | TradeLegNotification | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |
| 2 | TradeLegStatement | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Narrative participant: [trading venue](../../../../../../../shared/reference/participants/participant-src-000052-trading-venue.md).

Narrative participant: [trading member firm](../../../../../../../shared/reference/participants/participant-src-000052-trading-member-firm.md).

Narrative participant: [buyer](../../../../../../../shared/reference/participants/participant-src-000052-buyer.md).

Narrative participant: [seller](../../../../../../../shared/reference/participants/participant-src-000052-seller.md).

Exact definition bindings use the actual source053 MDR Part2 definition headings: [TradeLegNotification / secl.001.001.05](../../../../messages/secl.001.001.05/index.md) (file pages 6-63; 2 MX secl.001.001.05 TradeLegNotificationV05), [TradeLegStatement / secl.003.001.05](../../../../messages/secl.003.001.05/index.md) (file pages 124-190; 4 MX secl.003.001.05 TradeLegStatementV05). Names outside this MDR scope remain unbound to a particular version.
