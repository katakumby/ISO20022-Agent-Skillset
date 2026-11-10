---
template: false
document_kind: "message-business"
review_status: "needs-review"
manual_curated: true
domain: "securities"
message_id: "semt.031.001.01"
message_family: "semt.031"
source_ids: ["src-000380", "src-000381"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
source_locations: [{"source_id": "src-000380", "locator": "Functionality P167–P183; BusinessTransactions P293–P298"}, {"source_id": "src-000381", "file_page": 97, "heading_path": ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01"]}]
participant_ids: ["participant-src-000380-t2s", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-instructing-party", "participant-src-000380-executing-servicing-party", "participant-src-000380-account-owner", "participant-src-000380-requestor"]
flow_ids: ["flow-src-000380-p101-settlement-condition-modification-request-query-and-report", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode", "flow-src-000380-p293-securities-settlement-conditions-modification-request-report-semt-031"]
limitations: ["Business requirements remain distinct from XSD validation.", "Institutional/system senders are preserved as the source states them; functional roles and data-party fields are not globally equated.", "Source wording discrepancies P200/P235 remain issue-000056."]
updated: "2026-11-09"
---

# semt.031.001.01 — Settlement Restrictions business use

The Securities Settlement Conditions Modification Request Report message is sent by T2S to a CSD or any other T2S participant. This message is used to provide information on Securities Settlement Conditions Modification Instructions for Settlement Instructions or Intra-position Movement Instructions. This message is composed of the following message building blocks:

[src-000380](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; Functionality P167–P183. Exact-definition binding: src-000381 file page 97.

## Sender, receiver and usage conditions

T2S sends this response/report to a CSD or another directly connected T2S participant/party as stated in the cited narrative.

**P295** — The Securities Settlement Conditions Modification Request Report message is sent by T2S to CSDs or other directly connected T2S parties. This message is used as response to the semt.030 message, containing information on Securities Settlement Conditions Modification Instructions.

**P297** — The message is also sent by T2S as a report triggered by defined business and time events. The delta version returns new Securities Settlement Conditions Modification Instructions not reported to the requestor in a previous execution of the Securities Settlement Conditions Modification Request report.

## Business rules and building-block conditions

The following source clauses retain mandatory/optional, repetitive/non-repetitive, FULL/STTS, activity and exclusive-location conditions. These are MDR requirements; successful XSD validation alone does not establish compliance.

| Source paragraph | Literal substantive clause |
| --- | --- |
| P170 | This building block is mandatory and non-repetitive. It contains information about pagination of the message. |
| P172 | This building block is mandatory and non-repetitive. It contains general characteristics related to the report information.  |
| P174 | &lt;Query Type&gt;: it defines whether the query response (or report) outputs full details or only the current status values. |
| P175 | &lt;Activity Indicator&gt;: it indicates whether there is activity or information update reported in the statement. |
| P178 | This building block is optional and repetitive. It contains details on the modification requests corresponding to the criteria of the query. Several rules apply which are: |
| P179 | If &lt;Activity Indicator&gt; is equal to false, then &lt;Modifications&gt; must be absent. |
| P180 | If &lt;Activity Indicator&gt; is equal to true, then &lt;Modifications&gt; must be present. |
| P181 | &lt;Account Owner&gt; must be present or &lt;Account Owner&gt; linked to &lt;Modification&gt; must be present, but not both. |
| P182 | &lt;Safekeeping Account&gt; must be present or &lt;Safekeeping Account&gt; linked to &lt;Modification&gt; must be present, but not both. |
| P183 | &lt;Processing Status&gt; must be present or &lt;Processing Status&gt; linked to &lt;Modification&gt; must be present, but not both. |



## Source block names

| Source paragraph | Block heading |
| --- | --- |
| P169 | Pagination |
| P171 | Report General Details |
| P177 | Modifications |



The following clauses belong to the preceding block heading in the source; the paragraph locators preserve this order.

## Source-scoped participants and reusable flows

- [T2S](../../../../../shared/reference/participants/participant-src-000380-t2s.md)
- [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md)
- [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md)
- [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Account Owner](../../../../../shared/reference/participants/participant-src-000380-account-owner.md)
- [Requestor](../../../../../shared/reference/participants/participant-src-000380-requestor.md)

- [Settlement-condition modification request query and report](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p101-settlement-condition-modification-request-query-and-report.md)
- [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md)
- [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md)
- [Securities Settlement Conditions Modification Request Report (semt.031)](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p293-securities-settlement-conditions-modification-request-report-semt-031.md)

## Shared header and related context

P119 requires Business Application Header family `head.001`; it does not identify an exact version. Retrieve the shared header catalog for supplied exact definitions. Context families `sese.020`, `sese.027`, `sese.030`, `sese.031` and business-error family `sese.022` are retained at family scope where the source does not print a full identifier. Cancellation query/reporting does not constitute a reversal.

[All source diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/index.md) · [Literal business examples and XML checks](../../message-sets/t2s-settlement-restrictions/september-2025/business-examples.md) · [Source limitations](../../../../../tracking/issues.md)
