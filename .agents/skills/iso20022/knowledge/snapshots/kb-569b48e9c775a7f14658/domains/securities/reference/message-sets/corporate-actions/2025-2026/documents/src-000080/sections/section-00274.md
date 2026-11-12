---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.2 Structure"]
file_pages: [363, 364, 365, 366, 367, 368, 369, 370, 371, 372]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.2 Structure

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 363 to 372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnMvmntPrlimryAdvc> [1..1]  C9, C11,
C12,
C36,
C37,
C43,
C56,
C58,
C59,
C62,
C64,
C66,
C67
   Pagination <Pgntn> [0..1] ± 386
   MovementPreliminaryAdviceGeneralInformation
<MvmntPrlimryAdvcGnlInf>
[1..1]  386
     MovementPreliminaryAdviceIdentification
<MvmntPrlimryAdvcId>
[0..1] Text 387
     Type <Tp> [1..1] CodeSet 387
     Function <Fctn> [1..1] CodeSet 387
   PreviousMovementPreliminaryAdviceIdentification
<PrvsMvmntPrlimryAdvcId>
[0..1] ± 387
   NotificationIdentification <NtfctnId> [0..1] ± 387
   MovementConfirmationIdentification <MvmntConfId> [0..1] ± 388
   InstructionIdentification <InstrId> [0..1] ± 388
   OtherDocumentIdentification <OthrDocId> [0..*] ± 388
   EventsLinkage <EvtsLkg> [0..*] ± 389
   ReversalReason <RvslRsn> [0..1]  C5 389
     Reason <Rsn> [1..1]  390
{Or       Code <Cd> [1..1] CodeSet 390
Or}       Proprietary <Prtry> [1..1] ± 390
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 391
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C54 391
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 393
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 393
     ClassActionNumber <ClssActnNb> [0..1] Text 393
     EventProcessingType <EvtPrcgTp> [0..1] ± 393
     EventType <EvtTp> [1..1] ± C26 394
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 363 February 2026
```

## File page 364

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 394
     UnderlyingSecurity <UndrlygScty> [1..1]  C48,
C60
394
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C17,
C18,
C44,
C45,
C57
396
       PlaceOfListing <PlcOfListg> [0..1] ± 397
       DayCountBasis <DayCntBsis> [0..1] ± 397
       ClassificationType <ClssfctnTp> [0..1] ± 397
       OptionStyle <OptnStyle> [0..1] ± 398
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 398
       NextCouponDate <NxtCpnDt> [0..1] Date 398
       ExpiryDate <XpryDt> [0..1] Date 398
       FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 398
       MaturityDate <MtrtyDt> [0..1] Date 398
       IssueDate <IsseDt> [0..1] Date 399
       NextCallableDate <NxtCllblDt> [0..1] Date 399
       PutableDate <PutblDt> [0..1] Date 399
       DatedDate <DtdDt> [0..1] Date 399
       ConversionDate <ConvsDt> [0..1] Date 399
       InterestRate <IntrstRate> [0..1] ± 399
       NextInterestRate <NxtIntrstRate> [0..1] ± 399
       PercentageOfDebtClaim <PctgOfDebtClm> [0..1] ± 400
       PreviousFactor <PrvsFctr> [0..1] ± 400
       NextFactor <NxtFctr> [0..1] ± 400
       WarrantParity <WarrtParity> [0..1] ± 401
       MinimumNominalQuantity <MinNmnlQty> [0..1] ± C19 401
       ContractSize <CtrctSz> [0..1] ± C19 401
   AccountDetails <AcctDtls> [1..1]  402
{Or     ForAllAccounts <ForAllAccts> [1..1] ± 403
Or}     AccountsListAndBalanceDetails <AcctsListAndBalDtls> [1..*]  C68,
C69,
C70,
C71
404
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 364 February 2026
```

## File page 365

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       SafekeepingAccount <SfkpgAcct> [0..1] Text 406
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 406
       AccountOwner <AcctOwnr> [0..1] ± 406
       SafekeepingPlace <SfkpgPlc> [0..1] ± 406
       Balance <Bal> [0..1]  C7 407
         TotalEligibleBalance <TtlElgblBal> [0..1] ± 408
         BlockedBalance <BlckdBal> [0..1] ± 409
         BorrowedBalance <BrrwdBal> [0..1] ± 409
         CollateralInBalance <CollInBal> [0..1] ± 409
         CollateralOutBalance <CollOutBal> [0..1] ± 410
         OnLoanBalance <OnLnBal> [0..1] ± 410
         PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 410
         PendingReceiptBalance <PdgRctBal> [0..*] ± 411
         OutForRegistrationBalance <OutForRegnBal> [0..1] ± 411
         SettlementPositionBalance <SttlmPosBal> [0..*] ± 411
         StreetPositionBalance <StrtPosBal> [0..1] ± 412
         TradeDatePositionBalance <TradDtPosBal> [0..1] ± 412
         InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 412
         RegisteredBalance <RegdBal> [0..1] ± 413
         ObligatedBalance <OblgtdBal> [0..1] ± 413
         UninstructedBalance <UinstdBal> [0..1] ± 413
         InstructedBalance <InstdBal> [0..1] ± 414
         AffectedBalance <AfctdBal> [0..1] ± 414
         UnaffectedBalance <UafctdBal> [0..1] ± 414
   CorporateActionDetails <CorpActnDtls> [0..1]  415
     DateDetails <DtDtls> [0..1]  415
       RecordDate <RcrdDt> [0..1] ± 416
       ExDividendDate <ExDvddDt> [0..1] ± 416
       LotteryDate <LtryDt> [0..1] ± 416
     SecuritiesQuantity <SctiesQty> [0..1]  417
       BaseDenomination <BaseDnmtn> [0..1] ± C20 417
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 365 February 2026
```

## File page 366

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       IncrementalDenomination <IncrmtlDnmtn> [0..1] ± C20 417
     EventStage <EvtStag> [0..1] ± 418
     AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 418
     FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 418
     LotteryType <LtryTp> [0..1] ± 419
   CorporateActionMovementDetails <CorpActnMvmntDtls> [0..*]  C6, C10,
C22,
C23,
C24,
C25,
C42,
C65,
C55
419
     OptionNumber <OptnNb> [1..1] Text 430
     OptionType <OptnTp> [1..1] ± 430
     FractionDisposition <FrctnDspstn> [0..1] ± 430
     OfferType <OfferTp> [0..*]  430
{Or       Code <Cd> [1..1] CodeSet 431
Or}       Proprietary <Prtry> [1..1] ± 431
     OptionFeatures <OptnFeatrs> [0..*]  431
{Or       Code <Cd> [1..1] CodeSet 432
Or}       Proprietary <Prtry> [1..1] ± 433
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
436
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 366 February 2026
```

## File page 367

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C45,
C57
     DateDetails <DtDtls> [0..1]  437
       EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 437
       CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 438
       ProtectDeadline <PrtctDdln> [0..1] ± 438
       MarketDeadline <MktDdln> [0..1] ± 438
       ResponseDeadline <RspnDdln> [0..1] ± 439
       ExpiryDate <XpryDt> [0..1] ± 439
       SubscriptionCostDebitDate <SbcptCostDbtDt> [0..1] ± 440
       DepositoryCoverExpirationDate <DpstryCoverXprtnDt> [0..1] ± 440
       StockLendingDeadline <StockLndgDdln> [0..1] ± 440
       BorrowerStockLendingDeadline <BrrwrStockLndgDdln> [0..*]  441
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
       TaxableIncomePerDividendShare <TaxblIncmPerDvddShr> [0..*] ± 447
       TaxOnIncome <TaxOnIncm> [0..1] ± 448
     PriceDetails <PricDtls> [0..1]  448
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 367 February 2026
```

## File page 368

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 449
       OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 449
       MaximumCashToInstruct <MaxCshToInst> [0..1] ± 449
       MinimumCashToInstruct <MinCshToInst> [0..1] ± 450
       MinimumMultipleCashToInstruct <MinMltplCshToInst> [0..1] ± 450
     SecuritiesQuantity <SctiesQty> [0..1]  450
       MaximumQuantityToInstruct <MaxQtyToInst> [0..1] ± C21 451
       MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C21 451
       MinimumMultipleQuantityToInstruct <MinMltplQtyToInst> [0..1] ± C20 451
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 368 February 2026
```

## File page 369

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         ConversionDate <ConvsDt> [0..1] Date 462
         PreviousFactor <PrvsFctr> [0..1] ± 462
         NextFactor <NxtFctr> [0..1] ± 462
         InterestRate <IntrstRate> [0..1] ± 463
         NextInterestRate <NxtIntrstRate> [0..1] ± 463
         MinimumNominalQuantity <MinNmnlQty> [0..1] ± C19 463
         MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C19 464
         MinimumMultipleQuantityToInstruct <MinMltplQtyToInst> [0..1] ± C19 464
         ContractSize <CtrctSz> [0..1] ± C19 465
         IssuePrice <IssePric> [0..1] ± 465
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 466
       TemporaryFinancialInstrumentIndicator
<TempFinInstrmInd>
[0..1] ± 466
       NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1]  466
{Or         Code <Cd> [1..1] CodeSet 467
Or}         Proprietary <Prtry> [1..1] ± 467
       IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  467
{Or         Code <Cd> [1..1] CodeSet 467
Or}         Proprietary <Prtry> [1..1] ± 468
       NewSecuritiesIssuanceIndicator <NewSctiesIssncInd> [0..1] CodeSet 468
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 369 February 2026
```

## File page 370

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         DividendRankingDate <DvddRnkgDt> [0..1] ± 472
         EarliestPaymentDate <EarlstPmtDt> [0..1] ± 473
         PariPassuDate <PrpssDt> [0..1] ± 473
         LastTradingDate <LastTradgDt> [0..1] ± 473
       RateDetails <RateDtls> [0..1]  474
         AdditionalQuantityForSubscribedResultantSecurities
<AddtlQtyForSbcbdRsltntScties>
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
{Or           IndicativePrice <IndctvPric> [1..1] ± 479
Or}           MarketPrice <MktPric> [1..1] ± 480
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 370 February 2026
```

## File page 371

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 487
       ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 487
       NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1] ± 488
       IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  488
{Or         Code <Cd> [1..1] CodeSet 488
Or}         Proprietary <Prtry> [1..1] ± 488
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 371 February 2026
```

## File page 372

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         TaxArrearAmount <TaxArrearAmt> [0..1] Amount C1, C14 500
         AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C1, C14 500
         WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C14 501
         SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C14 501
         FiscalStampAmount <FsclStmpAmt> [0..1] Amount C1, C14 501
         ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C1, C14 502
         PayingAgentCommissionAmount <PngAgtComssnAmt> [0..1] Amount C1, C14 502
         LocalBrokerCommissionAmount <LclBrkrComssnAmt> [0..1] Amount C1, C14 503
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
         BackUpWithholdingTaxAmount <BckUpWhldgTaxAmt> [0..1] Amount C1, C14 507
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 372 February 2026
```

