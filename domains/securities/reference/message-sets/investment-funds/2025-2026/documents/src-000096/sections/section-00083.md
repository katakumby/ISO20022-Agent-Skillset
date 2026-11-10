---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "9.4 Message Building Blocks", "9.4.7 EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.042.001.04"]
---

# 9.4.7 EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
9.4.7 EstimatedFundCashForecastDetails
<EstmtdFndCshFcstDtls>
Presence: [1..*]
Definition: Information related to the estimated cash-in and cash-out flows for a specific trade date as a
result of transactions in shares in an investment fund, for example, subscriptions, redemptions or
switches. The information provided is sorted by pre-defined criteria such as country, institution, currency
or user defined criteria.
Impacted by: C11 "ExceptionalCashFlowIndicatorRule"
EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls> contains the following elements
(see "EstimatedFundCashForecast5" on page 4671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4672
   TradeDateTime <TradDtTm> [1..1] ± 4672
   PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4672
   FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4673
   EstimatedTotalNAV <EstmtdTtlNAV> [0..*] Amount C2, C10 4673
   PreviousTotalNAV <PrvsTtlNAV> [0..*] Amount C2, C10 4674
   EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> [0..1] ± 4674
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4674
   EstimatedTotalNAVChangeRate
<EstmtdTtlNAVChngRate>
[0..1] Rate 4675
   InvestmentCurrency <InvstmtCcy> [0..*] CodeSet C2 4675
   CurrencyStatus <CcySts> [0..1] ± 4675
   ExceptionalNetCashFlowIndicator
<XcptnlNetCshFlowInd>
[1..1] Indicator 4675
   Price <Pric> [0..1] ± 4675
   ForeignExchangeRate <FXRate> [0..1] ± 4676
   EstimatedPercentageOfShareClassTotalNAV
<EstmtdPctgOfShrClssTtlNAV>
[0..1] Rate 4676
   BreakdownByParty <BrkdwnByPty> [0..*] ± 4676
   BreakdownByCountry <BrkdwnByCtry> [0..*] ± 4677
   BreakdownByCurrency <BrkdwnByCcy> [0..*] ± 4678
   BreakdownByUserDefinedParameter
<BrkdwnByUsrDfndParam>
[0..*] ± C17 4679
   EstimatedNetCashForecastDetails
<EstmtdNetCshFcstDtls>
[0..*] ± C5 4680
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 123 May 2026
```

