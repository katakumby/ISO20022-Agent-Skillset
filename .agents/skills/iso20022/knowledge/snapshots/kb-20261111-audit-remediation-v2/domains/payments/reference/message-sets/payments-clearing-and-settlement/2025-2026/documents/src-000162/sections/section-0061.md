---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit"]
content_origin: "source-transcription"
---

# FIToFIPaymentStatusReport with Direct Debit

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Direct Debit / FIToFIPaymentStatusReport with Direct Debit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P496** FIToFIPaymentStatusReport with Direct Debit

**P497** The negative FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

**P498** The negative FIToFIPaymentStatusReport message is to be sent before settlement. Indeed, after settlement, the correct message to be used is the PaymentReturn message.

