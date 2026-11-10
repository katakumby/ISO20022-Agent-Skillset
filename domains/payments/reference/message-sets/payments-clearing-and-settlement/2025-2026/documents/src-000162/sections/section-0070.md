---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "Creditor Agent sends FIToFIPaymentStatusRequest"]
content_origin: "source-transcription"
---

# Creditor Agent sends FIToFIPaymentStatusRequest

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / Creditor Agent sends FIToFIPaymentStatusRequest.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P575** Creditor Agent sends FIToFIPaymentStatusRequest

**P576** In the previous scenarios, the (optional) possibility of confirming the processability of the FIToFICustomerDirectDebit via a FIToFIPaymentStatusReport was always mentioned/included. In some payment schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

[fig-0043 - original figure evidence](../diagrams/fig-0043.md)

**P578** Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.2.2, 6.2.3, 6.2.4, 6.2.5), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

