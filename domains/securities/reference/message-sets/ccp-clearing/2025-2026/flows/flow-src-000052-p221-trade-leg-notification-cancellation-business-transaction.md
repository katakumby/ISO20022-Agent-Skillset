---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p221-trade-leg-notification-cancellation-business-transaction"
title: "Trade Leg Notification Cancellation BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification Cancellation BusinessTransaction"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification Cancellation BusinessTransaction"], "locator": "/w:document/w:body/w:p[222]", "paragraph_id": "P222", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification Cancellation BusinessTransaction"], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Trade Leg Notification Cancellation BusinessTransaction"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}]
participants: ["participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-trading-venue"]
message_mapping_evidence: [{"source_label": "TradeLegNotification", "message_id": "secl.001.001.05", "source_id": "src-000053", "locator": "file pages 6-63; 2 MX secl.001.001.05 TradeLegNotificationV05"}, {"source_label": "TradeLegNotificationCancellation", "message_id": "secl.002.001.05", "source_id": "src-000053", "locator": "file pages 64-123; 3 MX secl.002.001.05 TradeLegNotificationCancellationV05"}]
message_ids: ["secl.001.001.05", "secl.002.001.05"]
message_families: ["secl.001", "secl.002"]
search_terms: ["Trade Leg Notification Cancellation BusinessTransaction", "Central Counterparty (CCP)"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000030"]
---







# Trade Leg Notification Cancellation BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The CCP notifies cancellation of a previously sent TradeLegNotification. P223 expressly prohibits using this message to cancel TradeLegStatement. T12 distinguishes a cancellation request from the trading venue from an opposite-trade arrangement, which follows the ordinary Accept Trade path.

The related [source process](flow-src-000052-p113-trade-management-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P222** The TradeLegNotificationCancellation message is sent by a central counterparty (CCP) to the clearing member to notify the cancellation of a TradeLegNotification message previously sent. 

**P223** The TradeLegNotificationCancellation message cannot be sent to notify the cancellation of the TradeLegStatement message.

Source diagram evidence: [fig-0013](../documents/src-000052/diagrams/fig-0013.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessTransactions / Trade Leg Notification Cancellation BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0013.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | TradeLegNotification | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |
| 2 | TradeLegNotificationCancellation | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Narrative participant: [trading venue](../../../../../../../shared/reference/participants/participant-src-000052-trading-venue.md).

Exact definition bindings use the actual source053 MDR Part2 definition headings: [TradeLegNotification / secl.001.001.05](../../../../messages/secl.001.001.05/index.md) (file pages 6-63; 2 MX secl.001.001.05 TradeLegNotificationV05), [TradeLegNotificationCancellation / secl.002.001.05](../../../../messages/secl.002.001.05/index.md) (file pages 64-123; 3 MX secl.002.001.05 TradeLegNotificationCancellationV05). Names outside this MDR scope remain unbound to a particular version.
