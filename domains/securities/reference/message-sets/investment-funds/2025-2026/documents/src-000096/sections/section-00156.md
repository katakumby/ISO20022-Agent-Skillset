---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.2 Structure"]
file_pages: [224, 225, 226, 227, 228]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 224 to 228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
14.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PricRptCxl> [1..1]  C9, C10
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 231
   PreviousReference <PrvsRef> [0..1] ± 0
   MessagePagination <MsgPgntn> [1..1] ± 0
   PriceReportIdentification <PricRptId> [1..1] Text 0
   CancellationIdentification <CxlId> [1..1] Text 232
   CancellationReason <CxlRsn> [0..1] Text 0
   ExpectedPriceCorrectionDate <XpctdPricCrrctnDt> [0..1] ± 233
   CompletePriceCancellation <CmpltPricCxl> [1..1] Indicator 0
   CancelledPriceValuationDetails <CancPricValtnDtls> [0..*]  233
     PriceValuationDetails <PricValtnDtls> [1..*]  C20 238
       Identification <Id> [0..1] Text 245
       ValuationDateTime <ValtnDtTm> [0..1] ± 245
       NAVDateTime <NAVDtTm> [1..1] ± 245
       FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C17 245
         Identification <Id> [1..10]  247
{Or           ISIN <ISIN> [1..1] IdentifierSet 247
Or           SEDOL <SEDOL> [1..1] IdentifierSet 248
Or           CUSIP <CUSIP> [1..1] IdentifierSet 248
Or           RIC <RIC> [1..1] IdentifierSet 248
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 248
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 248
Or           CTA <CTA> [1..1] IdentifierSet 248
Or           QUICK <QUICK> [1..1] IdentifierSet 248
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 249
Or           Dutch <Dtch> [1..1] IdentifierSet 249
Or           Valoren <Vlrn> [1..1] IdentifierSet 249
Or           Sicovam <SCVM> [1..1] IdentifierSet 249
Or           Belgian <Belgn> [1..1] IdentifierSet 249
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 224 May 2026
```

## File page 225

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           Common <Cmon> [1..1] IdentifierSet 249
Or           DTI <DTI> [1..1] IdentifierSet 249
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  250
             Identification <Id> [1..1] Text 250
             IdentificationSource <IdSrc> [1..1] ± 250
         Name <Nm> [0..1] Text 250
         ShortName <ShrtNm> [0..1] Text 250
         SupplementaryIdentification <SplmtryId> [0..1] Text 250
         DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 251
         ClassType <ClssTp> [0..1] Text 251
         SecuritiesForm <SctiesForm> [0..1] CodeSet 251
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 251
         DualFundIndicator <DualFndInd> [1..1] Indicator 252
         ProductGroup <PdctGrp> [0..1] Text 252
         SeriesIdentification <SrsId> [0..1]  C21 252
           SeriesDate <SrsDt> [0..1] ± 252
           SeriesName <SrsNm> [0..1] Text 252
       FundManagementCompany <FndMgmtCpny> [0..1] ± 253
       TotalNAV <TtlNAV> [0..*] Amount C3, C12 253
       TotalUnitsNumber <TtlUnitsNb> [0..1] ± 253
       NextValuationDateTime <NxtValtnDtTm> [0..1] ± 254
       PreviousValuationDateTime <PrvsValtnDtTm> [0..1] ± 254
       ValuationType <ValtnTp> [1..1] CodeSet 254
       ValuationFrequency <ValtnFrqcy> [0..1] CodeSet 254
       OfficialValuationIndicator <OffclValtnInd> [1..1] Indicator 255
       SuspendedIndicator <SspdInd> [1..1] Indicator 255
       PriceDetails <PricDtls> [0..*]  C8 255
         PriceType <PricTp> [1..1]  C18 258
{Or           Code <Cd> [1..1] CodeSet 258
Or}           Proprietary <Prtry> [1..1] Text 259
         PriceMethod <PricMtd> [0..1] CodeSet 259
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 225 May 2026
```

## File page 226

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         ValueInInvestmentCurrency <ValInInvstmtCcy> [1..*] ± 260
         ValueInAlternativeCurrency <ValInAltrntvCcy> [0..*] ± 260
         ForExecutionIndicator <ForExctnInd> [1..1] Indicator 260
         CumDividendIndicator <CumDvddInd> [1..1] Indicator 260
         CalculationBasis <ClctnBsis> [0..1] Rate 260
         EstimatedPriceIndicator <EstmtdPricInd> [1..1] Indicator 261
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 261
         TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C3 261
         TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  261
{Or           Code <Cd> [1..1] CodeSet 261
Or}           Proprietary <Prtry> [1..1] Text 262
         TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 262
         EUDividendStatus <EUDvddSts> [0..1]  262
{Or           Code <Cd> [1..1] CodeSet 262
Or}           Proprietary <Prtry> [1..1] Text 263
         ChargeDetails <ChrgDtls> [0..*]  263
           Type <Tp> [1..1]  263
{Or             Code <Cd> [1..1] CodeSet 263
Or}             Proprietary <Prtry> [1..1] Text 264
           ChargesFees <ChrgsFees> [1..1] ± 264
           CalculationBasis <ClctnBsis> [0..1]  264
{Or             Code <Cd> [1..1] CodeSet 265
Or}             Proprietary <Prtry> [1..1] Text 265
         TaxLiabilityDetails <TaxLbltyDtls> [0..*]  C4 265
           Type <Tp> [1..1]  266
{Or             Code <Cd> [1..1] CodeSet 266
Or}             Proprietary <Prtry> [1..1] Text 267
           Amount <Amt> [0..7] Amount C3 267
           Rate <Rate> [0..1] Rate 267
           Country <Ctry> [1..1] CodeSet C11 268
           TaxCalculationDetails <TaxClctnDtls> [0..1]  268
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 226 May 2026
```

## File page 227

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             EUCapitalGain <EUCptlGn> [0..1]  268
{Or               Code <Cd> [1..1] CodeSet 269
Or}               Proprietary <Prtry> [1..1] Text 269
             PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 269
             PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 269
             TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 269
             EUDividendStatus <EUDvddSts> [0..1]  270
{Or               Code <Cd> [1..1] CodeSet 270
Or}               Proprietary <Prtry> [1..1] Text 270
         TaxRefundDetails <TaxRfndDtls> [0..*]  C4 270
           Type <Tp> [1..1]  271
{Or             Code <Cd> [1..1] CodeSet 271
Or}             Proprietary <Prtry> [1..1] Text 272
           Amount <Amt> [0..7] Amount C3 272
           Rate <Rate> [0..1] Rate 272
           Country <Ctry> [1..1] CodeSet C11 273
           TaxCalculationDetails <TaxClctnDtls> [0..1]  273
             EUCapitalGain <EUCptlGn> [0..1]  273
{Or               Code <Cd> [1..1] CodeSet 274
Or}               Proprietary <Prtry> [1..1] Text 274
             PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 274
             PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 274
             TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 274
             EUDividendStatus <EUDvddSts> [0..1]  275
{Or               Code <Cd> [1..1] CodeSet 275
Or}               Proprietary <Prtry> [1..1] Text 275
       ValuationStatistics <ValtnSttstcs> [0..*]  C13,
C14,
C15
275
         Currency <Ccy> [1..1] CodeSet C3 277
         PriceTypeChangeBasis <PricTpChngBsis> [1..1]  C19 277
           Structured <Strd> [1..1] CodeSet 278
           AdditionalInformation <AddtlInf> [0..1] Text 279
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 227 May 2026
```

## File page 228

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         PriceChange <PricChng> [1..1]  C5, C6 279
           Amount <Amt> [0..1] Amount C3 280
           AmountSign <AmtSgn> [0..1] Indicator 280
           Rate <Rate> [0..1] Rate 280
         Yield <Yld> [0..1] Rate 280
         ByPredefinedTimePeriods <ByPrdfndTmPrds> [0..1]  280
           HighestPriceValue12Months <HghstPricVal12Mnths> [0..1]  281
             Amount <Amt> [1..1] Amount C3 281
           LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  282
             Amount <Amt> [1..1] Amount C3 282
           OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 282
             Amount <Amt> [0..1] Amount C3 283
             AmountSign <AmtSgn> [0..1] Indicator 283
             Rate <Rate> [0..1] Rate 283
           ThreeYearPriceChange <ThreeYrPricChng> [0..1]  C5, C6 283
             Amount <Amt> [0..1] Amount C3 284
             AmountSign <AmtSgn> [0..1] Indicator 284
             Rate <Rate> [0..1] Rate 284
           FiveYearPriceChange <FiveYrPricChng> [0..1]  C5, C6 284
             Amount <Amt> [0..1] Amount C3 285
             AmountSign <AmtSgn> [0..1] Indicator 285
             Rate <Rate> [0..1] Rate 285
         ByUserDefinedTimePeriod <ByUsrDfndTmPrd> [0..*]  286
           Period <Prd> [1..1]  286
{Or             Date <Dt> [1..1] ± 286
Or}             DateTime <DtTm> [1..1] ± 287
           HighestPriceValue <HghstPricVal> [0..1]  287
             Amount <Amt> [1..1] Amount C3 287
           LowestPriceValue <LwstPricVal> [0..1]  287
             Amount <Amt> [1..1] Amount C3 287
           PriceChange <PricChng> [0..1]  C5, C6 288
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 228 May 2026
```

