---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"]
content_origin: "source-transcription"
---

# Creditor Agent and Debtor Agent are not correspondents

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Creditor Agent and Debtor Agent are not correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P607** Creditor Agent and Debtor Agent are not correspondents

**P608** The scenario covers the case where the creditor has the authority to request direct debits to the debtor agent in the currency of the transaction(s), but requests to move the funds to an account the creditor owns at another bank (the creditor agent). The debtor agent and the creditor agent are not correspondents in the currency of the transaction(s), but have a common correspondent (the intermediary agent). 

**P609** Althought the FinancialInstitutionDirectDebit allows for multiple intermediary agents, for sake of simplicity only one intermediary agent has been illustrated. 

[fig-0046 - original figure evidence](../diagrams/fig-0046.md)

**P611** The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent to request the move of funds to his account with the creditor agent, through an intermediary agent.

**P612** The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

**P613** The debtor agent sends the FinancialInstitutionCreditTransfer to the intermediary agent to move the funds to the creditor.

**P614** The intermediary agent optionally confirms the processability of the FinancialInstitutionTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P615** The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

**P616** The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message.

**P617** Out of Scope

**P618** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P619** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included. 

**P620** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

**P621** If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement and no FinancialInstitutionCreditTransfer will be sent to the intermediary agent.

