---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p524-request-and-status-bulk"
title: "Order Cancellation and Status  / Subscription  / Request and Status - Bulk "
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[524]", "paragraph_id": "P524", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[525]", "paragraph_id": "P525", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[526]", "paragraph_id": "P526", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[527]", "paragraph_id": "P527", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[528]", "paragraph_id": "P528", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[529]", "paragraph_id": "P529", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[530]", "paragraph_id": "P530", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[531]", "paragraph_id": "P531", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "], "locator": "/w:document/w:body/w:p[532]", "paragraph_id": "P532", "table_id": null}]
participants: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[8]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2523; 47 setr.007.001.05 SubscriptionBulkOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[9]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2761; 48 setr.008.001.05 SubscriptionBulkOrderCancellationRequestV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[10]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2766; 49 setr.009.001.05 SubscriptionBulkOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[12]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3243; 51 setr.011.001.05 SubscriptionOrderCancellationRequestV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[13]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}]
message_ids: []
message_families: ["setr.007", "setr.008", "setr.009", "setr.010", "setr.011", "setr.012", "setr.017"]
search_terms: ["Request and Status - Bulk", "Instructing Party", "Executing Party", "Intermediary", "setr.007", "setr.008", "setr.009", "setr.010", "setr.011", "setr.012", "setr.017"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P529: cancellation cancels the entire previous bulk message; unaffected party2/other orders must be re-instructed. P528: bulk has not yet executed. Figure shows party1 cancellation status before new bulk, whereas prose P529 precedes P530; prose paragraph order is not substituted for figure order.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0074.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Order Cancellation and Status  / Subscription  / Request and Status - Bulk 

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); source heading P524, direct-body paragraph P532.

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
| [intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Explicit figure sender/receiver; see step table. |
| [investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P525** Instructing party 1 sends a SubscriptionOrder message to the intermediary party. Instructing party 2 sends a SubscriptionOrder message to the intermediary party. There may be many instructing parties sending subscription orders to the intermediary party.

**P526** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder message to the executing party.

**P527** Subsequently, instructing party 1 sends a SubscriptionOrderCancellationRequest message to the intermediary party. In turn, the intermediary party sends a SubscriptionBulkOrderCancellationRequest message to the executing party.

**P528** As the bulk order has not yet been executed, the executing party effects the cancellation and sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the intermediary party.

**P529** The SubscriptionBulkOrderCancellationRequest message cancels the entire previously sent bulk order message, therefore, the intermediary party sends a SubscriptionBulkOrder message to re-instruct the order from instructing party 2 (and orders from other instructing parties for the same financial instrument).

**P530** After the intermediary party cancels the order of instructing party 1, the intermediary party sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to instructing party 1.

**P531** Later, when the new bulk order has been executed, the executing party sends a SubscriptionBulkOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrderConfirmation message to instructing party 2.

### fig-0074

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0074.md) (Word file page 70).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrder |
| 2 | [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrder |
| 3 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionBulkOrder |
| 4 | [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionOrderCancellationRequest |
| 5 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionBulkOrderCancellationRequest |
| 6 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | OrderCancellationStatusReport (CAND) |
| 7 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | OrderCancellationStatusReport (CAND) |
| 8 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | SubscriptionBulkOrder |
| 9 | [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | SubscriptionBulkOrderConfirmation |
| 10 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | SubscriptionOrderConfirmation |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| setr.007 | [setr.007.001.05](../../../../messages/setr.007.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.008 | [setr.008.001.05](../../../../messages/setr.008.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.009 | [setr.009.001.05](../../../../messages/setr.009.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.010 | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.011 | [setr.011.001.05](../../../../messages/setr.011.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.012 | [setr.012.001.06](../../../../messages/setr.012.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| setr.017 | [setr.017.001.05](../../../../messages/setr.017.001.05/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P529: cancellation cancels the entire previous bulk message; unaffected party2/other orders must be re-instructed. P528: bulk has not yet executed. Figure shows party1 cancellation status before new bulk, whereas prose P529 precedes P530; prose paragraph order is not substituted for figure order.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
