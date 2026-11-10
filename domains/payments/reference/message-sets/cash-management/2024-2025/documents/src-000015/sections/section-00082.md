---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.3 PaymentIdentification <PmtId>", "4.4.2.2.2.2.3.3.4 LongBusinessIdentification <LngBizId>", "4.4.2.2.2.2.3.3.4.3 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.3.4.3 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 151 to 151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
4.4.2.2.2.2.3.3.4.3  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [1..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
Datatype: "ImpliedCurrencyAndAmount" on page 848
4.4.2.2.2.2.3.3.4.4  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [1..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 883
4.4.2.2.2.2.3.3.4.5  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Message type with which the instruction has been initiated.
PaymentMethod <PmtMtd> contains one of the following PaymentOrigin1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FINMessageType <FINMT> [1..1] Text 151
Or   XMLMessageName <XMLMsgNm> [1..1] Text 151
Or   Proprietary <Prtry> [1..1] Text 151
Or}   Instrument <Instrm> [1..1] CodeSet 151
4.4.2.2.2.2.3.3.4.5.1  FINMessageType <FINMT>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT FIN format message, for example, MT
103.
Datatype: "Max3NumericText" on page 889
4.4.2.2.2.2.3.3.4.5.2  XMLMessageName <XMLMsgNm>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT XML message.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.3.4.5.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies that the payment was included in a proprietary format message.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.3.4.5.4  Instrument <Instrm>
Presence: [1..1]
Definition: Specifies the type of payment when not included in a SWIFT or proprietary format.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 151 February 2025
```

