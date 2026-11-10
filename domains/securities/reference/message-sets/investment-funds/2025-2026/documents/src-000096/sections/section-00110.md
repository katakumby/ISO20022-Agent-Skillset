---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.2 Structure"]
file_pages: [161, 162, 163, 164, 165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 161 to 165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
13.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PricRpt> [1..1]  C16
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 168
   PreviousReference <PrvsRef> [0..*] ± 168
   RelatedReference <RltdRef> [0..1] ± 0
   MessagePagination <MsgPgntn> [1..1] ± 0
   PriceReportIdentification <PricRptId> [1..1] Text 0
   Function <Fctn> [1..1] CodeSet 0
   CancellationIdentification <CxlId> [0..1] Text 0
   PriceValuationDetails <PricValtnDtls> [1..*]  C19 0
     Identification <Id> [0..1] Text 176
     ValuationDateTime <ValtnDtTm> [0..1] ± 176
     NAVDateTime <NAVDtTm> [1..1] ± 176
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C15 176
       Identification <Id> [1..10]  178
{Or         ISIN <ISIN> [1..1] IdentifierSet 178
Or         SEDOL <SEDOL> [1..1] IdentifierSet 179
Or         CUSIP <CUSIP> [1..1] IdentifierSet 179
Or         RIC <RIC> [1..1] IdentifierSet 179
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 179
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 179
Or         CTA <CTA> [1..1] IdentifierSet 179
Or         QUICK <QUICK> [1..1] IdentifierSet 179
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 180
Or         Dutch <Dtch> [1..1] IdentifierSet 180
Or         Valoren <Vlrn> [1..1] IdentifierSet 180
Or         Sicovam <SCVM> [1..1] IdentifierSet 180
Or         Belgian <Belgn> [1..1] IdentifierSet 180
Or         Common <Cmon> [1..1] IdentifierSet 180
Or         DTI <DTI> [1..1] IdentifierSet 180
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 161 May 2026
```

## File page 162

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  181
           Identification <Id> [1..1] Text 181
           IdentificationSource <IdSrc> [1..1] ± 181
       Name <Nm> [0..1] Text 181
       ShortName <ShrtNm> [0..1] Text 181
       SupplementaryIdentification <SplmtryId> [0..1] Text 181
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 182
       ClassType <ClssTp> [0..1] Text 182
       SecuritiesForm <SctiesForm> [0..1] CodeSet 182
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 182
       DualFundIndicator <DualFndInd> [1..1] Indicator 183
       ProductGroup <PdctGrp> [0..1] Text 183
       SeriesIdentification <SrsId> [0..1]  C20 183
         SeriesDate <SrsDt> [0..1] ± 183
         SeriesName <SrsNm> [0..1] Text 183
     FundManagementCompany <FndMgmtCpny> [0..1] ± 184
     TotalNAV <TtlNAV> [0..*] Amount C3, C10 184
     TotalUnitsNumber <TtlUnitsNb> [0..1] ± 184
     NextValuationDateTime <NxtValtnDtTm> [0..1] ± 185
     PreviousValuationDateTime <PrvsValtnDtTm> [0..1] ± 185
     ValuationType <ValtnTp> [1..1] CodeSet 185
     ValuationFrequency <ValtnFrqcy> [0..1] CodeSet 185
     OfficialValuationIndicator <OffclValtnInd> [1..1] Indicator 186
     SuspendedIndicator <SspdInd> [1..1] Indicator 186
     PriceDetails <PricDtls> [0..*]  C8 186
       PriceType <PricTp> [1..1]  C17 189
{Or         Code <Cd> [1..1] CodeSet 189
Or}         Proprietary <Prtry> [1..1] Text 190
       PriceMethod <PricMtd> [0..1] CodeSet 190
       ValueInInvestmentCurrency <ValInInvstmtCcy> [1..*] ± 191
       ValueInAlternativeCurrency <ValInAltrntvCcy> [0..*] ± 191
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 162 May 2026
```

## File page 163

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ForExecutionIndicator <ForExctnInd> [1..1] Indicator 191
       CumDividendIndicator <CumDvddInd> [1..1] Indicator 191
       CalculationBasis <ClctnBsis> [0..1] Rate 191
       EstimatedPriceIndicator <EstmtdPricInd> [1..1] Indicator 192
       NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 192
       TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C3 192
       TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> [0..1]  192
{Or         Code <Cd> [1..1] CodeSet 193
Or}         Proprietary <Prtry> [1..1] Text 193
       TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 193
       EUDividendStatus <EUDvddSts> [0..1]  193
{Or         Code <Cd> [1..1] CodeSet 194
Or}         Proprietary <Prtry> [1..1] Text 194
       ChargeDetails <ChrgDtls> [0..*]  194
         Type <Tp> [1..1]  194
{Or           Code <Cd> [1..1] CodeSet 195
Or}           Proprietary <Prtry> [1..1] Text 195
         ChargesFees <ChrgsFees> [1..1] ± 195
         CalculationBasis <ClctnBsis> [0..1]  196
{Or           Code <Cd> [1..1] CodeSet 196
Or}           Proprietary <Prtry> [1..1] Text 196
       TaxLiabilityDetails <TaxLbltyDtls> [0..*]  C4 196
         Type <Tp> [1..1]  197
{Or           Code <Cd> [1..1] CodeSet 197
Or}           Proprietary <Prtry> [1..1] Text 198
         Amount <Amt> [0..7] Amount C3 198
         Rate <Rate> [0..1] Rate 198
         Country <Ctry> [1..1] CodeSet C9 199
         TaxCalculationDetails <TaxClctnDtls> [0..1]  199
           EUCapitalGain <EUCptlGn> [0..1]  199
{Or             Code <Cd> [1..1] CodeSet 200
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 163 May 2026
```

## File page 164

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] Text 200
           PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 200
           PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 200
           TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 200
           EUDividendStatus <EUDvddSts> [0..1]  201
{Or             Code <Cd> [1..1] CodeSet 201
Or}             Proprietary <Prtry> [1..1] Text 201
       TaxRefundDetails <TaxRfndDtls> [0..*]  C4 201
         Type <Tp> [1..1]  202
{Or           Code <Cd> [1..1] CodeSet 202
Or}           Proprietary <Prtry> [1..1] Text 203
         Amount <Amt> [0..7] Amount C3 203
         Rate <Rate> [0..1] Rate 203
         Country <Ctry> [1..1] CodeSet C9 204
         TaxCalculationDetails <TaxClctnDtls> [0..1]  204
           EUCapitalGain <EUCptlGn> [0..1]  204
{Or             Code <Cd> [1..1] CodeSet 205
Or}             Proprietary <Prtry> [1..1] Text 205
           PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 205
           PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 205
           TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 205
           EUDividendStatus <EUDvddSts> [0..1]  206
{Or             Code <Cd> [1..1] CodeSet 206
Or}             Proprietary <Prtry> [1..1] Text 206
     ValuationStatistics <ValtnSttstcs> [0..*]  C11,
C12,
C13
206
       Currency <Ccy> [1..1] CodeSet C3 208
       PriceTypeChangeBasis <PricTpChngBsis> [1..1]  C18 208
         Structured <Strd> [1..1] CodeSet 209
         AdditionalInformation <AddtlInf> [0..1] Text 210
       PriceChange <PricChng> [1..1]  C5, C6 210
         Amount <Amt> [0..1] Amount C3 211
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 164 May 2026
```

## File page 165

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         AmountSign <AmtSgn> [0..1] Indicator 211
         Rate <Rate> [0..1] Rate 211
       Yield <Yld> [0..1] Rate 211
       ByPredefinedTimePeriods <ByPrdfndTmPrds> [0..1]  211
         HighestPriceValue12Months <HghstPricVal12Mnths> [0..1]  212
           Amount <Amt> [1..1] Amount C3 212
         LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  213
           Amount <Amt> [1..1] Amount C3 213
         OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 213
           Amount <Amt> [0..1] Amount C3 214
           AmountSign <AmtSgn> [0..1] Indicator 214
           Rate <Rate> [0..1] Rate 214
         ThreeYearPriceChange <ThreeYrPricChng> [0..1]  C5, C6 214
           Amount <Amt> [0..1] Amount C3 215
           AmountSign <AmtSgn> [0..1] Indicator 215
           Rate <Rate> [0..1] Rate 215
         FiveYearPriceChange <FiveYrPricChng> [0..1]  C5, C6 215
           Amount <Amt> [0..1] Amount C3 216
           AmountSign <AmtSgn> [0..1] Indicator 216
           Rate <Rate> [0..1] Rate 216
       ByUserDefinedTimePeriod <ByUsrDfndTmPrd> [0..*]  217
         Period <Prd> [1..1]  217
{Or           Date <Dt> [1..1] ± 217
Or}           DateTime <DtTm> [1..1] ± 218
         HighestPriceValue <HghstPricVal> [0..1]  218
           Amount <Amt> [1..1] Amount C3 218
         LowestPriceValue <LwstPricVal> [0..1]  218
           Amount <Amt> [1..1] Amount C3 218
         PriceChange <PricChng> [0..1]  C5, C6 219
           Amount <Amt> [0..1] Amount C3 219
           AmountSign <AmtSgn> [0..1] Indicator 220
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 165 May 2026
```

