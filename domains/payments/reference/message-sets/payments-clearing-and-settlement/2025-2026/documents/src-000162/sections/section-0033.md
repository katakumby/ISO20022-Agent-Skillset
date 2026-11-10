---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are Direct Correspondents"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Direct Correspondents

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are Direct Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P214** Debtor Agent and Creditor Agent are Direct Correspondents

**P215** Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

**P217** This scenario covers the case where the creditor agent (or a branch/head office of the creditor agent) services an account for the debtor agent. In the cases where the debtor agent services an account for the creditor agent and in the case of clearing system payments, the creditor agent will inform about the non-processability by using a PaymentReturn message.

**P218** The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

**P219** The creditor agent sends a negative FIToFIPaymentStatusReport message to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction (for example, due to missing or incorrect information).

**P220** Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed with the debtor, the debtor agent may inform the debtor of the repair with an updated FIToFIPaymentStatusReport message.

