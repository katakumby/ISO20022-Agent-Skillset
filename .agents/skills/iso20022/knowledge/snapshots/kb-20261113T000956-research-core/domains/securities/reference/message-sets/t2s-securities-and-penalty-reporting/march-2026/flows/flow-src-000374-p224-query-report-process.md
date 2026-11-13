---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p224-query-report-process"
title: "Query Report Process"
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000374", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}]
participants: ["participant-src-000374-account-owner", "participant-src-000374-account-servicer", "participant-src-000374-central-counterparty", "participant-src-000374-central-securities-depositories-csd", "participant-src-000374-csd-participant", "participant-src-000374-direct-connected-participant-dcp", "participant-src-000374-executing-servicing-party", "participant-src-000374-instructing-party", "participant-src-000374-national-central-bank", "participant-src-000374-penalty-creditor", "participant-src-000374-penalty-debtor", "participant-src-000374-servicing-party", "participant-src-000374-settlement-infrastructure", "participant-src-000374-system-application", "participant-src-000374-t2s-operator"]
message_mapping_evidence: []
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
message_families: ["semt.025", "semt.026", "semt.027", "semt.040", "semt.044"]
search_terms: ["Query Report Process", "Instructing Party", "Servicing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
flow_scope: "parent process with query/report modes"
---











# Query Report Process

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process provides responses to queries regarding Settlement instructions previously sent, Securities Account Balances and Penalties computed due to Settlement failures and allows the sending of reconciliation results via query responses or via reporting.

Evidence: [T8](../documents/src-000374/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered either by the system through a scheduled event in case of reports or by the receipt of a query request sent by the Instructing Party.

Evidence: [T8](../documents/src-000374/tables/tbl-0008.md), source row 3.

### Pre-conditions

The respective business object (i.e settlement Instructions, Securities Accounts, Penalties computed) must exist to query within the scope of the Instructing Party and which correspond to the criteria as defined within the query and report.
The Instructing Party must hold necessary privileges within the Static Data configuration to receive reports.

Evidence: [T8](../documents/src-000374/tables/tbl-0008.md), source row 4.

### Post-conditions

None

Evidence: [T8](../documents/src-000374/tables/tbl-0008.md), source row 5.

### Role

Instructing Party for the query. 
Executing Party / Servicing Party for the query response and for reporting.

Evidence: [T8](../documents/src-000374/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000374-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000374/tables/tbl-0008.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: BusinessProcess Description.

## Curated source flow

Native use-case notation preserves four actor symbols, their stereotypes, the directed business-area-to-actor links and the plain business-area/process link. The lower process hierarchy is reconstructed in the linked detail view, preserving its rectangles, diamonds, ellipses, dashed arrows and green reporting scope. No include/extend or inheritance semantics are inferred. P205 explicitly identifies only green reporting processes as scope; surrounding instruction, cancellation, modification and confirmation processes are context.

[Complete source diagram](../diagrams/curated/fig-0004.md).

Scoped participants: [csd participant](../../../../../../../shared/reference/participants/participant-src-000374-csd-participant.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [central counterparty](../../../../../../../shared/reference/participants/participant-src-000374-central-counterparty.md), [system application](../../../../../../../shared/reference/participants/participant-src-000374-system-application.md), [t2s operator](../../../../../../../shared/reference/participants/participant-src-000374-t2s-operator.md), [national central bank](../../../../../../../shared/reference/participants/participant-src-000374-national-central-bank.md).

## Curated source flow

The source overview links Settlement & Reconciliation to Instruction, Status reporting, Confirmation and Reconciliation. Instruction branches to Modification and Cancellation request, both pointing to Status reporting. Confirmation points to Status reporting and Reversal. Reconciliation points to Reporting and Query/Response; these three nodes alone are green. Cancellation requests and reversals remain distinct contextual processes; the diagram does not assign their messages to the five reporting definitions.

[Complete source diagram](../diagrams/curated/fig-0005.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [direct connected participant dcp](../../../../../../../shared/reference/participants/participant-src-000374-direct-connected-participant-dcp.md).

## Curated source flow

The context diagram starts with Instruction then Status reporting, Cash Penalties Calculation and Settlement Confirmation. Each of the last three information stages feeds Reconciliation, the only green node, which leads to the final symbol. This is a high-level business context, not a claim that every instruction incurs a penalty or that each arrow is a separate XML message. P250 explicitly includes pending and posted transactions and computed penalties if any.

[Complete source diagram](../diagrams/curated/fig-0013.md).

### Adjacent source narrative

**P247** BusinessTransactions

**P248** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a Business Transaction.

**P250** In the context of a Business Transaction, the process enables the reconciliation of (pending and posted) transactions and their computed penalties (if any) by providing the associated data. The main processes are highlighted in green, the surrounding processes in blue.

**P252** The reconciliation communication flows can be represented as follows:

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000374-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md), [account owner](../../../../../../../shared/reference/participants/participant-src-000374-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000374-account-servicer.md), [central securities depositories csd](../../../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md), [csd participant](../../../../../../../shared/reference/participants/participant-src-000374-csd-participant.md), [penalty debtor](../../../../../../../shared/reference/participants/participant-src-000374-penalty-debtor.md), [penalty creditor](../../../../../../../shared/reference/participants/participant-src-000374-penalty-creditor.md).

## Preconditions, trigger and outcome

T8 requires the relevant business objects to exist within the instructing party scope and criteria, and static-data privileges for report reception. Postconditions are explicitly None. Query modes are initiated by the Instructing Party; penalty reporting is initiated by a scheduled system event. T12 additionally requires the subscriber to have configured interest in receiving the report.

[Complete usage conditions, account roles and source examples](../business-rules.md).
