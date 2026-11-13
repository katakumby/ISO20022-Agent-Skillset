---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]
content_origin: "source-transcription"
---

# PaymentReturn Initiated by Debtor Agent

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / PaymentReturn with Direct Debit / PaymentReturn Initiated by Debtor Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P280** PaymentReturn Initiated by Debtor Agent

**P281** A PaymentReturn message is initiated by the debtor agent (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

[fig-0024 - original figure evidence](../diagrams/fig-0024.md)

**P283** With respect to the RefundRequest, the payment return process can be triggered by a RefundRequest by the debtor or initiated by the debtor agent.

**P284** If the booking of the original instruction on the creditor's account has already taken place, the return of the funds will be notified to the creditor through return information included in a BankToCustomerNotification message and/or a BankToCustomerAccountReport or a BankToCustomerStatement message.

**P285** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P286** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport to the creditor.

**P287** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P288** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P289** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

**P290** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent.

**P291** If the debtor agent is unable to make the collection from the debtor Account for one or several reasons (for example, insufficient funds, customer deceased), the debtor agent will initiate a PaymentReturn message, and route it through the clearing and settlement agent to the creditor agent, giving the reason for the Return.

**P292** The clearing and settlement agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P293** The clearing and settlement agent forwards the PaymentReturn message to the creditor agent.

**P294** If the clearing and settlement agent are two parties the Clearing Agent prepares the (returned) payment information for the Settlement Agent (the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date) in accordance with the agreed and published settlement cycle. The Settlement Agent performs the transfer of cash from the credit party to the debit party (in accordance with the agreed published settlement cycle). (Out of scope and not illustrated).

**P295** The creditor agent will optionally confirm receipt of the PaymentReturn message to the clearing and settlement agent. Depending on agreements between the creditor and the creditor agent, the creditor may be informed either through a negative CustomerPaymentStatusReport message, or through a CustomerToBankDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message ('statement') about the funds return and thus the debit on his account.

