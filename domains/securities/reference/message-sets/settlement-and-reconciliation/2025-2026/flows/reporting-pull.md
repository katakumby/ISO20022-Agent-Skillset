---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Reconciliation and reporting: pull mode"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-reporting-pull"
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-reporting-third-party"]
message_ids: ["semt.002.001.12", "semt.003.001.12", "semt.016.001.10", "semt.017.001.14", "semt.018.001.15", "semt.019.001.12", "semt.021.001.09", "semt.022.001.07", "sese.021.001.08", "sese.022.001.08"]
limitations: ["The source narrative describes alternative requested statements and optional query-status responses. The list of report arrows is not a requirement to return every report for a query.", "Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P591", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[591]"}, {"source_id": "src-000196", "paragraph_id": "P592", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[592]"}, {"source_id": "src-000196", "paragraph_id": "P593", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[593]"}, {"source_id": "src-000196", "paragraph_id": "P594", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[594]"}, {"source_id": "src-000196", "paragraph_id": "P595", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[595]"}, {"source_id": "src-000196", "paragraph_id": "P596", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[596]"}, {"source_id": "src-000196", "paragraph_id": "P597", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[597]"}, {"source_id": "src-000196", "paragraph_id": "P598", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[598]"}, {"source_id": "src-000196", "paragraph_id": "P599", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[599]"}, {"source_id": "src-000196", "paragraph_id": "P600", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[600]"}, {"source_id": "src-000196", "paragraph_id": "P601", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[601]"}, {"source_id": "src-000196", "paragraph_id": "P602", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[602]"}, {"source_id": "src-000196", "paragraph_id": "P603", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[603]"}, {"source_id": "src-000196", "paragraph_id": "P604", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"], "xml_path": "/w:document/w:body/w:p[604]"}]
diagram_ids: ["fig-0002", "fig-0023", "fig-0032", "fig-0068"]
---

# Reconciliation and reporting: pull mode

## Purpose and boundaries

Respond to a request for statement or transaction status.

**Trigger:** Receipt of statement/status request.

**Preconditions:** No additional formal pull-mode precondition list is provided.

**Outcome/postconditions:** Requested statement/status is returned after successful processing; request status may also be advised.

**Evidence:** [src-000196](<../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>), §5.11 Pull Mode paragraphs288–300 and table44; §6.11 paragraphs602–604.

## Participants

- [instructing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md>)
- [executing servicing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md>)
- [reporting third party](<../../../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md>)

## Activities, decisions and alternatives

Instructing party sends SecuritiesStatementQuery or SecuritiesTransactionStatusQuery. Executing party validates request and may return SecuritiesStatusOrStatementQueryStatusAdvice before requested report. A third party can request a detailed report on a pending transaction and receive audit trail. Statement selection, optional request status and failed validation are separate decisions.

- [Complete source table 44](<../documents/src-000196/tables/tbl-0044.md>) — §5.11 Pull Mode paragraphs288–300 and table44; §6.11 paragraphs602–604.

## Messages and navigation

- [semt.021.001.09](<../../../../messages/semt.021.001.09/index.md>)
- [sese.021.001.08](<../../../../messages/sese.021.001.08/index.md>)
- [sese.022.001.08](<../../../../messages/sese.022.001.08/index.md>)
- [semt.022.001.07](<../../../../messages/semt.022.001.07/index.md>)

[Participant index](<../participants.md>) · [Flow index](<index.md>)

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Reporting pull mode with third party](../diagrams/settlement-sequences/fig-0068.md)

src-000196 P591–P605.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- C — Third Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P591** — Pull Mode Scenario

**src-000196 P592** — This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a sub-custodian for instance), upon request of the account owner, the executing/reporting party sends back a specific statement.

**src-000196 P593** — The instructing party requests a statement with a SecuritiesStatementQuery or requests a status on a securities transaction using the SecuritiesTransactionStatusQuery.

**src-000196 P594** — The executing/servicing party may send back a SecuritiesStatusOrStatementQueryStatusAdvice to provide a status on the request.

**src-000196 P595** — The executing/servicing party sends back the statement requested, for instance:

**src-000196 P596** — SecuritiesBalanceCustodyReport

**src-000196 P597** — SecuritiesBalanceAccountingReport

**src-000196 P598** — SecuritiesTransactionPostingReport

**src-000196 P599** — SecuritiesTransactionPendingReport

**src-000196 P600** — SecuritiesSettlementTransactionAllegementReport

**src-000196 P601** — IntraPositionMovementPostingReport

**src-000196 P602** — A third party may also be involved (for example a CSD) in the reporting/reconciliation process. In this scenario, the third party requests a detailed report on a pending securities transaction to the executing/servicing party.

**src-000196 P603** — The executing/servicing party may send back a SecuritiesStatusOrStatementQueryStatusAdvice to provide a status on the request.

**src-000196 P604** — The executing/servicing party sends back the SecuritiesTransactionAuditTrailReport to the third party.

### Source activity responsibilities

[Activity table T44 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0044.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The source narrative describes alternative requested statements and optional query-status responses. The list of report arrows is not a requirement to return every report for a query.

<!-- SETTLEMENT-SEQUENCE-END -->















<!-- SOURCE-ACTIVITY-0002-START -->
[Reporting communication overview — source activity/communication diagram](../diagrams/settlement-activities/fig-0002.md)
<!-- SOURCE-ACTIVITY-0002-END -->

<!-- SOURCE-ACTIVITY-0023-START -->
[Statement or status query validation — source activity/communication diagram](../diagrams/settlement-activities/fig-0023.md)
<!-- SOURCE-ACTIVITY-0023-END -->

<!-- SOURCE-ACTIVITY-0032-START -->
[Reporting pull activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0032.md)
<!-- SOURCE-ACTIVITY-0032-END -->
