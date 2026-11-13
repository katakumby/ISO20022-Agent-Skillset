---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks"]
file_pages: [168, 169, 170, 171, 172, 173, 174, 175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C20"], "until_heading": "13.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 168, "topic": "13.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00111.md"}]
---

# 13.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 168 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 168, C20 before **13.4 Message Building Blocks** continue [13.3 Constraints](section-00111.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 168

```text
If SuspendedIndicator is "false" or "0" (No), and if FinancialInstrumentDetails /
DualFundIndicator is "true" or "1" (Yes), then PriceDetails must be present two or more times
and PriceDetails/Type must be present with the values "BIDE" and "OFFR".
C20 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
13.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
13.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
13.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference10" on page 4545
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
13.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 168 May 2026
```

## File page 169

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
13.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
13.4.5 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination1" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4817
   LastPageIndicator <LastPgInd> [1..1] Indicator 4817
13.4.6 PriceReportIdentification <PricRptId>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the price report, as assigned by the reporting party.
Datatype: "Max35Text" on page 5403
13.4.7 Function <Fctn>
Presence: [1..1]
Definition: Function of the price report, that is, whether the price report is a new price report or a
replacement of some kind.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 169 May 2026
```

## File page 170

```text
Datatype: "PriceReportFunction1Code" on page 5343
CodeName Name Definition
REPL CompleteReplacementPriceReport The price report conveys the correction
of the complete set of prices previously
sent for the same price report
identification.
NEWP NewPriceReport The price report is 'new', that is the
report is not being used as a correction
of previously sent prices.
PART PartialCorrectionPriceReport The price report conveys the correction
of some of the prices previously sent for
the same price report identification.
13.4.8 CancellationIdentification <CxlId>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the cancellation of the previous price report, as
assigned by the reporting party.
Datatype: "Max35Text" on page 5403
13.4.9 PriceValuationDetails <PricValtnDtls>
Presence: [1..*]
Definition: Information related to the price valuation of a financial instrument.
Impacted by: C19 "PriceDetailsRule"
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 170 May 2026
```

## File page 171

```text
PriceValuationDetails <PricValtnDtls> contains the following PriceValuation5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 176
   ValuationDateTime <ValtnDtTm> [0..1] ± 176
   NAVDateTime <NAVDtTm> [1..1] ± 176
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C15 176
     Identification <Id> [1..10]  178
{Or       ISIN <ISIN> [1..1] IdentifierSet 178
Or       SEDOL <SEDOL> [1..1] IdentifierSet 179
Or       CUSIP <CUSIP> [1..1] IdentifierSet 179
Or       RIC <RIC> [1..1] IdentifierSet 179
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 179
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 179
Or       CTA <CTA> [1..1] IdentifierSet 179
Or       QUICK <QUICK> [1..1] IdentifierSet 179
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 180
Or       Dutch <Dtch> [1..1] IdentifierSet 180
Or       Valoren <Vlrn> [1..1] IdentifierSet 180
Or       Sicovam <SCVM> [1..1] IdentifierSet 180
Or       Belgian <Belgn> [1..1] IdentifierSet 180
Or       Common <Cmon> [1..1] IdentifierSet 180
Or       DTI <DTI> [1..1] IdentifierSet 180
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  181
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
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 171 May 2026
```

## File page 172

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       Code <Cd> [1..1] CodeSet 189
Or}       Proprietary <Prtry> [1..1] Text 190
     PriceMethod <PricMtd> [0..1] CodeSet 190
     ValueInInvestmentCurrency <ValInInvstmtCcy> [1..*] ± 191
     ValueInAlternativeCurrency <ValInAltrntvCcy> [0..*] ± 191
     ForExecutionIndicator <ForExctnInd> [1..1] Indicator 191
     CumDividendIndicator <CumDvddInd> [1..1] Indicator 191
     CalculationBasis <ClctnBsis> [0..1] Rate 191
     EstimatedPriceIndicator <EstmtdPricInd> [1..1] Indicator 192
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 192
     TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C3 192
     TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  192
{Or       Code <Cd> [1..1] CodeSet 193
Or}       Proprietary <Prtry> [1..1] Text 193
     TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 193
     EUDividendStatus <EUDvddSts> [0..1]  193
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 172 May 2026
```

## File page 173

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 194
Or}       Proprietary <Prtry> [1..1] Text 194
     ChargeDetails <ChrgDtls> [0..*]  194
       Type <Tp> [1..1]  194
{Or         Code <Cd> [1..1] CodeSet 195
Or}         Proprietary <Prtry> [1..1] Text 195
       ChargesFees <ChrgsFees> [1..1] ± 195
       CalculationBasis <ClctnBsis> [0..1]  196
{Or         Code <Cd> [1..1] CodeSet 196
Or}         Proprietary <Prtry> [1..1] Text 196
     TaxLiabilityDetails <TaxLbltyDtls> [0..*]  C4 196
       Type <Tp> [1..1]  197
{Or         Code <Cd> [1..1] CodeSet 197
Or}         Proprietary <Prtry> [1..1] Text 198
       Amount <Amt> [0..7] Amount C3 198
       Rate <Rate> [0..1] Rate 198
       Country <Ctry> [1..1] CodeSet C9 199
       TaxCalculationDetails <TaxClctnDtls> [0..1]  199
         EUCapitalGain <EUCptlGn> [0..1]  199
{Or           Code <Cd> [1..1] CodeSet 200
Or}           Proprietary <Prtry> [1..1] Text 200
         PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 200
         PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 200
         TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 200
         EUDividendStatus <EUDvddSts> [0..1]  201
{Or           Code <Cd> [1..1] CodeSet 201
Or}           Proprietary <Prtry> [1..1] Text 201
     TaxRefundDetails <TaxRfndDtls> [0..*]  C4 201
       Type <Tp> [1..1]  202
{Or         Code <Cd> [1..1] CodeSet 202
Or}         Proprietary <Prtry> [1..1] Text 203
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 173 May 2026
```

## File page 174

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Amount <Amt> [0..7] Amount C3 203
       Rate <Rate> [0..1] Rate 203
       Country <Ctry> [1..1] CodeSet C9 204
       TaxCalculationDetails <TaxClctnDtls> [0..1]  204
         EUCapitalGain <EUCptlGn> [0..1]  204
{Or           Code <Cd> [1..1] CodeSet 205
Or}           Proprietary <Prtry> [1..1] Text 205
         PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 205
         PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 205
         TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 205
         EUDividendStatus <EUDvddSts> [0..1]  206
{Or           Code <Cd> [1..1] CodeSet 206
Or}           Proprietary <Prtry> [1..1] Text 206
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
       AmountSign <AmtSgn> [0..1] Indicator 211
       Rate <Rate> [0..1] Rate 211
     Yield <Yld> [0..1] Rate 211
     ByPredefinedTimePeriods <ByPrdfndTmPrds> [0..1]  211
       HighestPriceValue12Months
<HghstPricVal12Mnths>
[0..1]  212
         Amount <Amt> [1..1] Amount C3 212
       LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  213
         Amount <Amt> [1..1] Amount C3 213
       OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 213
         Amount <Amt> [0..1] Amount C3 214
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 174 May 2026
```

## File page 175

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Date <Dt> [1..1] ± 217
Or}         DateTime <DtTm> [1..1] ± 218
       HighestPriceValue <HghstPricVal> [0..1]  218
         Amount <Amt> [1..1] Amount C3 218
       LowestPriceValue <LwstPricVal> [0..1]  218
         Amount <Amt> [1..1] Amount C3 218
       PriceChange <PricChng> [0..1]  C5, C6 219
         Amount <Amt> [0..1] Amount C3 219
         AmountSign <AmtSgn> [0..1] Indicator 220
         Rate <Rate> [0..1] Rate 220
       Yield <Yld> [0..1] Rate 220
   PerformanceDetails <PrfrmncDtls> [0..1]  C1 220
     CorporateActionFactor <CorpActnFctr> [0..1] Quantity 220
     CumulativeCorporateActionFactor
<CmltvCorpActnFctr>
[0..1] Quantity 221
     AccumulationPeriod <AcmltnPrd> [0..1] ± 221
     NormalPerformance <NrmlPrfrmnc> [0..1] Quantity 221
Constraints
• PriceDetailsRule
If SuspendedIndicator is "true" or "1" (Yes), then PriceDetails is optional.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 175 May 2026
```

