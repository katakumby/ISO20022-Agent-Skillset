---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p124-cash-account-audit-trail-query"
title: "Cash Account Audit Trail Query"
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party", "participant-src-000350-recipient-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.039.001.01", "reda.040.001.01"]
message_families: ["reda.039", "reda.040"]
search_terms: ["Cash Account Audit Trail Query", "Executing / Servicing Party", "Instructing Party", "reda.039"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---





# Cash Account Audit Trail Query

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Instructing Party asks the Executing/Servicing Party a response to a query.

Evidence: [T9](../documents/src-000350/tables/tbl-0009.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends a Cash Account Audit Trail Query message.

Evidence: [T9](../documents/src-000350/tables/tbl-0009.md), source row 3.

### Pre-conditions

The query type must be known by the Instructing party and the Executing/Servicing Party.

Evidence: [T9](../documents/src-000350/tables/tbl-0009.md), source row 4.

### Post-conditions

The Cash Account Audit Trail Report message including all of the retrieved Cash Account Audit Trail records.

Evidence: [T9](../documents/src-000350/tables/tbl-0009.md), source row 5.

### Role

Instructing Party.

Evidence: [T9](../documents/src-000350/tables/tbl-0009.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T9](../documents/src-000350/tables/tbl-0009.md).

## Messages and alternative paths

Source-supported message family mentions: `reda.039`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: BusinessProcess Description.

## Curated source flow

One start symbol leads to three paths: Account Query List followed by Account List Report; unsolicited Cash Account Activity Advice; and Cash Account Audit Trail Query followed by Cash Account Audit Trail Report. All converge at a common end. No exclusive-choice diamond or parallel bar is drawn. T8/T9 require both parties to know the query type and define report content as all retrieved records. T10 requires a standing instruction for automatically produced activity advice and names acknowledgement of sending as postcondition; this does not add an acknowledgement arrow to the artwork.

[Complete source diagram](../diagrams/curated/fig-0002.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md), [recipient party](../../../../../../../shared/reference/participants/participant-src-000350-recipient-party.md).

Exact definitions applicable to this flow: [reda.039.001.01](../../../../messages/reda.039.001.01/index.md), [reda.040.001.01](../../../../messages/reda.040.001.01/index.md). Other messages in the shared overview belong to their separately linked processes.
