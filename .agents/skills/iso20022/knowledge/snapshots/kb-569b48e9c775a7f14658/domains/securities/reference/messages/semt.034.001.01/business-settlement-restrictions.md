---
template: false
document_kind: "message-business"
review_status: "needs-review"
manual_curated: true
domain: "securities"
message_id: "semt.034.001.01"
message_family: "semt.034"
source_ids: ["src-000380", "src-000381"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
source_locations: [{"source_id": "src-000380", "locator": "Functionality P215–P231; BusinessTransactions P308–P310"}, {"source_id": "src-000381", "file_page": 169, "heading_path": ["8 semt.034.001.01 IntraPositionMovementPendingReportV01"]}]
participant_ids: ["participant-src-000380-t2s", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-instructing-party", "participant-src-000380-executing-servicing-party", "participant-src-000380-account-owner"]
flow_ids: ["flow-src-000380-p263-push-mode", "flow-src-000380-p308-intra-position-movement-pending-report-semt-034", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
limitations: ["Business requirements remain distinct from XSD validation.", "Institutional/system senders are preserved as the source states them; functional roles and data-party fields are not globally equated.", "Source wording discrepancies P200/P235 remain issue-000056."]
updated: "2026-11-09"
---

# semt.034.001.01 — Settlement Restrictions business use

The Intra Position Movement Pending Report is sent by T2S to a CSD or a directly connected T2S participant who can receive this report in delta mode or full mode. This message is used to provide information on pending intra position movement instructions. 

[src-000380](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; Functionality P215–P231. Exact-definition binding: src-000381 file page 169.

## Sender, receiver and usage conditions

T2S sends this response/report to a CSD or another directly connected T2S participant/party as stated in the cited narrative.

**P309** — The Intra Position Movement Pending Report message is sent by T2S to a CSD or a directly connected T2S participant. This message is used to provide information on pending intra position movement instructions in delta mode. 

**P310** — This report is triggered by defined business and time events. The delta version returns new pending intra-position movements or pending intra position movements, which were modified or cancelled.

## Business rules and building-block conditions

The following source clauses retain mandatory/optional, repetitive/non-repetitive, FULL/STTS, activity and exclusive-location conditions. These are MDR requirements; successful XSD validation alone does not establish compliance.

| Source paragraph | Literal substantive clause |
| --- | --- |
| P216 | The Intra Position Movement Pending Report is sent by T2S to a CSD or a directly connected T2S participant who can receive this report in delta mode or full mode. This message is used to provide information on pending intra position movement instructions.  |
| P217 | In T2S context, this report is triggered by defined business and time events. It returns all new pending intra position movement instructions or pending intra position movement instructions, which were modified or cancelled since the creation of the previous report (delta report). |
| P220 | This building block is mandatory and non-repetitive. It contains information about pagination of the report. |
| P222 | This building block is mandatory and non-repetitive. It contains general characteristics related to the report information. |
| P224 | This building block is optional and non-repetitive. It must contain the identification of the party that owns the account to or from which an entry is made. |
| P226 | This building block is mandatory and non-repetitive. It identifies the account to or from which a securities entry is made. |
| P228 | This building block is optional and repetitive. It provides the details of the movements reported. Several rules apply which are: |
| P229 | If &lt;Activity Indicator&gt; is equal to false, then &lt;Movements&gt; must be absent. |
| P230 | If &lt;Activity Indicator&gt; is equal to true, then &lt;Movements&gt; must be present. |
| P231 | &lt;Status And Reason&gt; must be present or &lt;Status And Reason&gt; linked to &lt;Movement&gt; must be present, but not both. |



## Source block names

| Source paragraph | Block heading |
| --- | --- |
| P219 | Pagination |
| P221 | Report General Details |
| P223 | Account Owner |
| P225 | Safekeeping Account |
| P227 | Movements |



The following clauses belong to the preceding block heading in the source; the paragraph locators preserve this order.

## Source-scoped participants and reusable flows

- [T2S](../../../../../shared/reference/participants/participant-src-000380-t2s.md)
- [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md)
- [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md)
- [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Account Owner](../../../../../shared/reference/participants/participant-src-000380-account-owner.md)

- [Intra-position movement query, response and pending report](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p91-intra-position-movement-query-response-and-pending-report.md)
- [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md)
- [Intra Position Movement Pending Report (semt.034)](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p308-intra-position-movement-pending-report-semt-034.md)

## Shared header and related context

P119 requires Business Application Header family `head.001`; it does not identify an exact version. Retrieve the shared header catalog for supplied exact definitions. Context families `sese.020`, `sese.027`, `sese.030`, `sese.031` and business-error family `sese.022` are retained at family scope where the source does not print a full identifier. Cancellation query/reporting does not constitute a reversal.

[All source diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/index.md) · [Literal business examples and XML checks](../../message-sets/t2s-settlement-restrictions/september-2025/business-examples.md) · [Source limitations](../../../../../tracking/issues.md)
