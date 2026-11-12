---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Status - Intermediary"]
content_origin: "source-transcription"
---

# Status - Intermediary

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status  / Status - Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P881** Status - Intermediary

**P882** An instructing party sends a TransferOutInstruction message to the executing party via one or several intermediaries.

**P883** Subsequently, as specified in the Service Level Agreement (SLA) in place between the two parties, the executing party sends a TransferInstructionStatusReport message to the instructing party, via one or several intermediaries. The status report gives the status of the transfer instruction, for example, Accepted (PACK).

**P884** The message flow works in a similar way when a TransferInInstruction message is sent.

[fig-0126 - original figure evidence](../diagrams/fig-0126.md)

