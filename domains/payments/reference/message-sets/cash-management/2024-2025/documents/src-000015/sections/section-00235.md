---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.4 Message Building Blocks", "7.4.2 PaymentIdentification <PmtId>", "7.4.2.2 UETR <UETR>"]
file_pages: [353]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7.4.2.2 UETR <UETR>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 353 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 353

```text
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
7.4.2.2  UETR <UETR>
Presence: [1..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
7.4.2.3  QueueIdentification <QId>
Presence: [1..1]
Definition: Identification of the payment instruction by its position in a queue managed by the clearing
agent.
QueueIdentification <QId> contains the following QueueTransactionIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueueIdentification <QId> [1..1] Text 353
   PositionInQueue <PosInQ> [1..1] Text 353
7.4.2.3.1  QueueIdentification <QId>
Presence: [1..1]
Definition: Identification of the payment queue where the payment instruction resides.
Datatype: "Max16Text" on page 888
7.4.2.3.2  PositionInQueue <PosInQ>
Presence: [1..1]
Definition: Position of the payment instruction within the identified queue.
Datatype: "Max16Text" on page 888
7.4.2.4  LongBusinessIdentification <LngBizId>
Presence: [1..1]
Definition: Business identification of the payment instruction given by the clearing agent.
Impacted by: C9 "TransactionIdentificationPresenceRule"
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 353 February 2025
```

