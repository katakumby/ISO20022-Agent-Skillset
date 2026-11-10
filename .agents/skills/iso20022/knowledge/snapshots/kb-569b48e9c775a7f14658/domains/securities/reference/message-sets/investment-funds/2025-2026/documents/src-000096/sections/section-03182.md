---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.3 NetCashForecast3"]
file_pages: [4412]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.3 NetCashForecast3

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4412 to 4412.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4412

```text
AdditionalBalance <AddtlBal> contains the following elements (see "FundBalance1" on page 4389
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalUnitsFromUnitOrders <TtlUnitsFrUnitOrdrs> [0..1] ± 4389
   TotalUnitsFromCashOrders <TtlUnitsFrCshOrdrs> [0..1] ± 4389
   TotalCashFromUnitOrders <TtlCshFrUnitOrdrs> [0..1] Amount C2, C10 4390
   TotalCashFromCashOrders <TtlCshFrCshOrdrs> [0..1] Amount C2, C10 4390
66.1.7.3  NetCashForecast3
Definition: Net cash movement to a fund as a result of investment funds transactions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NetAmount <NetAmt> [0..1] Amount C2, C10 4412
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4412
   FlowDirection <FlowDrctn> [1..1] CodeSet 4413
66.1.7.3.1  NetAmount <NetAmt>
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
66.1.7.3.2  NetUnitsNumber <NetUnitsNb>
Presence: [0..1]
Definition: Net amount, expressed as a number of units.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4412 May 2026
```

