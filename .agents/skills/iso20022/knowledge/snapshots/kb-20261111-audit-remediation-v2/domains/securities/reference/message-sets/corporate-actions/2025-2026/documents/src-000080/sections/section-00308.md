---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.12 CorporateActionDetails <CorpActnDtls>", "7.4.12.6 LotteryType <LtryTp>"]
file_pages: [419, 420, 421, 422, 423, 424, 425, 426, 427, 428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.12.6 LotteryType <LtryTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 419 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 419

```text
FollowingEventTypeIndicator <FllwngEvtTpInd> contains one of the following elements (see
"IntermediateSecuritiesDistributionTypeFormat19Choice" on page 986 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 986
Or}   Proprietary <Prtry> [1..1] ± 987
7.4.12.6  LotteryType <LtryTp>
Presence: [0..1]
Definition: Specifies the type of lottery announced.
LotteryType <LtryTp> contains one of the following elements (see "LotteryTypeFormat4Choice" on
page 979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
7.4.13 CorporateActionMovementDetails
<CorpActnMvmntDtls>
Presence: [0..*]
Definition: Information about the corporate action option.
Impacted by: C6 "AdditionalTextRule", C10 "AppliedOptionRule", C22 "DissenterRights1Rule", C23
"DissenterRights1UGRule", C24 "DissenterRights2Rule", C25 "DissenterRights2UGRule", C42
"InstructCashAmountRule", C65 "RevocabilityPeriodRule", C55 "OptionNumberGuideline"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 419 February 2026
```

## File page 420

```text
CorporateActionMovementDetails <CorpActnMvmntDtls> contains the following
CorporateActionOption252 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] Text 430
   OptionType <OptnTp> [1..1] ± 430
   FractionDisposition <FrctnDspstn> [0..1] ± 430
   OfferType <OfferTp> [0..*]  430
{Or     Code <Cd> [1..1] CodeSet 431
Or}     Proprietary <Prtry> [1..1] ± 431
   OptionFeatures <OptnFeatrs> [0..*]  431
{Or     Code <Cd> [1..1] CodeSet 432
Or}     Proprietary <Prtry> [1..1] ± 433
   OptionAvailabilityStatus <OptnAvlbtySts> [0..1] ± 433
   CertificationBreakdownType <CertfctnBrkdwnTp> [0..*] ± 433
   NonDomicileCountry <NonDmclCtry> [0..*] CodeSet C13 434
   ValidDomicileCountry <VldDmclCtry> [0..*] CodeSet C13 434
   CurrencyOption <CcyOptn> [0..1] CodeSet C1 434
   DefaultProcessingOrStandingInstruction
<DfltPrcgOrStgInstr>
[1..1] ± 435
   ChargesAppliedIndicator <ChrgsApldInd> [0..1] Indicator 435
   CertificationBreakdownIndicator <CertfctnBrkdwnInd> [0..1] Indicator 435
   WithdrawalAllowedIndicator <WdrwlAllwdInd> [0..1] Indicator 435
   ChangeAllowedIndicator <ChngAllwdInd> [0..1] Indicator 435
   AppliedOptionIndicator <ApldOptnInd> [0..1] Indicator 436
   SecurityIdentification <SctyId> [0..1] ± C17,
C18,
C44,
C45,
C57
436
   DateDetails <DtDtls> [0..1]  437
     EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 437
     CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 438
     ProtectDeadline <PrtctDdln> [0..1] ± 438
     MarketDeadline <MktDdln> [0..1] ± 438
     ResponseDeadline <RspnDdln> [0..1] ± 439
     ExpiryDate <XpryDt> [0..1] ± 439
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 420 February 2026
```

## File page 421

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SubscriptionCostDebitDate <SbcptCostDbtDt> [0..1] ± 440
     DepositoryCoverExpirationDate
<DpstryCoverXprtnDt>
[0..1] ± 440
     StockLendingDeadline <StockLndgDdln> [0..1] ± 440
     BorrowerStockLendingDeadline
<BrrwrStockLndgDdln>
[0..*]  441
       StockLendingDeadline <StockLndgDdln> [1..1] ± 441
       Borrower <Brrwr> [1..1] ± 441
     DocumentationDeadline <DcmnttnDdln> [0..1] ± 441
   RateAndAmountDetails <RateAndAmtDtls> [0..1]  C31,
C33,
C50,
C52,
C72,
C74,
C76,
C80,
C82
442
     AdditionalTax <AddtlTax> [0..1] ± 443
     GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 444
     NetDistributionRate <NetDstrbtnRate> [0..*] ± 444
     GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 445
     MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] ± 446
     ProrationRate <PrratnRate> [0..1] ± 446
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 447
     SecondLevelTax <ScndLvlTax> [0..*] ± 447
     TaxableIncomePerDividendShare
<TaxblIncmPerDvddShr>
[0..*] ± 447
     TaxOnIncome <TaxOnIncm> [0..1] ± 448
   PriceDetails <PricDtls> [0..1]  448
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 449
     OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 449
     MaximumCashToInstruct <MaxCshToInst> [0..1] ± 449
     MinimumCashToInstruct <MinCshToInst> [0..1] ± 450
     MinimumMultipleCashToInstruct
<MinMltplCshToInst>
[0..1] ± 450
   SecuritiesQuantity <SctiesQty> [0..1]  450
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 421 February 2026
```

## File page 422

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     MaximumQuantityToInstruct <MaxQtyToInst> [0..1] ± C21 451
     MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C21 451
     MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C20 451
     NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C20 452
     NewDenominationQuantity <NewDnmtnQty> [0..1] ± C20 452
     FrontEndOddLotQuantity <FrntEndOddLotQty> [0..1] ± C20 453
     BackEndOddLotQuantity <BckEndOddLotQty> [0..1] ± C20 453
   SecuritiesMovementDetails <SctiesMvmntDtls> [0..*]  C27,
C38,
C40,
C46
454
     SecurityDetails <SctyDtls> [1..1]  C49,
C61
457
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C17,
C18,
C44,
C45,
C57
459
       PlaceOfListing <PlcOfListg> [0..1] ± 460
       DayCountBasis <DayCntBsis> [0..1] ± 460
       ClassificationType <ClssfctnTp> [0..1] ± 460
       OptionStyle <OptnStyle> [0..1] ± 461
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 461
       NextCouponDate <NxtCpnDt> [0..1] Date 461
       FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 461
       MaturityDate <MtrtyDt> [0..1] Date 461
       IssueDate <IsseDt> [0..1] Date 461
       NextCallableDate <NxtCllblDt> [0..1] Date 462
       PutableDate <PutblDt> [0..1] Date 462
       DatedDate <DtdDt> [0..1] Date 462
       ConversionDate <ConvsDt> [0..1] Date 462
       PreviousFactor <PrvsFctr> [0..1] ± 462
       NextFactor <NxtFctr> [0..1] ± 462
       InterestRate <IntrstRate> [0..1] ± 463
       NextInterestRate <NxtIntrstRate> [0..1] ± 463
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 422 February 2026
```

## File page 423

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       MinimumNominalQuantity <MinNmnlQty> [0..1] ± C19 463
       MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C19 464
       MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C19 464
       ContractSize <CtrctSz> [0..1] ± C19 465
       IssuePrice <IssePric> [0..1] ± 465
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 466
     TemporaryFinancialInstrumentIndicator
<TempFinInstrmInd>
[0..1] ± 466
     NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1]  466
{Or       Code <Cd> [1..1] CodeSet 467
Or}       Proprietary <Prtry> [1..1] ± 467
     IssuerOfferorTaxabilityIndicator
<IssrOfferrTaxbltyInd>
[0..1]  467
{Or       Code <Cd> [1..1] CodeSet 467
Or}       Proprietary <Prtry> [1..1] ± 468
     NewSecuritiesIssuanceIndicator
<NewSctiesIssncInd>
[0..1] CodeSet 468
     IncomeType <IncmTp> [0..1] ± 468
     OtherIncomeType <OthrIncmTp> [0..*] ± 469
     ExemptionType <XmptnTp> [0..*] ± 469
     EntitledQuantity <EntitldQty> [0..1] ± 469
     SafekeepingPlace <SfkpgPlc> [0..1] ± 470
     CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C13 470
     FractionDisposition <FrctnDspstn> [0..1] ± 470
     CurrencyOption <CcyOptn> [0..1] CodeSet C1 471
     TradingPeriod <TradgPrd> [0..1] ± 471
     DateDetails <DtDtls> [1..1]  471
       PaymentDate <PmtDt> [1..1] ± 472
       AvailableDate <AvlblDt> [0..1] ± 472
       DividendRankingDate <DvddRnkgDt> [0..1] ± 472
       EarliestPaymentDate <EarlstPmtDt> [0..1] ± 473
       PariPassuDate <PrpssDt> [0..1] ± 473
       LastTradingDate <LastTradgDt> [0..1] ± 473
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 423 February 2026
```

## File page 424

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RateDetails <RateDtls> [0..1]  474
       AdditionalQuantityForSubscribedResultantSecuriti
es <AddtlQtyForSbcbdRsltntScties>
[0..1] ± 474
       AdditionalQuantityForExistingSecurities
<AddtlQtyForExstgScties>
[0..1] ± 475
       NewToOld <NewToOd> [0..1] ± 475
       TransformationRate <TrfrmatnRate> [0..1] Rate 476
       ChargesFees <ChrgsFees> [0..1] ± 476
       FiscalStamp <FsclStmp> [0..1] ± 476
       ApplicableRate <AplblRate> [0..1] ± 477
       TaxCreditRate <TaxCdtRate> [0..1] ± 477
       FinancialTransactionTaxRate <FinTxTaxRate> [0..1] ± 477
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 477
       SecondLevelTax <ScndLvlTax> [0..*] ± 478
     PriceDetails <PricDtls> [0..1]  C29 478
       IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  479
{Or         IndicativePrice <IndctvPric> [1..1] ± 479
Or}         MarketPrice <MktPric> [1..1] ± 480
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 480
       CashValueForTax <CshValForTax> [0..1] ± 480
       GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 481
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 481
     AmountDetails <AmtDtls> [0..1]  482
       WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C14 482
       SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C14 483
   CashMovementDetails <CshMvmntDtls> [0..*]  C28,
C39,
C41,
C47
483
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 487
     ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 487
     NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1] ± 488
     IssuerOfferorTaxabilityIndicator
<IssrOfferrTaxbltyInd>
[0..1]  488
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 424 February 2026
```

## File page 425

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 488
Or}       Proprietary <Prtry> [1..1] ± 488
     IncomeType <IncmTp> [0..1] ± 489
     OtherIncomeType <OthrIncmTp> [0..*] ± 489
     ExemptionType <XmptnTp> [0..*] ± 489
     CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C13 490
     CashAccountIdentification <CshAcctId> [0..1] ± 490
     AmountDetails <AmtDtls> [0..1]  490
       GrossAmount <GrssAmt> [0..1] Amount C1, C14 492
       NetAmount <NetAmt> [0..1] Amount C1, C14 493
       SolicitationFees <SlctnFees> [0..1] Amount C1, C14 493
       CashInLieuOfShare <CshInLieuOfShr> [0..1] Amount C1, C14 493
       CapitalGain <CptlGn> [0..1] Amount C1, C14 494
       InterestAmount <IntrstAmt> [0..1] Amount C1, C14 494
       MarketClaimAmount <MktClmAmt> [0..1] Amount C1, C14 495
       IndemnityAmount <IndmntyAmt> [0..1] Amount C1, C14 495
       ManufacturedDividendPaymentAmount
<ManfctrdDvddPmtAmt>
[0..1] Amount C1, C14 495
       ReinvestmentAmount <RinvstmtAmt> [0..1] Amount C1, C14 496
       FullyFrankedAmount <FullyFrnkdAmt> [0..1] Amount C1, C14 496
       UnfrankedAmount <UfrnkdAmt> [0..1] Amount C1, C14 497
       SundryOrOtherAmount <SndryOrOthrAmt> [0..1] Amount C1, C14 497
       TaxFreeAmount <TaxFreeAmt> [0..1] Amount C1, C14 497
       TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C1, C14 498
       ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C1, C14 498
       StampDutyAmount <StmpDtyAmt> [0..1] Amount C1, C14 499
       TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C1, C14 499
       TaxCreditAmount <TaxCdtAmt> [0..1] Amount C1, C14 499
       TaxArrearAmount <TaxArrearAmt> [0..1] Amount C1, C14 500
       AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C1, C14 500
       WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C14 501
       SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C14 501
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 425 February 2026
```

## File page 426

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       FiscalStampAmount <FsclStmpAmt> [0..1] Amount C1, C14 501
       ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C1, C14 502
       PayingAgentCommissionAmount
<PngAgtComssnAmt>
[0..1] Amount C1, C14 502
       LocalBrokerCommissionAmount
<LclBrkrComssnAmt>
[0..1] Amount C1, C14 503
       RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C1, C14 503
       ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C1, C14 503
       ChargesAmount <ChrgsAmt> [0..1] Amount C1, C14 504
       EntitledAmount <EntitldAmt> [0..1] Amount C1, C14 504
       OriginalAmount <OrgnlAmt> [0..1] Amount C1, C14 505
       AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C1, C14 505
       IncomePortion <IncmPrtn> [0..1] Amount C1, C14 505
       EqualisationAmount <EqulstnAmt> [0..1] Amount C1, C14 506
       FATCATaxAmount <FATCATaxAmt> [0..1] Amount C1, C14 506
       NRATaxAmount <NRATaxAmt> [0..1] Amount C1, C14 507
       BackUpWithholdingTaxAmount
<BckUpWhldgTaxAmt>
[0..1] Amount C1, C14 507
       TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C1, C14 507
       TransactionTax <TxTax> [0..1] Amount C1, C14 508
       DeemedAmount <DmdAmt> [0..1] Amount C1, C14 508
       ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C1, C14 509
       DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C1, C14 509
       DeemedFundAmount <DmdFndAmt> [0..1] Amount C1, C14 509
       DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C1, C14 510
       DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C1, C14 510
       BuyUpAmount <BuyUpAmt> [0..1] Amount C1, C14 511
     DateDetails <DtDtls> [1..1]  511
       PaymentDate <PmtDt> [1..1] ± 511
       ValueDate <ValDt> [0..1] ± 512
       ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 512
       EarliestPaymentDate <EarlstPmtDt> [0..1] ± 512
     ForeignExchangeDetails <FXDtls> [0..1] ± 513
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 426 February 2026
```

## File page 427

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RateAndAmountDetails <RateAndAmtDtls> [0..1]  C15,
C16,
C32,
C34,
C51,
C53,
C73,
C75,
C77,
C81,
C83
513
       AdditionalTax <AddtlTax> [0..1] ± 516
       GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 516
       GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 516
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 517
       SecondLevelTax <ScndLvlTax> [0..*] ± 517
       ChargesFees <ChrgsFees> [0..1] ± 518
       EarlySolicitationFeeRate <EarlySlctnFeeRate> [0..1] ± 518
       FiscalStamp <FsclStmp> [0..1] ± 519
       ThirdPartyIncentiveRate <ThrdPtyIncntivRate> [0..1] ± 519
       NetDistributionRate <NetDstrbtnRate> [0..*] ± 519
       ApplicableRate <AplblRate> [0..1] ± 520
       SolicitationFeeRate <SlctnFeeRate> [0..1] ± 520
       TaxCreditRate <TaxCdtRate> [0..1] ± 521
       TaxOnIncome <TaxOnIncm> [0..1] ± 521
       TaxOnProfits <TaxOnPrfts> [0..1] ± 521
       TaxReclaimRate <TaxRclmRate> [0..1] ± 522
       EqualisationRate <EqulstnRate> [0..1] ± 522
       DeemedRate <DmdRate> [0..*] ± 522
     PriceDetails <PricDtls> [0..1]  C30 523
       GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 524
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 524
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 525
   AdditionalInformation <AddtlInf> [0..1]  C3 525
     AdditionalText <AddtlTxt> [0..1]  526
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 427 February 2026
```

## File page 428

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalInformation <AddtlInf> [1..1] Text 526
     NarrativeVersion <NrrtvVrsn> [0..1]  527
       AdditionalInformation <AddtlInf> [1..1] Text 527
     InformationConditions <InfConds> [0..1]  527
       AdditionalInformation <AddtlInf> [1..*] Text 527
     InformationToComplyWith <InfToCmplyWth> [0..1]  527
       AdditionalInformation <AddtlInf> [1..*] Text 528
     SecurityRestriction <SctyRstrctn> [0..1]  528
       AdditionalInformation <AddtlInf> [1..*] Text 528
     TaxationConditions <TaxtnConds> [0..1]  528
       AdditionalInformation <AddtlInf> [1..*] Text 528
     Disclaimer <Dsclmr> [0..1]  528
       AdditionalInformation <AddtlInf> [1..*] Text 529
     CertificationBreakdown <CertfctnBrkdwn> [0..1]  529
       AdditionalInformation <AddtlInf> [1..*] Text 529
Constraints
• AdditionalTextRule
If OptionType/Code is OTHR (Other), then AdditionalInformation/AdditionalText/AdditionalInformation
must be present.
(MT564 NVR C5).
On Condition
    /OptionType is present
 And    /OptionType/Code is equal to value 'Other'
Following Must be True
    /AdditionalInformation Must be present
 And    /AdditionalInformation/AdditionalText Must be present
 And    /AdditionalInformation/AdditionalText/AdditionalInformation Must be 
present
• AppliedOptionRule
If DefaultProcessingOrStandingInstruction/DefaultOptionIndicator is present and its value is '1' or
'true' (Yes), then AppliedOptionIndicator value must not be '1' or 'true' (Yes).
• DissenterRights1Rule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal to
NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
On Condition
    /OfferType[*]/Code is equal to value 'DissenterRights'
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 428 February 2026
```

