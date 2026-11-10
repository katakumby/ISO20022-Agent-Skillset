---
template: false
document_kind: "message-business"
review_status: "needs-review"
manual_curated: true
domain: "securities"
message_id: "semt.028.001.01"
message_family: "semt.028"
source_ids: ["src-000380", "src-000381"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
source_locations: [{"source_id": "src-000380", "locator": "Functionality P126–P134; BusinessTransactions P282–P284"}, {"source_id": "src-000381", "file_page": 7, "heading_path": ["2 semt.028.001.01 IntraPositionMovementQueryV01"]}]
participant_ids: ["participant-src-000380-t2s", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-instructing-party", "participant-src-000380-executing-servicing-party"]
flow_ids: ["flow-src-000380-p259-pull-mode", "flow-src-000380-p282-intra-position-movement-query-semt-028", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
limitations: ["Business requirements remain distinct from XSD validation.", "Institutional/system senders are preserved as the source states them; functional roles and data-party fields are not globally equated.", "Source wording discrepancies P200/P235 remain issue-000056."]
updated: "2026-11-09"
---

# semt.028.001.01 — Settlement Restrictions business use

A CSD or other directly connected T2S party sends the Intra Position Movement Query message to T2S. This message allows CSDs or T2S Participants to query for all Intra Position Movement instructions satisfying a set of criteria, including business processing statuses and a corresponding date range period.

[src-000380](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; Functionality P126–P134. Exact-definition binding: src-000381 file page 7.

## Sender, receiver and usage conditions

The CSD or other directly connected T2S party sends this query to T2S.

**P283** — The Intra Position Movement Query message is sent by a CSD or other directly connected T2S party to T2S. This message is used to request information on Intra-Position Movement instructions.

**P284** — In response to the Intra Position Movement Query message, T2S sends a semt.029 message with the corresponding requested intra position movements or a sese.022 message in the case of a business error.

## Business rules and building-block conditions

The following source clauses retain mandatory/optional, repetitive/non-repetitive, FULL/STTS, activity and exclusive-location conditions. These are MDR requirements; successful XSD validation alone does not establish compliance.

| Source paragraph | Literal substantive clause |
| --- | --- |
| P129 | If the query specifies the Full [FULL] parameter as query type then the response to the query will include full details on the movements reported. |
| P130 | If the query specifies the Status [STTS] parameter as query type then the response will include limited details including the status on the movements reported. |
| P133 | This building block is mandatory and non-repetitive. It defines whether the query requests full details on the movements to be reported or only limited details including the status of the movements to be reported. It defines as well the criteria for extracting intra position movement information. |



## Source block names

| Source paragraph | Block heading |
| --- | --- |
| P132 | Query Definition |



The following clauses belong to the preceding block heading in the source; the paragraph locators preserve this order.

## Source-scoped participants and reusable flows

- [T2S](../../../../../shared/reference/participants/participant-src-000380-t2s.md)
- [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md)
- [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md)
- [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)

- [Intra-position movement query, response and pending report](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p91-intra-position-movement-query-response-and-pending-report.md)
- [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md)
- [Intra Position Movement Query (semt.028)](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p282-intra-position-movement-query-semt-028.md)

## Shared header and related context

P119 requires Business Application Header family `head.001`; it does not identify an exact version. Retrieve the shared header catalog for supplied exact definitions. Context families `sese.020`, `sese.027`, `sese.030`, `sese.031` and business-error family `sese.022` are retained at family scope where the source does not print a full identifier. Cancellation query/reporting does not constitute a reversal.

[All source diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/index.md) · [Literal business examples and XML checks](../../message-sets/t2s-settlement-restrictions/september-2025/business-examples.md) · [Source limitations](../../../../../tracking/issues.md)
