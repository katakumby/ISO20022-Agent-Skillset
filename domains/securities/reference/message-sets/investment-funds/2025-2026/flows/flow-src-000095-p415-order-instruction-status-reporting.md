---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p415-order-instruction-status-reporting"
title: "Order Instruction Status Reporting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[415]", "paragraph_id": "P415", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[416]", "paragraph_id": "P416", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[417]", "paragraph_id": "P417", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[418]", "paragraph_id": "P418", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[419]", "paragraph_id": "P419", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[420]", "paragraph_id": "P420", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[421]", "paragraph_id": "P421", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[422]", "paragraph_id": "P422", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Instruction Status Reporting"], "locator": "/w:document/w:body/w:p[423]", "paragraph_id": "P423", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[2]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05"}]
message_ids: []
message_families: ["setr.016"]
search_terms: ["Order Instruction Status Reporting", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor", "setr.016"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Instruction Status Reporting

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

**P416** This message flow section illustrates the use of the OrderInstructionStatusReport message in typical message sequencing scenarios. The OrderInstructionStatusReport message is sent by the executing party to the instructing party. It is used to inform the instructing party of the status of its order/s or order message.

**P417** There may be one or more intermediaries in the transaction chain.

**P418** Different message flows may exist depending on the service level agreement (SLA). These include: 

**P419** how frequently an order instruction status message must be sent,

**P420** when, and if, an order instruction status message must be sent at a pre-defined time (at cut-off time or once a day) or upon request, 

**P421** which statuses will be sent, for example, 'rejected only', 'received and rejected only’, ‘sent to next party’ and accepted only’.

**P422** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P423** The intermediary party is, for example, a distributor.

## Messages and alternative paths

Source-supported message family mentions: `setr.016`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Order Instruction Status Reporting.
