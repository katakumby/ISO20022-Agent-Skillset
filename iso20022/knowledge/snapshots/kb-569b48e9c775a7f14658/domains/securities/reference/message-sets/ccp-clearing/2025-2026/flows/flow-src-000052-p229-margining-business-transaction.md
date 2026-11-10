---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p229-margining-business-transaction"
title: "Margining BusinessTransaction"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[229]", "paragraph_id": "P229", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[230]", "paragraph_id": "P230", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[235]", "paragraph_id": "P235", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[236]", "paragraph_id": "P236", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[237]", "paragraph_id": "P237", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions", "Margining BusinessTransaction"], "locator": "/w:document/w:body/w:p[239]", "paragraph_id": "P239", "table_id": null}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-individual-or-general-clearing-member"]
message_mapping_evidence: [{"source_label": "MarginReport", "message_id": "secl.005.001.02", "source_id": "src-000053", "locator": "file pages 232-245; 6 MX secl.005.001.02 MarginReportV02"}]
message_ids: ["secl.005.001.02"]
message_families: ["secl.005"]
search_terms: ["Margining BusinessTransaction", "Central Counterparty (CCP)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---







# Margining BusinessTransaction

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose and ordered exchange: The report includes exposure from trade positions, collateral market value held by the CCP, and the resulting risk difference (P230-P233). A call may follow if calculated risk exceeds posted collateral; the clearing member may propose collateral and the CCP may accept or reject it. After rejection the proposal/response sequence may repeat (P236-P237). These optional collateral exchanges are outside this project scope (P238).

The related [source process](flow-src-000052-p131-margining-process.md) supplies its formal trigger, preconditions, postconditions and responsible role. These process-level conditions are distinct from the individual message sequence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P230** The central counterparty (CCP) calculates the risk linked to the net position of each clearing member. The MarginReport message is sent by a CCP to the clearing member to report on:

**P231** the exposure resulting from the trade positions

**P232** the value of the collateral held by the CCP (market value of this collateral)

**P233** the resulting difference representing the risk encountered by the CCP.

**P234** Optional flows:

**P235** Depending on the CCP’s internal rules:

**P236** The CCP may send the MarginCallRequest message in case the risk that has been calculated is greater than the amount of collateral that has been posted by the clearing member.

**P237** The clearing member may propose specific collateral to cover the risk encountered by the CCP. In this case, the clearing member sends the CollateralProposal message. The CCP may respond using the CollateralProposalResponse message to either accept or reject the piece of collateral that was proposed by the clearing member. (This sequence of messages can be repeated in case of rejection of the collateral proposed).

**P238** Note that these optional flows are not part of the scope of this project and will not be described in this document. They are only shown for the sake of completeness. For more information please refer to the Collateral Management project.

Source diagram evidence: [fig-0015](../documents/src-000052/diagrams/fig-0015.md). The source reconstruction is linked below; its review evidence records the actual checks.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: BusinessTransactions / Margining BusinessTransaction.

## Curated message exchange and participants

[Source sequence reconstruction](../diagrams/business-transactions/fig-0015.md). The two diagram participants are [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) and [Clearing Member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

| Step | Message | Sender participant | Receiver participant | Optionality |
| --- | --- | --- | --- | --- |
| 1 | MarginReport | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Mandatory in source sequence |
| 2 | MarginCallRequest | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Optional/potential; source conditions apply |
| 3 | CollateralProposal | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | Optional/potential; source conditions apply |
| 4 | CollateralProposalResponse | [CCP](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | [CM](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | Optional/potential; source conditions apply |


The linked source process and activity tables preserve additional alternative and out-of-scope paths. Participants named in those passages remain relevant even when the sequence omits them.

Exact definition bindings use the actual source053 MDR Part2 definition headings: [MarginReport / secl.005.001.02](../../../../messages/secl.005.001.02/index.md) (file pages 232-245; 6 MX secl.005.001.02 MarginReportV02). Names outside this MDR scope remain unbound to a particular version.
