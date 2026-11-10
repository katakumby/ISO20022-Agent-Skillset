---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: []
file_pages: [36, 37, 38, 39, 40, 41, 42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# Continuation at file page 36

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 36 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         NextInterestRate <NxtIntrstRate> [0..1] ± 180
         MinimumNominalQuantity <MinNmnlQty> [0..1] ± C25 180
         MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C25 181
         MinimumMultipleQuantityToInstruct <MinMltplQtyToInst> [0..1] ± C25 181
         ContractSize <CtrctSz> [0..1] ± C25 182
         IssuePrice <IssePric> [0..1] ± 182
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 183
       TemporaryFinancialInstrumentIndicator
<TempFinInstrmInd>
[0..1] ± 183
       NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1]  183
{Or         Code <Cd> [1..1] CodeSet 184
Or}         Proprietary <Prtry> [1..1] ± 184
       IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  184
{Or         Code <Cd> [1..1] CodeSet 184
Or}         Proprietary <Prtry> [1..1] ± 185
       NewSecuritiesIssuanceIndicator <NewSctiesIssncInd> [0..1] CodeSet 185
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 36 February 2026
```

## File page 37

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       RateDetails <RateDtls> [0..1]  191
         AdditionalQuantityForSubscribedResultantSecurities
<AddtlQtyForSbcbdRsltntScties>
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
{Or           IndicativePrice <IndctvPric> [1..1] ± 196
Or}           MarketPrice <MktPric> [1..1] ± 197
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
{Or         Code <Cd> [1..1] CodeSet 205
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 37 February 2026
```

## File page 38

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 205
       IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  206
{Or         Code <Cd> [1..1] CodeSet 206
Or}         Proprietary <Prtry> [1..1] ± 206
       IncomeType <IncmTp> [0..1] ± 206
       OtherIncomeType <OthrIncmTp> [0..*] ± 207
       ExemptionType <XmptnTp> [0..*] ± 207
       PriceCalculationMethod <PricClctnMtd> [0..1]  207
{Or         Code <Cd> [1..1] CodeSet 208
Or}         Proprietary <Prtry> [1..1] ± 208
       CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C17 208
       CashAccountIdentification <CshAcctId> [0..1] ± 209
       AmountDetails <AmtDtls> [0..1]  209
         GrossAmount <GrssAmt> [0..1] Amount C2, C18 211
         NetAmount <NetAmt> [0..1] Amount C2, C18 212
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 38 February 2026
```

## File page 39

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C2, C18 219
         WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 219
         SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 219
         FiscalStampAmount <FsclStmpAmt> [0..1] Amount C2, C18 220
         ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C2, C18 220
         PayingAgentCommissionAmount <PngAgtComssnAmt> [0..1] Amount C2, C18 221
         LocalBrokerCommissionAmount <LclBrkrComssnAmt> [0..1] Amount C2, C18 221
         RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C2, C18 221
         ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C2, C18 222
         ChargesAmount <ChrgsAmt> [0..1] Amount C2, C18 222
         EntitledAmount <EntitldAmt> [0..1] Amount C2, C18 223
         OriginalAmount <OrgnlAmt> [0..1] Amount C2, C18 223
         PrincipalOrCorpus <PrncplOrCrps> [0..1] Amount C2, C18 223
         RedemptionPremiumAmount <RedPrmAmt> [0..1] Amount C2, C18 224
         IncomePortion <IncmPrtn> [0..1] Amount C2, C18 224
         StockExchangeTax <StockXchgTax> [0..1] Amount C2, C18 225
         EUTaxRetentionAmount <EUTaxRtntnAmt> [0..1] Amount C2, C18 225
         AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C18 225
         EqualisationAmount <EqulstnAmt> [0..1] Amount C2, C18 226
         FATCATaxAmount <FATCATaxAmt> [0..1] Amount C2, C18 226
         NRATaxAmount <NRATaxAmt> [0..1] Amount C2, C18 227
         BackUpWithholdingTaxAmount <BckUpWhldgTaxAmt> [0..1] Amount C2, C18 227
         TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C2, C18 227
         TransactionTax <TxTax> [0..1] Amount C2, C18 228
         DeemedAmount <DmdAmt> [0..1] Amount C2, C18 228
         ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C2, C18 229
         DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C2, C18 229
         DeemedFundAmount <DmdFndAmt> [0..1] Amount C2, C18 229
         DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C2, C18 230
         DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C2, C18 230
         BuyUpAmount <BuyUpAmt> [0..1] Amount C2, C18 231
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 39 February 2026
```

## File page 40

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 40 February 2026
```

## File page 41

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
       InformationToComplyWith <InfToCmplyWth> [0..*]  248
         Language <Lang> [1..1] CodeSet 248
         AdditionalInformation <AddtlInf> [1..*] Text 248
       SecurityRestriction <SctyRstrctn> [0..*]  249
         Language <Lang> [1..1] CodeSet 249
         AdditionalInformation <AddtlInf> [1..*] Text 249
       TaxationConditions <TaxtnConds> [0..*]  249
         Language <Lang> [1..1] CodeSet 249
         AdditionalInformation <AddtlInf> [1..*] Text 250
       Disclaimer <Dsclmr> [0..*]  250
         Language <Lang> [1..1] CodeSet 250
         AdditionalInformation <AddtlInf> [1..*] Text 250
       CertificationBreakdown <CertfctnBrkdwn> [0..*]  250
         Language <Lang> [1..1] CodeSet 250
         AdditionalInformation <AddtlInf> [1..*] Text 251
   AdditionalInformation <AddtlInf> [0..1]  C6 0
     AdditionalText <AddtlTxt> [0..*]  C7 253
       Language <Lang> [1..1] CodeSet 253
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 41 February 2026
```

## File page 42

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalInformation <AddtlInf> [1..*] Text 253
     NarrativeVersion <NrrtvVrsn> [0..*]  C7 254
       Language <Lang> [1..1] CodeSet 254
       AdditionalInformation <AddtlInf> [1..*] Text 254
     InformationConditions <InfConds> [0..*]  C7 254
       Language <Lang> [1..1] CodeSet 255
       AdditionalInformation <AddtlInf> [1..*] Text 255
     InformationToComplyWith <InfToCmplyWth> [0..*]  C7 255
       Language <Lang> [1..1] CodeSet 255
       AdditionalInformation <AddtlInf> [1..*] Text 255
     TaxationConditions <TaxtnConds> [0..*]  C7 256
       Language <Lang> [1..1] CodeSet 256
       AdditionalInformation <AddtlInf> [1..*] Text 256
     Disclaimer <Dsclmr> [0..*]  C7 256
       Language <Lang> [1..1] CodeSet 257
       AdditionalInformation <AddtlInf> [1..*] Text 257
     PartyContactNarrative <PtyCtctNrrtv> [0..*]  C7 257
       Language <Lang> [1..1] CodeSet 257
       AdditionalInformation <AddtlInf> [1..*] Text 257
     RegistrationDetails <RegnDtls> [0..*]  C7 258
       Language <Lang> [1..1] CodeSet 258
       AdditionalInformation <AddtlInf> [1..*] Text 258
     BasketOrIndexInformation <BsktOrIndxInf> [0..*]  C7 258
       Language <Lang> [1..1] CodeSet 259
       AdditionalInformation <AddtlInf> [1..*] Text 259
     CertificationBreakdown <CertfctnBrkdwn> [0..*]  C7 259
       Language <Lang> [1..1] CodeSet 259
       AdditionalInformation <AddtlInf> [1..*] Text 259
     URLAddress <URLAdr> [0..*]  260
       Language <Lang> [1..1] CodeSet 260
       URLAddress <URLAdr> [1..1] Text 260
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 42 February 2026
```

