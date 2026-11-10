---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["7 camt.040.001.04 FundEstimatedCashForecastReportV04", "7.4 Message Building Blocks", "7.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>"]
file_pages: [103]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.040.001.04"]
---

# 7.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 103 to 103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 103

```text
EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls> contains the following elements
(see "EstimatedFundCashForecast6" on page 4691 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4692
   TradeDateTime <TradDtTm> [1..1] ± 4692
   PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4693
   FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4693
   EstimatedTotalNAV <EstmtdTtlNAV> [0..*] Amount C2, C10 4694
   PreviousTotalNAV <PrvsTtlNAV> [0..*] Amount C2, C10 4694
   EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> [0..1] ± 4694
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4695
   EstimatedTotalNAVChangeRate
<EstmtdTtlNAVChngRate>
[0..1] Rate 4695
   InvestmentCurrency <InvstmtCcy> [0..*] CodeSet C2 4695
   CurrencyStatus <CcySts> [0..1] ± 4695
   ExceptionalNetCashFlowIndicator
<XcptnlNetCshFlowInd>
[1..1] Indicator 4696
   Price <Pric> [0..1] ± 4696
   ForeignExchangeRate <FXRate> [0..1] ± 4696
   EstimatedPercentageOfShareClassTotalNAV
<EstmtdPctgOfShrClssTtlNAV>
[0..1] Rate 4696
   EstimatedCashInForecastDetails <EstmtdCshInFcstDtls> [0..*] ± C3 4697
   EstimatedCashOutForecastDetails
<EstmtdCshOutFcstDtls>
[0..*] ± C4 4697
   EstimatedNetCashForecastDetails
<EstmtdNetCshFcstDtls>
[0..*] ± C5 4698
Constraints
• ExceptionalCashFlowIndicatorRule
If Exceptional NetCashFlowIndicator is "true" or "1" (Yes), then either
EstimatedCashInForecastDetails/ExceptionalCashFlowIndicator or
EstimatedCashOutForecastDetails/ExceptionalCashFlowIndicator must be present. Both may be
present.
7.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>
Presence: [0..1]
Definition: Estimated net cash as a result of the cash-in and cash-out flows.
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 103 May 2026
```

