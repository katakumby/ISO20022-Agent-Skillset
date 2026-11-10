---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer", "Debtor Agent and Creditor Agent are Correspondents "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Correspondents 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer / Debtor Agent and Creditor Agent are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P379** Debtor Agent and Creditor Agent are Correspondents 

**P380** Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0030 - original figure evidence](../diagrams/fig-0030.md)

**P382** The scenario covers the case where the creditor agent services an account for the debtor agent.

**P383** In cases where the debtor agent services an account for the creditor agent, or debtor agent and creditor agent are linked through a clearing and settlement system, the creditor agent will inform on the non-processability of the instruction by using a PaymentReturn message.

**P384** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P385** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P386** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

**P387** The creditor agent sends a negative FIToFIPaymentStatusReport message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

**P388** The debtor agent might try to correct and re-submit the instruction and inform the debtor about this correction with an updated FIToFIPaymentStatusReport message. If status is now positive no further action is required, but the debtor might be informed on the positive outcome through a positive FIToFIPaymentStatusReport message.

**P389** Out of Scope 

**P390** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

