---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]
content_origin: "source-transcription"
---

# Negative FIToFIPaymentStatusReport Initiated by Debtor Agent

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / FIToFIPaymentStatusReport with Direct Debit / Negative FIToFIPaymentStatusReport Initiated by Debtor Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P509** Negative FIToFIPaymentStatusReport Initiated by Debtor Agent

**P510** A negative FIToFIPaymentStatusReport message is initiated by the debtor agent to reject the FIToFICustomerDirectDebit message. (After settlement the correct message to be used by the debtor agent is the PaymentReturn message.

**P511** Whenever possible the creditor agent will correct/complement the instruction and re-submit. Consequently he would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

[fig-0039 - original figure evidence](../diagrams/fig-0039.md)

**P513** * Information: If the creditor agent books after collection, for example, the cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return. 

**P514** The creditor sends a CustomerDirectDebitInitiation message to its agent (the creditor agent).

**P515** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a CustomerPaymentStatusReport message to the creditor.

**P516** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P517** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending an FIToFIPaymentStatusReport message to the creditor agent.

**P518** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with  the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

**P519** If settlement has not yet taken place, the debtor agent may send a negative FIToFIPaymentStatusReport message to the clearing and settlement agent, to inform it about the rejection of the FIToFICustomerDirectDebit instruction. This negative FIToFIPaymentStatusReport message may subsequently be forwarded to the creditor agent. The creditor agent may inform its customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

