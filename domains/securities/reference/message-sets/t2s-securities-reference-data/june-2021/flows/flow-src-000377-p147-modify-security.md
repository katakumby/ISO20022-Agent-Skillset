---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p147-modify-security"
title: "Modify Security"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[9]", "paragraph_id": null, "table_id": "T9"}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.007"]
search_terms: ["Modify Security", "Executing/Servicing Party", "Instructing Party", "reda.007"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Modify Security

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

When an Instructing Party is in charge of the modification of a specific security already supported by the Executing/Servicing Party system, the Instructing Party asks the Executing/Servicing Party to modify a security in the Executing/Servicing Party system.

Evidence: [T9](../documents/src-000377/tables/tbl-0009.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends a Security Maintenance Request message.

Evidence: [T9](../documents/src-000377/tables/tbl-0009.md), source row 3.

### Pre-conditions

The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. An attribute of the security has changed which requires a modification of the security in the Executing/Servicing Party system.

Evidence: [T9](../documents/src-000377/tables/tbl-0009.md), source row 4.

### Post-conditions

The acknowledgement of the processing of the maintenance request.

Evidence: [T9](../documents/src-000377/tables/tbl-0009.md), source row 5.

### Role

Instructing Party

Evidence: [T9](../documents/src-000377/tables/tbl-0009.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T9](../documents/src-000377/tables/tbl-0009.md).

## Messages and alternative paths

Source-supported message family mentions: `reda.007`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessProcess Description.
