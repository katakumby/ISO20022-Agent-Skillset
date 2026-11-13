---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p204-settlement-management-buy-in-process"
title: "Settlement Management – Buy-In Process"
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[205]", "paragraph_id": "P205", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[206]", "paragraph_id": "P206", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-central-securities-depository-csd", "participant-src-000052-clearing-member-cm", "participant-src-000052-individual-or-general-clearing-member", "participant-src-000052-preferred-brokers", "participant-src-000052-settlement-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Settlement Management – Buy-In Process", "Central Counterparty (CCP)", "Clearing Member (CM)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Settlement Management – Buy-In Process

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in [the related source process](flow-src-000052-p161-buy-in-process.md).

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing Member (CM) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0011](../documents/src-000052/diagrams/fig-0011.md). The source reconstruction and actual review record are linked below.

Source table [T17](../documents/src-000052/tables/tbl-0017.md).

| Source column 1 | Source column 2 |
| --- | --- |
| Descriptions of the BusinessActivities |  |
| Central Counterparty (CCP) | Clearing Member (CM) |
| Identify position subject to buy-in:<br>Depending on the CCP’s internal rules, when the CCP has identified the positions that did/will not settle on due time, it notifies the failing seller clearing member. | Process the information:<br>The CM may send a response to the CCP asking for some delay (only valid for continuous netting systems). |
| Acknowledge the request:<br>Process where the CCP acknowledges the request for a delay (this will be done via telephone)  (out of scope). |  |
| Notify buy-in process has been launched:<br>The CCP notifies the failing seller clearing member that the buy-in process has been launched and that CCP tries to get the missing securities, for example, depending on the CCP, through an auction or by contacting a pool of preferred brokers. | Process the information:<br>Internal validation of the information. |
| Cancel settlement instruction:<br>The CCP cancels the settlement instruction sent previously to the CSD and creates a new one (settlement process (out of scope). |  |
| Confirm the buy-in process:<br>One business day after the buy-in date, the CCP confirms the buy-in process to all CMs that were bought in. | Process the information:<br>Internal validation of the information. |
| Any penalty fees or other buy-in fees will be debited from the clearing member account (payment process – out of scope). | Cancel settlement instruction: <br>The clearing member cancels the settlement instruction sent previously to the settlement agent/ CSD (settlement process – out of scope). |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: Description of BusinessActivities / Settlement Management – Buy-In Process.

## Curated activity and relationship account

The warning starts X days after intended settlement date. A clearing member may request delay; the CCP acknowledges and that response path ends. The source also has a thin curved warning-to-launch connector annotated And/or; it is preserved as a directed And/or relationship without imposing an exclusive decision. Launch notification reaches a source parallel bar feeding CCP settlement-instruction cancellation and later buy-in confirmation. Confirmation is annotated Buy in Date +1 and leads to out-of-scope payment and member cancellation of its settlement-agent instruction. T17 says acknowledgment is by telephone, delay is valid only for continuous netting systems, and confirmation is one business day after buy-in. Source labels are retained; no fixed number of days is invented.

[Source activity reconstruction](../diagrams/processes/fig-0011.md).

- [central counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- [individual or general clearing member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
- [settlement agent](../../../../../../../shared/reference/participants/participant-src-000052-settlement-agent.md).
- [preferred brokers](../../../../../../../shared/reference/participants/participant-src-000052-preferred-brokers.md).
- [central securities depository csd](../../../../../../../shared/reference/participants/participant-src-000052-central-securities-depository-csd.md).
