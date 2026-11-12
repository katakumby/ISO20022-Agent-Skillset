---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer", "Debtor Agent and Creditor are Correspondents "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor are Correspondents 

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer / Debtor Agent and Creditor are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P367** Debtor Agent and Creditor are Correspondents 

**P368** Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0029 - original figure evidence](../diagrams/fig-0029.md)

**P370** The scenario covers the case where the creditor services an account for the debtor agent.

**P371** In cases where the debtor agent services an account for the creditor, or debtor agent and creditor are linked through a clearing and settlement system, the creditor will inform about the non-processability of the instruction by using a PaymentReturn message.

**P372** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P373** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P374** The debtor agent forwards the FinancialInstitutionCreditTransfer instruction to the creditor.

**P375** The creditor sends a negative FIToFIPaymentStatusReport message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

**P376** The debtor agent might try to correct and re-submit the instruction and inform the debtor about this correction with an updated FIToFIPaymentStatusReport message. If the status is now positive, no further action is required but the debtor might be informed on the positive outcome through a positive FIToFIPaymentStatusReport message.

**P377** Out of Scope 

**P378** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

