---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp"
title: "Securities Account Position Query and Securities Account Position Response"
source_locations: [{"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[235]", "paragraph_id": "P235", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[236]", "paragraph_id": "P236", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[237]", "paragraph_id": "P237", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "table_id": null}]
participants: ["participant-src-000374-account-owner", "participant-src-000374-account-servicer", "participant-src-000374-authorised-party", "participant-src-000374-central-securities-depositories-csd", "participant-src-000374-direct-connected-participant-dcp", "participant-src-000374-executing-servicing-party", "participant-src-000374-instructing-party", "participant-src-000374-servicing-party", "participant-src-000374-t2s-actor"]
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.025.001.01", "semt.040.001.01"]
message_families: ["semt.025", "semt.040"]
search_terms: ["Securities Account Position Query and Securities Account Position Response", "Executing / Servicing Party", "Instructing Party", "Servicing Party", "semt.025", "semt.040"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
flow_scope: "query mode"
related_message_families: ["sese.022"]
---









# Securities Account Position Query and Securities Account Position Response

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000374/diagrams/fig-0010.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T10](../documents/src-000374/tables/tbl-0010.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Reconcile Securities Positions | Instructing Party sends a query to the Executing/Servicing Party to request details of the related securities positions. | Instructing Party |
| Validate Request | Technical and business validation of the query before further processing or not. <br>• If Yes, i.e., the request is valid, go to Querying process based in the selected criteria. <br>• If No, Update Status is triggered. | Servicing Party |
| Update Status | Routes error response to communication layer | Servicing Party |
| Querying process based in the selected criteria | Retrieves the requested data and routes the response message to communication layer. | Servicing Party |
| Process Status | Check for incoming communications associated with original instruction and process its content. | Instructing Party |
| Update Securities Account Position | External process of reconciling based on the content of the message response to the original instruction. | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `semt.025`, `semt.040`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: Description of BusinessActivities / Securities Account Position Query and Securities Account Position Response.

## Curated source flow

A CSD or directly connected party sends criteria and an optional date range to T2S acting as Servicing Party. The response covers matching positions across the accounts and securities selected. Complete Word6 displays this image only: embedded legacy actor fragments/text in the same paragraph do not create extra visible actors or a second response. P258 adds the error-family sese.022, absent from this success-only picture; its exact version is not specified here.

[Complete source diagram](../diagrams/curated/fig-0001.md).

### Adjacent source narrative

**P257** Securities Account Position Query (semt.025)

**P258** The Securities Account Position Query message returns the latest securities position at the given time of the day that the query has been requested for the specified securities accounts. In case the T2S Actor requests for a Securities Account Position History Query, he should indicate either the securities account or the account owner as search criteria. In a Securities Account Position History Query, T2S returns all closing securities positions on the dates within the specified time period for the specified securities accounts. In response to the Securities Account Position Query message, T2S sends a semt.040 message with the list of the different securities positions of a T2S Actor's securities account or a sese.022 message in case of error.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [servicing party](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000374-direct-connected-participant-dcp.md), [account owner](../../../../../../../shared/reference/participants/participant-src-000374-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000374-account-servicer.md), [authorised party](../../../../../../../shared/reference/participants/participant-src-000374-authorised-party.md), [t2s actor](../../../../../../../shared/reference/participants/participant-src-000374-t2s-actor.md).

## Curated source flow

The Instructing Party initiates reconciliation by querying securities positions. Servicing Party validates access and the technical/business request: an unsuccessful check updates status and sends an error; a valid query retrieves matching data. Both return to Process Status. The Instructing Party ends on failure or updates its position reconciliation on success. T10 defines the update as an external reconciliation process, not a platform ownership transfer or settlement instruction. P258 names sese.022 for error and requires account or account owner for history queries.

[Complete source diagram](../diagrams/curated/fig-0010.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [servicing party](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md), [account owner](../../../../../../../shared/reference/participants/participant-src-000374-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000374-account-servicer.md), [authorised party](../../../../../../../shared/reference/participants/participant-src-000374-authorised-party.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000374-direct-connected-participant-dcp.md), [t2s actor](../../../../../../../shared/reference/participants/participant-src-000374-t2s-actor.md).

## Preconditions, trigger and outcome

T8 requires the relevant business objects to exist within the instructing party scope and criteria, and static-data privileges for report reception. Postconditions are explicitly None. Query modes are initiated by the Instructing Party; penalty reporting is initiated by a scheduled system event. T12 additionally requires the subscriber to have configured interest in receiving the report.

Business-error response uses the sese.022 family (P258/P266). Its exact version is unspecified here. No cancellation or settlement reversal is implied by that error.

[Complete usage conditions, account roles and source examples](../business-rules.md).
