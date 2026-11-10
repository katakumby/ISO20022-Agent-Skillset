---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Debtor Agent sends FIToFIPaymentStatusRequest "]
content_origin: "source-transcription"
---

# Debtor Agent sends FIToFIPaymentStatusRequest 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / Debtor Agent sends FIToFIPaymentStatusRequest .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P292** Debtor Agent sends FIToFIPaymentStatusRequest 

**P293** In the previous scenarios, the (optional) possibility of confirming the processability of the FIToFICustomerCreditTransfer via a FIToFIPaymentStatusReport was always mentioned/included. In some schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In the case the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. This message requests to receive a FITFIPaymentStatusReport message. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

**P295** Sending an FIToFIPaymentStatusRequest is possible in all FIToFICustomerCreditTransfer scenarios described before (section 6.1.1, 6.1.2 and 6.1.3), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

