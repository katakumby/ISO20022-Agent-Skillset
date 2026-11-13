---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are correspondents"]
content_origin: "source-transcription"
---

# Creditor Agent and Debtor Agent are correspondents

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Creditor Agent and Debtor Agent are correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P595** Creditor Agent and Debtor Agent are correspondents

**P596** The scenario covers the case where the creditor has the authority to request Direct Debits to the debtor agent in the currency of the transaction, but requests to move the funds to an account the creditor owns at another bank (the creditor agent).

[fig-0045 - original figure evidence](../diagrams/fig-0045.md)

**P598** The creditor requests with a FinancialInstitutionDirectDebit message to move the amount(s) to the account with the creditor agent. This creditor agent and the debtor agent are correspondents in the currency of the transaction(s).

**P599** The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

**P600** The debtor agent sends the FinancialInstitutionCreditTransfer to the creditor agent to move the funds to the creditor.

**P601** The creditor agent (optionally) confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport.

**P602**  Out of Scope

**P603** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P604** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included. 

**P605** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

**P606** If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement and no FinancialInstitutionCreditTransfer will be sent to the creditor agent.

