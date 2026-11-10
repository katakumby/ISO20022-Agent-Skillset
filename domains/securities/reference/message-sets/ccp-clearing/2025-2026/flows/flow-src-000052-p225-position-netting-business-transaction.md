---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p225-position-netting-business-transaction"
title: "Position Netting BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Position Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Position Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Position Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Position Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}]
participants: ["participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-individual-or-general-clearing-member"]
message_mapping_evidence: [{"source_label": "NetPosition", "message_id": "secl.004.001.04", "source_id": "src-000053", "locator": "file pages 191-231; 5 MX secl.004.001.04 NetPositionV04"}]
message_ids: ["secl.004.001.04"]
message_families: ["secl.004"]
search_terms: ["Position Netting BusinessTransaction", "Central Counterparty (CCP)"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000030"]
---







# Position Netting BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The CCP reports the net position of all trade legs reported during the day (P226). T13 says the clearing member reconciles its calculation with CCP results using the netting parameters.

The related [source process](flow-src-000052-p125-netting-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P226** The NetPosition message is sent by a central counterparty (CCP) to the clearing member to report the net position of all trade legs reported during the day.

Source diagram evidence: [fig-0014](../documents/src-000052/diagrams/fig-0014.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessTransactions / Position Netting BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0014.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | NetPosition | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Exact definition bindings use the actual source053 MDR Part2 definition headings: [NetPosition / secl.004.001.04](../../../../messages/secl.004.001.04/index.md) (file pages 191-231; 5 MX secl.004.001.04 NetPositionV04). Names outside this MDR scope remain unbound to a particular version.
