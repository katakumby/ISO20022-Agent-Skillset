---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor sends FIToFIPaymentStatusRequest"]
content_origin: "source-transcription"
---

# Creditor sends FIToFIPaymentStatusRequest

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Creditor sends FIToFIPaymentStatusRequest.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P645** Creditor sends FIToFIPaymentStatusRequest

**P646** In the previous scenarios, the (optional) possibility of confirming the processability of the FinancialInstitutionDirectDebit via a FIToFIPaymentStatusReport was always mentioned/included. In some payment schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

[fig-0049 - original figure evidence](../diagrams/fig-0049.md)

**P648** Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.2.7.2, 6.2.7.2, 6.2.7.3, 6.2.7.4), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

