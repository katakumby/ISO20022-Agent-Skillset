---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]
content_origin: "source-transcription"
---

# Creditor and Debtor Agent are correspondents

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Creditor and Debtor Agent are correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P585** Creditor and Debtor Agent are correspondents

**P586** The scenario covers the case where the debtor agent services an account for the creditor and for the debtor(s).  For sake of simplicity, only 1 Debtor is represented in the sequence diagram.

[fig-0044 - original figure evidence](../diagrams/fig-0044.md)

**P588** The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent. Creditor and debtor agent are correspondents in the currency of the transaction and by sending the message the creditor requests to credit the amount on his account with the debtor agent

**P589** The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

**P590** Out of Scope

**P591** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P592** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included. 

**P593** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

**P594** If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement.

