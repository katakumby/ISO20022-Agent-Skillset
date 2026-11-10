---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor Agent are Correspondents "]
content_origin: "source-transcription"
---

# Debtor and Creditor Agent are Correspondents 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Credit Transfer / FinancialInstitutionCreditTransfer  / Debtor and Creditor Agent are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P310** Debtor and Creditor Agent are Correspondents 

[fig-0023 - original figure evidence](../diagrams/fig-0023.md)

**P312** The scenario covers both cases where the debtor services an account for the creditor agent and where the creditor agent services an account for the debtor.

**P313** The debtor sends the FinancialInstitutionCreditTransfer message to the creditor agent.

**P314** The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P315** Out of Scope

**P316** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

