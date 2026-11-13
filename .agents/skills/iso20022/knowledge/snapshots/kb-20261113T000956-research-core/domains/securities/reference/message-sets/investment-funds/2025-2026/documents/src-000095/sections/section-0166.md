---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Intermediary - Double Leg"]
content_origin: "source-transcription"
---

# Two Account Owners – Intermediary - Double Leg

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Individual Asset Transfer / Two Account Owners – Intermediary - Double Leg.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P837** Two Account Owners – Intermediary - Double Leg

**P838** Instructing party 1 sends a TransferOutInstruction message to intermediary 1. 

**P839** The message requests intermediary 1 to withdraw a quantity of financial instrument from the account of instructing party 1 and deliver the financial instrument to instructing party 2, which has its account at intermediary 2. Intermediary 1, in turn, has an account at the executing party and sends a TransferOutInstruction message to the executing party. 

**P840** At the same time, instructing party 2 sends a TransferInInstruction message to intermediary 2. The message requests intermediary 2 to receive the financial instrument from instructing party 1, via intermediary 1, via the executing party. Intermediary 2, in turn, sends a TransferInInstruction message to the executing party. 

**P841** The executing party sends a TransferOutConfirmation message to intermediary 1 to confirm the delivery. Intermediary 1, in turn, sends a TransferOutConfirmation message to instructing party 1 to confirm the delivery. The executing party sends a TransferInConfirmation message to intermediary 2 to confirm the receipt. Intermediary 2, in turn, sends a TransferInConfirmation message to instructing party 2 to confirm the receipt.

[fig-0118 - original figure evidence](../diagrams/fig-0118.md)

