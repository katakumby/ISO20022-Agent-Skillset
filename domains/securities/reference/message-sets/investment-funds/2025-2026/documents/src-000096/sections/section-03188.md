---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.5 FundDetailedConfirmedCashForecastReport3", "66.1.7.5.2 FundCashForecastDetails <FndCshFcstDtls>", "66.1.7.5.2.1 Identification <Id>"]
file_pages: [4419]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.5.2.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4419 to 4419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4419

```text
BreakdownByCountry/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashOutForecast/ExceptionalCashFlowIndicator.
66.1.7.5.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique technical identifier for an instance of a fund cash forecast within a fund cash forecast
report as assigned by the issuer of the report.
Datatype: "Max35Text" on page 5403
66.1.7.5.2.2  TradeDateTime <TradDtTm>
Presence: [1..1]
Definition: Date and, if required, the time, at which the price has been applied.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTimeChoice"
on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.7.5.2.3  PreviousTradeDateTime <PrvsTradDtTm>
Presence: [0..1]
Definition: Previous date and time at which the price was applied.
PreviousTradeDateTime <PrvsTradDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.7.5.2.4  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the cash flow is related.
Impacted by: C12 "FinancialInstrumentIdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4419 May 2026
```

