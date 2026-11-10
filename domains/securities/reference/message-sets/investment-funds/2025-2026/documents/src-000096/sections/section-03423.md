---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.1 Fund2", "66.1.25.1.14 NetCashForecastDetails <NetCshFcstDtls>", "66.1.25.1.14.1 CashSettlementDate <CshSttlmDt>"]
file_pages: [4670]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.1.14.1 CashSettlementDate <CshSttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4670 to 4670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4670

```text
NetCashForecastDetails <NetCshFcstDtls> contains the following NetCashForecast5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [0..1] Date 4670
   NetAmount <NetAmt> [0..1] Amount C2, C10 4670
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4670
   FlowDirection <FlowDrctn> [1..1] CodeSet 4670
66.1.25.1.14.1  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
66.1.25.1.14.2  NetAmount <NetAmt>
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
66.1.25.1.14.3  NetUnitsNumber <NetUnitsNb>
Presence: [0..1]
Definition: Net amount, expressed as a number of units.
NetUnitsNumber <NetUnitsNb> contains the following elements (see "FinancialInstrumentQuantity1"
on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.1.14.4  FlowDirection <FlowDrctn>
Presence: [1..1]
Definition: Specifies the direction of the cash flow from the perspective of the fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4670 May 2026
```

