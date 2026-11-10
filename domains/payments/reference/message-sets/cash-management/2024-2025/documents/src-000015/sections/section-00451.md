---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.2 OriginalPaymentIdentification <OrgnlPmtId>"]
file_pages: [610]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.2 OriginalPaymentIdentification <OrgnlPmtId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 610 to 610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 610

```text
23.4.2.2  OriginalPaymentIdentification <OrgnlPmtId>
Presence: [0..1]
Definition: Identification of the original transaction identification, when the request for which the receipt
is generated is a payment transaction.
OriginalPaymentIdentification <OrgnlPmtId> contains one of the following
PaymentIdentification8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TransactionIdentification <TxId> [1..1] Text 611
Or   UETR <UETR> [1..1] IdentifierSet 611
Or   QueueIdentification <QId> [1..1]  611
     QueueIdentification <QId> [1..1] Text 611
     PositionInQueue <PosInQ> [1..1] Text 611
Or   LongBusinessIdentification <LngBizId> [1..1]  C7 611
     TransactionIdentification <TxId> [0..1] Text 612
     UETR <UETR> [0..1] IdentifierSet 612
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 613
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 613
     PaymentMethod <PmtMtd> [0..1]  613
{Or       FINMessageType <FINMT> [1..1] Text 613
Or       XMLMessageName <XMLMsgNm> [1..1] Text 613
Or       Proprietary <Prtry> [1..1] Text 613
Or}       Instrument <Instrm> [1..1] CodeSet 613
     InstructingAgent <InstgAgt> [1..1] ± 614
     InstructedAgent <InstdAgt> [1..1] ± 615
     EntryType <NtryTp> [0..1] IdentifierSet 616
     EndToEndIdentification <EndToEndId> [0..1] Text 616
Or   ShortBusinessIdentification <ShrtBizId> [1..1]  C8 616
     TransactionIdentification <TxId> [0..1] Text 617
     UETR <UETR> [0..1] IdentifierSet 617
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 617
     InstructingAgent <InstgAgt> [1..1] ± 617
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 618
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 610 February 2025
```

