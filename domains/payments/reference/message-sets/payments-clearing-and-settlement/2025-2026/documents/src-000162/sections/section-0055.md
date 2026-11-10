---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor Agent and Creditor are Correspondents"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor are Correspondents

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FinancialInstitutionCreditTransfer  / Debtor Agent and Creditor are Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P420** Debtor Agent and Creditor are Correspondents

**P421** The debtor agent and the creditor are correspondents. A return is exchanged after settlement has taken place.

[fig-0033 - original figure evidence](../diagrams/fig-0033.md)

**P423** The scenario covers the case where the debtor agent services an account for the creditor and where the debtor agent and the creditor are linked through a payment clearing system.

**P424** If the creditor services an account for the debtor agent, the creditor will inform about the non- processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message.

**P425** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P426** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P427** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor.

**P428** If the debtor agent services an account for the creditor, that is, is also the creditor agent, the debtor agent will send a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement ('statement') message instead of forwarding the FinancialInstitutionCreditTransfer message. In scope: The creditor sends a PaymentReturn message including the return reason to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

**P429** Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor of the repair with an updated FIToFIPaymentStatusReport message.

**P430** The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor.

**P431** Out of Scope

**P432** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

