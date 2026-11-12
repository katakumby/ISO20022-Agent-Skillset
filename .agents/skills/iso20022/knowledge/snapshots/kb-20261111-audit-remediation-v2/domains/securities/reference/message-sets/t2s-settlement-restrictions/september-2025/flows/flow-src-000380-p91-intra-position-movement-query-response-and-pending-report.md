---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"
title: "Intra-position movement query, response and pending report"
source_locations: [{"source_id": "src-000380", "locator": "direct-body paragraph P97", "heading_path": ["Scope and Functionality", "Scope", "Intra Position Movement Query, Query Response and Pending Report"], "xml_path": "/w:document/w:body/w:p[97]", "word_file_page": 6}]
limitations: ["The first two messages are the pull query/response; the dotted pending-report arrow is an independently configured push report, not a compulsory third step after every query (P98–P99).", "Source arrows distinguish query green, response black and pending report blue. Native sequence rendering retains labels and line styles; these colors are stated here rather than interpreted as extra message states."]
manual_curated: true
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-t2s"]
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.034.001.01"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0001.md"]
---

# Intra-position movement query, response and pending report





<!-- SETTLEMENT-RESTRICTIONS-FIG-1-START -->
## Curated source-grounded flow

[Intra-position movement query, response and pending report](../diagrams/settlement-restrictions/fig-0001.md)

### Source narrative and mode conditions

**src-000380 P91** — Intra Position Movement Query, Query Response and Pending Report

**src-000380 P92** — The scope of the Intra Position Movement Query, Query Response and Pending Report is supported by the following messages:

**src-000380 P93** — semt.028: Intra Position Movement Query.

**src-000380 P94** — semt.029: Intra Position Movement Query Response.

**src-000380 P95** — semt.034: Intra Position Movement Pending Report.

**src-000380 P96** — The communication flow can be represented as follows:

**src-000380 P98** — The Intra Position Query and Query Response provide T2S and T2S Participants with the ability to query and report details of any previously sent Intra Position Movement Instructions and the related securities positions. This business activity is performed in pull mode.

**src-000380 P99** — The Intra Position Pending Report provides detailed reporting (in delta mode or in full mode) only on unsettled Intra Position Movement Instructions and the related securities positions. It is only available as per subscription services within T2S and therefore only provided in push mode.

### Trigger, preconditions, postconditions and responsibilities

[Complete T4](../documents/src-000380/tables/tbl-0004.md)

| MessageDefinition | Message Identifier |
| --- | --- |
| Intra Position Movement Query | semt.028 |
| Intra Position Movement Query Response | semt.029 |
| Securities Settlement Conditions Modification Request Query | semt.030 |
| Securities Settlement Conditions Modification Request Report  | semt.031 |
| Securities Transaction Cancellation Request Query | semt.032 |
| Securities Transaction Cancellation Request Report | semt.033 |
| Intra Position Movement Pending Report | semt.034 |


[Complete T5](../documents/src-000380/tables/tbl-0005.md)

| Description | Definition |
| --- | --- |
| Instructing Party | Party that instructs the executing/servicing party to process and monitor a transaction. |
| Executing / Servicing Party | Party that processes, monitors and reports on transactions received from the Instructing party. |


[Complete T6](../documents/src-000380/tables/tbl-0006.md)

| Description | Definition |
| --- | --- |
| Settlement Infrastructure | The party that provides services to its members for the settlement of transactions and holding of assets (e.g., T2S, RTGS). |
| Central Securities Depositories (CSD) | An infrastructure that, holds or controls, the holding of physical or dematerialised financial instruments belonging to all, or a large portion of, the investors in a securities market. This affects the centralised transfer of ownership of such securities by entries on its books and records. |
| Direct Connected Participant (DCP) | The party, which is not a CSD and that, is directly connected to the Settlement Infrastructure Platform. It could be a local custodian, a global custodian, a stock exchange , a central counterparty, etc. |
| Central Counterparty | An infrastructure that is very often a component of a clearinghouse, and facilitates clearing and settlement for its members by standing between the buyer and the seller of a trade. It may net transactions, and substitutes itself as settlement counterparty to each position. |
| T2S Operator | The T2S operator is the top level of the hierarchical role and access rights model. The T2S operator role classification includes all T2S system users of the entity, which will be responsible for the day-to-day operation and management of T2S. The T2S actors managed by this entity shall be CSDs and NCBs participating in T2S. At the highest level, the T2S operator shall have access to all data and functionality in the subordinate level. |


[Complete T7](../documents/src-000380/tables/tbl-0007.md)

| BusinessRole | Instructing Party | Executing/Servicing Party |
| --- | --- | --- |
| Settlement Infrastructure |  | X |
| Central Securities Depositories (CSD) | X |  |
| Direct Connected Participant (DCP) | X |  |
| Central Counterparty | X |  |
| T2S Operator | X |  |


[Complete T8](../documents/src-000380/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | The process provides responses to queries regarding maintenance of Settlement and intra-position movement instructions (cancellation /modification request) previously sent and allows sending of reconciliation results of intra-position movement instructions (pending and posted) via query responses or via reporting. |
| Trigger | The process is triggered either by the system through a scheduled or by the receipt of a query request sent by the Instructing Party. |
| Pre-conditions | Settlement or Intra position movement instructions must exist to query within the scope of the Instructing Party and which correspond to the criteria as defined within the query and report.<br>The Instructing Party must hold necessary privileges within the Static Data configuration in order to receive reports. |
| Post-conditions | None |
| Role | Instructing Party for the query. <br>Executing Party / Servicing Party for the query response and for reporting. |


### Participants and exact definitions

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)

| Canonical exact definition | Exact-definition evidence |
| --- | --- |
| [semt.028.001.01](../../../../messages/semt.028.001.01/index.md) | src-000381 September2025 file page 7 |
| [semt.029.001.01](../../../../messages/semt.029.001.01/index.md) | src-000381 September2025 file page 57 |
| [semt.034.001.01](../../../../messages/semt.034.001.01/index.md) | src-000381 September2025 file page 169 |



The exact identifiers above come from the separately cited companion Part2 in the same September2025 message-set publication. Unversioned context families are not assigned arbitrary definitions.

### Alternatives and source distinctions

- The first two messages are the pull query/response; the dotted pending-report arrow is an independently configured push report, not a compulsory third step after every query (P98–P99).
- Source arrows distinguish query green, response black and pending report blue. Native sequence rendering retains labels and line styles; these colors are stated here rather than interpreted as extra message states.

<!-- SETTLEMENT-RESTRICTIONS-FIG-1-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-START -->
[semt.028.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.028.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-START -->
[semt.029.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.029.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-START -->
[semt.034.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.034.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-END -->
