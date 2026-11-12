---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.7 FundCashForecastDetails <FndCshFcstDtls>", "10.4.7.7 TotalUnitsNumber <TtlUnitsNb>"]
file_pages: [137]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.7.7 TotalUnitsNumber <TtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 137 to 137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 137

```text
Definition: Previous value of all the holdings, less the fund's liabilities, attributable to a specific
investment fund class.
Impacted by: C4 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
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
10.4.7.7  TotalUnitsNumber <TtlUnitsNb>
Presence: [0..1]
Definition: Total number of investment fund class units that have been issued.
TotalUnitsNumber <TtlUnitsNb> contains the following elements (see "FinancialInstrumentQuantity1"
on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
10.4.7.8  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous total number of investment fund class units that have been issued.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
10.4.7.9  TotalNAVChangeRate <TtlNAVChngRate>
Presence: [0..1]
Definition: Rate of change of the net asset value.
Datatype: "PercentageRate" on page 5401
10.4.7.10  InvestmentCurrency <InvstmtCcy>
Presence: [0..*]
Definition: Currency of the investment fund class.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 137 May 2026
```

