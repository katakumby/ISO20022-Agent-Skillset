---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p125-cash-account-activity-advice"
title: "Cash Account Activity Advice"
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party", "participant-src-000350-recipient-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.038.001.01"]
message_families: ["reda.038"]
search_terms: ["Cash Account Activity Advice", "Executing / Servicing Party", "reda.038"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---





# Cash Account Activity Advice

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Recipient Party receives a Cash Account Activity Advice statement which has been automatically produced by the Executing/Servicing Party.

Evidence: [T10](../documents/src-000350/tables/tbl-0010.md), source row 2.

### Trigger

The process is triggered automatically.

Evidence: [T10](../documents/src-000350/tables/tbl-0010.md), source row 3.

### Pre-conditions

A standing instruction is in place at the Executing/Servicing Party for sending of the statement.

Evidence: [T10](../documents/src-000350/tables/tbl-0010.md), source row 4.

### Post-conditions

The acknowledgement of the sending of the statement.

Evidence: [T10](../documents/src-000350/tables/tbl-0010.md), source row 5.

### Role

Executing/Servicing Party.

Evidence: [T10](../documents/src-000350/tables/tbl-0010.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T10](../documents/src-000350/tables/tbl-0010.md).

## Messages and alternative paths

Source-supported message family mentions: `reda.038`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: BusinessProcess Description.

## Curated source flow

One start symbol leads to three paths: Account Query List followed by Account List Report; unsolicited Cash Account Activity Advice; and Cash Account Audit Trail Query followed by Cash Account Audit Trail Report. All converge at a common end. No exclusive-choice diamond or parallel bar is drawn. T8/T9 require both parties to know the query type and define report content as all retrieved records. T10 requires a standing instruction for automatically produced activity advice and names acknowledgement of sending as postcondition; this does not add an acknowledgement arrow to the artwork.

[Complete source diagram](../diagrams/curated/fig-0002.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md), [recipient party](../../../../../../../shared/reference/participants/participant-src-000350-recipient-party.md).

Exact definitions applicable to this flow: [reda.038.001.01](../../../../messages/reda.038.001.01/index.md). Other messages in the shared overview belong to their separately linked processes.
