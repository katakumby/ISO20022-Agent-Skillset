---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p253-query-report-process"
title: "Query Report Process"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}]
participants: ["participant-src-000380-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Query Report Process", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Query Report Process

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process provides responses to queries regarding maintenance of Settlement and intra-position movement instructions (cancellation /modification request) previously sent and allows sending of reconciliation results of intra-position movement instructions (pending and posted) via query responses or via reporting.

Evidence: [T8](../documents/src-000380/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered either by the system through a scheduled or by the receipt of a query request sent by the Instructing Party.

Evidence: [T8](../documents/src-000380/tables/tbl-0008.md), source row 3.

### Pre-conditions

Settlement or Intra position movement instructions must exist to query within the scope of the Instructing Party and which correspond to the criteria as defined within the query and report.
The Instructing Party must hold necessary privileges within the Static Data configuration in order to receive reports.

Evidence: [T8](../documents/src-000380/tables/tbl-0008.md), source row 4.

### Post-conditions

None

Evidence: [T8](../documents/src-000380/tables/tbl-0008.md), source row 5.

### Role

Instructing Party for the query. 
Executing Party / Servicing Party for the query response and for reporting.

Evidence: [T8](../documents/src-000380/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000380/tables/tbl-0008.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessProcess Description.
