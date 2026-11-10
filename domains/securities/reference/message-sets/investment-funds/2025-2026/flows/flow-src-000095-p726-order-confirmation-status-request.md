---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p726-order-confirmation-status-request"
title: "Order Confirmation Status Request"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "locator": "/w:document/w:body/w:p[726]", "paragraph_id": "P726", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "locator": "/w:document/w:body/w:p[727]", "paragraph_id": "P727", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "locator": "/w:document/w:body/w:p[728]", "paragraph_id": "P728", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "locator": "/w:document/w:body/w:p[729]", "paragraph_id": "P729", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "locator": "/w:document/w:body/w:p[730]", "paragraph_id": "P730", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[5]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[6]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4303; 65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03"}]
message_ids: []
message_families: ["setr.057", "setr.058"]
search_terms: ["Order Confirmation Status Request", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor", "setr.057", "setr.058"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Confirmation Status Request

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

**P727** This message flow section illustrates the use of the RequestForOrderConfirmationStatusReport message in typical message sequencing scenarios. The RequestForOrderConfirmationStatusReport message is sent by the executing party to the instructing party. It is used to request the status of one or several order confirmation messages. There may be one or more intermediaries in the transaction chain.

**P728** The reply to the RequestForOrderConfirmationStatusReport message is an OrderConfirmationStatusReport message.

**P729** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P730** The intermediary party is, for example, a distributor.

## Messages and alternative paths

Source-supported message family mentions: `setr.057`, `setr.058`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Order Confirmation Status Request .
