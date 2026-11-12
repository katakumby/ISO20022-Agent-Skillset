---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P208** Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer

**P209** The negative FIToFIPaymentStatusReport message is used, point to point between two parties, to report about the negative processability of an instruction, that is, to report about the rejection of the instruction, and is used to:

**P210** Reject an FIToFICustomerCreditTransfer

**P211** Reject a FinancialInstitutionCreditTransfer

**P212** The negative FIToFIPaymentStatusReport message is sent before settlement.

**P213** After settlement, the correct message to be used is the PaymentReturn message, the BankToCustomerDebitCreditNotification message ('notification') and/or the BankToCustomerAccountReport/ BankToCustomerStatement message ('statement'). Different options are illustrated in the sequence diagram.

