---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.1 PaymentIdentification <PmtId>", "6.4.2.1.1 TransactionIdentification <TxId>"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.1.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
PaymentIdentification <PmtId> contains one of the following PaymentIdentification8Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TransactionIdentification <TxId> [1..1] Text 333
Or   UETR <UETR> [1..1] IdentifierSet 334
Or   QueueIdentification <QId> [1..1]  334
     QueueIdentification <QId> [1..1] Text 334
     PositionInQueue <PosInQ> [1..1] Text 334
Or   LongBusinessIdentification <LngBizId> [1..1]  C4 334
     TransactionIdentification <TxId> [0..1] Text 335
     UETR <UETR> [0..1] IdentifierSet 335
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 336
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 336
     PaymentMethod <PmtMtd> [0..1]  336
{Or       FINMessageType <FINMT> [1..1] Text 336
Or       XMLMessageName <XMLMsgNm> [1..1] Text 336
Or       Proprietary <Prtry> [1..1] Text 336
Or}       Instrument <Instrm> [1..1] CodeSet 336
     InstructingAgent <InstgAgt> [1..1] ± 337
     InstructedAgent <InstdAgt> [1..1] ± 338
     EntryType <NtryTp> [0..1] IdentifierSet 339
     EndToEndIdentification <EndToEndId> [0..1] Text 339
Or   ShortBusinessIdentification <ShrtBizId> [1..1]  C5 339
     TransactionIdentification <TxId> [0..1] Text 340
     UETR <UETR> [0..1] IdentifierSet 340
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 340
     InstructingAgent <InstgAgt> [1..1] ± 340
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 341
6.4.2.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 333 February 2025
```

