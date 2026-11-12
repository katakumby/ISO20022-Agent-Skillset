---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p166-elective-corporate-action-events-sequence"
title: "Elective Corporate Action Events Sequence"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Elective Corporate Action Events Sequence"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Elective Corporate Action Events Sequence

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

Source diagram evidence: [fig-0009](../documents/src-000079/diagrams/fig-0009.md). Mermaid reconstruction and visual review are pending.

**P168** The process flows hereafter describe a possible high level sequence of the processes defined in the previous section 4.1.

**P169** The corporate actions process flows differ significantly between events with options and events without options. For this reason two process flows are presented here.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: Description of BusinessActivities / BusinessActivities Timeline / Elective Corporate Action Events Sequence.

## Curated illustrative phase sequence

| Phase | Initiating / sending role | Receiving role | Information/action | Source date label |
| --- | --- | --- | --- | --- |
| Announcement | Account Servicer | Account Owner | Announcement of Event | Not specified |
| Eligibility | Account Servicer | Account Owner | Eligible balance | Ex-Date / Record Date / Effective Date |
| Instruction | Account Owner | Account Servicer | Instruction | Not specified |
| Status | Account Servicer | Account Owner | Status of Event/Instruction/Reminder of event details and/or instructed/uninstructed balance | Not specified |
| Entitlement | Account Servicer | Account Owner | Notification of Entitled Position | Response deadline |
| Pre-advice/Final Entitlement | Account Servicer | Account Owner | Securities / cash Movements Preliminary Advice | Not specified |
| Confirmation | Account Servicer | Account Owner | Confirmation of Account Posting | Payment Date |


P161-P169 explicitly limits this to a possible sequence, permitting event-dependent variation and concurrent activities. Formal triggers, preconditions/postconditions, cancellation and detailed status paths are not enumerated by this timeline. [Source timeline reconstruction](../diagrams/timelines/fig-0009.md).
