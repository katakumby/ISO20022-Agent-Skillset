---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.4 Fund3", "66.1.25.4.7 EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb>"]
file_pages: [4691]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.4.7 EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4691 to 4691.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4691

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.25.4.7  EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb>
Presence: [0..1]
Definition: Estimated total number of units of the fund/sub fund.
EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.4.8  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous total number of units of the fund/sub fund.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.4.9  EstimatedPercentageOfFundTotalNAV <EstmtdPctgOfFndTtlNAV>
Presence: [0..1]
Definition: Estimated consolidated net cash flow expressed as a percentage of the previous total NAV
for the fund/sub fund.
Datatype: "PercentageRate" on page 5401
66.1.25.5  EstimatedFundCashForecast6
Definition: Cash movements from or to a fund as a result of investment funds transactions, eg,
subscriptions or redemptions.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4691 May 2026
```

