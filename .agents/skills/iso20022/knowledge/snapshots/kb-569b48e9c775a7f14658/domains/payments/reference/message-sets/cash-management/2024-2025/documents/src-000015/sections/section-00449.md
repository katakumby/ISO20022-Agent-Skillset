---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks"]
file_pages: [607, 608]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 607 to 608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 607

```text
C6 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C7 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C8 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
23.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
23.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader9" on page 810 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 810
   CreationDateTime <CreDtTm> [0..1] DateTime 810
   RequestType <ReqTp> [0..1]  810
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 810
Or     Enquiry <Enqry> [1..1] CodeSet 811
Or}     Proprietary <Prtry> [1..1] ± 811
23.4.2 ReceiptDetails <RctDtls>
Presence: [1..*]
Definition: Details of the receipt.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 607 February 2025
```

## File page 608

```text
ReceiptDetails <RctDtls> contains the following Receipt7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1]  609
     MessageIdentification <MsgId> [1..1] Text 609
     MessageNameIdentification <MsgNmId> [0..1] Text 609
     OriginatorName <OrgtrNm> [0..1] Text 609
   OriginalPaymentIdentification <OrgnlPmtId> [0..1]  610
{Or     TransactionIdentification <TxId> [1..1] Text 611
Or     UETR <UETR> [1..1] IdentifierSet 611
Or     QueueIdentification <QId> [1..1]  611
       QueueIdentification <QId> [1..1] Text 611
       PositionInQueue <PosInQ> [1..1] Text 611
Or     LongBusinessIdentification <LngBizId> [1..1]  C7 611
       TransactionIdentification <TxId> [0..1] Text 612
       UETR <UETR> [0..1] IdentifierSet 612
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 613
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 613
       PaymentMethod <PmtMtd> [0..1]  613
{Or         FINMessageType <FINMT> [1..1] Text 613
Or         XMLMessageName <XMLMsgNm> [1..1] Text 613
Or         Proprietary <Prtry> [1..1] Text 613
Or}         Instrument <Instrm> [1..1] CodeSet 613
       InstructingAgent <InstgAgt> [1..1] ± 614
       InstructedAgent <InstdAgt> [1..1] ± 615
       EntryType <NtryTp> [0..1] IdentifierSet 616
       EndToEndIdentification <EndToEndId> [0..1] Text 616
Or     ShortBusinessIdentification <ShrtBizId> [1..1]  C8 616
       TransactionIdentification <TxId> [0..1] Text 617
       UETR <UETR> [0..1] IdentifierSet 617
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 617
       InstructingAgent <InstgAgt> [1..1] ± 617
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 618
   RequestHandling <ReqHdlg> [0..*]  C4 618
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 608 February 2025
```

