---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.5 FundDetailedConfirmedCashForecastReport3", "66.1.7.5.1 FundOrSubFundDetails <FndOrSubFndDtls>"]
file_pages: [4416]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.5.1 FundOrSubFundDetails <FndOrSubFndDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4416 to 4416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4416

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FundOrSubFundDetails <FndOrSubFndDtls> [0..1] ± C14,
C15,
C16
4416
   FundCashForecastDetails <FndCshFcstDtls> [1..*]  C11 4417
     Identification <Id> [1..1] Text 4419
     TradeDateTime <TradDtTm> [1..1] ± 4419
     PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4419
     FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4419
     TotalNAV <TtlNAV> [0..*] Amount C2, C10 4420
     PreviousTotalNAV <PrvsTtlNAV> [0..*] Amount C2, C10 4420
     TotalUnitsNumber <TtlUnitsNb> [0..1] ± 4421
     PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4421
     TotalNAVChangeRate <TtlNAVChngRate> [0..1] Rate 4421
     InvestmentCurrency <InvstmtCcy> [0..*] CodeSet C2 4421
     CurrencyStatus <CcySts> [0..1] ± 4422
     ExceptionalNetCashFlowIndicator
<XcptnlNetCshFlowInd>
[1..1] Indicator 4422
     Price <Pric> [0..1] ± 4422
     ForeignExchangeRate <FXRate> [0..1] ± 4422
     PercentageOfShareClassTotalNAV
<PctgOfShrClssTtlNAV>
[0..1] Rate 4423
     BreakdownByParty <BrkdwnByPty> [0..*] ± 4423
     BreakdownByCountry <BrkdwnByCtry> [0..*] ± 4424
     BreakdownByCurrency <BrkdwnByCcy> [0..*] ± 4425
     BreakdownByUserDefinedParameter
<BrkdwnByUsrDfndParam>
[0..*] ± C17 4426
     NetCashForecastDetails <NetCshFcstDtls> [0..*] ± C5 4427
   ConsolidatedNetCashForecast <CnsltdNetCshFcst> [0..1] ± 4428
   Extension <Xtnsn> [0..*] ± C16 4428
66.1.7.5.1  FundOrSubFundDetails <FndOrSubFndDtls>
Presence: [0..1]
Definition: Information about the fund/sub fund when the report either specifies cash flow for the
fund/sub fund or for a share class of the fund/sub fund.
Impacted by: C14 "FundIdentification1Rule", C15 "FundIdentification2Rule", C16
"FundIdentification3Rule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4416 May 2026
```

