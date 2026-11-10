---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p759-portfolio-transfer-management"
title: "Portfolio Transfer Management"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:p[759]", "paragraph_id": "P759", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:p[760]", "paragraph_id": "P760", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:p[761]", "paragraph_id": "P761", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:p[762]", "paragraph_id": "P762", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:p[763]", "paragraph_id": "P763", "table_id": null}]
participants: ["participant-src-000095-transferor", "participant-src-000095-transferee"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 943; 35 sese.012.001.12 PortfolioTransferInstructionV12"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 1302; 37 sese.014.001.09 PortfolioTransferCancellationRequestV09"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[2]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: []
message_families: ["sese.009", "sese.011", "sese.012", "sese.014"]
search_terms: ["Portfolio Transfer Management", "Transferor", "Transferee", "sese.009", "sese.011", "sese.012", "sese.014"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Portfolio Transfer Management

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transferor | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transferor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transferee | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transferee.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P760** This message flow section illustrates the use of the portfolio transfer messages in typical message sequencing scenarios. The portfolio transfer instruction and confirmation messages are exchanged between a transferee (new plan manager) and the transferor (old plan manager).

**P761** The PortfolioTransferInstruction message is sent by the transferee and may be accepted or rejected by the transferor. The transferor may report on the status of a PortfolioTransferInstruction message with the TransferInstructionStatusReport message.

**P762** The PortfolioTransferInstruction message may be cancelled by the transferee with the PortfolioTransferCancellationRequest message. The transferor may report on the status of a PortfolioTransferCancellationRequest message with the TransferInstructionStatusReport message.

**P763** The transferee may query the status of a previously sent PortfolioTransferInstruction message with a RequestForTransferStatusReport message.

## Messages and alternative paths

Source-supported message family mentions: `sese.009`, `sese.011`, `sese.012`, `sese.014`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Portfolio Transfer Management.
