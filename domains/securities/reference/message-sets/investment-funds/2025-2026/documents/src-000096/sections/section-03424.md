---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.2 EstimatedFundCashForecast5"]
file_pages: [4671]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.2 EstimatedFundCashForecast5

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4671 to 4671.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4671

```text
Datatype: "FlowDirectionType1Code" on page 5304
CodeName Name Definition
INCG Incoming Amount of money received.
OUTG Outgoing Amount of money paid out.
66.1.25.2  EstimatedFundCashForecast5
Definition: Cash movements from or to a fund as a result of investment funds transactions, eg,
subscriptions or redemptions.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4671 May 2026
```

