---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.3 PaymentIdentification <PmtId>", "4.4.2.2.2.2.3.3.2 UETR <UETR>"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.3.2 UETR <UETR>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.3.2  UETR <UETR>
Presence: [1..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
4.4.2.2.2.2.3.3.3  QueueIdentification <QId>
Presence: [1..1]
Definition: Identification of the payment instruction by its position in a queue managed by the clearing
agent.
QueueIdentification <QId> contains the following QueueTransactionIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueueIdentification <QId> [1..1] Text 149
   PositionInQueue <PosInQ> [1..1] Text 149
4.4.2.2.2.2.3.3.3.1  QueueIdentification <QId>
Presence: [1..1]
Definition: Identification of the payment queue where the payment instruction resides.
Datatype: "Max16Text" on page 888
4.4.2.2.2.2.3.3.3.2  PositionInQueue <PosInQ>
Presence: [1..1]
Definition: Position of the payment instruction within the identified queue.
Datatype: "Max16Text" on page 888
4.4.2.2.2.2.3.3.4  LongBusinessIdentification <LngBizId>
Presence: [1..1]
Definition: Business identification of the payment instruction given by the clearing agent.
Impacted by: C17 "TransactionIdentificationPresenceRule"
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 149 February 2025
```

