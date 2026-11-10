---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"]
content_origin: "source-transcription"
---

# Two Account Owners – Direct – SLT Market Practice

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Two Account Owners – Direct – SLT Market Practice.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P828** Two Account Owners – Direct – SLT Market Practice

**P829** The transferee's bank sends a TransferInInstruction message to the transferor's bank. The message instructs the transferor's bank party to withdraw a quantity of financial instrument from the end client's account and deliver the financial instrument to the account of the transferee's bank at the transfer agent. 

**P830** The transferor replies with a TransferInstructionStatusReport message with the status Accepted (PACK).

**P831** The transferor's bank then actions the transfer by sending a Transfer Out Instruction message to the transfer agent.

**P832** The transfer agent replies with a TransferInstructionStatusReport message with the status Accepted (PACK).

**P833** The transfer agent carries out the transfer and sends:

**P834** a TransferOutConfirmation message to the transferor's bank 

**P835** a TransferInConfirmation message to the transferee's bank

[fig-0117 - original figure evidence](../diagrams/fig-0117.md)

