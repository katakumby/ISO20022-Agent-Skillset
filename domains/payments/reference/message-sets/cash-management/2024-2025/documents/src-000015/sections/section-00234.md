---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.4 Message Building Blocks", "7.4.2 PaymentIdentification <PmtId>", "7.4.2.1 TransactionIdentification <TxId>"]
file_pages: [352]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7.4.2.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 352 to 352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 352

```text
PaymentIdentification <PmtId> contains one of the following PaymentIdentification8Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TransactionIdentification <TxId> [1..1] Text 352
Or   UETR <UETR> [1..1] IdentifierSet 353
Or   QueueIdentification <QId> [1..1]  353
     QueueIdentification <QId> [1..1] Text 353
     PositionInQueue <PosInQ> [1..1] Text 353
Or   LongBusinessIdentification <LngBizId> [1..1]  C9 353
     TransactionIdentification <TxId> [0..1] Text 354
     UETR <UETR> [0..1] IdentifierSet 354
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 355
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 355
     PaymentMethod <PmtMtd> [0..1]  355
{Or       FINMessageType <FINMT> [1..1] Text 355
Or       XMLMessageName <XMLMsgNm> [1..1] Text 355
Or       Proprietary <Prtry> [1..1] Text 355
Or}       Instrument <Instrm> [1..1] CodeSet 355
     InstructingAgent <InstgAgt> [1..1] ± 356
     InstructedAgent <InstdAgt> [1..1] ± 357
     EntryType <NtryTp> [0..1] IdentifierSet 358
     EndToEndIdentification <EndToEndId> [0..1] Text 358
Or   ShortBusinessIdentification <ShrtBizId> [1..1]  C10 358
     TransactionIdentification <TxId> [0..1] Text 359
     UETR <UETR> [0..1] IdentifierSet 359
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 359
     InstructingAgent <InstgAgt> [1..1] ± 359
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 360
7.4.2.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 352 February 2025
```

