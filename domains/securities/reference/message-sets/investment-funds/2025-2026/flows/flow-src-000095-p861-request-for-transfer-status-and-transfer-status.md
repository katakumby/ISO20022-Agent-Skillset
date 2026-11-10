---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p861-request-for-transfer-status-and-transfer-status"
title: "Request for Transfer Status and Transfer Status"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "locator": "/w:document/w:body/w:p[861]", "paragraph_id": "P861", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "locator": "/w:document/w:body/w:p[862]", "paragraph_id": "P862", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "locator": "/w:document/w:body/w:p[863]", "paragraph_id": "P863", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "locator": "/w:document/w:body/w:p[864]", "paragraph_id": "P864", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "locator": "/w:document/w:body/w:p[865]", "paragraph_id": "P865", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "locator": "/w:document/w:body/w:p[866]", "paragraph_id": "P866", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[2]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[3]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 809; 33 sese.010.001.07 TransferCancellationStatusReportV07"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: []
message_families: ["sese.009", "sese.010", "sese.011"]
search_terms: ["Request for Transfer Status and Transfer Status", "Instructing Party", "Executing Party", "Transfer Agent", "sese.009", "sese.010", "sese.011"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Request for Transfer Status and Transfer Status

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P862** This message flow section illustrates the use of the transfer status messages in typical message sequencing scenarios. 

**P863** The RequestForTransferStatusReport message is sent by an instructing party to the executing party to request the status of a transfer instruction. The response to a RequestForTransferStatusReport is a TransferInstructionStatusReport or a TransferCancellationStatusReport message.

**P864** The TransferInstructionStatusReport is sent by the executing party to the instructing party. There may be one or more intermediaries in the transaction chain.

**P865** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P866** If the Service Level Agreement (SLA) allows it, a TransferInstructionStatusReport or a TransferCancellationStatusReport message may be sent by the executing party to the instructing party even though no RequestForTransferStatusReport message has been received by the executing party.

## Messages and alternative paths

Source-supported message family mentions: `sese.009`, `sese.010`, `sese.011`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status .
