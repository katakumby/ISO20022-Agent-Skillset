---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p504-order-cancellation-and-status"
title: "Order Cancellation and Status"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[504]", "paragraph_id": "P504", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[505]", "paragraph_id": "P505", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[506]", "paragraph_id": "P506", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[507]", "paragraph_id": "P507", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[508]", "paragraph_id": "P508", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[509]", "paragraph_id": "P509", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[510]", "paragraph_id": "P510", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[511]", "paragraph_id": "P511", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[512]", "paragraph_id": "P512", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "locator": "/w:document/w:body/w:p[513]", "paragraph_id": "P513", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}]
message_ids: []
message_families: ["setr.017"]
search_terms: ["Order Cancellation and Status", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor", "setr.017"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Cancellation and Status

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Distributor | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P505** This message flow section illustrates the use of the order cancellation messages in typical message sequencing scenarios. The different order cancellation request messages are sent by the instructing party to the executing party. There may be one or more intermediaries in the transaction chain.

**P506** The OrderCancellationStatusReport message is sent by the executing party to the instructing party to inform the instructing party of the acceptance or rejection of an order cancellation request message that was previously sent by the instructing party. 

**P507** The deadline and acceptance of an order cancellation request message is subject to a service level agreement (SLA). 

**P508** Depending on the scenario, the executing party will verify whether:

**P509** it is legally possible to cancel the order, 

**P510** the party that initiated the cancellation request has the right to do so, 

**P511** the cancellation request is allowed by the service level agreement (SLA). 

**P512** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P513** The intermediary party is, for example, an distributor.

## Messages and alternative paths

Source-supported message family mentions: `setr.017`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Order Cancellation and Status .
