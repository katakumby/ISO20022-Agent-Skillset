---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer", "Debtor and Creditor are Correspondents "]
content_origin: "source-transcription"
---

# Debtor and Creditor are Correspondents 

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer / Debtor and Creditor are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P353** Debtor and Creditor are Correspondents 

**P354** Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0027 - original figure evidence](../diagrams/fig-0027.md)

**P356** The scenario covers the case where the creditor services an account for the debtor, that is, the debtor agent.

**P357** For cases where the debtor services an account for the creditor, or the debtor and creditor are linked through a clearing and settlement system, the creditor will inform about the non-processability of the instruction, by using a PaymentReturn message.

**P358** The debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

**P359** The creditor sends a negative FIToFIPaymentStatusReport message to inform the debtor about the non- processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

