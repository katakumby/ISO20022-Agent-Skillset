---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Own Account - Direct"]
content_origin: "source-transcription"
---

# Own Account - Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Own Account - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P811** Own Account - Direct

**P812** An instructing party sends a TransferOutInstruction message to the executing party. The message requests the executing party to withdraw a quantity of financial instrument from one account the instructing party owns and deliver it to another account it also owns at the executing party. 

**P813** As the transfer is an own account transfer, both parties have agreed that it is not necessary for the instructing party to send the executing party the corresponding TransferInInstruction message.

**P814** The executing party sends a TransferOutConfirmation message to the instructing party to confirm the delivery.

[fig-0114 - original figure evidence](../diagrams/fig-0114.md)

