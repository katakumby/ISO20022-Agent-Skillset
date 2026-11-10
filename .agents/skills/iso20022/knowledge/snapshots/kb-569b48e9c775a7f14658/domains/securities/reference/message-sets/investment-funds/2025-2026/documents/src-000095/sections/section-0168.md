---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Reversal "]
content_origin: "source-transcription"
---

# Transfer In Reversal 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Transfer In Reversal .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P848** Transfer In Reversal 

**P849** An instructing party sends a TransferInInstruction message to the executing party. The message requests the executing party to receive a quantity of financial instrument from another account.

**P850** The executing party sends a TransferInConfirmation message to the instructing party, to confirm a receipt into the account of the instructing party. 

**P851** Subsequently, the executing party sends a ReversalOfTransferInConfirmation message to reverse the TransferInConfirmation message.

[fig-0120 - original figure evidence](../diagrams/fig-0120.md)

