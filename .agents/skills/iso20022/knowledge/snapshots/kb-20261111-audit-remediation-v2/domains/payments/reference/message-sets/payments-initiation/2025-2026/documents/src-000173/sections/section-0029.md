---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]
content_origin: "source-transcription"
---

# CustomerCreditTransferInitiation - Relay

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / CustomerCreditTransferInitiation - Relay.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P179** CustomerCreditTransferInitiation - Relay

**P180** The CustomerCreditTransferInitiation message is sent from the initiating party to the forwarding agent.

**P181** Depending on the service level agreed between the forwarding agent and the initiating party, the forwarding agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

**P182** After performing a series of checks, the forwarding agent will forward the CustomerCreditTransferInitiation message to the relevant debtor agent, that is, the agent that will debit the debtor account.

**P183** A relay scenario always requires service level agreements between all parties involved, in which obligations and responsibilities for each party are stipulated.

**P184** A number of additional message flows have been included to illustrate the complete end-to-end execution of the payment initiation. However, these messages are out of scope.

**P185** The below scenarios show the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

**P186** On the initiating side, up to three customer roles can be specified: the initiating party, that is., the party sending the message, the debtor, that is, the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor, as a result of receipt of goods or services.

**P187** These three roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

**P188** On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

