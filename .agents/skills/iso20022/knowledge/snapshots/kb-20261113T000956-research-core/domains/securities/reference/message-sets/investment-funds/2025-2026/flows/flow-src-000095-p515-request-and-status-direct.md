---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p515-request-and-status-direct"
title: "Order Cancellation and Status  / Subscription  / Request and Status - Direct"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Direct"], "locator": "/w:document/w:body/w:p[515]", "paragraph_id": "P515", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Direct"], "locator": "/w:document/w:body/w:p[516]", "paragraph_id": "P516", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Direct"], "locator": "/w:document/w:body/w:p[517]", "paragraph_id": "P517", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Direct"], "locator": "/w:document/w:body/w:p[518]", "paragraph_id": "P518", "table_id": null}]
participants: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[12]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3243; 51 setr.011.001.05 SubscriptionOrderCancellationRequestV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}]
message_ids: []
message_families: ["setr.010", "setr.011", "setr.017"]
search_terms: ["Request and Status - Direct", "Instructing Party", "Executing Party", "setr.010", "setr.011", "setr.017"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P507–511: deadline and acceptance depend on SLA; executing party checks legality, initiator right and SLA permission. P517: cancellation possible and completed.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0072.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Order Cancellation and Status  / Subscription  / Request and Status - Direct

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P515, direct-body paragraph P518.

## Purpose, trigger and common conditions

**P505** This message flow section illustrates the use of the order cancellation messages in typical message sequencing scenarios. The different order cancellation request messages are sent by the instructing party to the executing party. There may be one or more intermediaries in the transaction chain.

**P506** The OrderCancellationStatusReport message is sent by the executing party to the instructing party to inform the instructing party of the acceptance or rejection of an order cancellation request message that was previously sent by the instructing party.

**P507** The deadline and acceptance of an order cancellation request message is subject to a service level agreement (SLA).

**P508** Depending on the scenario, the executing party will verify whether:

**P509** it is legally possible to cancel the order,

**P510** the party that initiated the cancellation request has the right to do so,

**P511** the cancellation request is allowed by the service level agreement (SLA).

**P512** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent.

**P513** The intermediary party is, for example, an distributor.

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [executing party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Explicit figure sender/receiver; see step table. |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Explicit figure sender/receiver; see step table. |
| [investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P516** The instructing party sends a SubscriptionOrder message to the executing party.

**P517** Subsequently, the instructing party sends a SubscriptionOrderCancellationRequest message to the executing party. As it is possible to cancel the order, the executing party responds by sending an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

### fig-0072

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0072.md) (Word file page 69).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrder |
| 2 | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionOrderCancellationRequest |
| 3 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | OrderCancellationStatusReport (CAND) |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| setr.010 | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.011 | [setr.011.001.05](../../../../messages/setr.011.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.017 | [setr.017.001.05](../../../../messages/setr.017.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P507–511: deadline and acceptance depend on SLA; executing party checks legality, initiator right and SLA permission. P517: cancellation possible and completed.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
