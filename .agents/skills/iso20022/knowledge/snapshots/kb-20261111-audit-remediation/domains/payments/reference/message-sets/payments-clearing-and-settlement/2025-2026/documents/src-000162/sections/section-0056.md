---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor Agent and Creditor Agent are Correspondents"]
content_origin: "source-transcription"
---

# Debtor Agent and Creditor Agent are Correspondents

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FinancialInstitutionCreditTransfer  / Debtor Agent and Creditor Agent are Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P433** Debtor Agent and Creditor Agent are Correspondents

**P434** A return is exchanged after settlement has taken place.

[fig-0034 - original figure evidence](../diagrams/fig-0034.md)

**P436** The scenario covers the case where the debtor agent services an account for the creditor agent and where the debtor agent and the creditor agent are linked through a payment clearing system.

**P437** If the creditor agent services an account for the debtor agent, the creditor agent will inform about the non-processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message.

**P438** The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

**P439** The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P440** The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

**P441** The creditor agent sends a PaymentReturn message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

**P442** Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor about the repair with an updated FIToFIPaymentStatusReport message.

**P443** Out of Scope

**P444** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

