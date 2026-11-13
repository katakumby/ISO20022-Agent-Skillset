---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.36 AdditionalInformation <AddtlInf>", "3.4.10.36.3 URLAddress <URLAdr>", "3.4.10.36.3.1 Language <Lang>"]
file_pages: [129, 130, 131, 132, 133, 134, 135, 136, 137, 138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.36.3.1 Language <Lang>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 129 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
3.4.10.36.3.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.10.36.3.2  URLAddress <URLAdr>
Presence: [1..1]
Definition: Provides the web address, that is, the address for the Universal Resource Locator (URL), to
use over the www (HTTP) service where additional information may be found.
Datatype: "Max2048Text" on page 1249
3.4.10.36.4  EventProcessingWebSiteAddress <EvtPrcgWebSiteAdr>
Presence: [0..1]
Definition: Provides web address of an account servicer (or of a service provider) that contains
information solely intended for the immediate account holder to enable or facilitate event processing
between parties.
Datatype: "Max2048Text" on page 1249
3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>
Presence: [0..*]
Definition: Information about the corporate action option.
Impacted by: C8 "AdditionalTextRule", C12 "AppliedOptionRule", C55 "InstructCashAmountRule", C89
"OptionTypeUnknownProceedsUsageRule", C98 "RevocabilityPeriodRule", C88
"OptionNumberGuideline"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 129 February 2026
```

## File page 130

```text
CorporateActionOptionDetails <CorpActnOptnDtls> contains the following
CorporateActionOption251 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] Text 140
   OptionType <OptnTp> [1..1] ± 140
   FractionDisposition <FrctnDspstn> [0..1] ± 140
   OptionFeatures <OptnFeatrs> [0..*]  141
{Or     Code <Cd> [1..1] CodeSet 141
Or}     Proprietary <Prtry> [1..1] ± 142
   OptionAvailabilityStatus <OptnAvlbtySts> [0..1] ± 142
   CertificationBreakdownType <CertfctnBrkdwnTp> [0..*] ± 142
   BidRangeType <BidRgTp> [0..1] ± 143
   ProrationBelowMinimumQuantity <PrratnBlwMinQty> [0..1]  143
{Or     Code <Cd> [1..1] CodeSet 143
Or}     Proprietary <Prtry> [1..1] ± 144
   NonDomicileCountry <NonDmclCtry> [0..*] CodeSet C17 144
   ValidDomicileCountry <VldDmclCtry> [0..*] CodeSet C17 144
   CurrencyOption <CcyOptn> [0..1] CodeSet C2 145
   DefaultProcessingOrStandingInstruction
<DfltPrcgOrStgInstr>
[1..1] ± 145
   ChargesAppliedIndicator <ChrgsApldInd> [0..1] Indicator 145
   CertificationBreakdownIndicator <CertfctnBrkdwnInd> [0..1] Indicator 145
   WithdrawalAllowedIndicator <WdrwlAllwdInd> [0..1] Indicator 146
   ChangeAllowedIndicator <ChngAllwdInd> [0..1] Indicator 146
   AppliedOptionIndicator <ApldOptnInd> [0..1] Indicator 146
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C23,
C24,
C61,
C62,
C91
146
   DateDetails <DtDtls> [0..1]  147
     EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 148
     CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 148
     ProtectDeadline <PrtctDdln> [0..1] ± 149
     MarketDeadline <MktDdln> [0..1] ± 149
     ResponseDeadline <RspnDdln> [0..1] ± 149
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 130 February 2026
```

## File page 131

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ExpiryDate <XpryDt> [0..1] ± 150
     SubscriptionCostDebitDate <SbcptCostDbtDt> [0..1] ± 150
     DepositoryCoverExpirationDate
<DpstryCoverXprtnDt>
[0..1] ± 151
     StockLendingDeadline <StockLndgDdln> [0..1] ± 151
     BorrowerStockLendingDeadline
<BrrwrStockLndgDdln>
[0..*]  151
       StockLendingDeadline <StockLndgDdln> [1..1] ± 151
       Borrower <Brrwr> [1..1] ± 152
     EndOfSecuritiesBlockingPeriod
<EndOfSctiesBlckgPrd>
[0..1] ± 152
     DocumentationDeadline <DcmnttnDdln> [0..1] ± 152
   PeriodDetails <PrdDtls> [0..1]  153
     PriceCalculationPeriod <PricClctnPrd> [0..1] ± 153
     ParallelTradingPeriod <ParllTradgPrd> [0..1] ± 153
     ActionPeriod <ActnPrd> [0..1] ± 154
     RevocabilityPeriod <RvcbltyPrd> [0..1] ± 154
     PrivilegeSuspensionPeriod <PrvlgSspnsnPrd> [0..1] ± 154
     AccountServicerRevocabilityPeriod
<AcctSvcrRvcbltyPrd>
[0..1] ± 154
     DepositorySuspensionPeriodForWithdrawal
<DpstrySspnsnPrdForWdrwl>
[0..1] ± 155
   RateAndAmountDetails <RateAndAmtDtls> [0..1]  C43,
C45,
C78,
C80,
C105,
C107,
C109,
C114,
C116
155
     AdditionalTax <AddtlTax> [0..1] ± 157
     GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 157
     NetDistributionRate <NetDstrbtnRate> [0..*] ± 158
     GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 159
     MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] ± 160
     ProrationRate <PrratnRate> [0..1] ± 160
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 161
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 131 February 2026
```

## File page 132

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SecondLevelTax <ScndLvlTax> [0..*] ± 161
     TaxableIncomePerDividendShare
<TaxblIncmPerDvddShr>
[0..*] ± 161
     IssuerDeclaredExchangeRate <IssrDclrdXchgRate> [0..1] ± 162
     TaxOnIncome <TaxOnIncm> [0..1] ± 162
     BidInterval <BidIntrvl> [0..1] ± 162
   PriceDetails <PricDtls> [0..1]  163
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 163
     OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 164
     MaximumCashToInstruct <MaxCshToInst> [0..1] ± 164
     MinimumCashToInstruct <MinCshToInst> [0..1] ± 164
     MinimumMultipleCashToInstruct
<MinMltplCshToInst>
[0..1] ± 165
     MaximumPrice <MaxPric> [0..1] ± 165
     MinimumPrice <MinPric> [0..1] ± 165
     FirstBidIncrementPrice <FrstBidIncrmtPric> [0..1] ± 166
     LastBidIncrementPrice <LastBidIncrmtPric> [0..1] ± 166
   SecuritiesQuantity <SctiesQty> [0..1]  167
     MaximumQuantityToInstruct <MaxQtyToInst> [0..1] ± C26 167
     MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C26 168
     MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C27 168
     NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C27 169
     NewDenominationQuantity <NewDnmtnQty> [0..1] ± C27 169
     FrontEndOddLotQuantity <FrntEndOddLotQty> [0..1] ± C27 170
     BackEndOddLotQuantity <BckEndOddLotQty> [0..1] ± C27 170
   SecuritiesMovementDetails <SctiesMvmntDtls> [0..*]  C34,
C50,
C52,
C64
171
     SecurityDetails <SctyDtls> [1..1]  C71,
C95
174
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C23,
C24,
C61,
C62,
C91
176
       PlaceOfListing <PlcOfListg> [0..1] ± 177
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 132 February 2026
```

## File page 133

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DayCountBasis <DayCntBsis> [0..1] ± 177
       ClassificationType <ClssfctnTp> [0..1] ± 177
       OptionStyle <OptnStyle> [0..1] ± 178
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 178
       NextCouponDate <NxtCpnDt> [0..1] Date 178
       FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 178
       MaturityDate <MtrtyDt> [0..1] Date 178
       IssueDate <IsseDt> [0..1] Date 178
       NextCallableDate <NxtCllblDt> [0..1] Date 179
       PutableDate <PutblDt> [0..1] Date 179
       DatedDate <DtdDt> [0..1] Date 179
       ConversionDate <ConvsDt> [0..1] Date 179
       PreviousFactor <PrvsFctr> [0..1] ± 179
       NextFactor <NxtFctr> [0..1] ± 179
       InterestRate <IntrstRate> [0..1] ± 180
       NextInterestRate <NxtIntrstRate> [0..1] ± 180
       MinimumNominalQuantity <MinNmnlQty> [0..1] ± C25 180
       MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C25 181
       MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C25 181
       ContractSize <CtrctSz> [0..1] ± C25 182
       IssuePrice <IssePric> [0..1] ± 182
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 183
     TemporaryFinancialInstrumentIndicator
<TempFinInstrmInd>
[0..1] ± 183
     NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1]  183
{Or       Code <Cd> [1..1] CodeSet 184
Or}       Proprietary <Prtry> [1..1] ± 184
     IssuerOfferorTaxabilityIndicator
<IssrOfferrTaxbltyInd>
[0..1]  184
{Or       Code <Cd> [1..1] CodeSet 184
Or}       Proprietary <Prtry> [1..1] ± 185
     NewSecuritiesIssuanceIndicator
<NewSctiesIssncInd>
[0..1] CodeSet 185
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 133 February 2026
```

## File page 134

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IncomeType <IncmTp> [0..1] ± 185
     OtherIncomeType <OthrIncmTp> [0..*] ± 186
     ExemptionType <XmptnTp> [0..*] ± 186
     EntitledQuantity <EntitldQty> [0..1] ± 186
     SafekeepingPlace <SfkpgPlc> [0..1] ± 187
     CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C17 187
     FractionDisposition <FrctnDspstn> [0..1] ± 187
     CurrencyOption <CcyOptn> [0..1] CodeSet C2 188
     TradingPeriod <TradgPrd> [0..1] ± 188
     DateDetails <DtDtls> [1..1]  188
       PaymentDate <PmtDt> [1..1] ± 189
       AvailableDate <AvlblDt> [0..1] ± 189
       DividendRankingDate <DvddRnkgDt> [0..1] ± 189
       EarliestPaymentDate <EarlstPmtDt> [0..1] ± 190
       PariPassuDate <PrpssDt> [0..1] ± 190
       LastTradingDate <LastTradgDt> [0..1] ± 190
     RateDetails <RateDtls> [0..1]  191
       AdditionalQuantityForSubscribedResultantSecuriti
es <AddtlQtyForSbcbdRsltntScties>
[0..1] ± 191
       AdditionalQuantityForExistingSecurities
<AddtlQtyForExstgScties>
[0..1] ± 192
       NewToOld <NewToOd> [0..1] ± 192
       TransformationRate <TrfrmatnRate> [0..1] Rate 193
       ChargesFees <ChrgsFees> [0..1] ± 193
       FiscalStamp <FsclStmp> [0..1] ± 193
       ApplicableRate <AplblRate> [0..1] ± 194
       TaxCreditRate <TaxCdtRate> [0..1] ± 194
       FinancialTransactionTaxRate <FinTxTaxRate> [0..1] ± 194
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 194
       SecondLevelTax <ScndLvlTax> [0..*] ± 195
     PriceDetails <PricDtls> [0..1]  C40 195
       IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  196
{Or         IndicativePrice <IndctvPric> [1..1] ± 196
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 134 February 2026
```

## File page 135

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         MarketPrice <MktPric> [1..1] ± 197
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 197
       CashValueForTax <CshValForTax> [0..1] ± 197
       GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 198
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 198
     AmountDetails <AmtDtls> [0..1]  199
       WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 199
       SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 200
   CashMovementDetails <CshMvmntDtls> [0..*]  C35,
C51,
C53,
C65,
C41
200
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 204
     ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 205
     NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1]  205
{Or       Code <Cd> [1..1] CodeSet 205
Or}       Proprietary <Prtry> [1..1] ± 205
     IssuerOfferorTaxabilityIndicator
<IssrOfferrTaxbltyInd>
[0..1]  206
{Or       Code <Cd> [1..1] CodeSet 206
Or}       Proprietary <Prtry> [1..1] ± 206
     IncomeType <IncmTp> [0..1] ± 206
     OtherIncomeType <OthrIncmTp> [0..*] ± 207
     ExemptionType <XmptnTp> [0..*] ± 207
     PriceCalculationMethod <PricClctnMtd> [0..1]  207
{Or       Code <Cd> [1..1] CodeSet 208
Or}       Proprietary <Prtry> [1..1] ± 208
     CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C17 208
     CashAccountIdentification <CshAcctId> [0..1] ± 209
     AmountDetails <AmtDtls> [0..1]  209
       GrossAmount <GrssAmt> [0..1] Amount C2, C18 211
       NetAmount <NetAmt> [0..1] Amount C2, C18 212
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 135 February 2026
```

## File page 136

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SolicitationFees <SlctnFees> [0..1] Amount C2, C18 212
       CashInLieuOfShare <CshInLieuOfShr> [0..1] Amount C2, C18 212
       CapitalGain <CptlGn> [0..1] Amount C2, C18 213
       InterestAmount <IntrstAmt> [0..1] Amount C2, C18 213
       IndemnityAmount <IndmntyAmt> [0..1] Amount C2, C18 214
       ManufacturedDividendPaymentAmount
<ManfctrdDvddPmtAmt>
[0..1] Amount C2, C18 214
       ReinvestmentAmount <RinvstmtAmt> [0..1] Amount C2, C18 215
       FullyFrankedAmount <FullyFrnkdAmt> [0..1] Amount C2, C18 215
       UnfrankedAmount <UfrnkdAmt> [0..1] Amount C2, C18 215
       SundryOrOtherAmount <SndryOrOthrAmt> [0..1] Amount C2, C18 216
       TaxFreeAmount <TaxFreeAmt> [0..1] Amount C2, C18 216
       TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C2, C18 217
       ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C2, C18 217
       StampDutyAmount <StmpDtyAmt> [0..1] Amount C2, C18 217
       TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C2, C18 218
       TaxCreditAmount <TaxCdtAmt> [0..1] Amount C2, C18 218
       AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C2, C18 219
       WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 219
       SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 219
       FiscalStampAmount <FsclStmpAmt> [0..1] Amount C2, C18 220
       ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C2, C18 220
       PayingAgentCommissionAmount
<PngAgtComssnAmt>
[0..1] Amount C2, C18 221
       LocalBrokerCommissionAmount
<LclBrkrComssnAmt>
[0..1] Amount C2, C18 221
       RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C2, C18 221
       ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C2, C18 222
       ChargesAmount <ChrgsAmt> [0..1] Amount C2, C18 222
       EntitledAmount <EntitldAmt> [0..1] Amount C2, C18 223
       OriginalAmount <OrgnlAmt> [0..1] Amount C2, C18 223
       PrincipalOrCorpus <PrncplOrCrps> [0..1] Amount C2, C18 223
       RedemptionPremiumAmount <RedPrmAmt> [0..1] Amount C2, C18 224
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 136 February 2026
```

## File page 137

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IncomePortion <IncmPrtn> [0..1] Amount C2, C18 224
       StockExchangeTax <StockXchgTax> [0..1] Amount C2, C18 225
       EUTaxRetentionAmount <EUTaxRtntnAmt> [0..1] Amount C2, C18 225
       AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C18 225
       EqualisationAmount <EqulstnAmt> [0..1] Amount C2, C18 226
       FATCATaxAmount <FATCATaxAmt> [0..1] Amount C2, C18 226
       NRATaxAmount <NRATaxAmt> [0..1] Amount C2, C18 227
       BackUpWithholdingTaxAmount
<BckUpWhldgTaxAmt>
[0..1] Amount C2, C18 227
       TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C2, C18 227
       TransactionTax <TxTax> [0..1] Amount C2, C18 228
       DeemedAmount <DmdAmt> [0..1] Amount C2, C18 228
       ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C2, C18 229
       DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C2, C18 229
       DeemedFundAmount <DmdFndAmt> [0..1] Amount C2, C18 229
       DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C2, C18 230
       DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C2, C18 230
       BuyUpAmount <BuyUpAmt> [0..1] Amount C2, C18 231
     DateDetails <DtDtls> [1..1]  231
       PaymentDate <PmtDt> [1..1] ± 231
       ValueDate <ValDt> [0..1] ± 232
       ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 232
       EarliestPaymentDate <EarlstPmtDt> [0..1] ± 232
     ForeignExchangeDetails <FXDtls> [0..1] ± 233
     RateAndAmountDetails <RateAndAmtDtls> [0..1]  C21,
C22,
C44,
C46,
C79,
C81,
C106,
C108,
C110,
C115,
C117
233
       AdditionalTax <AddtlTax> [0..1] ± 236
       GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 236
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 137 February 2026
```

## File page 138

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 236
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 237
       SecondLevelTax <ScndLvlTax> [0..*] ± 237
       ChargesFees <ChrgsFees> [0..1] ± 238
       EarlySolicitationFeeRate <EarlySlctnFeeRate> [0..1] ± 238
       FiscalStamp <FsclStmp> [0..1] ± 239
       ThirdPartyIncentiveRate <ThrdPtyIncntivRate> [0..1] ± 239
       NetDistributionRate <NetDstrbtnRate> [0..*] ± 239
       ApplicableRate <AplblRate> [0..1] ± 240
       SolicitationFeeRate <SlctnFeeRate> [0..1] ± 240
       TaxCreditRate <TaxCdtRate> [0..1] ± 241
       TaxOnIncome <TaxOnIncm> [0..1] ± 241
       TaxOnProfits <TaxOnPrfts> [0..1] ± 241
       TaxReclaimRate <TaxRclmRate> [0..1] ± 242
       EqualisationRate <EqulstnRate> [0..1] ± 242
       DeemedRate <DmdRate> [0..*] ± 242
     PriceDetails <PricDtls> [0..1]  C42 243
       GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 244
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 244
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 245
   AdditionalInformation <AddtlInf> [0..1]  C5 245
     AdditionalText <AddtlTxt> [0..*]  246
       Language <Lang> [1..1] CodeSet 247
       AdditionalInformation <AddtlInf> [1..1] Text 247
     NarrativeVersion <NrrtvVrsn> [0..*]  247
       Language <Lang> [1..1] CodeSet 247
       AdditionalInformation <AddtlInf> [1..1] Text 247
     InformationConditions <InfConds> [0..*]  248
       Language <Lang> [1..1] CodeSet 248
       AdditionalInformation <AddtlInf> [1..*] Text 248
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 138 February 2026
```

