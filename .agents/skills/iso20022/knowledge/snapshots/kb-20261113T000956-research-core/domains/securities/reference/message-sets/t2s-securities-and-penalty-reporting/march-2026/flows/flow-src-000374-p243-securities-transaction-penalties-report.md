---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p243-securities-transaction-penalties-report"
title: "Securities Transaction Penalties Report"
source_locations: [{"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:p[243]", "paragraph_id": "P243", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:p[244]", "paragraph_id": "P244", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:p[245]", "paragraph_id": "P245", "table_id": null}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:p[246]", "paragraph_id": "P246", "table_id": null}]
participants: ["participant-src-000374-account-servicer", "participant-src-000374-central-securities-depositories-csd", "participant-src-000374-csd-participant", "participant-src-000374-executing-servicing-party", "participant-src-000374-external-csd", "participant-src-000374-instructing-party", "participant-src-000374-penalty-creditor", "participant-src-000374-penalty-debtor", "participant-src-000374-servicing-party", "participant-src-000374-settlement-infrastructure", "participant-src-000374-t2s-actor"]
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.044.001.01"]
message_families: ["semt.044"]
search_terms: ["Securities Transaction Penalties Report", "Instructing Party", "Servicing Party", "semt.044"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
flow_scope: "scheduled reporting mode"
---









# Securities Transaction Penalties Report

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0012](../documents/src-000374/diagrams/fig-0012.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T12](../documents/src-000374/tables/tbl-0012.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Generate Report | System process that creates report from previously calculated cash penalties satisfying reporting criteria (i.e., business day, debtor, creditor…), assuming the Instructing Party has specified an interested in Receiving the Report. | Servicing Party |
| Report cash Penalties Calculated | Route the previously generated report to the communication layer | Servicing Party |
| Monitor | Check for incoming communications associated with the Report configuration previously introduced in the system. | Instructing Party |
| Reconcile | External process reconciling impact of the penalties computed on the Settlement instructions previously sent to the system. | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `semt.044`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: Description of BusinessActivities / Securities Account Position Query and Securities Account Position Response / Securities Transaction Penalties Report.

## Curated source flow

The first instruction and returning status advice are surrounding context; only semt.044 is the green in-scope report. Cash penalties are computed daily for instructions unsettled after their intended settlement date and can be modified by a CSD or recalculated after reference-data changes. The picture retains the solid instruction and dashed returning status/report directions. The report is system-triggered (T8/T12), so the three arrows do not require one immediate penalty report for every instruction. Source sese.023/sese.024 family labels are retained without choosing an exact definition from another edition.

[Complete source diagram](../diagrams/curated/fig-0003.md).

### Adjacent source narrative

**P276** Securities Transaction Penalties Report (semt.044)

**P277** The Securities Transaction Penalties Report message is sent by T2S to T2S Actors, i.e. CSDs or CSD participants, to provide them with the Daily Penalty List, the List of Modified Penalties and the Monthly Aggregated Amounts of penalties for the previous month. T2S shall allow the relevant T2S Actor to receive penalties information under its default data scope.

**P278** In case of a CSD, the information shall include the penalties that are either imposed or credited to all the parties belonging to the CSD data scope.

**P279** In case of a CSD participant (or an External CSD), the information shall include the penalties that are either imposed or credited to the CSD participant (or the External CSD).


Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [servicing party](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [csd participant](../../../../../../../shared/reference/participants/participant-src-000374-csd-participant.md), [external csd](../../../../../../../shared/reference/participants/participant-src-000374-external-csd.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000374-account-servicer.md), [penalty debtor](../../../../../../../shared/reference/participants/participant-src-000374-penalty-debtor.md), [penalty creditor](../../../../../../../shared/reference/participants/participant-src-000374-penalty-creditor.md), [t2s actor](../../../../../../../shared/reference/participants/participant-src-000374-t2s-actor.md).

## Curated source flow

Servicing Party starts from a system event. If no report is required, the process ends. Otherwise it generates the report; a failure goes through internal Error Processing and ends without a drawn outbound error message. Success reports cash penalties to the subscribing Instructing Party, which monitors and reconciles. T12 requires report interest/configuration and criteria such as business day, debtor and creditor; T8 also requires static-data privileges and in-scope existing business objects. The technical sender is T2S; the recipient functional label does not imply that the subscriber initiated this scheduled event.

[Complete source diagram](../diagrams/curated/fig-0012.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [servicing party](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [csd participant](../../../../../../../shared/reference/participants/participant-src-000374-csd-participant.md), [external csd](../../../../../../../shared/reference/participants/participant-src-000374-external-csd.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000374-account-servicer.md), [penalty debtor](../../../../../../../shared/reference/participants/participant-src-000374-penalty-debtor.md), [penalty creditor](../../../../../../../shared/reference/participants/participant-src-000374-penalty-creditor.md), [t2s actor](../../../../../../../shared/reference/participants/participant-src-000374-t2s-actor.md).

## Preconditions, trigger and outcome

T8 requires the relevant business objects to exist within the instructing party scope and criteria, and static-data privileges for report reception. Postconditions are explicitly None. Query modes are initiated by the Instructing Party; penalty reporting is initiated by a scheduled system event. T12 additionally requires the subscriber to have configured interest in receiving the report.

Daily reports cover a given business day; modified-penalty reports cover changes since previous recalculation, including removal, reinclusion, reallocation, switching and reference-data-driven updates; monthly reports aggregate the previous month using the last available penalty amounts (P181/P183/P185). CSDs receive data-scope party penalties; CSD participants or External CSDs receive their own penalties (P277-P279).

[Complete usage conditions, account roles and source examples](../business-rules.md).
