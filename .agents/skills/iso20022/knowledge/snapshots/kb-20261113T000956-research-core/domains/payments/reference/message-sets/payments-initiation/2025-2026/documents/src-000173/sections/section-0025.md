---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "CustomerCreditTransferInitiation"]
content_origin: "source-transcription"
---

# CustomerCreditTransferInitiation

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / CustomerCreditTransferInitiation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P155** CustomerCreditTransferInitiation

**P156** The CustomerCreditTransferInitiation message is sent from the initiating party to the debtor agent. Depending on the service level agreed between the debtor agent and the initiating party, the debtor agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

**P157** A number of additional message flows have been included to illustrate the complete end-to-end execution of the CustomerCreditTransferInitiation. However, these messages are out of scope. These message flows are:

**P158** Account information from debtor agent to initiating party

**P159** Depending on the service level agreed, the debtor agent may provide the initiating party with a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement ('statement') once the payment has been executed and the debit entry has been posted to the debtor account. The logical, chronological sequence for sending these messages is defined by the bank implementing and offering these services.

**P160** Interbank clearing and settlement between debtor agent and creditor agent

**P161** Depending on the interbank clearing and settlement method chosen, a number of messages may be exchanged between the agent parties in the payment chain.

**P162** Account information from creditor agent to creditor

**P163** Depending on the service level agreed, the creditor agent may provide the creditor with a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement ('statement') once the payment has been posted to the creditor account. The logical, chronological sequence for sending these messages is defined by the bank implementing and offering these services.

**P164** The scenarios below illustrate the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

**P165** On the initiating side, up to three customer roles can be specified: the initiating party, that is, the party sending the message, the debtor, that is the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor as a result of receipt of goods or services.

**P166** These three roles can be played by one and the same actor, or they can be played by different actors.

**P167** The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

**P168** On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors.

**P169** The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

