---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Payment Return in a FinancialInstitutionDirectDebit scenario"]
content_origin: "source-transcription"
---

# Payment Return in a FinancialInstitutionDirectDebit scenario

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Payment Return in a FinancialInstitutionDirectDebit scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P623** Payment Return in a FinancialInstitutionDirectDebit scenario

**P624**  The scenario covers the case where the creditor has the authority to request direct debits to the debtor agent in the currency of the transaction(s), but creditor (nor creditor agent) and debtor agent are not correspondents in the currency of the transaction(s). For sake of simplicity only one intermediary agent has been illustrated. 

[fig-0047 - original figure evidence](../diagrams/fig-0047.md)

**P627** The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent to request the move of funds to his account with the creditor agent, through an intermediary agent.

**P628** The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

**P630** The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

**P631** The creditor agent cannot process the FinancialInstitutionCreditTransfer and sends a negative FIToFIPaymentStatusReport message to the intermediary agent.

**P632** If the settlement had already taken place, the intermediary agent sends a PaymentReturn message to the debtor agent.

**P633** The debtor agent optionally confirms the processability of the PaymentReturn message by sending a postitive FIToFIPaymentStatusReport message to the intermediary agent.

**P634** The debtor agent optionally informs the creditor with a negative FIToFIPaymentStatusReport message.

**P635** Whenever possible, the intermediary agent or debtor agent might try to repair and re-submit the instruction and may inform the creditor agent with an updated FIToFIPaymentStatusReport.

**P636** Out of Scope

**P637** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P638** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included. 

**P639** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

