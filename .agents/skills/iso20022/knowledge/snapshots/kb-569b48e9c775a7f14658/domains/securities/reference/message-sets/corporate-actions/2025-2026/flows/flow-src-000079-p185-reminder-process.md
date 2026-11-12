---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p185-reminder-process"
title: "Reminder Process"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Reminder Process"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Reminder Process"], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Reminder Process"], "locator": "/w:document/w:body/w:tbl[24]", "paragraph_id": null, "table_id": "T24"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reminder Process", "Account Servicer", "Account Owner"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Reminder Process

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0015](../documents/src-000079/diagrams/fig-0015.md). Mermaid reconstruction and visual review are pending.

Source table [T24](../documents/src-000079/tables/tbl-0024.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Reminder | Provide a reminder of the event details and/or instructed/uninstructed balance for a previously announced corporate action event. | Account Servicer |
| Process reminder | Process the reminder. | Account Owner |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: Description of BusinessActivities / BusinessActivities  / Reminder Process.
