---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.5 EstimatedFundCashForecast6", "66.1.25.5.8 PreviousTotalUnitsNumber <PrvsTtlUnitsNb>"]
file_pages: [4695]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.5.8 PreviousTotalUnitsNumber <PrvsTtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4695 to 4695.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4695

```text
EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.5.8  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous value of all the holdings, less the fund's liabilities, attributable to a specific
investment fund class.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.5.9  EstimatedTotalNAVChangeRate <EstmtdTtlNAVChngRate>
Presence: [0..1]
Definition: Rate of change of the net asset value.
Datatype: "PercentageRate" on page 5401
66.1.25.5.10  InvestmentCurrency <InvstmtCcy>
Presence: [0..*]
Definition: Currency of the investment fund class.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.25.5.11  CurrencyStatus <CcySts>
Presence: [0..1]
Definition: Information about the designation of the share class currency, that is, whether it is for
onshore or offshore purposes and other information that may be required. This is typically only required
for CNY funds.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4695 May 2026
```

