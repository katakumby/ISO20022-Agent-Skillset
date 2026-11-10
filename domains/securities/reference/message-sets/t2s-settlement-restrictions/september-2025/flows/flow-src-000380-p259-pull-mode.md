---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p259-pull-mode"
title: "Pull mode"
source_locations: [{"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}]
participants: ["participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party"]
message_mapping_evidence: []
message_ids: ["semt.028.001.01", "semt.029.001.01"]
message_families: []
search_terms: ["Pull mode", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-servicing-executing-party", "participant-src-000380-t2s"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0010.md"]
---













# Pull mode

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

The curated section below links this segment to its source-defined process conditions and activity responsibilities.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000380/diagrams/fig-0010.md). See the maintained canonical reconstruction and review evidence below.

Source table [T10](../documents/src-000380/tables/tbl-0010.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Request Intra Position Movement Instructions. | Instructing Party sends a query to the Executing/Servicing Party to request details of any previously sent Intra Position Movement Instructions and the related securities positions. | Instructing Party. |
| Process query. | Technical and business validation of the query before further processing or not. <br>• If Yes, i.e., the request is valid, go to Send Intra Position Movement Instructions Response. <br>• If No, Error Processing is triggered. | Executing/Servicing Party. |
| Error Processing. | Adds operational errors to response before routing to Send Error Response. | Executing/Servicing Party. |
| Send Error Response. | Routes error response to communication layer. | Executing/Servicing Party. |
| Send Intra Position Movement Instructions Response. | Routes response to communication layer. | Executing/Servicing Party. |
| Monitor | Check for incoming communications associated with original instruction. | Instructing Party. |
| Reconcile | External process reconciling impact of current status of original instruction. | Instructing Party. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: Description of BusinessActivities / Intra Position Movement Query, Query Response and Pending Report / Pull mode.




<!-- SETTLEMENT-RESTRICTIONS-FIG-10-START -->
## Curated source-grounded flow

[Pull-mode intra-position movement query processing](../diagrams/settlement-restrictions/fig-0010.md)

### Source narrative and mode conditions

**src-000380 P259** — Pull mode

### Trigger, preconditions, postconditions and responsibilities

[Complete T8](../documents/src-000380/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | The process provides responses to queries regarding maintenance of Settlement and intra-position movement instructions (cancellation /modification request) previously sent and allows sending of reconciliation results of intra-position movement instructions (pending and posted) via query responses or via reporting. |
| Trigger | The process is triggered either by the system through a scheduled or by the receipt of a query request sent by the Instructing Party. |
| Pre-conditions | Settlement or Intra position movement instructions must exist to query within the scope of the Instructing Party and which correspond to the criteria as defined within the query and report.<br>The Instructing Party must hold necessary privileges within the Static Data configuration in order to receive reports. |
| Post-conditions | None |
| Role | Instructing Party for the query. <br>Executing Party / Servicing Party for the query response and for reporting. |


[Complete T10](../documents/src-000380/tables/tbl-0010.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Request Intra Position Movement Instructions. | Instructing Party sends a query to the Executing/Servicing Party to request details of any previously sent Intra Position Movement Instructions and the related securities positions. | Instructing Party. |
| Process query. | Technical and business validation of the query before further processing or not. <br>• If Yes, i.e., the request is valid, go to Send Intra Position Movement Instructions Response. <br>• If No, Error Processing is triggered. | Executing/Servicing Party. |
| Error Processing. | Adds operational errors to response before routing to Send Error Response. | Executing/Servicing Party. |
| Send Error Response. | Routes error response to communication layer. | Executing/Servicing Party. |
| Send Intra Position Movement Instructions Response. | Routes response to communication layer. | Executing/Servicing Party. |
| Monitor | Check for incoming communications associated with original instruction. | Instructing Party. |
| Reconcile | External process reconciling impact of current status of original instruction. | Instructing Party. |


### Participants and exact definitions

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Servicing/Executing Party](../../../../../../../shared/reference/participants/participant-src-000380-servicing-executing-party.md)

| Canonical exact definition | Exact-definition evidence |
| --- | --- |
| [semt.028.001.01](../../../../messages/semt.028.001.01/index.md) | src-000381 September2025 file page 7 |
| [semt.029.001.01](../../../../messages/semt.029.001.01/index.md) | src-000381 September2025 file page 57 |



The exact identifiers above come from the separately cited companion Part2 in the same September2025 message-set publication. Unversioned context families are not assigned arbitrary definitions.

### Alternatives and source distinctions

- The literal source response label spells Movemenrt; it is not silently corrected. The source vertical bar and converging error/response lines remain explicit. T9 defines a bar as parallel initiation, but the source drawing uses it where these branches converge; no new concurrent business action is inferred.
- T10 includes technical and business validation, operational error preparation, routing the response, monitoring and external reconciliation. Business errors may use sese.022 under P284; no exact sese.022 version is inferred.

<!-- SETTLEMENT-RESTRICTIONS-FIG-10-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-START -->
[semt.028.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.028.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-START -->
[semt.029.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.029.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-END -->
