---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.1 PaymentIdentification <PmtId>", "5.4.2.1.3.1.4 LongBusinessIdentification <LngBizId>", "5.4.2.1.3.1.4.3 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.1.4.3 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
5.4.2.1.3.1.4.3  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [1..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
Datatype: "ImpliedCurrencyAndAmount" on page 848
5.4.2.1.3.1.4.4  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [1..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 883
5.4.2.1.3.1.4.5  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Message type with which the instruction has been initiated.
PaymentMethod <PmtMtd> contains one of the following PaymentOrigin1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FINMessageType <FINMT> [1..1] Text 260
Or   XMLMessageName <XMLMsgNm> [1..1] Text 260
Or   Proprietary <Prtry> [1..1] Text 260
Or}   Instrument <Instrm> [1..1] CodeSet 260
5.4.2.1.3.1.4.5.1  FINMessageType <FINMT>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT FIN format message, for example, MT
103.
Datatype: "Max3NumericText" on page 889
5.4.2.1.3.1.4.5.2  XMLMessageName <XMLMsgNm>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT XML message.
Datatype: "Max35Text" on page 889
5.4.2.1.3.1.4.5.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies that the payment was included in a proprietary format message.
Datatype: "Max35Text" on page 889
5.4.2.1.3.1.4.5.4  Instrument <Instrm>
Presence: [1..1]
Definition: Specifies the type of payment when not included in a SWIFT or proprietary format.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 260 February 2025
```

