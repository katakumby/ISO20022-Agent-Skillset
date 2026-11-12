---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran"
title: "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"
source_locations: [{"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:p[239]", "paragraph_id": "P239", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:p[240]", "paragraph_id": "P240", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:p[241]", "paragraph_id": "P241", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:p[242]", "paragraph_id": "P242", "table_id": null}]
participants: ["participant-src-000374-central-securities-depositories-csd", "participant-src-000374-direct-connected-participant-dcp", "participant-src-000374-executing-servicing-party", "participant-src-000374-instructing-party", "participant-src-000374-payment-bank", "participant-src-000374-settlement-bank", "participant-src-000374-settlement-infrastructure"]
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.026.001.01", "semt.027.001.01"]
message_families: ["semt.026", "semt.027"]
search_terms: ["Securities Settlement Transaction Query and Securities Settlement Transaction Query Response", "Executing / Servicing Party", "Instructing Party", "semt.026", "semt.027"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
flow_scope: "query mode"
related_message_families: ["sese.022"]
---









# Securities Settlement Transaction Query and Securities Settlement Transaction Query Response

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0011](../documents/src-000374/diagrams/fig-0011.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T11](../documents/src-000374/tables/tbl-0011.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Send Securities Settlement Instructions Query. | Instructing Party sends a query to the Executing/Servicing Party for querying all securities settlement instructions corresponding to the criteria as defined within the query message. | Instructing Party |
| Process Query. | Technical and business validation of the request query before further processing or not. <br>• If Yes, i.e., the request query is valid, go to Send Securities Settlement Instructions Query Response. <br>• If No, Error Processing is triggered. | Executing/Servicing Party. |
| Error Processing. | Adds operational errors to response before routing to Send Error Response. | Executing/Servicing Party. |
| Send Error Response. | Routes error response to communication layer. | Executing/Servicing Party. |
| Send Securities Settlement Instructions Query Response. | Routes response to communication layer. | Executing/Servicing Party. |
| Monitor. | Check for incoming communications associated with original instruction. | Instructing Party. |
| Reconcile. | External process reconciling impact of current status of original instruction. | Instructing Party. |

## Messages and alternative paths

Source-supported message family mentions: `semt.026`, `semt.027`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: Description of BusinessActivities / Securities Account Position Query and Securities Account Position Response / Securities Settlement Transaction Query and Securities Settlement Transaction Query Response.

## Curated source flow

A CSD or directly connected T2S participant sends an instruction, current-status or status-period query. The response returns matching settlement instructions. P266 specifies a sese.022-family response on business error; this success-only picture omits that alternative. The exact error-message definition is not resolved from Part1.

[Complete source diagram](../diagrams/curated/fig-0002.md).

### Adjacent source narrative

**P259** Securities Settlement Transaction Query (semt.026)

**P260** The Securities Settlement Transaction Query message is sent by a Central Securities Depository or a directly connected T2S participant (e.g. payment bank/settlement bank) to T2S. This message is used to request information on Settlement Instructions.

**P261** This message is sent to T2S for the following query types:

**P262** Settlement Instruction Query.

**P263** Settlement Instruction Current Status Query.

**P264** Settlement Instruction Status Audit Trail Query.

**P266** In response to the Securities Settlement Transaction Query message, T2S sends a Securities Settlement Transaction Query Response message (semt.027) with the corresponding requested settlement instructions or a Securities Status Or Statement Query Status Advice message (sese.022) in the case of a business error.

**P267** Securities Settlement Transaction Query Response (semt.027)

**P268** The Securities Settlement Transaction Query Response message is sent by T2S to a Central Securities Depository or a directly connected T2S participant (e.g. payment bank/settlement bank). This message is used to provide information on Settlement Instructions based on the criteria as defined within the query message.

**P270** To request the Securities Settlement Transaction Query Response message, the sender sends a semt.026 message containing search criteria to restrict the query. This message is sent by T2S in the following message usages:

**P271** Settlement Instruction Query Response.

**P272** Settlement Instruction Current Status Query Response.

**P273** Settlement Instruction Status Audit Trail Query Response.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000374-direct-connected-participant-dcp.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000374-payment-bank.md), [settlement bank](../../../../../../../shared/reference/participants/participant-src-000374-settlement-bank.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).

## Curated source flow

The query initiator requests instructions matching its criteria. Executing/Servicing Party validates the query. The No branch adds operational error details and sends an error response; Yes sends the requested instruction response. Both source arrows join at the black bar and return to Monitor, then Reconcile. The preceding Yes/No decision is exclusive; the bar is retained without inventing parallel execution. The original vertical bar appears horizontally in this top-down native layout. T11 and P266 identify the error alternative; the exact sese.022 definition is unspecified.

[Complete source diagram](../diagrams/curated/fig-0011.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000374-direct-connected-participant-dcp.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000374-payment-bank.md), [settlement bank](../../../../../../../shared/reference/participants/participant-src-000374-settlement-bank.md).

## Preconditions, trigger and outcome

T8 requires the relevant business objects to exist within the instructing party scope and criteria, and static-data privileges for report reception. Postconditions are explicitly None. Query modes are initiated by the Instructing Party; penalty reporting is initiated by a scheduled system event. T12 additionally requires the subscriber to have configured interest in receiving the report.

Business-error response uses the sese.022 family (P258/P266). Its exact version is unspecified here. No cancellation or settlement reversal is implied by that error.

[Complete usage conditions, account roles and source examples](../business-rules.md).
