---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.5 FundDetailedConfirmedCashForecastReport3", "66.1.7.5.2 FundCashForecastDetails <FndCshFcstDtls>", "66.1.7.5.2.7 TotalUnitsNumber <TtlUnitsNb>"]
file_pages: [4421]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.5.2.7 TotalUnitsNumber <TtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4421 to 4421.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4421

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
66.1.7.5.2.7  TotalUnitsNumber <TtlUnitsNb>
Presence: [0..1]
Definition: Total number of investment fund class units that have been issued.
TotalUnitsNumber <TtlUnitsNb> contains the following elements (see "FinancialInstrumentQuantity1"
on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.7.5.2.8  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous total number of investment fund class units that have been issued.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.7.5.2.9  TotalNAVChangeRate <TtlNAVChngRate>
Presence: [0..1]
Definition: Rate of change of the net asset value.
Datatype: "PercentageRate" on page 5401
66.1.7.5.2.10  InvestmentCurrency <InvstmtCcy>
Presence: [0..*]
Definition: Currency of the investment fund class.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4421 May 2026
```

