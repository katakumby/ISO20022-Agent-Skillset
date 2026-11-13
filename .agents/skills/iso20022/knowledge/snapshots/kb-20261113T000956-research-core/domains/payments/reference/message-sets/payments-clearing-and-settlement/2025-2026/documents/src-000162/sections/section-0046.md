---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor Agent and Creditor Agent are Not Correspondents"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Not Correspondents

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / FinancialInstitutionCreditTransfer  / Debtor Agent and Creditor Agent are Not Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P335** Debtor Agent and Creditor Agent are Not Correspondents

**P336** There is an intermediary agent between the debtor agent and creditor agent.

[fig-0026 - original figure evidence](../diagrams/fig-0026.md)

**P338** For sake of simplicity only one intermediary agent has been illustrated. The scenario also caters for clearing payments with direct communication with the Clearing and settlement agent.

**P339** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P340** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P341** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the intermediary agent. 

**P342** The intermediary agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P343** The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent. 

**P344** The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the intermediary agent. 

**P345** Out of Scope 

**P346** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

