---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p110-billing-report"
title: "Billing Report"
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[110]", "paragraph_id": "P110", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000347", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[111]", "paragraph_id": "P111", "table_id": null}]
participants: ["participant-src-000347-central-system", "participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party", "participant-src-000347-system-member"]
message_mapping_evidence: [{"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
message_families: ["camt.076", "camt.077"]
search_terms: ["Billing Report", "camt.077"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Flow interpretation checked against its linked source diagram; table review is recorded separately."]
manual_curated: true
---



# Billing Report

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Billing Report is sent by Central System as official invoice, status of a previously sent cancellation of the latest valid invoice, consumption data message or as a response of a System member query containing information backing the actual valid invoice. The latter is a query response to the query message, containing information on requested items (cumulative or itemised billing data) or business error reports.

Evidence: [T8](../documents/src-000347/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered by an event within the Central system for the corresponding billing period or by a System member querying billing data information.

Evidence: [T8](../documents/src-000347/tables/tbl-0008.md), source row 3.

### Pre-conditions

All generated invoice data (monthly or intra-month) are available for query purposes, no matter if they have the status "cancelled" or "not confirmed". However, the System Member can query for his Invoice Data by using the Billing Reference (Invoice Number) as a distinct search criterion to be sure that the returned data are active and confirmed.

Evidence: [T8](../documents/src-000347/tables/tbl-0008.md), source row 4.

### Post-conditions

The acknowledgement of the billing report process

Evidence: [T8](../documents/src-000347/tables/tbl-0008.md), source row 5.

### Role

Instructing/Servicing Party

Evidence: [T8](../documents/src-000347/tables/tbl-0008.md), source row 6.

## Participants

The curated scoped participant links below resolve diagram and narrative roles for this flow.

## Ordered activities and source narrative

Source table [T8](../documents/src-000347/tables/tbl-0008.md).

## Messages and alternative paths

Source-supported message family mentions: `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: BusinessProcess Description.

## Curated source process

One source start point has separate arrows to Query Billing information and Billing Report. A dotted directed relationship goes from the query to the report. Both process boxes lead to a shared end point. The overview does not draw an exclusive-choice diamond or a parallel bar. T8 provides the formal trigger, preconditions and postconditions.

[Complete source diagram reconstruction](../diagrams/curated/fig-0002.md).

| Participant | Source-specific responsibility |
| --- | --- |
| [system member](../../../../../../../shared/reference/participants/participant-src-000347-system-member.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [central system](../../../../../../../shared/reference/participants/participant-src-000347-central-system.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |


