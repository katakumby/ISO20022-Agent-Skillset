---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FIToFICustomerCreditTransfer ", "Debtor Agent and Creditor Agent are not Correspondents - 1"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are not Correspondents - 1

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FIToFICustomerCreditTransfer  / Debtor Agent and Creditor Agent are not Correspondents - 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P260** Debtor Agent and Creditor Agent are not Correspondents - 1

**P261** There is an intermediary agent between the debtor agent and creditor agent (so-called 3-party serial payment). A return is exchanged after settlement has taken place.

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P263** The scenario covers the case where the intermediary agent services an account for the creditor agent or the case where the intermediary agent and the creditor agent are linked through a payment clearing system.

**P264** If the creditor agent services an account for the intermediary agent, the creditor agent will inform about the non-processability with a negative FIToFIPaymentStatusReport (status Reject) message.

**P265** Depending on whether settlement has taken place or not, the intermediary agent might report to the debtor agent with a negative FIToFIPaymentStatusReport or a PaymentReturn message.

**P266** The debtor agent sends the FIToFICustomerCreditTransfer message to the intermediary agent.

**P267** The intermediary agent optionally confirms the processability of the FIToFICustomerCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P268** The intermediary agent forwards the FIToFICustomerCreditTransfer message to the creditor agent. 

**P269** The creditor agent sends a PaymentReturn message to inform the intermediary agent about the non- processability of the FIToFICustomerCreditTransfer (for example due to missing/incorrect information) including the return reason.

**P270** The intermediary agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P271** The intermediary agent might try to repair and re-submit the instruction when possible and inform the debtor agent with an updated FIToFIPaymentStatusReport message accordingly.

**P272** The intermediary agent forwards the PaymentReturn message including the return reason to the debtor agent to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction.

**P273** The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the intermediary agent.

**P274** The debtor agent might try to repair and re-submit the instruction when possible and inform the debtor with an updated FIToFIPaymentStatusReport message accordingly.

**P275** Out of Scope

**P276** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

