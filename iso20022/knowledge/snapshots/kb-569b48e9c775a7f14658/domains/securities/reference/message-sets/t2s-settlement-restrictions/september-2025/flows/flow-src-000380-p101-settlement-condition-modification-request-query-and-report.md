---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p101-settlement-condition-modification-request-query-and-report"
title: "Settlement-condition modification request query and report"
source_locations: [{"source_id": "src-000380", "locator": "direct-body paragraph P107", "heading_path": ["Scope and Functionality", "Scope", "Securities Settlement Conditions Modification Request Query/Report"], "xml_path": "/w:document/w:body/w:p[107]", "word_file_page": 7}]
limitations: ["The original green arrows are query/report scope; black instruction/status arrows provide the preceding business context. Exact versions of context families sese.030 and sese.031 are not supplied by this figure and are not guessed.", "P108 describes pull retrieval of a previously sent modification request. P109 separately describes delta or full push reporting configured by subscription. PUSH/PULL belongs to the report arrow; no mandatory query is inferred for a push report.", "The retained full Word page preserves the native connector/text composite and institutional pictograms. Component images alone do not contain the complete figure. Mermaid participant boxes replace the artwork while preserving the functional labels, sender/receiver direction and solid/dashed lines."]
manual_curated: true
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-requestor", "participant-src-000380-servicing-party", "participant-src-000380-t2s"]
message_ids: ["semt.030.001.01", "semt.031.001.01"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0002.md"]
---

# Settlement-condition modification request query and report




<!-- SETTLEMENT-RESTRICTIONS-FIG-2-START -->
## Curated source-grounded flow

[Settlement-condition modification request query and report](../diagrams/settlement-restrictions/fig-0002.md)

### Source narrative and mode conditions

**src-000380 P101** — Securities Settlement Conditions Modification Request Query/Report

**src-000380 P102** — The scope of the Securities Settlement Conditions Modification Request Query and the Securities Settlement Conditions Modification Report is supported by the following messages:

**src-000380 P103** — semt.030: Securities Settlement Conditions Modification Request Query.

**src-000380 P104** — semt.031: Securities Settlement Conditions Modification Report.

**src-000380 P105** — The communication flow can be represented as follows:

**src-000380 P108** — The Securities Settlement Conditions Modification Request Query and Query Response provide T2S and T2S participants with the ability to query and report details of any previously sent Securities Settlement Condition Modification Request. This business activity is performed in pull mode.

**src-000380 P109** — The Securities Settlement Conditions Modification Report provides detailed reporting (in delta mode or in full mode) on Securities Settlement Condition Modification Requests. In T2S, it is only available as per subscription configurations defining its triggering and therefore is provided in push mode.

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
- [Servicing Party](../../../../../../../shared/reference/participants/participant-src-000380-servicing-party.md)

| Canonical exact definition | Exact-definition evidence |
| --- | --- |
| [semt.030.001.01](../../../../messages/semt.030.001.01/index.md) | src-000381 September2025 file page 87 |
| [semt.031.001.01](../../../../messages/semt.031.001.01/index.md) | src-000381 September2025 file page 97 |



The exact identifiers above come from the separately cited companion Part2 in the same September2025 message-set publication. Unversioned context families are not assigned arbitrary definitions.

### Alternatives and source distinctions

- The original green arrows are query/report scope; black instruction/status arrows provide the preceding business context. Exact versions of context families sese.030 and sese.031 are not supplied by this figure and are not guessed.
- P108 describes pull retrieval of a previously sent modification request. P109 separately describes delta or full push reporting configured by subscription. PUSH/PULL belongs to the report arrow; no mandatory query is inferred for a push report.
- The retained full Word page preserves the native connector/text composite and institutional pictograms. Component images alone do not contain the complete figure. Mermaid participant boxes replace the artwork while preserving the functional labels, sender/receiver direction and solid/dashed lines.

<!-- SETTLEMENT-RESTRICTIONS-FIG-2-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.030-START -->
[semt.030.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.030.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.030-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-START -->
[semt.031.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.031.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-END -->
