---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.1 PaymentIdentification <PmtId>", "5.4.2.1.3.1.2 UETR <UETR>"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.1.2 UETR <UETR>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
5.4.2.1.3.1.2  UETR <UETR>
Presence: [1..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
5.4.2.1.3.1.3  QueueIdentification <QId>
Presence: [1..1]
Definition: Identification of the payment instruction by its position in a queue managed by the clearing
agent.
QueueIdentification <QId> contains the following QueueTransactionIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueueIdentification <QId> [1..1] Text 258
   PositionInQueue <PosInQ> [1..1] Text 258
5.4.2.1.3.1.3.1  QueueIdentification <QId>
Presence: [1..1]
Definition: Identification of the payment queue where the payment instruction resides.
Datatype: "Max16Text" on page 888
5.4.2.1.3.1.3.2  PositionInQueue <PosInQ>
Presence: [1..1]
Definition: Position of the payment instruction within the identified queue.
Datatype: "Max16Text" on page 888
5.4.2.1.3.1.4  LongBusinessIdentification <LngBizId>
Presence: [1..1]
Definition: Business identification of the payment instruction given by the clearing agent.
Impacted by: C18 "TransactionIdentificationPresenceRule"
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 258 February 2025
```

