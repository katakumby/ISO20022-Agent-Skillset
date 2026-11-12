---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.12 GeneratedOrder <GnrtdOrdr>"]
file_pages: [298]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.12 GeneratedOrder <GnrtdOrdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 298 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.12  GeneratedOrder <GnrtdOrdr>
Presence: [0..1]
Definition: Payment is a liquidity transfer order that has been executed automatically following a
predefined or standing order.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 886):
• Meaning When True: True
• Meaning When False: False
5.4.2.1.3.2.1.4.13  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: This is the former PaymentInstructionReference.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.14  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 883
5.4.2.1.3.2.1.4.15  EndToEndIdentification <EndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction.
It can be included in several messages related to the transaction.
Usage: This is the former related reference.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.16  Parties <Pties>
Presence: [0..1]
Definition: Defines the party fields used to search for a payment.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 298 February 2025
```

