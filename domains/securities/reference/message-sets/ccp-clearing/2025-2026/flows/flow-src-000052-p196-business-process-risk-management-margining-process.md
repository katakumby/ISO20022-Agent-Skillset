---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p196-business-process-risk-management-margining-process"
title: "BusinessProcess - Risk Management – Margining Process"
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-clearing-member-cm", "participant-src-000052-individual-or-general-clearing-member"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess - Risk Management – Margining Process", "Central Counterparty (CCP)", "Clearing Member (CM)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# BusinessProcess - Risk Management – Margining Process

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in [the related source process](flow-src-000052-p131-margining-process.md).

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing Member (CM) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000052/diagrams/fig-0008.md). The source reconstruction and actual review record are linked below.

Source table [T14](../documents/src-000052/tables/tbl-0014.md).

| Source column 1 | Source column 2 |
| --- | --- |
| Descriptions of the BusinessActivities |  |
| Central Counterparty (CCP) | Clearing Member (CM) |
| Calculate a risk: <br>The CCP calculates the risk and sends a report to the CMs (with either the deficit or excess).<br>Note: This can be done at the end of the day or intraday.  | Process information: <br>The CM reconciles its calculation with the CCP results (if possible, since the calculation comparison may be very difficult). |
| Margin call follow up: <br>After calculation of the initial or variation margin, the CCP requests or not the transfer of collateral (if the CM is in deficit, collateral is required). |  |
| Scenario 1 |  |
| Optional activity: <br>When collateral is required, some CCPs may take cash automatically from the CM account (out of scope). |  |
| Scenario 2 |  |
| Optional activity: <br>CCPs may send a margin call request (this depends on each CCP’s internal rules). | Optional: <br>Based on the margin call, the CM may propose to deliver specific collateral. |
| Collateral accepted? |  |
|  | If Yes, deliver the securities/cash/other:<br>The CM delivers the securities/cash accepted as new collateral (out of scope). |
| If yes, receive the securities/cash/other:<br>The CCP receives the securities/cash accepted as new collateral (out of scope). |  |
| If no, notify the CM | Propose new collateral? |
|  | If Yes, then process starts again.<br>If No, then process ends. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: Description of BusinessActivities / BusinessProcess - Risk Management – Margining Process.

## Curated activity and relationship account

The source start branches to risk calculation/information and margin-call follow-up. Scenario 1 permits automatic cash debit; Scenario 2 allows the member to propose collateral. CCP rejection leads to the member choosing whether to propose again; acceptance reaches a parallel bar, followed by receiving and delivering securities/cash. The three out-of-scope cash/securities paths share the source end marker. The source bar is retained as a thick bar symbol, not converted into an exclusive decision. T14 supplies collateral-deficit conditions and the CCP-rule dependency.

[Source activity reconstruction](../diagrams/processes/fig-0008.md).

- [central counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- [individual or general clearing member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
