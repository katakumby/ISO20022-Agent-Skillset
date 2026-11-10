---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Reconciliation and reporting: push mode"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-reporting-push"
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-reporting-third-party"]
message_ids: ["semt.002.001.12", "semt.003.001.12", "semt.016.001.10", "semt.017.001.14", "semt.018.001.15", "semt.019.001.12", "semt.022.001.07"]
limitations: ["The picture lists available reports. Narrative P582 and account setup determine which reports are supplied; the list is not a requirement to send every report every time.", "Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P572", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[572]"}, {"source_id": "src-000196", "paragraph_id": "P573", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[573]"}, {"source_id": "src-000196", "paragraph_id": "P574", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[574]"}, {"source_id": "src-000196", "paragraph_id": "P575", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[575]"}, {"source_id": "src-000196", "paragraph_id": "P576", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[576]"}, {"source_id": "src-000196", "paragraph_id": "P577", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[577]"}, {"source_id": "src-000196", "paragraph_id": "P578", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[578]"}, {"source_id": "src-000196", "paragraph_id": "P579", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting"], "xml_path": "/w:document/w:body/w:p[579]"}, {"source_id": "src-000196", "paragraph_id": "P580", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[580]"}, {"source_id": "src-000196", "paragraph_id": "P581", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[581]"}, {"source_id": "src-000196", "paragraph_id": "P582", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[582]"}, {"source_id": "src-000196", "paragraph_id": "P583", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[583]"}, {"source_id": "src-000196", "paragraph_id": "P584", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[584]"}, {"source_id": "src-000196", "paragraph_id": "P585", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[585]"}, {"source_id": "src-000196", "paragraph_id": "P586", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[586]"}, {"source_id": "src-000196", "paragraph_id": "P587", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[587]"}, {"source_id": "src-000196", "paragraph_id": "P588", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[588]"}, {"source_id": "src-000196", "paragraph_id": "P589", "heading_path": ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"], "xml_path": "/w:document/w:body/w:p[589]"}]
diagram_ids: ["fig-0002", "fig-0031", "fig-0067"]
---

# Reconciliation and reporting: push mode

## Purpose and boundaries

Provide data for reconciliation of holdings, transactions and allegements.

**Trigger:** Account setup and account-owner reporting requirements.

**Preconditions:** High-level Reconciliation definition states None.

**Outcome/postconditions:** High-level definition states None; detected breaks may lead to investigation and other processes.

**Evidence:** [src-000196](../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §4 Reconciliation table26; §5.11 Push Mode paragraphs275–286 and table43.

## Participants

- [instructing party](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- [executing servicing party](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- [reporting third party](../../../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md)

## Activities, decisions and alternatives

Executing/servicing party provides statements according to setup and SLA; not all reports are always supplied. Instructing party reconciles holdings and transactions, then investigates breaks. A third party may receive audit trail for each individual pending instruction covering its status and modification history. Keep this participant even if a two-party diagram omits it.

- [Complete source table 26](../documents/src-000196/tables/tbl-0026.md) — §4 Reconciliation table26; §5.11 Push Mode paragraphs275–286 and table43.
- [Complete source table 43](../documents/src-000196/tables/tbl-0043.md) — §4 Reconciliation table26; §5.11 Push Mode paragraphs275–286 and table43.

## Messages and navigation

- [semt.002.001.12](../../../../messages/semt.002.001.12/index.md)
- [semt.003.001.12](../../../../messages/semt.003.001.12/index.md)
- [semt.016.001.10](../../../../messages/semt.016.001.10/index.md)
- [semt.017.001.14](../../../../messages/semt.017.001.14/index.md)
- [semt.018.001.15](../../../../messages/semt.018.001.15/index.md)
- [semt.019.001.12](../../../../messages/semt.019.001.12/index.md)
- [semt.022.001.07](../../../../messages/semt.022.001.07/index.md)

[Participant index](../participants.md) · [Flow index](index.md)

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Reporting push mode with third party](../diagrams/settlement-sequences/fig-0067.md)

src-000196 P572–P590.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- C — Third Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P572** — Reconciliation and Reporting

**src-000196 P573** — This section describes the various reports an account servicer can provide to the account owner or designated agent.

**src-000196 P574** — For instance these reports can provide at a specified moment in time:

**src-000196 P575** — the details of pending increases and decreases of holdings, for all or selected securities in a specified safekeeping account, for all or selected reasons why the transaction is pending

**src-000196 P576** — the details of any increases and/or decreases of holdings, which may have occurred over a specified period of time, for all or a selected quantity of securities in the requested safekeeping account, which the account servicer 

**src-000196 P577** — holds for the account owner

**src-000196 P578** — the quantity and identification of financial instruments that the account servicer maintains for the account owner

**src-000196 P579** — the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle

**src-000196 P580** — Push Mode Scenario

**src-000196 P581** — This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a sub-custodian for instance).

**src-000196 P582** — Based on an account set up at a specified moment in time the executing/servicing party can send the following reports to the instructing party:

**src-000196 P583** — SecuritiesBalanceCustodyReport

**src-000196 P584** — SecuritiesBalanceAccountingReport

**src-000196 P585** — SecuritiesTransactionPostingReport

**src-000196 P586** — SecuritiesTransactionPendingReport

**src-000196 P587** — SecuritiesSettlementTransactionAllegementReport

**src-000196 P588** — IntraPositionMovementPostingReport

**src-000196 P589** — A third party may also be involved (for example a CSD) in the reporting/reconciliation process. In this scenario, the executing/servicing party sends the SecuritiesSettlementTransactionAudiTrailReport for each individual pending instruction to the third party. This message is used to advise of the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle.

### Source activity responsibilities

[Activity table T43 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0043.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The picture lists available reports. Narrative P582 and account setup determine which reports are supplied; the list is not a requirement to send every report every time.

<!-- SETTLEMENT-SEQUENCE-END -->










<!-- SOURCE-ACTIVITY-0002-START -->
[Reporting communication overview — source activity/communication diagram](../diagrams/settlement-activities/fig-0002.md)
<!-- SOURCE-ACTIVITY-0002-END -->

<!-- SOURCE-ACTIVITY-0031-START -->
[Reporting push activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0031.md)
<!-- SOURCE-ACTIVITY-0031-END -->
