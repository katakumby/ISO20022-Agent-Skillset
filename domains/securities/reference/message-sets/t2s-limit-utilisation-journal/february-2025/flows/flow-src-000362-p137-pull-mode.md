---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
flow_id: "flow-src-000362-p137-pull-mode"
title: "Pull mode"
source_locations: [{"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "table_id": null}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "table_id": null}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}]
participants: ["participant-src-000362-central-counterparty", "participant-src-000362-central-securities-depositories-csd", "participant-src-000362-credit-consumer", "participant-src-000362-credit-provider", "participant-src-000362-direct-connected-participant-dcp", "participant-src-000362-executing-servicing-party", "participant-src-000362-executing-servicing-party-t2s-in-this-case", "participant-src-000362-instructing-party", "participant-src-000362-national-central-bank-ncb", "participant-src-000362-payment-agent", "participant-src-000362-payment-bank", "participant-src-000362-responsible-party", "participant-src-000362-settlement-bank", "participant-src-000362-settlement-infrastructure", "participant-src-000362-t2s-operator"]
message_mapping_evidence: []
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_families: ["camt.064", "camt.065"]
search_terms: ["Pull mode", "Executing/Servicing Party (T2S in this case)", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
flow_scope: "pull mode"
---











# Pull mode

Source context: T2S LimitUtilisationJournal. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party (T2S in this case) | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party-t2s-in-this-case.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000362/diagrams/fig-0010.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T10](../documents/src-000362/tables/tbl-0010.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Request Limit Utilisation Journal | Send a query to the Executing/Servicing Party to request information regarding the limits as managed by the credit provider and corresponding to the criteria as defined within the message. | Instructing Party |
| Validate Request | Technical and business validation of the request before further processing or not.<br>• If Yes, i.e., the request is valid, go to the Process Request. <br>• If No, the Send Reject is triggered. | Executing/Servicing Party (T2S in this case) |
| Send Reject | Generate a report and route it to the communication layer to inform the Instructing Party that the Request is rejected with a specification of the operational error resulting from the validation of a request. | Executing/Servicing Party (T2S in this case) |
| Process Request | Generate a report providing information regarding the limits as managed by the credit provider and corresponding to the criteria received within the incoming query message and trigger the Send Report. | Executing/Servicing Party (T2S in this case) |
| Send Report | Route a report to the communication layer. | Executing/Servicing Party (T2S in this case) |
| Receive Report | Go to the requested reporting activity. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000362](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Heading path: Description of BusinessActivities / Pull mode.

## Curated source flow

The scope picture shows an NCB/payment/settlement-bank query to Settlement Infrastructure and the returning report. P51 additionally names CSDs; P62/P77 also name directly connected system participants. Those narrative actors are included in the flow and participant library even though this particular picture omits them. Complete Word6 confirms the floating source text is part of the settlement-infrastructure label, with no additional actor or message. The query/report uses Business Application Header head.001 (P55), not Business File Header.

[Complete source diagram](../diagrams/curated/fig-0001.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000362-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md), [settlement bank](../../../../../../../shared/reference/participants/participant-src-000362-settlement-bank.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000362-settlement-infrastructure.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000362-direct-connected-participant-dcp.md).

## Curated source flow

The source lists six contextual business-role alternatives beside Instructing Party and Settlement infrastructure beside Executing/Servicing Party. Dotted annotation leaders point from the two role/lifeline areas toward their labels; these are mapping annotations, not additional message exchanges. T7 independently confirms the mappings. The reconstruction uses native notes for the labels while retaining the exact leader appearance in the original.

[Complete source diagram](../diagrams/curated/fig-0003.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000362-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000362-direct-connected-participant-dcp.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md), [payment agent](../../../../../../../shared/reference/participants/participant-src-000362-payment-agent.md), [central counterparty](../../../../../../../shared/reference/participants/participant-src-000362-central-counterparty.md), [t2s operator](../../../../../../../shared/reference/participants/participant-src-000362-t2s-operator.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000362-settlement-infrastructure.md).

## Curated source flow

An instructing party investigating limits triggers Request Limit Utilisation Journal. The servicing/executing party validates the request: No sends a rejection report specifying the operational error; Yes processes and sends the requested report. Both paths reach the source black join bar and return to Receive Report, followed by Reconcile Limits and an end point. The native fork/join bar preserves the source mark without asserting parallel execution: the preceding Yes/No choice is exclusive. T8 requires limits to exist within the instructing party scope; the source states postconditions as none. T10 preserves technical and business validation and the communication-layer handoff.

[Complete source diagram](../diagrams/curated/fig-0010.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000362-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md), [credit provider](../../../../../../../shared/reference/participants/participant-src-000362-credit-provider.md), [credit consumer](../../../../../../../shared/reference/participants/participant-src-000362-credit-consumer.md), [responsible party](../../../../../../../shared/reference/participants/participant-src-000362-responsible-party.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000362-direct-connected-participant-dcp.md).

## Curated source flow

Instructing Party sends the query to the source-labelled Execution/Servicing Party and receives the report. P151-P153 explains that the central system returns limit amounts, utilisation and the transaction journal managed by the credit provider and matching query criteria. The broader source describes an additional scheduled push mode; this two-message picture depicts the request/response exchange only. Rejection uses the same report with operational error content (T10 and P314-P316), not a distinct cancellation or reversal message.

[Complete source diagram](../diagrams/curated/fig-0012.md).

### Adjacent source narrative

**P150** Limit Utilisation Journal Query

**P151** A CSD, NCB, payment bank or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counterparty) sends a Limit Utilisation Journal Query via camt.064 to the central system (e.g. T2S in this case). Its purpose is to query information regarding the journal of transaction impacting the utilisation of limits that have been defined by the system participant.

**P152** Limit Utilisation Journal Report

**P153** The LimitUtilisationJournalReport message (camt.065) is exchanged between the central system, (e.g. T2S in this case) and a CSD, NCB, payment bank or a directly connected system party (the central securities depository participant granted direct access, like a bank or central counterparty). It is used to return information about the limit amounts, utilisation and journal of transactions impacting the utilisation of limits. Its purpose is to report information regarding the limits as managed by the credit provider and corresponding to the criteria received within the incoming query message (camt.064).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000362-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md), [national central bank ncb](../../../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md), [payment bank](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000362-direct-connected-participant-dcp.md), [credit provider](../../../../../../../shared/reference/participants/participant-src-000362-credit-provider.md), [credit consumer](../../../../../../../shared/reference/participants/participant-src-000362-credit-consumer.md), [responsible party](../../../../../../../shared/reference/participants/participant-src-000362-responsible-party.md).

## Source-defined conditions and direction

T8 requires limits to exist within the scope of the Instructing Party and states postconditions as none. Its two triggers are a participant query or a scheduled system event at end of day. This mode is triggered by an Instructing Party query and sends camt.064 to Executing/Servicing Party; camt.065 returns data or an operational error.

Linked modes: [pull mode](flow-src-000362-p137-pull-mode.md), [push mode](flow-src-000362-p143-push-mode.md).
