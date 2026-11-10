---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]
content_origin: "source-transcription"
---

# Negative Customer and FIToFIPaymentStatusReport with Direct Debit

Source: [src-000173](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Negative Customer and FIToFIPaymentStatusReport with Direct Debit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P231** Negative Customer and FIToFIPaymentStatusReport with Direct Debit

**P232** The negative CustomerPaymentStatusReport message (single or grouped) or FItoFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

**P233** The negative CustomerPaymentStatusReport message FIToFIPaymentStatusReport message used to reject a direct debit instruction, is to be sent before settlement. After settlement, the correct message to be used is the PaymentReturn message.

