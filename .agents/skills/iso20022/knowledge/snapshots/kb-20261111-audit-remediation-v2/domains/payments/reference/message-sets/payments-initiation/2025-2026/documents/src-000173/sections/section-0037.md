---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]
content_origin: "source-transcription"
---

# Negative FIToFIPaymentStatusReport - Debtor Agent

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / Negative Customer and FIToFIPaymentStatusReport with Direct Debit / Negative FIToFIPaymentStatusReport - Debtor Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P249** Negative FIToFIPaymentStatusReport - Debtor Agent

**P250** A negative FIToFIPaymentStatusReport message is initiated by the debtor agent to reject the FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

[fig-0022 - original figure evidence](../diagrams/fig-0022.md)

**P252** Whenever possible, the creditor agent will correct or complement the instruction and re-submit. If this is the case, the creditor agent would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

**P253** With respect to ‘Information’ above: if the creditor agent books after collection, for example, cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return. 

**P254** The creditor sends a CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P255** The creditor agent confirms the processability of the CustomerDirectDebitInitiation message by sending a positive

