---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p121-billing-report"
title: "Billing Report"
source_locations: [{"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}]
participants: ["participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party", "participant-src-000347-national-central-bank", "participant-src-000347-operator", "participant-src-000347-settlement-infrastructure", "participant-src-000347-system-member"]
message_mapping_evidence: [{"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.077.001.01"]
message_families: ["camt.077"]
search_terms: ["Billing Report", "Executing / Servicing Party", "Instructing Party", "camt.077"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Flow interpretation checked against its linked source diagram; table review is recorded separately."]
manual_curated: true
---



# Billing Report

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P122** Notes: in the frame of the flow, Settlement Infrastructure corresponds to the executing party, the System Member to the Instructing Party.

Source diagram evidence: [fig-0008](../documents/src-000347/diagrams/fig-0008.md). Dedicated source reconstruction and actual review evidence are linked below.

Source table [T11](../documents/src-000347/tables/tbl-0011.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Process Check Event | Executing/Servicing Party system checks if the event for the generation of billing data is reached.  | Executing/Servicing Party  |
| Process Generate Invoice, Generate Invoice Cancellation and Deliver | If the event is reached, the Executing/Servicing Party processes the invoice data and return the generated billing information to the Instructing Party.<br>This process is triggered periodically to return invoices to all subscribed Instructing Parties.  | Executing/Servicing Party |
| Process Receive Invoice / Process Receive Invoice Cancellation | Instructing Party monitors the status of the generation of the invoice/invoice cancellation. | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: Description of BusinessActivities / Billing / Billing Report.

## Curated source process

Settlement Infrastructure checks whether the event has been reached. No ends locally; Yes generates invoice data. If invoice processing is not cancelled, the source parallel bar initiates cumulative-invoice delivery and billing-data storage; storage ends locally, while System Member receives the invoice. If cancelled, cancellation is generated and delivered to System Member. Both receipt paths lead to its shared end. P122 explicitly maps Settlement Infrastructure to executing party and System Member to Instructing Party. T11 says periodic processing returns invoices to subscribed instructing parties. P161-P168 separately describes official invoice/NCB-only consumption reports at the business-day event and cancellation-status reports after processing an operator cancellation request.

[Complete source diagram reconstruction](../diagrams/curated/fig-0008.md).

| Participant | Source-specific responsibility |
| --- | --- |
| [system member](../../../../../../../shared/reference/participants/participant-src-000347-system-member.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000347-settlement-infrastructure.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [operator](../../../../../../../shared/reference/participants/participant-src-000347-operator.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [national central bank](../../../../../../../shared/reference/participants/participant-src-000347-national-central-bank.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |


