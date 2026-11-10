---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p123-account-query-list"
title: "Account Query List"
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party", "participant-src-000350-recipient-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["acmt.025.001.02", "acmt.026.001.02"]
message_families: ["acmt.025", "acmt.026"]
search_terms: ["Account Query List", "Executing / Servicing Party", "Instructing Party", "acmt.025", "acmt.026"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---





# Account Query List

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Instructing Party asks the Executing/Servicing Party a response to a query.

Evidence: [T8](../documents/src-000350/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends an Account Query List message.

Evidence: [T8](../documents/src-000350/tables/tbl-0008.md), source row 3.

### Pre-conditions

The query type must be known by the Instructing party and the Executing/Servicing Party.

Evidence: [T8](../documents/src-000350/tables/tbl-0008.md), source row 4.

### Post-conditions

The Account List Report message including all of the retrieved Cash Account records.

Evidence: [T8](../documents/src-000350/tables/tbl-0008.md), source row 5.

### Role

Instructing Party.

Evidence: [T8](../documents/src-000350/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000350/tables/tbl-0008.md).

## Messages and alternative paths

Source-supported message family mentions: `acmt.025`, `acmt.026`. Full versions are retained only when explicitly present: none established in this segment.

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

Exact definitions applicable to this flow: [acmt.025.001.02](../../../../messages/acmt.025.001.02/index.md), [acmt.026.001.02](../../../../messages/acmt.026.001.02/index.md). Other messages in the shared overview belong to their separately linked processes.
