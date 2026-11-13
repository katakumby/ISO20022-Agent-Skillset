---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p180-instruction-process-elective-event"
title: "Instruction Process (Elective Event)"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Instruction Process (Elective Event)"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Instruction Process (Elective Event)"], "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Instruction Process (Elective Event)"], "locator": "/w:document/w:body/w:p[182]", "paragraph_id": "P182", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Instruction Process (Elective Event)"], "locator": "/w:document/w:body/w:tbl[22]", "paragraph_id": null, "table_id": "T22"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Instruction Process (Elective Event)", "Account Servicer", "Account Owner"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source T20 defines bars as parallel actions, yet this artwork combines bars with Yes/No conditional labels. Every source branch is retained; exclusive-choice and synchronization semantics remain unresolved under issue-000020."]
manual_curated: true
issue_ids: ["issue-000020"]
---







# Instruction Process (Elective Event)

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P181** This diagram only describes the instruction process (for event with voluntary events or mandatory events with options). In line, with the “Corporate Action Chronology of Events” figures, these activities typically occur between the corporate action announcement and the notification of balance and entitlements.

Source diagram evidence: [fig-0013](../documents/src-000079/diagrams/fig-0013.md). Mermaid reconstruction and visual review are pending.

Source table [T22](../documents/src-000079/tables/tbl-0022.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Process Instruction | Process the received election instruction | Account Servicer |
| Instruct Election | Election instruction is sent to the account servicer based on the options proposed in the CA announcement | Account Owner |
| Reminder | If the response deadline is approaching or if a part of the account owner balance remains uninstructed, the account servicer may remind the account owner of the situation. | Account Servicer |
| Reminder | The account owner may do nothing or provide election for the part of the remaining part of the balance. | Account Owner |
| Instruction processed Yes/No | Yes, go to 'Report Instruction Status' and go to the next activity (see Generic Corporate Action Process diagram).<br>No, go to 'Report Instruction Status' | Account Servicer |
| Report instruction status | Reports the status of the received election instruction. The status may be positive or negative. | Account Servicer |
| Process instruction status | Process the instruction status report. | Account Owner |
| Instruction status OK? | If No, no further action or go to Instruct election process. If Yes, end of activities. | Account Owner |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: Description of BusinessActivities / BusinessActivities  / Instruction Process (Elective Event).

## Source activity reconstruction

The source lanes assign activities to Account Servicer and Account Owner. Named activities, all cross-lane arrows, all source endpoints, and repeated Yes/No branches are preserved. Source bars are explicitly labeled as bars in the reconstruction rather than converted into exclusive decision diamonds. Annotation boxes are retained as source notes, not extra activities or participants. The source note defines omitted context and is reproduced in the diagram.

[Elective instruction activities](../diagrams/detailed-activities/fig-0013.md). Source T20 defines bars as parallel actions, yet this artwork combines bars with Yes/No conditional labels. Every source branch is retained; exclusive-choice and synchronization semantics remain unresolved under issue-000020.

## Responsible roles from process definitions

Source T11-T19 provides the functional responsibilities independently of drawing layout: Account Servicer for notification, entitlement, reminder, preliminary advice, confirmation, reversal and status; Account Owner for election; cancellation can involve either role according to its target. [Election process (T14)](../documents/src-000079/tables/tbl-0014.md); [Cancellation process (T18)](../documents/src-000079/tables/tbl-0018.md). These source roles do not turn a process arrow into an exact message exchange.
