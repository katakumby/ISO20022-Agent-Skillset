---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>"]
file_pages: [330, 331]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2 Modification <Mod>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 330 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
6.4.2 Modification <Mod>
Presence: [1..*]
Definition: Identifies the list of modifications to be executed.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 330 February 2025
```

## File page 331

```text
Modification <Mod> contains the following TransactionModification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [1..1]  332
{Or     TransactionIdentification <TxId> [1..1] Text 333
Or     UETR <UETR> [1..1] IdentifierSet 334
Or     QueueIdentification <QId> [1..1]  334
       QueueIdentification <QId> [1..1] Text 334
       PositionInQueue <PosInQ> [1..1] Text 334
Or     LongBusinessIdentification <LngBizId> [1..1]  C4 334
       TransactionIdentification <TxId> [0..1] Text 335
       UETR <UETR> [0..1] IdentifierSet 335
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 336
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 336
       PaymentMethod <PmtMtd> [0..1]  336
{Or         FINMessageType <FINMT> [1..1] Text 336
Or         XMLMessageName <XMLMsgNm> [1..1] Text 336
Or         Proprietary <Prtry> [1..1] Text 336
Or}         Instrument <Instrm> [1..1] CodeSet 336
       InstructingAgent <InstgAgt> [1..1] ± 337
       InstructedAgent <InstdAgt> [1..1] ± 338
       EntryType <NtryTp> [0..1] IdentifierSet 339
       EndToEndIdentification <EndToEndId> [0..1] Text 339
Or     ShortBusinessIdentification <ShrtBizId> [1..1]  C5 339
       TransactionIdentification <TxId> [0..1] Text 340
       UETR <UETR> [0..1] IdentifierSet 340
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 340
       InstructingAgent <InstgAgt> [1..1] ± 340
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 341
   NewPaymentValueSet <NewPmtValSet> [1..1]  341
     Instruction <Instr> [0..1] CodeSet 342
     Type <Tp> [0..1]  342
{Or       Code <Cd> [1..1] CodeSet 343
Or}       Proprietary <Prtry> [1..1] Text 344
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 331 February 2025
```

