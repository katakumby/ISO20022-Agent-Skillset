---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p116-query-billing-information"
title: "Query Billing Information"
source_locations: [{"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:p[119]", "paragraph_id": "P119", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "table_id": null}]
participants: ["participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party", "participant-src-000347-system-member", "participant-src-000347-system-transaction-administrator"]
message_mapping_evidence: []
message_ids: ["camt.076.001.01", "camt.077.001.01"]
message_families: ["camt.076", "camt.077"]
search_terms: ["Query Billing Information", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Flow interpretation checked against its linked source diagram; table review is recorded separately."]
manual_curated: true
---



# Query Billing Information

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P117** Notes: in the frame of the flow, System Transaction Administrator corresponds to the executing party, the System Member to the Instructing Party.

Source diagram evidence: [fig-0007](../documents/src-000347/diagrams/fig-0007.md). Dedicated source reconstruction and actual review evidence are linked below.

Source table [T10](../documents/src-000347/tables/tbl-0010.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Process Request Billing Data | Instruct the Executing/Servicing Party to return: <br>• Cumulative Billing Data<br>• Itemised Billing Data | Instructing Party  |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information. | Executing/Servicing Party  |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and return the requested information to the Instructing Party. | Executing/Servicing Party |
| Process Generate Error | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Process Billing Data / Process Handle Error | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: Description of BusinessActivities / Billing / Query Billing Information.

## Curated source process

System Member starts by requesting billing data. System Transaction Administrator checks validation, permission and availability in sequence; any No branch generates an error, returned for handling before termination. All Yes branches reach extraction and the cumulative/itemised choice. The selected delivery path crosses the source black bar before System Member processes the data and reaches the shared end. P117 maps System Member to Instructing Party and System Transaction Administrator to executing party. T10 additionally checks new/already-handled occurrence and requires REJECTED with errors/reasons when validation fails. The bar is preserved as drawn; the mutually exclusive data-type branches are not silently converted into a requirement for both reports.

[Complete source diagram reconstruction](../diagrams/curated/fig-0007.md).

| Participant | Source-specific responsibility |
| --- | --- |
| [system member](../../../../../../../shared/reference/participants/participant-src-000347-system-member.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [system transaction administrator](../../../../../../../shared/reference/participants/participant-src-000347-system-transaction-administrator.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |


