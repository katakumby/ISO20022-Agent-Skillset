---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.15 TransactionIdentification <TxId>"]
file_pages: [167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.15 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 167 to 167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 167

```text
CodeName Name Definition
TFRO TimeFrom Payment instruction will be valid and
eligible for execution from the date and
time stipulated.
4.4.2.2.2.2.3.15  TransactionIdentification <TxId>
Presence: [0..*]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.16  UETR <UETR>
Presence: [0..*]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
4.4.2.2.2.2.3.17  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..*]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Usage: this is the former InterbankValueDate.
Datatype: "ISODate" on page 883
4.4.2.2.2.2.3.18  EndToEndIdentification <EndToEndId>
Presence: [0..*]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction.
It can be included in several messages related to the transaction.
Usage: this is the former RelatedReference.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.19  Parties <Pties>
Presence: [0..1]
Definition: Defines the party fields used to search for a payment.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 167 February 2025
```

