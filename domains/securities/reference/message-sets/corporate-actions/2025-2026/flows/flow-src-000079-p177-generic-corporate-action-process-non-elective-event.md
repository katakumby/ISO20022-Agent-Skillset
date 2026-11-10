---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p177-generic-corporate-action-process-non-elective-event"
title: "Generic Corporate Action Process (Non Elective Event)"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Generic Corporate Action Process (Non Elective Event)"], "locator": "/w:document/w:body/w:p[177]", "paragraph_id": "P177", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Generic Corporate Action Process (Non Elective Event)"], "locator": "/w:document/w:body/w:p[178]", "paragraph_id": "P178", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Generic Corporate Action Process (Non Elective Event)"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Generic Corporate Action Process (Non Elective Event)"], "locator": "/w:document/w:body/w:tbl[21]", "paragraph_id": null, "table_id": "T21"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer", "participant-src-000079-csd-icsd", "participant-src-000079-market-data-provider", "participant-src-000079-sub-custodian"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Generic Corporate Action Process (Non Elective Event)", "Market Data Provider", "Account Servicer", "Account Owner", "Sub-Custodian", "CSD / ICSD"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source T20 defines bars as parallel actions, yet this artwork combines bars with Yes/No conditional labels. Every source branch is retained; exclusive-choice and synchronization semantics remain unresolved under issue-000020."]
manual_curated: true
issue_ids: ["issue-000020"]
---







# Generic Corporate Action Process (Non Elective Event)

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Market Data Provider | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-market-data-provider.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Sub-Custodian | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-sub-custodian.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CSD / ICSD | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-csd-icsd.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0012](../documents/src-000079/diagrams/fig-0012.md). Mermaid reconstruction and visual review are pending.

Source table [T21](../documents/src-000079/tables/tbl-0021.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Announce new CA event | The CA event is announced based on information received from the CSD, ICSD, market data provider, sub-custodian. | Account Servicer |
| Process new CA announcement | Processing of the new announcement. | Account Owner |
| Event confirmed? | If the CA event is confirmed on the market and details are complete, an update to the announcement may still be sent (if updates are received from an external source) or notification of balance and entitlements can take place.<br>If the CA event is confirmed and details are not complete (preliminary), an update to the CA event announcement may be sent.<br>If the CA event is not confirmed, details are by default preliminary, an update to the CA event announcement may be sent. | Account Servicer |
| CA announcement update | Processing of the announcement update | Account Owner |
| CA event is cancelled by account servicer | Processing of the cancellation | Account Owner |
| Notify Balance and Entitlements | Advise balance of holdings and entitlements.<br>Updated balance and entitlement advice may be provided. | Account Servicer |
| Notify Balance and Entitlements | Process balance and entitlements advice or updates. | Account Owner |
| Confirm cash/securities postings | When payment date is reached, cash/securities postings are confirmed. These postings may be reversed if necessary. | Account Servicer |
| Reflect cash/securities movement | Reflect cash/securities movements in internal accounts. | Account Owner |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: Description of BusinessActivities / BusinessActivities  / Generic Corporate Action Process (Non Elective Event).

## Source activity reconstruction

The source lanes assign activities to Account Servicer and Account Owner. Named activities, all cross-lane arrows, all source endpoints, and repeated Yes/No branches are preserved. Source bars are explicitly labeled as bars in the reconstruction rather than converted into exclusive decision diamonds. Annotation boxes are retained as source notes, not extra activities or participants. The source note defines omitted context and is reproduced in the diagram.

[Generic non-elective corporate action activities](../diagrams/detailed-activities/fig-0012.md). Source T20 defines bars as parallel actions, yet this artwork combines bars with Yes/No conditional labels. Every source branch is retained; exclusive-choice and synchronization semantics remain unresolved under issue-000020.

## Responsible roles from process definitions

Source T11-T19 provides the functional responsibilities independently of drawing layout: Account Servicer for notification, entitlement, reminder, preliminary advice, confirmation, reversal and status; Account Owner for election; cancellation can involve either role according to its target. [Election process (T14)](../documents/src-000079/tables/tbl-0014.md); [Cancellation process (T18)](../documents/src-000079/tables/tbl-0018.md). These source roles do not turn a process arrow into an exact message exchange.
