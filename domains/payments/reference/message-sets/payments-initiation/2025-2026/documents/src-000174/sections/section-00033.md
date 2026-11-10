---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.7 ChequeInstruction <ChqInstr>", "2.4.2.19.7.4 DeliveryMethod <DlvryMtd>", "2.4.2.19.7.4.1 Code <Cd>"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.7.4.1 Code <Cd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
2.4.2.19.7.4.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the delivery method of the cheque by the debtor's agent.
Datatype: "ChequeDelivery1Code" on page 588
CodeName Name Definition
MLDB MailToDebtor Cheque is to be sent through mail
services to debtor.
MLCD MailToCreditor Cheque is to be sent through mail
services to creditor.
MLFA MailToFinalAgent Cheque is to be sent through mail
services to creditor agent.
CRDB CourierToDebtor Cheque is to be sent through courier
services to debtor.
CRCD CourierToCreditor Cheque is to be sent through courier
services to creditor.
CRFA CourierToFinalAgent Cheque is to be sent through courier
services to creditor agent.
PUDB PickUpByDebtor Cheque will be picked up by the debtor.
PUCD PickUpByCreditor Cheque will be picked up by the creditor.
PUFA PickUpByFinalAgent Cheque will be picked up by the creditor
agent.
RGDB RegisteredMailToDebtor Cheque is to be sent through registered
mail services to debtor.
RGCD RegisteredMailToCreditor Cheque is to be sent through registered
mail services to creditor.
RGFA RegisteredMailToFinalAgent Cheque is to be sent through registered
mail services to creditor agent.
2.4.2.19.7.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a proprietary delivery method of the cheque by the debtor's agent.
Datatype: "Max35Text" on page 609
2.4.2.19.7.5  DeliverTo <DlvrTo>
Presence: [0..1]
Definition: Party to whom the debtor's agent needs to send the cheque.
DeliverTo <DlvrTo> contains the following NameAndAddress18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 60
   Address <Adr> [1..1] ± 60
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 59 March 2026
```

