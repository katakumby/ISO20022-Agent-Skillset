---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]
content_origin: "source-transcription"
---

# Debtor and Creditor are Correspondents

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / FinancialInstitutionCreditTransfer  / Debtor and Creditor are Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P303** Debtor and Creditor are Correspondents

[fig-0022 - original figure evidence](../diagrams/fig-0022.md)

**P305** The scenario covers the case where the creditor services an account for the debtor, that is, the debtor agent. In scope: the debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

**P306** The creditor optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P307** Out of Scope

**P308** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P309** If the debtor services an account for the creditor, that is, the creditor agent, then instead of sending a FinancialInstitutionCreditTransfer message, the debtor will send a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

