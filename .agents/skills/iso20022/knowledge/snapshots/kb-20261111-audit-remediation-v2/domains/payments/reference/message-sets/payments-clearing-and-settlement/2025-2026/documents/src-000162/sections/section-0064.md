---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]
content_origin: "source-transcription"
---

# Positive FI To FI Payment Status Report with Direct Debit

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Direct Debit / Positive FI To FI Payment Status Report with Direct Debit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P520** Positive FI To FI Payment Status Report with Direct Debit

**P521** The positive FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the receiver that the instruction received (either single or grouped) is processable.

**P522** A positive FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message or an FIToFIPaymentReversal message.

**P523** The positive FIToFIPaymentStatusReport message is also meant to be generic to ensure re-usability with other Payments Instruments.

**P524** The FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per optional bilateral agreements and may be complemented by an BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

[fig-0040 - original figure evidence](../diagrams/fig-0040.md)

**P526** The positive CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are optional.

**P527** As added value service to creditors, some banks may update CustomerPaymentStatusReport messages to inform creditors about the status of transactions during their lifecycle.

**P528** Mixed CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages may be exchanged, that is, ‘partially accepted’ on group level, indicated that the group contains a mix of accepted, pending and/or rejected transactions.

