---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.8 Fund4", "66.1.25.8.7 TotalUnitsNumber <TtlUnitsNb>"]
file_pages: [4710]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.8.7 TotalUnitsNumber <TtlUnitsNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4710 to 4710.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4710

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
66.1.25.8.7  TotalUnitsNumber <TtlUnitsNb>
Presence: [0..1]
Definition: Total number of units of the fund/sub fund.
TotalUnitsNumber <TtlUnitsNb> contains the following elements (see "FinancialInstrumentQuantity1"
on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.8.8  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous total number of units of the fund/sub fund.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.8.9  PercentageOfFundTotalNAV <PctgOfFndTtlNAV>
Presence: [0..1]
Definition: Consolidated net cash flow expressed as a percentage of the total NAV for the fund/sub
fund.
Datatype: "PercentageRate" on page 5401
66.1.26 InvestmentFundOrder
66.1.26.1  PensionTransferScope1Choice
Definition: Choice of formats for the scope of a pension transfer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4710 May 2026
```

