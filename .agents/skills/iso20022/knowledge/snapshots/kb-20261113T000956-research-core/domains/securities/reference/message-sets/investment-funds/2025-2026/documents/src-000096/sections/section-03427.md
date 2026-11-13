---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.2 EstimatedFundCashForecast5", "66.1.25.2.6 PreviousTotalNAV <PrvsTtlNAV>"]
file_pages: [4674]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.2.6 PreviousTotalNAV <PrvsTtlNAV>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4674 to 4674.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4674

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.25.2.6  PreviousTotalNAV <PrvsTtlNAV>
Presence: [0..*]
Definition: Previous value of all the holdings, less the fund's liabilities, attributable to a specific
investment fund class.
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
66.1.25.2.7  EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb>
Presence: [0..1]
Definition: Estimated total number of investment fund class units that have been issued.
EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.2.8  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous value of all the holdings, less the fund's liabilities, attributable to a specific
investment fund class.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4674 May 2026
```

