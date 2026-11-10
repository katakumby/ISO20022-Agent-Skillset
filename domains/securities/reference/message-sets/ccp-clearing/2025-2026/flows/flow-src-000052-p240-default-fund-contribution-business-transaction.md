---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p240-default-fund-contribution-business-transaction"
title: "Default Fund Contribution BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[240]", "paragraph_id": "P240", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[241]", "paragraph_id": "P241", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[242]", "paragraph_id": "P242", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[243]", "paragraph_id": "P243", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[244]", "paragraph_id": "P244", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[245]", "paragraph_id": "P245", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Default Fund Contribution BusinessTransaction"], "locator": "/w:document/w:body/w:p[246]", "paragraph_id": "P246", "table_id": null}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-individual-or-general-clearing-member"]
message_mapping_evidence: [{"source_label": "DefaultFundContributionReport", "message_id": "secl.006.001.02", "source_id": "src-000053", "locator": "file pages 246-253; 7 MX secl.006.001.02 DefaultFundContributionReportV02"}]
message_ids: ["secl.006.001.02"]
message_families: ["secl.006"]
search_terms: ["Default Fund Contribution BusinessTransaction", "Central Counterparty (CCP)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---







# Default Fund Contribution BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The CCP reports the calculated default-fund contribution and potential net excess or deficit (P241-P242). Depending on CCP rules, it may send a margin call for a deficit. The optional call belongs to collateral management and is outside this MDR scope (P244-P245).

The related [source process](flow-src-000052-p137-default-fund-contribution-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P241** Central counterparties require participants to post assets in a clearing fund that can be used in the event of a default by a participant to compensate non-defaulting participants for losses they suffer due to this default. Contributions are linked to the riskiness of a participant's activity as measured by margin posted, by size of position or sometimes by stress-testing results. 

**P242** The DefaultFundContributionReport message is sent by a central counterparty (CCP) to the clearing member to report on the calculation of the default fund contribution and the potential net excess or deficit.

**P243** Optional flow:

**P244** Depending on the CCP’s internal rules, the CCP may send a MarginCallRequest message for the deficit amount required to cover the default fund.

**P245** Note that this flow is not part of the scope of this project and will not be described in this document. It is only shown for the sake of completeness. For more information please refer to the Collateral Management project.

Source diagram evidence: [fig-0016](../documents/src-000052/diagrams/fig-0016.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessTransactions / Default Fund Contribution BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0016.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | DefaultFundContributionReport | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |
| 2 | MarginCallRequest | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Optional/potential; source conditions apply |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Exact definition bindings use the actual source053 MDR Part2 definition headings: [DefaultFundContributionReport / secl.006.001.02](../../../../messages/secl.006.001.02/index.md) (file pages 246-253; 7 MX secl.006.001.02 DefaultFundContributionReportV02). Names outside this MDR scope remain unbound to a particular version.
