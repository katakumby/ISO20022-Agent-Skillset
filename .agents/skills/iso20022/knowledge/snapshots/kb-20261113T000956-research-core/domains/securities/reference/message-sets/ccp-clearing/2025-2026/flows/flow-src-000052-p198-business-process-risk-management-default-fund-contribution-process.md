---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process"
title: "BusinessProcess - Risk Management – Default Fund Contribution Process"
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Default Fund Contribution Process"], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Default Fund Contribution Process"], "locator": "/w:document/w:body/w:p[199]", "paragraph_id": "P199", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Default Fund Contribution Process"], "locator": "/w:document/w:body/w:p[200]", "paragraph_id": "P200", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Default Fund Contribution Process"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-clearing-member-cm", "participant-src-000052-individual-or-general-clearing-member"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess - Risk Management – Default Fund Contribution Process", "Central Counterparty (CCP)", "Clearing Member (CM)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# BusinessProcess - Risk Management – Default Fund Contribution Process

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in [the related source process](flow-src-000052-p137-default-fund-contribution-process.md).

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing Member (CM) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0009](../documents/src-000052/diagrams/fig-0009.md). The source reconstruction and actual review record are linked below.

Source table [T15](../documents/src-000052/tables/tbl-0015.md).

| Source column 1 | Source column 2 |
| --- | --- |
| Descriptions of the BusinessActivities |  |
| Central Counterparty (CCP) | Clearing Member (CM) |
| Assess participant risk level: <br>The CCP evaluates the risk level of each participant based on each participant’s position (daily or monthly). |  |
| Calculate the default fund contribution: <br>Depending on the CCP’s internal rules, every day or once a month, the CCP calculates for each CM if the default fund contribution is sufficient or not. | Process information: <br>Internal validation of  the information. |
| Sufficient? Yes/No |  |
| If deficit: <br>Either the CCP debits the CM account automatically or sends a payment instruction on behalf of the CM (if POA exists) - (out of scope).<br>The CCP may also send a Margin Call Request (optional, depends on each CCP’s rules)<br>If excess:<br>The CCP may return part of the contribution. |  |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: Description of BusinessActivities / BusinessProcess - Risk Management – Default Fund Contribution Process.

## Curated activity and relationship account

The CCP assesses risk and calculates the contribution, while the member processes the result. A sufficient contribution reaches the source end marker; a deficit enters an out-of-scope payment process. The source does not draw an end beyond the payment process, so none is added. T15 preserves daily/monthly calculation, automatic debit or payment on behalf under power of attorney, optional margin calls, and possible return of excess.

[Source activity reconstruction](../diagrams/processes/fig-0009.md).

- [central counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- [individual or general clearing member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
