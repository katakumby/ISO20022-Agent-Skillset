---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor Agent and Creditor Agent are Not Correspondents "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Not Correspondents 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FinancialInstitutionCreditTransfer  / Debtor Agent and Creditor Agent are Not Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P445** Debtor Agent and Creditor Agent are Not Correspondents 

**P446** A return is exchanged after settlement has taken place.

[fig-0035 - original figure evidence](../diagrams/fig-0035.md)

**P448** For sake of simplicity, only one intermediary agent has been added.

**P449** The scenario covers the case where the intermediary agent services an account for the creditor agent or the case where the intermediary agent and the creditor agent are linked through a payment clearing system.

**P450** If the creditor agent services an account for the intermediary agent, the creditor agent will inform about the non-processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message. In scope: The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P451** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P452** The debtor agent forwards the FinancialInstitutionCreditTransfer to the intermediary agent.

**P453** The intermediary agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P454** The intermediary agent forwards the FinancialInstitutionCreditTransfer instruction to the creditor agent. 

**P455** The creditor agent sends a PaymentReturn message including the return reason to inform the intermediary agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/ incorrect information).

**P456** Whenever possible, the intermediary agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor agent of the repair with an updated FIToFIPaymentStatusReport message.

**P457** The intermediary agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P458** The intermediary agent forwards the PaymentReturn message including the return reason to the debtor agent to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

**P459** Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor about the repair with an updated FIToFIPaymentStatusReport message.

**P460** The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the intermediary agent.

**P461** Out of Scope 

**P462** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

