---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p250-buy-in-business-transaction"
title: "Buy-in BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[263]", "paragraph_id": "P263", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Buy-in BusinessTransaction"], "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "table_id": null}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-preferred-brokers", "participant-src-000052-settlement-agent"]
message_mapping_evidence: [{"source_label": "BuyInNotification", "message_id": "secl.007.001.03", "source_id": "src-000053", "locator": "file pages 254-273; 8 MX secl.007.001.03 BuyInNotificationV03"}, {"source_label": "BuyInResponse", "message_id": "secl.008.001.03", "source_id": "src-000053", "locator": "file pages 274-293; 9 MX secl.008.001.03 BuyInResponseV03"}, {"source_label": "BuyInConfirmation", "message_id": "secl.009.001.03", "source_id": "src-000053", "locator": "file pages 294-315; 10 MX secl.009.001.03 BuyInConfirmationV03"}]
message_ids: ["secl.007.001.03", "secl.008.001.03", "secl.009.001.03"]
message_families: ["secl.007", "secl.008", "secl.009"]
search_terms: ["Buy-in BusinessTransaction", "Central Counterparty (CCP)", "Central Counterparty", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---







# Buy-in BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The CCP buys stock to cover failed transactions. Notification may warn some days before the actual start (P252); response is optional under each CCP rules (P253). Confirmation reports the resulting transaction details (P254). T17 adds a possible delay request, telephone acknowledgment, obtaining securities via auction or preferred brokers, cancellation/replacement of settlement instructions, and out-of-scope payment of penalties/buy-in fees.

The related [source process](flow-src-000052-p161-buy-in-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Central Counterparty | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P251** The buy-in process is a process by which the central counterparty (CCP) buys in stock to cover failed transactions.

**P252** The BuyInNotification message is sent by a central counterparty (CCP) to the clearing member to notify the start of the buy-in process. This message can also be sent, as a warning, some days before the buy-in process actually starts.

**P253** The BuyInResponse message is sent by the clearing member to the CCP as a response to the previously sent buy-in notification message. The use of this message in the buy-in process is optional and depends on the rules set out by each central counterparty.

**P254** The BuyInConfirmation message is sent by the CCP to the clearing member to confirm the details of the transaction resulting from the buy-in process.

Source diagram evidence: [fig-0018](../documents/src-000052/diagrams/fig-0018.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessTransactions / Buy-in BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0018.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | BuyInNotification | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |
| 2 | BuyInResponse | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | Optional/potential; source conditions apply |
| 3 | BuyInConfirmation | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Narrative participant: [preferred brokers](../../../../../../../shared/reference/participants/participant-src-000052-preferred-brokers.md).

Narrative participant: [settlement agent](../../../../../../../shared/reference/participants/participant-src-000052-settlement-agent.md).

Exact definition bindings use the actual source053 MDR Part2 definition headings: [BuyInNotification / secl.007.001.03](../../../../messages/secl.007.001.03/index.md) (file pages 254-273; 8 MX secl.007.001.03 BuyInNotificationV03), [BuyInResponse / secl.008.001.03](../../../../messages/secl.008.001.03/index.md) (file pages 274-293; 9 MX secl.008.001.03 BuyInResponseV03), [BuyInConfirmation / secl.009.001.03](../../../../messages/secl.009.001.03/index.md) (file pages 294-315; 10 MX secl.009.001.03 BuyInConfirmationV03). Names outside this MDR scope remain unbound to a particular version.
