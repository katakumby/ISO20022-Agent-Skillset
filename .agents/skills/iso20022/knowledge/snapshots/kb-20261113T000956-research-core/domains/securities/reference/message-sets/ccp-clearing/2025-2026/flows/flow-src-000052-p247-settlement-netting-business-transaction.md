---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p247-settlement-netting-business-transaction"
title: "Settlement Netting BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Settlement Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[247]", "paragraph_id": "P247", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Settlement Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Settlement Netting BusinessTransaction"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}]
participants: ["participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-central-securities-depository-csd", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-paying-agent"]
message_mapping_evidence: [{"source_label": "SettlementObligationReport", "message_id": "secl.010.001.04", "source_id": "src-000053", "locator": "file pages 316-372; 11 MX secl.010.001.04 SettlementObligationReportV04"}]
message_ids: ["secl.010.001.04"]
message_families: ["secl.010"]
search_terms: ["Settlement Netting BusinessTransaction", "Central Counterparty (CCP)"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000030"]
---







# Settlement Netting BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The CCP reports settlement obligations to be submitted for settlement (P248). T16 additionally includes CSD result and corporate-event reports, optional position updates/netting/event application, and settlement instructions to the CSD. A clearing member normally sends instructions to its paying agent; with power of attorney, the CCP sends the instructions to the CSD on its behalf. The two-actor sequence intentionally omits these related CSD/agent activities.

The related [source process](flow-src-000052-p155-settlement-netting-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P248** The SettlementObligationReport message is sent by a central counterparty (CCP) to a clearing member to report on the settlement(s) obligation(s) that will be submitted for settlement.

Source diagram evidence: [fig-0017](../documents/src-000052/diagrams/fig-0017.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: BusinessTransactions / Settlement Netting BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0017.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | SettlementObligationReport | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Narrative participant: [paying agent](../../../../../../../shared/reference/participants/participant-src-000052-paying-agent.md).

Narrative participant: [central securities depository csd](../../../../../../../shared/reference/participants/participant-src-000052-central-securities-depository-csd.md).

Exact definition bindings use the actual source053 MDR Part2 definition headings: [SettlementObligationReport / secl.010.001.04](../../../../messages/secl.010.001.04/index.md) (file pages 316-372; 11 MX secl.010.001.04 SettlementObligationReportV04). Names outside this MDR scope remain unbound to a particular version.
