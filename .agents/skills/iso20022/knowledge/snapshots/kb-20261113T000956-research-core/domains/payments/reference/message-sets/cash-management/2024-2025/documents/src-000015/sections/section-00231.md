---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.2 Structure"]
file_pages: [349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 349 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 349

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CclTx> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 351
   PaymentIdentification <PmtId> [1..1]  351
{Or     TransactionIdentification <TxId> [1..1] Text 352
Or     UETR <UETR> [1..1] IdentifierSet 353
Or     QueueIdentification <QId> [1..1]  353
       QueueIdentification <QId> [1..1] Text 353
       PositionInQueue <PosInQ> [1..1] Text 353
Or     LongBusinessIdentification <LngBizId> [1..1]  C9 353
       TransactionIdentification <TxId> [0..1] Text 354
       UETR <UETR> [0..1] IdentifierSet 354
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 355
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 355
       PaymentMethod <PmtMtd> [0..1]  355
{Or         FINMessageType <FINMT> [1..1] Text 355
Or         XMLMessageName <XMLMsgNm> [1..1] Text 355
Or         Proprietary <Prtry> [1..1] Text 355
Or}         Instrument <Instrm> [1..1] CodeSet 355
       InstructingAgent <InstgAgt> [1..1] ± 356
       InstructedAgent <InstdAgt> [1..1] ± 357
       EntryType <NtryTp> [0..1] IdentifierSet 358
       EndToEndIdentification <EndToEndId> [0..1] Text 358
Or     ShortBusinessIdentification <ShrtBizId> [1..1]  C10 358
       TransactionIdentification <TxId> [0..1] Text 359
       UETR <UETR> [0..1] IdentifierSet 359
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 359
       InstructingAgent <InstgAgt> [1..1] ± 359
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 360
   CashAccount <CshAcct> [0..1] ± C7, C6 360
   CancellationReason <CxlRsn> [0..1]  361
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 349 February 2025
```

