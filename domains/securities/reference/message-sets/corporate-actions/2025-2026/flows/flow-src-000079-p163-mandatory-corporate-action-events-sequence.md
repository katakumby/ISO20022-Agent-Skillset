---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p163-mandatory-corporate-action-events-sequence"
title: "Mandatory Corporate Action Events Sequence"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Mandatory Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Mandatory Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Mandatory Corporate Action Events Sequence"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Mandatory Corporate Action Events Sequence"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Mandatory Corporate Action Events Sequence

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000079/diagrams/fig-0008.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: Description of BusinessActivities / BusinessActivities Timeline / Mandatory Corporate Action Events Sequence.

## Curated illustrative phase sequence

| Phase | Initiating / sending role | Receiving role | Information/action | Source date label |
| --- | --- | --- | --- | --- |
| Announcement | Account Servicer | Account Owner | Announcement of Event | Not specified |
| Eligibility / Entitlement | Account Servicer | Account Owner | Notification of Entitled Position | Ex-Date / Record Date / Effective Date |
| Pre-advice/Final Entitlement | Account Servicer | Account Owner | Securities / cash Movements Preliminary Advice | Not specified |
| Confirmation | Account Servicer | Account Owner | Confirmation of Account Posting | Payment Date |


P161-P169 explicitly limits this to a possible sequence, permitting event-dependent variation and concurrent activities. Formal triggers, preconditions/postconditions, cancellation and detailed status paths are not enumerated by this timeline. [Source timeline reconstruction](../diagrams/timelines/fig-0008.md).
