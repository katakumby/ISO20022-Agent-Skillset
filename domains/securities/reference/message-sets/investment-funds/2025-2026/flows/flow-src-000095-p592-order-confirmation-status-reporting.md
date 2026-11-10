---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p592-order-confirmation-status-reporting"
title: "Order Confirmation Status Reporting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "locator": "/w:document/w:body/w:p[592]", "paragraph_id": "P592", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "locator": "/w:document/w:body/w:p[593]", "paragraph_id": "P593", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "locator": "/w:document/w:body/w:p[594]", "paragraph_id": "P594", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "locator": "/w:document/w:body/w:p[595]", "paragraph_id": "P595", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "locator": "/w:document/w:body/w:p[596]", "paragraph_id": "P596", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[5]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03"}]
message_ids: []
message_families: ["setr.057"]
search_terms: ["Order Confirmation Status Reporting", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor", "setr.057"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Confirmation Status Reporting

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

**P593** This message flow section illustrates the use of the OrderConfirmationStatusReport message in typical message sequencing scenarios. The OrderConfirmationStatusReport message is sent by the instructing party to the executing party to provide the status of a subscription, redemption or switch confirmation or confirmation amendment.

**P594** There may be one or more intermediaries in the transaction chain.

**P595** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P596** The intermediary party is, for example, a distributor.

## Messages and alternative paths

Source-supported message family mentions: `setr.057`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Order Confirmation Status Reporting .
