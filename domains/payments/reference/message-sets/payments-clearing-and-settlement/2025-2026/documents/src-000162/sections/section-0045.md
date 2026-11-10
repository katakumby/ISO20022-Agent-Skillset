---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor Agent and Creditor Agent are Correspondents"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Correspondents

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / FinancialInstitutionCreditTransfer  / Debtor Agent and Creditor Agent are Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P327** Debtor Agent and Creditor Agent are Correspondents

[fig-0025 - original figure evidence](../diagrams/fig-0025.md)

**P329** The scenario includes both cases where the debtor agent services an account for the creditor agent and vice versa. In scope: The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P330** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P331** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

**P332** The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P333** Out of Scope

**P334** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

