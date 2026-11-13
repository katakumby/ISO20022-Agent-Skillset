---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent"]
content_origin: "source-transcription"
---

# CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Direct Debit / FIToFIPaymentStatusReport with Direct Debit / CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P499** CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent

**P500** A negative FIToFIPaymentStatusReport message is  initiated by the clearing and settlement agent to reject an FIToFICustomerDirectDebit message.

**P501** Whenever possible the creditor agent will correct/complement the instruction and re-submit. Consequently he would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

[fig-0038 - original figure evidence](../diagrams/fig-0038.md)

**P503** * Information: If the creditor agent books after collection, for example, the cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return

**P504** The creditor sends the CustomerDirectDebitInitiation message to its agent (the creditor agent).

**P505** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P506** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P507** If information is missing and inter-bank settlement has not taken place yet, the clearing and settlement agent informs the creditor agent about the non processability of the FIToFICustomerDirectDebit instruction. The creditor agent may inform his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a negative CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

**P508** Before sending a negative CustomerPaymentStatusReport message to its customer, it is assumed that the creditor agent will try to correct the CustomerDirectDebitInitiation message information and re-submit an FIToFICustomerDirectDebit message to the clearing and settlement agent. In this case the creditor will not be involved.

