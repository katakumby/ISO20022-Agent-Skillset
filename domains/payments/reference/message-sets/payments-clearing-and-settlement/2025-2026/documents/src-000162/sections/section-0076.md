---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "FIToFIPaymentReversal with Direct Debit"]
content_origin: "source-transcription"
---

# FIToFIPaymentReversal with Direct Debit

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / FIToFIPaymentReversal with Direct Debit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P640** FIToFIPaymentReversal with Direct Debit

**P641** After the scenario described in 6.2.6.1, the creditor may realises (for example) that the FinancialInstitutionDirectDebit instruction was a duplicate. 

[fig-0048 - original figure evidence](../diagrams/fig-0048.md)

**P643** The creditor can initiate an FIToFIPaymentReversal message, after settlement, when a paid direct debit should not have been processed. 

**P644** The debtor agent can confirm the processability of the FIToFIPaymentReversal  by sending a positive FITFIPaymentsStatusReport to the creditor.

