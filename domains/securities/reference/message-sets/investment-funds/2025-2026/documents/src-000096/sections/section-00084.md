---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "9.4 Message Building Blocks", "9.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>"]
file_pages: [124, 125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.042.001.04"]
---

# 9.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 124 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
Constraints
• ExceptionalCashFlowIndicatorRule
If ExceptionalNetCashFlowIndicator is "true" or "1" (Yes), then at least one or more of the following
must be present:
BreakdownByParty/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByParty/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashOutForecast/ExceptionalCashFlowIndicator.
9.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>
Presence: [0..1]
Definition: Estimated net cash as a result of the cash-in and cash-out flows specified in the fund cash
forecast details.
ConsolidatedNetCashForecast <CnsltdNetCshFcst> contains the following elements (see
"NetCashForecast3" on page 4412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NetAmount <NetAmt> [0..1] Amount C2, C10 4412
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4412
   FlowDirection <FlowDrctn> [1..1] CodeSet 4413
9.4.9 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C12 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 124 May 2026
```

## File page 125

```text
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 125 May 2026
```

