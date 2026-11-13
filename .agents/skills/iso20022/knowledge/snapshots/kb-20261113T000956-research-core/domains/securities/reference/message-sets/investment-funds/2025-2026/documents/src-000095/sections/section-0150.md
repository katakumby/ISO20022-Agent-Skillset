---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Message Rejection"]
content_origin: "source-transcription"
---

# Message Rejection

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Message Rejection.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P752** Message Rejection

**P753** The SecuritiesMessageRejection message can be used to reject any securities message. One example of the use of the SecuritiesMessageRejection is illustrated below.

**P754** An instructing party sends a TransferOutInstruction message to the executing party. 

**P755** Subsequently, the instructing party sends a RequestForTransferStatusReport message to the executing party but, for example, it misquotes the message reference of the TransferOutInstruction message. 

**P756** The executing party cannot process the RequestForTransferStatusReport message because it does not know to which transfer instruction the instructing party is referring. Therefore, the executing party replies with a SecuritiesMessageRejection message with the reason 'UnknownOrInvalidReference'. 

**P757** The message flow works in a similar way when a TransferInInstruction is sent and a transfer instruction status report is subsequently requested with, for example, a misquoted reference.

[fig-0106 - original figure evidence](../diagrams/fig-0106.md)

