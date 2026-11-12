---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p194-business-process-risk-management-netting-process"
title: "BusinessProcess - Risk Management – Netting Process"
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Netting Process"], "locator": "/w:document/w:body/w:p[194]", "paragraph_id": "P194", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Netting Process"], "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "table_id": null}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Netting Process"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}]
participants: ["participant-src-000052-ccp", "participant-src-000052-central-counterparty", "participant-src-000052-central-counterparty-ccp", "participant-src-000052-clearing-member-cm", "participant-src-000052-individual-or-general-clearing-member"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess - Risk Management – Netting Process", "Central Counterparty (CCP)", "Clearing Member (CM)", "CCP"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# BusinessProcess - Risk Management – Netting Process

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in [the related source process](flow-src-000052-p125-netting-process.md).

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing Member (CM) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0007](../documents/src-000052/diagrams/fig-0007.md). The source reconstruction and actual review record are linked below.

Source table [T13](../documents/src-000052/tables/tbl-0013.md).

| Source column 1 | Source column 2 |
| --- | --- |
| Descriptions of the BusinessActivities |  |
| Central Counterparty (CCP) | Clearing Member (CM) |
| Milestone: End of real time session (EOD)<br>Note: Some CCPs may request intraday margin based on provisional intraday net position. | The CM receives a business session status message (once all End of day milestones from all markets have been received) (out of scope). |
| Position netting: <br>The CCP nets all the positions (per margin account – house and client). | Process Information: <br>The CM is informed of the netting results and it reconciles its netting calculation with the CCP results (based on the netting parameters). |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: Description of BusinessActivities / BusinessProcess - Risk Management – Netting Process.

## Curated activity and relationship account

The end-of-real-time-session milestone leads to position netting by the CCP and information processing by the clearing member. T13 additionally describes a business-session status message, house/client margin-account netting, reconciliation using netting parameters, and possible intraday margin on provisional net positions. The milestone box is source context, not an ISO message name.

[Source activity reconstruction](../diagrams/processes/fig-0007.md).

- [central counterparty](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- [individual or general clearing member](../../../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
