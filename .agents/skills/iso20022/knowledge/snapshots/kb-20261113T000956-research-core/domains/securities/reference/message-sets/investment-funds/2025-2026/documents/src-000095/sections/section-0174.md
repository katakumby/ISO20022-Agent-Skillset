---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Status - Direct"]
content_origin: "source-transcription"
---

# Status - Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status  / Status - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P876** Status - Direct

**P877** The instructing party sends a TransferOutInstruction message to the executing party. 

**P878** Subsequently, as specified in the SLA in place between the two parties, the executing party sends a TransferInstructionStatusReport message to the instructing party. The status report gives the status of the transfer instruction, for example, Accepted (PACK).

[fig-0125 - original figure evidence](../diagrams/fig-0125.md)

**P880** The message flow works in a similar way when a TransferInInstruction message is sent.

