---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer", "Debtor and Creditor Agent are Correspondents "]
content_origin: "source-transcription"
---

# Debtor and Creditor Agent are Correspondents 

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer / Debtor and Creditor Agent are Correspondents .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P360** Debtor and Creditor Agent are Correspondents 

**P361** Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

[fig-0028 - original figure evidence](../diagrams/fig-0028.md)

**P363** The scenario covers the case where the creditor agent services an account for the debtor.

**P364** In cases where the debtor services an account for the creditor agent, or debtor and creditor agent are linked through a clearing and settlement system, the creditor agent will inform about the non-processability of the instruction by using a PaymentReturn message.

**P365** The debtor sends the FinancialInstitutionCreditTransfer message to the creditor agent.

**P366** The creditor agent sends a negative FIToFIPaymentStatusReport message to inform the debtor about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

