---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.2 Structure"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FndDtldConfdCshFcstRpt> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 131
   PoolReference <PoolRef> [0..1] ± 131
   PreviousReference <PrvsRef> [0..*] ± 131
   RelatedReference <RltdRef> [0..*] ± 131
   MessagePagination <MsgPgntn> [1..1] ± 132
   FundOrSubFundDetails <FndOrSubFndDtls> [0..1] ± C14,
C15,
C16
132
   FundCashForecastDetails <FndCshFcstDtls> [1..*]  C11 134
     Identification <Id> [1..1] Text 135
     TradeDateTime <TradDtTm> [1..1] ± 135
     PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 135
     FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C13 135
     TotalNAV <TtlNAV> [0..*] Amount C4, C10 136
     PreviousTotalNAV <PrvsTtlNAV> [0..*] Amount C4, C10 136
     TotalUnitsNumber <TtlUnitsNb> [0..1] ± 137
     PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 137
     TotalNAVChangeRate <TtlNAVChngRate> [0..1] Rate 137
     InvestmentCurrency <InvstmtCcy> [0..*] CodeSet C4 137
     CurrencyStatus <CcySts> [0..1] ± 138
     ExceptionalNetCashFlowIndicator <XcptnlNetCshFlowInd> [1..1] Indicator 138
     Price <Pric> [0..1] ± 138
     ForeignExchangeRate <FXRate> [0..1] ± 139
     PercentageOfShareClassTotalNAV <PctgOfShrClssTtlNAV> [0..1] Rate 139
     BreakdownByParty <BrkdwnByPty> [0..*] ± 139
     BreakdownByCountry <BrkdwnByCtry> [0..*] ± 140
     BreakdownByCurrency <BrkdwnByCcy> [0..*] ± 141
     BreakdownByUserDefinedParameter
<BrkdwnByUsrDfndParam>
[0..*] ± C17 142
     NetCashForecastDetails <NetCshFcstDtls> [0..*] ± C7 143
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 128 May 2026
```

