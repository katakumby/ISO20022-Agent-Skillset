---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p149-query"
title: "Query"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[9]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[11]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[12]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.010", "reda.012", "reda.033", "reda.034"]
search_terms: ["Query", "Executing/Servicing Party", "Instructing Party", "reda.010", "reda.012", "reda.033", "reda.034"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Query

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Instructing Party asks the Executing/Servicing Party a response to a query or to an Audit Trail query.

Evidence: [T11](../documents/src-000377/tables/tbl-0011.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends a Security Query message or a Securities Audit Trail Query message.

Evidence: [T11](../documents/src-000377/tables/tbl-0011.md), source row 3.

### Pre-conditions

The query type must be known by the Instructing party and the Executing/Servicing Party.

Evidence: [T11](../documents/src-000377/tables/tbl-0011.md), source row 4.

### Post-conditions

The Security Report message including all of the retrieved securities records or the Securities Audit Trail Report message with all the requested audit trail information.

Evidence: [T11](../documents/src-000377/tables/tbl-0011.md), source row 5.

### Role

Instructing Party

Evidence: [T11](../documents/src-000377/tables/tbl-0011.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T11](../documents/src-000377/tables/tbl-0011.md).

## Messages and alternative paths

Source-supported message family mentions: `reda.010`, `reda.012`, `reda.033`, `reda.034`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessProcess Description.
