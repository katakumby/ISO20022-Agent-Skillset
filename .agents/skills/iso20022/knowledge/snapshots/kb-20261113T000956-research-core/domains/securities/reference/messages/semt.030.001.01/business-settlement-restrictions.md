---
template: false
document_kind: "message-business"
review_status: "needs-review"
manual_curated: true
domain: "securities"
message_id: "semt.030.001.01"
message_family: "semt.030"
source_ids: ["src-000380", "src-000381"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
source_locations: [{"source_id": "src-000380", "locator": "Functionality P157–P165; BusinessTransactions P289–P292"}, {"source_id": "src-000381", "file_page": 87, "heading_path": ["4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01"]}]
participant_ids: ["participant-src-000380-t2s", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-instructing-party", "participant-src-000380-executing-servicing-party", "participant-src-000380-requestor"]
flow_ids: ["flow-src-000380-p101-settlement-condition-modification-request-query-and-report", "flow-src-000380-p268-pull-mode", "flow-src-000380-p289-securities-settlement-conditions-modification-request-query-semt-030"]
limitations: ["Business requirements remain distinct from XSD validation.", "Institutional/system senders are preserved as the source states them; functional roles and data-party fields are not globally equated.", "Source wording discrepancies P200/P235 remain issue-000056."]
updated: "2026-11-09"
---

# semt.030.001.01 — Settlement Restrictions business use

A CSD or other directly connected party sends the Securities Settlement Conditions Modification Request Query message to T2S. This message allows the requestor to query the full details or current status of Settlement Condition Modification Requests over Settlement Instruction(s) and Intra-position Movement Instruction(s) based on a set of search criteria or business attributes including business processing statuses and a corresponding date range period.

[src-000380](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; Functionality P157–P165. Exact-definition binding: src-000381 file page 87.

## Sender, receiver and usage conditions

The CSD or other directly connected T2S party sends this query to T2S.

**P290** — The Securities Settlement Conditions Modification Request Query is sent by a CSD or a directly connected T2S party (T2S Actor) to T2S. It aims at querying either the full details or the current status of Securities Settlement Conditions Modification Instructions of Settlement Instructions and Intra-position Movement Instructions based on a set of search criteria or business attributes. 

**P291** — In response to the Securities Settlement Conditions Modification Request Query message, T2S sends a semt.031 message with the corresponding Securities Settlement Conditions Modification Instructions. In case an error occurs, T2S sends a sese.022 message.

## Business rules and building-block conditions

The following source clauses retain mandatory/optional, repetitive/non-repetitive, FULL/STTS, activity and exclusive-location conditions. These are MDR requirements; successful XSD validation alone does not establish compliance.

| Source paragraph | Literal substantive clause |
| --- | --- |
| P160 | If the query specifies the Full [FULL] parameter as query type, then the response to the query will include full details on the Securities Settlement Conditions Modification Instructions reported. |
| P161 | If the query specifies the Status [STTS] parameter as query type, then the response will include limited details including the status on the Securities Settlement Conditions Modification Instructions reported. |
| P164 | This building block is mandatory and non-repetitive. It defines the criteria to extract the Settlement Condition Modification Request information for Settlement Instructions or Intra-position Movement Instructions. It defines as well whether the query response outputs full details or only its current status values. |



## Source block names

| Source paragraph | Block heading |
| --- | --- |
| P163 | Query Definition |



The following clauses belong to the preceding block heading in the source; the paragraph locators preserve this order.

## Source-scoped participants and reusable flows

- [T2S](../../../../../shared/reference/participants/participant-src-000380-t2s.md)
- [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md)
- [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md)
- [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)
- [Requestor](../../../../../shared/reference/participants/participant-src-000380-requestor.md)

- [Settlement-condition modification request query and report](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p101-settlement-condition-modification-request-query-and-report.md)
- [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md)
- [Securities Settlement Conditions Modification Request Query (semt.030)](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p289-securities-settlement-conditions-modification-request-query-semt-030.md)

## Shared header and related context

P119 requires Business Application Header family `head.001`; it does not identify an exact version. Retrieve the shared header catalog for supplied exact definitions. Context families `sese.020`, `sese.027`, `sese.030`, `sese.031` and business-error family `sese.022` are retained at family scope where the source does not print a full identifier. Cancellation query/reporting does not constitute a reversal.

[All source diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/index.md) · [Literal business examples and XML checks](../../message-sets/t2s-settlement-restrictions/september-2025/business-examples.md) · [Source limitations](../../../../../tracking/issues.md)
