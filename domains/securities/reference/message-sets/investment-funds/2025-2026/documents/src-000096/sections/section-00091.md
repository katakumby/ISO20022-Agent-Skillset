---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.7 FundCashForecastDetails <FndCshFcstDtls>", "10.4.7.1 Identification <Id>"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.7.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
BreakdownByParty/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByParty/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashOutForecast/ExceptionalCashFlowIndicator.
10.4.7.1  Identification <Id>
Presence: [1..1]
Definition: Unique technical identifier for an instance of a fund cash forecast within a fund cash forecast
report as assigned by the issuer of the report.
Datatype: "Max35Text" on page 5403
10.4.7.2  TradeDateTime <TradDtTm>
Presence: [1..1]
Definition: Date and, if required, the time, at which the price has been applied.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTimeChoice"
on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
10.4.7.3  PreviousTradeDateTime <PrvsTradDtTm>
Presence: [0..1]
Definition: Previous date and time at which the price was applied.
PreviousTradeDateTime <PrvsTradDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
10.4.7.4  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 135 May 2026
```

