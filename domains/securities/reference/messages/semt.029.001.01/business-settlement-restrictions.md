---
template: false
document_kind: "message-business"
review_status: "needs-review"
manual_curated: true
domain: "securities"
message_id: "semt.029.001.01"
message_family: "semt.029"
source_ids: ["src-000380", "src-000381"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
source_locations: [{"source_id": "src-000380", "locator": "Functionality P136–P155; BusinessTransactions P285–P288"}, {"source_id": "src-000381", "file_page": 57, "heading_path": ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01"]}]
participant_ids: ["participant-src-000380-t2s", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-instructing-party", "participant-src-000380-executing-servicing-party", "participant-src-000380-account-owner"]
flow_ids: ["flow-src-000380-p259-pull-mode", "flow-src-000380-p285-intra-position-movement-query-response-semt-029", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
limitations: ["Business requirements remain distinct from XSD validation.", "Institutional/system senders are preserved as the source states them; functional roles and data-party fields are not globally equated.", "Source wording discrepancies P200/P235 remain issue-000056."]
updated: "2026-11-09"
---

# semt.029.001.01 — Settlement Restrictions business use

The Intra Position Movement Query Response message is sent in response to a semt.028 (Intra Position Movement Query). This message is sent by T2S to a CSD or other directly connected T2S participant. It is used to provide information on Intra-Position Movement instructions.

[src-000380](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; Functionality P136–P155. Exact-definition binding: src-000381 file page 57.

## Sender, receiver and usage conditions

T2S sends this response/report to a CSD or another directly connected T2S participant/party as stated in the cited narrative.

**P286** — The Intra Position Movement Query Response message is sent by T2S to CSD or other directly connected T2S party. This message is used to provide information on Intra Position Movement instructions.

**P287** — The Intra Position Movement Query Response is sent in response to a semt.028 message.

## Business rules and building-block conditions

The following source clauses retain mandatory/optional, repetitive/non-repetitive, FULL/STTS, activity and exclusive-location conditions. These are MDR requirements; successful XSD validation alone does not establish compliance.

| Source paragraph | Literal substantive clause |
| --- | --- |
| P140 | This building block is mandatory and non-repetitive. It contains information about pagination of the report. |
| P142 | This building block is mandatory and non-repetitive. It contains general characteristics related to the report information.  |
| P144 | &lt;Query Type&gt;: it defines whether the query response relates to an Instruction, Status or Status Period query. |
| P145 | &lt;Activity Indicator&gt;: it indicates whether there is activity or information update reported in the statement. |
| P148 | This building block is optional and repetitive. It contains information relating to the movements corresponding to the criteria as defined within the query. Several rules apply which are: |
| P149 | If &lt;Query Type&gt; is equal to Full [FULL], then &lt;Movement Details&gt; linked to &lt;Movements&gt; must be present. |
| P150 | If &lt;Query Type&gt; is equal to Status [STTS], then &lt;Movement Details&gt; linked to &lt;Movements&gt; must be absent. |
| P151 | If &lt;Activity Indicator&gt; is equal to false, then &lt;Movements&gt; must be absent. |
| P152 | If &lt;Activity Indicator&gt; is equal to true, then &lt;Movements&gt; must be present. |
| P153 | &lt;Account Owner&gt; must be present or &lt;Account Owner&gt; linked to &lt;Movement&gt; must be present, but not both. |
| P154 | &lt;Safekeeping Account&gt; must be present or &lt;Safekeeping Account&gt; linked to &lt;Movement&gt; must be present, but not both. |
| P155 | &lt;Status And Reason&gt; must be present or &lt;Status And Reason&gt; linked to &lt;Movement&gt; must be present, but not both. |



## Source block names

| Source paragraph | Block heading |
| --- | --- |
| P139 | Pagination |
| P141 | Report General Details |
| P147 | Movements |



The following clauses belong to the preceding block heading in the source; the paragraph locators preserve this order.

## Source-scoped participants and reusable flows

- [T2S](../../../../../shared/reference/participants/participant-src-000380-t2s.md)
- [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md)
- [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md)
- [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Account Owner](../../../../../shared/reference/participants/participant-src-000380-account-owner.md)

- [Intra-position movement query, response and pending report](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p91-intra-position-movement-query-response-and-pending-report.md)
- [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md)
- [Intra Position Movement Query Response (semt.029)](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p285-intra-position-movement-query-response-semt-029.md)

## Shared header and related context

P119 requires Business Application Header family `head.001`; it does not identify an exact version. Retrieve the shared header catalog for supplied exact definitions. Context families `sese.020`, `sese.027`, `sese.030`, `sese.031` and business-error family `sese.022` are retained at family scope where the source does not print a full identifier. Cancellation query/reporting does not constitute a reversal.

[All source diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/index.md) · [Literal business examples and XML checks](../../message-sets/t2s-settlement-restrictions/september-2025/business-examples.md) · [Source limitations](../../../../../tracking/issues.md)
