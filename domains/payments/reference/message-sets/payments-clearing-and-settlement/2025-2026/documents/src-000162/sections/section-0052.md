---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer", "Debtor Agent and Creditor Agent Not Correspondents "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent Not Correspondents 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer / Debtor Agent and Creditor Agent Not Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P391** Debtor Agent and Creditor Agent Not Correspondents 

**P392** Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0031 - original figure evidence](../diagrams/fig-0031.md)

**P394** For sake of simplicity only one intermediary agent has been added. The scenario covers the case where the creditor agent services an account for the intermediary agent.

**P395** In cases where the intermediary agent services an account for the creditor agent (including clearing payments where the intermediary agent is a central Clearing and/or settlement agent), the creditor agent will inform about the non- processability of the instruction by using a PaymentReturn message.

**P396** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P397** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P398** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the intermediary agent.

**P399** The intermediary agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P400** The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

**P401** The creditor agent sends a negative FIToFIPaymentStatusReport message to inform the intermediary agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

**P402** The intermediary agent might try to correct and re-submit the instruction and inform the debtor agent about this correction with an updated FIToFIPaymentStatusReport message. If status is now positive, no further action is required, but the debtor agent might be informed on the positive outcome through a positive FIToFIPaymentStatusReport message.

**P403** The intermediary agent sends a PaymentReturn message to the debtor agent.

**P404** The debtor agent might try to correct and re-submit the instruction and inform the debtor about this correction with an updated FIToFIPaymentStatusReport message. If Status is now positive, no further action is required, but the debtor might be informed on the positive outcome through a positive FIToFIPaymentStatusReport message.

**P405** Out of Scope

**P406** (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

