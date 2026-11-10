---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.1 PaymentIdentification <PmtId>", "5.4.2.1.3.1.1 TransactionIdentification <TxId>"]
file_pages: [257]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.1.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 257 to 257.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 257

```text
PaymentIdentification <PmtId> contains one of the following PaymentIdentification8Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TransactionIdentification <TxId> [1..1] Text 257
Or   UETR <UETR> [1..1] IdentifierSet 258
Or   QueueIdentification <QId> [1..1]  258
     QueueIdentification <QId> [1..1] Text 258
     PositionInQueue <PosInQ> [1..1] Text 258
Or   LongBusinessIdentification <LngBizId> [1..1]  C18 258
     TransactionIdentification <TxId> [0..1] Text 259
     UETR <UETR> [0..1] IdentifierSet 259
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 260
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 260
     PaymentMethod <PmtMtd> [0..1]  260
{Or       FINMessageType <FINMT> [1..1] Text 260
Or       XMLMessageName <XMLMsgNm> [1..1] Text 260
Or       Proprietary <Prtry> [1..1] Text 260
Or}       Instrument <Instrm> [1..1] CodeSet 260
     InstructingAgent <InstgAgt> [1..1] ± 261
     InstructedAgent <InstdAgt> [1..1] ± 262
     EntryType <NtryTp> [0..1] IdentifierSet 263
     EndToEndIdentification <EndToEndId> [0..1] Text 263
Or   ShortBusinessIdentification <ShrtBizId> [1..1]  C19 263
     TransactionIdentification <TxId> [0..1] Text 264
     UETR <UETR> [0..1] IdentifierSet 264
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 264
     InstructingAgent <InstgAgt> [1..1] ± 264
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 265
5.4.2.1.3.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 257 February 2025
```

