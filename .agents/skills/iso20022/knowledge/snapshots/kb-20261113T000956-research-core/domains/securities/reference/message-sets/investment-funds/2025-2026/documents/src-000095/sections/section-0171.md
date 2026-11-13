---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "]
content_origin: "source-transcription"
---

# Request for Transfer Status and Transfer Status 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P861** Request for Transfer Status and Transfer Status 

**P862** This message flow section illustrates the use of the transfer status messages in typical message sequencing scenarios. 

**P863** The RequestForTransferStatusReport message is sent by an instructing party to the executing party to request the status of a transfer instruction. The response to a RequestForTransferStatusReport is a TransferInstructionStatusReport or a TransferCancellationStatusReport message.

**P864** The TransferInstructionStatusReport is sent by the executing party to the instructing party. There may be one or more intermediaries in the transaction chain.

**P865** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P866** If the Service Level Agreement (SLA) allows it, a TransferInstructionStatusReport or a TransferCancellationStatusReport message may be sent by the executing party to the instructing party even though no RequestForTransferStatusReport message has been received by the executing party.

