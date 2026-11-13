---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FIToFICustomerCreditTransfer ", "Debtor Agent and Creditor Agent are not Correspondents - 2 "]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are not Correspondents - 2 

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FIToFICustomerCreditTransfer  / Debtor Agent and Creditor Agent are not Correspondents - 2 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P277** Debtor Agent and Creditor Agent are not Correspondents - 2 

**P278** The debtor agent and creditor agent are not correspondents in the currency of the transaction. There is an instructed reimbursement agent between them (so-called 3-party cover payment). A return is exchanged after settlement has taken place.

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

**P280** For sake of simplicity, it is assumed that the debtor agent and the creditor agent have the same reimbursement agent.

**P281** The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

**P282** The debtor agent sends a FinancialInstitutionCreditTransfer message to the reimbursement agent.

**P283** The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P284** The creditor agent cannot apply the payment instruction (for example creditor account closed) and sends a PaymentReturn message to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction including the return reason.

**P285** This PaymentReturn message exceptionally will not move funds, but will inform about the movement of funds (as was the case with the original FIToFICustomerCreditTransfer). The funds will be moved with the FinancialInstitutionCreditTransfer sent by the creditor agent as described below.

**P286** The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P287** The creditor agent sends a FinancialInstitutionCreditTransfer message to the reimbursement agent.

**P288** The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P289** If the creditor agent is not aware that inter-bank settlement has taken place, it might send a negative FIToFIPaymentStatusReport message to the debtor agent. It is assumed though, that once it finds out that settlement did take place (through BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement') from the reimbursement agent) the creditor agent will return the funds by sending a FinancialInstitutionCreditTransfer to the reimbursement agent.

**P290** Out of Scope

**P291** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

