---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.4 InstructedAmount <InstdAmt>", "5.4.2.1.3.2.1.4.4.1 AmountWithCurrency <AmtWthCcy>"]
file_pages: [292]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.4.1 AmountWithCurrency <AmtWthCcy>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 292 to 292.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 292

```text
5.4.2.1.3.2.1.4.4.1  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is explicit.
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 848
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.1.3.2.1.4.4.2  AmountWithoutCurrency <AmtWthtCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context.
Datatype: "ImpliedCurrencyAndAmount" on page 848
5.4.2.1.3.2.1.4.5  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
InterbankSettlementAmount <IntrBkSttlmAmt> contains one of the following elements (see
"Amount2Choice" on page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
5.4.2.1.3.2.1.4.6  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Datatype: "Max10Text" on page 887
5.4.2.1.3.2.1.4.7  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Indicates the message or event from which an instruction has been initiated.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 292 February 2025
```

