---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]
content_origin: "source-transcription"
---

# Negative CustomerPaymentStatusReport - Clearing And Settlement Agent

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / Negative Customer and FIToFIPaymentStatusReport with Direct Debit / Negative CustomerPaymentStatusReport - Clearing And Settlement Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P239** Negative CustomerPaymentStatusReport - Clearing And Settlement Agent

**P240** A negative FIToFIPaymentStatusReport message is initiated by the clearing and settlement agent to reject an FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

**P242** Whenever possible, the creditor agent will correct or complement the instruction and re-submit. If this is the case, the creditor agent would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

**P243** With respect to ‘Information’ above: If the creditor agent books after collection (that is cycle is 3 days) then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

**P244** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P245** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P246** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P247** If information is missing and interbank settlement has not taken place yet, the clearing and settlement agent informs the creditor agent about the non processability of the FIToFICustomerDirectDebit instruction. The creditor agent may inform (but not necessarily) his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a negative CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message.

**P248** Before sending a negative CustomerPaymentStatusReport message to its customer, it is assumed that the creditor agent will try to correct the CustomerDirectDebitInitiation message information and re-submit an FIToFICustomerDirectDebit message to the clearing and settlement agent. In this case the creditor will not be involved.

