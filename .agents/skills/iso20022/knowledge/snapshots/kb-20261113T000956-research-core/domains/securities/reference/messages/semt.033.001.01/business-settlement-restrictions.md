---
template: false
document_kind: "message-business"
review_status: "needs-review"
manual_curated: true
domain: "securities"
message_id: "semt.033.001.01"
message_family: "semt.033"
source_ids: ["src-000380", "src-000381"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
source_locations: [{"source_id": "src-000380", "locator": "Functionality P195–P213; BusinessTransactions P304–P307"}, {"source_id": "src-000381", "file_page": 145, "heading_path": ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01"]}]
participant_ids: ["participant-src-000380-t2s", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-instructing-party", "participant-src-000380-executing-servicing-party", "participant-src-000380-account-owner", "participant-src-000380-reporting-party", "participant-src-000380-requestor"]
flow_ids: ["flow-src-000380-p111-transaction-cancellation-request-query-and-report", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode", "flow-src-000380-p304-securities-transaction-cancellation-request-report-semt-033"]
limitations: ["Business requirements remain distinct from XSD validation.", "Institutional/system senders are preserved as the source states them; functional roles and data-party fields are not globally equated.", "Source wording discrepancies P200/P235 remain issue-000056."]
updated: "2026-11-09"
---

# semt.033.001.01 — Settlement Restrictions business use

The Securities Transaction Cancellation Request Report is sent by T2S to a CSD or any T2S party, it provides information on Cancellation Instructions for Settlement or Intra Position Movement Instructions.

[src-000380](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; Functionality P195–P213. Exact-definition binding: src-000381 file page 145.

## Sender, receiver and usage conditions

T2S sends this response/report to a CSD or another directly connected T2S participant/party as stated in the cited narrative.

**P305** — The Securities Transaction Cancellation Request Report message is sent by T2S to a CSD or a directly connected T2S party This message is used to provide information on Cancellation Instructions for Settlement and Intra Position Movement instructions. 

**P306** — Where used in response to a semt.032 request, the content will cover the requested scope.

**P307** — Where used in response to a configured report, the content will cover all Securities Accounts under the Reporting Party’s scope. The delta version returns new Cancellation Instructions not reported to the requestor in a previous execution of the Transaction Cancellation Request report.

## Business rules and building-block conditions

The following source clauses retain mandatory/optional, repetitive/non-repetitive, FULL/STTS, activity and exclusive-location conditions. These are MDR requirements; successful XSD validation alone does not establish compliance.

| Source paragraph | Literal substantive clause |
| --- | --- |
| P197 | When used in response to a semt.032 message (pull mode), it provides the information of those Cancellation Instructions that fulfilled the criteria specified previously on the Query Message. |
| P198 | When used in response to a configured report (push mode), the content will cover all Securities Accounts under the Reporting Party’s scope. The report in push mode is triggered by defined business and time events. |
| P200 | Query Definition |
| P201 | This building block is mandatory and non-repetitive. It defines the pagination of the message. |
| P203 | This building block is mandatory and non-repetitive. It provides general characteristics related to the report. Among this information we have: |
| P204 | &lt;Query Type&gt;: it defines whether the query response needs to retrieve full details of the Cancellation instruction or only its current status values. |
| P205 | &lt;Update Type&gt;: Indicates whether the report is complete (full mode) or contains changes only (delta mode). |
| P206 | &lt;Activity Indicator&gt;: it indicates whether there is activity or information update reported in the statement. |
| P208 | This building block is optional and repetitive. It contains details on the cancellation requests corresponding to the criteria of the query. Several rules apply which are: |
| P209 | &lt;Account Owner&gt; must be present or &lt;Account Owner&gt; nested under &lt;Cancellation&gt; block must be present, but not both. |
| P210 | &lt;Processing Status&gt; must be present or &lt;Processing Status&gt; nested under &lt;Cancellation&gt; block must be present, but not both. |
| P211 | &lt;Safekeeping Account&gt; must be present or &lt;Safekeeping Account&gt; nested under &lt;Cancellation&gt; block must be present, but not both. |
| P212 | If &lt;Activity Indicator&gt; is equal to false, then &lt;Cancellations&gt; must be absent. |
| P213 | If &lt;Activity Indicator&gt; is equal to true, then &lt;Cancellations&gt; must be present. |



P200 labels the block Query Definition while P201 says it defines pagination. The exact schema and companion definition remain separately authoritative for structure; the source label is preserved under issue-000056.

## Source block names

| Source paragraph | Block heading |
| --- | --- |
| P200 | Query Definition |
| P202 | Report General Details |
| P207 | Cancellations |



The following clauses belong to the preceding block heading in the source; the paragraph locators preserve this order.

## Source-scoped participants and reusable flows

- [T2S](../../../../../shared/reference/participants/participant-src-000380-t2s.md)
- [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md)
- [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md)
- [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Account Owner](../../../../../shared/reference/participants/participant-src-000380-account-owner.md)
- [Reporting Party](../../../../../shared/reference/participants/participant-src-000380-reporting-party.md)
- [Requestor](../../../../../shared/reference/participants/participant-src-000380-requestor.md)

- [Transaction cancellation request query and report](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p111-transaction-cancellation-request-query-and-report.md)
- [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md)
- [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md)
- [Securities Transaction Cancellation Request Report (semt.033)](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p304-securities-transaction-cancellation-request-report-semt-033.md)

## Shared header and related context

P119 requires Business Application Header family `head.001`; it does not identify an exact version. Retrieve the shared header catalog for supplied exact definitions. Context families `sese.020`, `sese.027`, `sese.030`, `sese.031` and business-error family `sese.022` are retained at family scope where the source does not print a full identifier. Cancellation query/reporting does not constitute a reversal.

[All source diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/index.md) · [Literal business examples and XML checks](../../message-sets/t2s-settlement-restrictions/september-2025/business-examples.md) · [Source limitations](../../../../../tracking/issues.md)
