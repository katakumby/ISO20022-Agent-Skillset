---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor and Creditor are direct Correspondents"]
content_origin: "source-transcription"
---

# Debtor and Creditor are direct Correspondents

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / PaymentReturn with FinancialInstitutionCreditTransfer  / Debtor and Creditor are direct Correspondents.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P409** Debtor and Creditor are direct Correspondents

**P410**  A return is exchanged after settlement has taken place.

[fig-0032 - original figure evidence](../diagrams/fig-0032.md)

**P412** The scenario covers the case where the debtor services an account for the creditor, that is, the creditor agent, and the case where the debtor and the creditor are linked through a payment clearing system.

**P413** For cases where the creditor services an account for the debtor, the creditor will inform about the non-processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message.

**P414** The debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

**P415** The creditor sends a PaymentReturn message including the return reason to inform the debtor about the non- processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information). In scope: The debtor optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor.

**P416** Out of Scope 

**P417** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

**P418** The case where the debtor and the creditor agent are correspondents is very similar. Therefore, it is not illustrated. The scenario would cover the case where the debtor services an account for the creditor agent and the case where the debtor and the creditor agent are linked through a clearing and settlement system.

**P419** If the creditor agent services an account for the debtor, the creditor agent will inform about the non- processability of the instruction by using a negative FIToFIPaymentStatusReport message to reject the instruction.

