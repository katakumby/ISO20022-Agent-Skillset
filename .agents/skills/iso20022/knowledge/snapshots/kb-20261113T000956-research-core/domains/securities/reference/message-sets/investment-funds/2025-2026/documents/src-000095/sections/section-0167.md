---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Transfer Out Reversal "]
content_origin: "source-transcription"
---

# Transfer Out Reversal 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Transfer Out Reversal .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P843** Transfer Out Reversal 

**P844** An instructing party sends a TransferOutInstruction message to the executing party. The message requests the executing party to withdraw a quantity of financial instrument from an account the instructing party owns and deliver it to another account. 

**P845** The executing party sends a TransferOutConfirmation message to the instructing party to confirm the delivery.

**P846** Subsequently, the executing party sends a ReversalOfTransferOutConfirmation message to reverse the TransferOutConfirmation message. 

[fig-0119 - original figure evidence](../diagrams/fig-0119.md)

