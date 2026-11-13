---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"]
content_origin: "source-transcription"
---

# Positive Customer and FIToFIPaymentStatusReport with Direct Debit

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / Positive Customer and FIToFIPaymentStatusReport with Direct Debit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P261** Positive Customer and FIToFIPaymentStatusReport with Direct Debit

**P262** The positive CustomerPaymentStatusReport message (single or grouped) and FIToFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the receiver that the instruction received is processable.

**P263** A positive CustomerPaymentStatusReport message or FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message (in case of FIToFI) or a PaymentReversal message.

**P264** The positive CustomerPaymentStatusReport message and FIToFIPaymentStatusReport message are also meant to be generic to ensure re-usability with other Payments Instruments.

**P265** The CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per bilateral agreements and may be complemented by a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

