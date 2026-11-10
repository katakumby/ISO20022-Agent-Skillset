---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p146-create-security"
title: "Create Security"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.006"]
search_terms: ["Create Security", "Executing/Servicing Party", "Instructing Party", "reda.006"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Create Security

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

When an Instructing Party would like to create a specific security that is not yet supported by the Executing/Servicing Party, an Instructing Party asks the Executing/Servicing Party to create the security in its system.

Evidence: [T8](../documents/src-000377/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends a Security Creation Request message.

Evidence: [T8](../documents/src-000377/tables/tbl-0008.md), source row 3.

### Pre-conditions

The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the securities’ coverage of the Executing/Servicing Party. The Instructing Party needs this security to be set-up at the Executing /Servicing Party to perform its activities.

Evidence: [T8](../documents/src-000377/tables/tbl-0008.md), source row 4.

### Post-conditions

The acknowledgement of the processing of the creation request.

Evidence: [T8](../documents/src-000377/tables/tbl-0008.md), source row 5.

### Role

Instructing Party

Evidence: [T8](../documents/src-000377/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000377/tables/tbl-0008.md).

## Messages and alternative paths

Source-supported message family mentions: `reda.006`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessProcess Description.
