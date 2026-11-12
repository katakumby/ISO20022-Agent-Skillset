---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor Agent and Creditor are Correspondents"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor are Correspondents

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / FinancialInstitutionCreditTransfer  / Debtor Agent and Creditor are Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P317** Debtor Agent and Creditor are Correspondents

[fig-0024 - original figure evidence](../diagrams/fig-0024.md)

**P319** The scenario covers the case where the creditor services an account for the debtor agent.

**P320** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P321** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P322** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor.

**P323** The creditor optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P324** Out of Scope

**P325** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

**P326** If the debtor agent services an account for the creditor, that is, the creditor agent, then instead of sending a FinancialInstitutionCreditTransfer message, the debtor agent will send a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

