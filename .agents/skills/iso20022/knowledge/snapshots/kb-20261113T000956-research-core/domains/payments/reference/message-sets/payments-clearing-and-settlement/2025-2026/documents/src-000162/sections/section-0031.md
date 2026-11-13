---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 2"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are not Correspondents - 2

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are not Correspondents - 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P198** Debtor Agent and Creditor Agent are not Correspondents - 2

**P199** The debtor agent and the creditor agent are not correspondents in the currency of the transaction. There is a reimbursement agent between them (so-called 3-party cover payment).

[fig-0014 - original figure evidence](../diagrams/fig-0014.md)

**P201** For the sake of simplicity, it is assumed that the debtor agent and the creditor agent have the same reimbursement agent. The FIToFICustomerCreditTransfer instruction will be covered through a separate FinancialInstitutionCreditTransfer message sent to the reimbursement agent (illustrated under the FinancialInstitutionCreditTransfer section).

**P202** The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

**P203** The creditor agent optionally confirms the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P204** The debtor agent sends a FinancialInstitutionCreditTransfer message to the reimbursement agent.

**P205** The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P206** Out of Scope

**P207** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

