---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.6 FundCashForecast7"]
file_pages: [4699]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.6 FundCashForecast7

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4699 to 4699.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4699

```text
On Condition
    /AdditionalBalance is present
Following Must be True
    /AdditionalBalance/TotalUnitsFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalUnitsFromCashOrders Must be present
 Or    /AdditionalBalance/TotalCashFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalCashFromCashOrders Must be present
66.1.25.6  FundCashForecast7
Definition: Cash movements from or to a fund as a result of investment funds transactions, eg,
subscriptions or redemptions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4700
   TradeDateTime <TradDtTm> [1..1] ± 4700
   PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4700
   FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4700
   TotalNAV <TtlNAV> [0..*] Amount C2, C10 4701
   PreviousTotalNAV <PrvsTtlNAV> [0..*] Amount C2, C10 4701
   TotalUnitsNumber <TtlUnitsNb> [0..1] ± 4702
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4702
   TotalNAVChangeRate <TtlNAVChngRate> [0..1] Rate 4702
   InvestmentCurrency <InvstmtCcy> [0..*] CodeSet C2 4702
   CurrencyStatus <CcySts> [0..1] ± 4703
   ExceptionalNetCashFlowIndicator
<XcptnlNetCshFlowInd>
[1..1] Indicator 4703
   Price <Pric> [0..1] ± 4703
   ForeignExchangeRate <FXRate> [0..1] ± 4703
   PercentageOfShareClassTotalNAV
<PctgOfShrClssTtlNAV>
[0..1] Rate 4704
   CashInForecastDetails <CshInFcstDtls> [0..*] ± C3 4704
   CashOutForecastDetails <CshOutFcstDtls> [0..*] ± C4 4705
   NetCashForecastDetails <NetCshFcstDtls> [0..*] ± C5 4705
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4699 May 2026
```

