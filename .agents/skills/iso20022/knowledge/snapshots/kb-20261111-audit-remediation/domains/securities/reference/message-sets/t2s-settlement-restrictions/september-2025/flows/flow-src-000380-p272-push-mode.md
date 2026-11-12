---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p272-push-mode"
title: "Push mode"
source_locations: [{"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:p[272]", "paragraph_id": "P272", "table_id": null}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:p[273]", "paragraph_id": "P273", "table_id": null}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:p[274]", "paragraph_id": "P274", "table_id": null}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:p[275]", "paragraph_id": "P275", "table_id": null}]
participants: ["participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party"]
message_mapping_evidence: []
message_ids: ["semt.031.001.01", "semt.033.001.01"]
message_families: []
search_terms: ["Push mode", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-reporting-party", "participant-src-000380-requestor", "participant-src-000380-servicing-party", "participant-src-000380-t2s"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0013.md"]
---













# Push mode

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

The curated section below links this segment to its source-defined process conditions and activity responsibilities.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0013](../documents/src-000380/diagrams/fig-0013.md). See the maintained canonical reconstruction and review evidence below.

Source table [T13](../documents/src-000380/tables/tbl-0013.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| System Event Triggered. | External process resulting in need for securities Movement Instructions<br>reporting. | Executing/Servicing Party. |
| Report Required. | Verification (message subscription rule set within static data) that reporting required for parties under current conditions.<br>• If Yes, i.e., the report is required then go to Generate Report.<br>• If No, then end of activity. | Executing/Servicing Party. |
| Generate Report. | Process that creates a report for Settlement or Intra Position Movement Cancellation/Modification Instructions satisfying a previously selected criteria.<br>• If Yes successfully generated, i.e., the report is properly generated then go to send Settlement or Intra Position Movement Cancellation/Modification <br>Report.<br>• If No, then Error Processing with end of activity. | Executing/Servicing Party. |
| Send Settlement or Intra Position Movement Cancellation/Modification Report | Routes report to Instructing Party under a selected criteria. | Executing/Servicing Party. |
| Monitor. | Check for incoming communications (Settlement or Intra Position Movement Cancellation/Modification Report). | Instructing Party. |
| Reconcile. | External process reconciling impact of current status of original instruction. | Instructing Party. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: Description of BusinessActivities / Securities Transaction Cancellation/Modification Request Query/Report / Push mode.




<!-- SETTLEMENT-RESTRICTIONS-FIG-13-START -->
## Curated source-grounded flow

[Push-mode cancellation or modification report processing](../diagrams/settlement-restrictions/fig-0013.md)

### Source narrative and mode conditions

**src-000380 P272** — Push mode

### Trigger, preconditions, postconditions and responsibilities

[Complete T8](../documents/src-000380/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | The process provides responses to queries regarding maintenance of Settlement and intra-position movement instructions (cancellation /modification request) previously sent and allows sending of reconciliation results of intra-position movement instructions (pending and posted) via query responses or via reporting. |
| Trigger | The process is triggered either by the system through a scheduled or by the receipt of a query request sent by the Instructing Party. |
| Pre-conditions | Settlement or Intra position movement instructions must exist to query within the scope of the Instructing Party and which correspond to the criteria as defined within the query and report.<br>The Instructing Party must hold necessary privileges within the Static Data configuration in order to receive reports. |
| Post-conditions | None |
| Role | Instructing Party for the query. <br>Executing Party / Servicing Party for the query response and for reporting. |


[Complete T13](../documents/src-000380/tables/tbl-0013.md)

| Step | Description | Initiator |
| --- | --- | --- |
| System Event Triggered. | External process resulting in need for securities Movement Instructions<br>reporting. | Executing/Servicing Party. |
| Report Required. | Verification (message subscription rule set within static data) that reporting required for parties under current conditions.<br>• If Yes, i.e., the report is required then go to Generate Report.<br>• If No, then end of activity. | Executing/Servicing Party. |
| Generate Report. | Process that creates a report for Settlement or Intra Position Movement Cancellation/Modification Instructions satisfying a previously selected criteria.<br>• If Yes successfully generated, i.e., the report is properly generated then go to send Settlement or Intra Position Movement Cancellation/Modification <br>Report.<br>• If No, then Error Processing with end of activity. | Executing/Servicing Party. |
| Send Settlement or Intra Position Movement Cancellation/Modification Report | Routes report to Instructing Party under a selected criteria. | Executing/Servicing Party. |
| Monitor. | Check for incoming communications (Settlement or Intra Position Movement Cancellation/Modification Report). | Instructing Party. |
| Reconcile. | External process reconciling impact of current status of original instruction. | Instructing Party. |


### Participants and exact definitions

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Servicing Party](../../../../../../../shared/reference/participants/participant-src-000380-servicing-party.md)

| Canonical exact definition | Exact-definition evidence |
| --- | --- |
| [semt.031.001.01](../../../../messages/semt.031.001.01/index.md) | src-000381 September2025 file page 97 |
| [semt.033.001.01](../../../../messages/semt.033.001.01/index.md) | src-000381 September2025 file page 145 |



The exact identifiers above come from the separately cited companion Part2 in the same September2025 message-set publication. Unversioned context families are not assigned arbitrary definitions.

### Alternatives and source distinctions

- The Yes label is printed before the Successful Process? decision, on the Generate Report arrow; its success branch has no label. The reconstruction preserves this placement.
- T13 checks subscription rules, generates matching previously received cancellation/modification instructions and ends locally when no report is required or generation fails. Configured report scopes and delta criteria are detailed in P297/P307; no query prerequisite is inferred.

<!-- SETTLEMENT-RESTRICTIONS-FIG-13-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-START -->
[semt.031.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.031.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-START -->
[semt.033.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.033.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-END -->
