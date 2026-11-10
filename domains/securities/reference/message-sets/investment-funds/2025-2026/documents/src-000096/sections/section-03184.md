---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.4 NetCashForecast4", "66.1.7.4.2 NetAmount <NetAmt>"]
file_pages: [4414]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.4.2 NetAmount <NetAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4414 to 4414.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4414

```text
66.1.7.4.2  NetAmount <NetAmt>
Presence: [0..1]
Definition: Net amount of the cash flow, expressed as an amount of money.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.7.4.3  NetUnitsNumber <NetUnitsNb>
Presence: [0..1]
Definition: Net amount, expressed as a number of units.
NetUnitsNumber <NetUnitsNb> contains the following elements (see "FinancialInstrumentQuantity1"
on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.7.4.4  FlowDirection <FlowDrctn>
Presence: [1..1]
Definition: Specifies the direction of the cash flow from the perspective of the fund.
Datatype: "FlowDirectionType1Code" on page 5304
CodeName Name Definition
INCG Incoming Amount of money received.
OUTG Outgoing Amount of money paid out.
66.1.7.4.5  AdditionalBalance <AddtlBal>
Presence: [0..1]
Definition: Additional balances for cash amounts and number of units.
In an estimated report, the total cash derived from orders placed as a number of units is an estimated
cash amount and the total number of units derived from orders placed as a cash amount is an
estimated number of units.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4414 May 2026
```

