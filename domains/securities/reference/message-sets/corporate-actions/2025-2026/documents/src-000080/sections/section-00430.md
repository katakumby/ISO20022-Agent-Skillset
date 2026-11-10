---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.11 CorporateActionDetails <CorpActnDtls>", "8.4.11.4 FollowingEventTypeIndicator <FllwngEvtTpInd>"]
file_pages: [575, 576, 577, 578, 579, 580, 581]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.11.4 FollowingEventTypeIndicator <FllwngEvtTpInd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 575 to 581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 575

```text
AdditionalBusinessProcessIndicator <AddtlBizPrcInd> contains one of the following elements (see
"AdditionalBusinessProcessFormat23Choice" on page 1021 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1021
Or}   Proprietary <Prtry> [1..1] ± 1022
8.4.11.4  FollowingEventTypeIndicator <FllwngEvtTpInd>
Presence: [0..1]
Definition: Specifies the event type of the following event.
FollowingEventTypeIndicator <FllwngEvtTpInd> contains one of the following elements (see
"IntermediateSecuritiesDistributionTypeFormat19Choice" on page 986 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 986
Or}   Proprietary <Prtry> [1..1] ± 987
8.4.11.5  LotteryType <LtryTp>
Presence: [0..1]
Definition: Specifies the type of lottery announced.
LotteryType <LtryTp> contains one of the following elements (see "LotteryTypeFormat4Choice" on
page 979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
8.4.12 CorporateActionConfirmationDetails
<CorpActnConfDtls>
Presence: [1..1]
Definition: Information about the corporate action option.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 575 February 2026
```

## File page 576

```text
CorporateActionConfirmationDetails <CorpActnConfDtls> contains the following
CorporateActionOption253 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] ± 582
   OptionType <OptnTp> [1..1] ± 582
   OptionFeatures <OptnFeatrs> [0..*]  582
{Or     Code <Cd> [1..1] CodeSet 583
Or}     Proprietary <Prtry> [1..1] ± 583
   FractionDisposition <FrctnDspstn> [0..1] ± 584
   CurrencyOption <CcyOptn> [0..1] CodeSet C1 584
   DateDetails <DtDtls> [0..1]  584
     CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 584
     TradingDate <TradgDt> [0..1] ± 585
   RateAndAmountDetails <RateAndAmtDtls> [0..1]  C24,
C26,
C42,
C44,
C63,
C65,
C67,
C73,
C75
585
     GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 587
     NetDistributionRate <NetDstrbtnRate> [0..*] ± 588
     GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 588
     MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] Rate 589
     ProrationRate <PrratnRate> [0..1] ± 589
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 589
     SecondLevelTax <ScndLvlTax> [0..*] ± 590
     AdditionalTax <AddtlTax> [0..1] ± 590
     TaxableIncomePerDividendShare
<TaxblIncmPerDvddShr>
[0..*] ± 591
   PriceDetails <PricDtls> [0..1]  C23 591
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 591
     OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 592
   PlaceOfTrade <PlcOfTrad> [0..1] ± C41 592
   SecuritiesMovementDetails <SctiesMvmntDtls> [0..*]  C19,
C31,
593
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 576 February 2026
```

## File page 577

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C33,
C39
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C15,
C16,
C36,
C37,
C48
596
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 597
     TemporaryFinancialInstrumentIndicator
<TempFinInstrmInd>
[0..1] ± 597
     NewSecuritiesIssuanceIndicator
<NewSctiesIssncInd>
[0..1] CodeSet 597
     IssuerOfferorTaxabilityIndicator
<IssrOfferrTaxbltyInd>
[0..1]  598
{Or       Code <Cd> [1..1] CodeSet 598
Or}       Proprietary <Prtry> [1..1] ± 598
     IncomeType <IncmTp> [0..1] ± 598
     OtherIncomeType <OthrIncmTp> [0..*] ± 599
     ExemptionType <XmptnTp> [0..*] ± 599
     CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C11 599
     PostingQuantity <PstngQty> [1..1] ± 600
     SafekeepingPlace <SfkpgPlc> [0..1] ± 600
     FractionDisposition <FrctnDspstn> [0..1] ± 600
     CurrencyOption <CcyOptn> [0..1] CodeSet C1 601
     DateDetails <DtDtls> [1..1]  601
       PostingDate <PstngDt> [1..1] ± 601
       AvailableDate <AvlblDt> [0..1] ± 602
       PariPassuDate <PrpssDt> [0..1] ± 602
       DividendRankingDate <DvddRnkgDt> [0..1] ± 602
       EarliestPaymentDate <EarlstPmtDt> [0..1] ± 603
       PaymentDate <PmtDt> [0..1] ± 603
     RateDetails <RateDtls> [0..1]  603
       AdditionalQuantityForSubscribedResultantSecuriti
es <AddtlQtyForSbcbdRsltntScties>
[0..1] ± 604
       AdditionalQuantityForExistingSecurities
<AddtlQtyForExstgScties>
[0..1] ± 604
       NewToOld <NewToOd> [0..1] ± 605
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 577 February 2026
```

## File page 578

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ChargesFees <ChrgsFees> [0..1] ± 605
       FiscalStamp <FsclStmp> [0..1] Rate 606
       ApplicableRate <AplblRate> [0..1] Rate 606
       TaxCreditRate <TaxCdtRate> [0..1] ± 606
       FinancialTransactionTaxRate <FinTxTaxRate> [0..1] Rate 606
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 606
       SecondLevelTax <ScndLvlTax> [0..*] ± 607
     PriceDetails <PricDtls> [0..1]  C21 607
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 608
       IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  608
{Or         IndicativePrice <IndctvPric> [1..1] ± 609
Or}         MarketPrice <MktPric> [1..1] ± 609
       CashValueForTax <CshValForTax> [0..1] ± 609
       GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 609
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 610
     AmountDetails <AmtDtls> [0..1]  610
       WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C12 611
       SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C12 611
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C50,
C51
612
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C50,
C51
612
   CashMovementDetails <CshMvmntDtls> [0..*]  C20,
C32,
C34,
C40
613
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 618
     ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 618
     IssuerOfferorTaxabilityIndicator
<IssrOfferrTaxbltyInd>
[0..1]  618
{Or       Code <Cd> [1..1] CodeSet 618
Or}       Proprietary <Prtry> [1..1] ± 619
     IncomeType <IncmTp> [0..1] ± 619
     OtherIncomeType <OthrIncmTp> [0..*] ± 619
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 578 February 2026
```

## File page 579

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ExemptionType <XmptnTp> [0..*] ± 619
     CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C11 620
     Account <Acct> [0..1]  620
{Or       CashAccount <CshAcct> [1..1] ± 620
Or       ChargesAccount <ChrgsAcct> [1..1] ± 621
Or}       TaxAccount <TaxAcct> [1..1] ± 621
     CashParties <CshPties> [0..1] ± 621
     AmountDetails <AmtDtls> [1..1]  622
       PostingAmount <PstngAmt> [1..1] Amount C1, C12 624
       GrossAmount <GrssAmt> [0..1] Amount C1, C12 625
       NetAmount <NetAmt> [0..1] Amount C1, C12 625
       SolicitationFees <SlctnFees> [0..1] Amount C1, C12 626
       CashInLieuOfShare <CshInLieuOfShr> [0..1] Amount C1, C12 626
       CapitalGain <CptlGn> [0..1] Amount C1, C12 626
       InterestAmount <IntrstAmt> [0..1] Amount C1, C12 627
       MarketClaimAmount <MktClmAmt> [0..1] Amount C1, C12 627
       IndemnityAmount <IndmntyAmt> [0..1] Amount C1, C12 628
       ManufacturedDividendPaymentAmount
<ManfctrdDvddPmtAmt>
[0..1] Amount C1, C12 628
       ReinvestmentAmount <RinvstmtAmt> [0..1] Amount C1, C12 629
       FullyFrankedAmount <FullyFrnkdAmt> [0..1] Amount C1, C12 629
       UnfrankedAmount <UfrnkdAmt> [0..1] Amount C1, C12 629
       SundryOrOtherAmount <SndryOrOthrAmt> [0..1] Amount C1, C12 630
       TaxFreeAmount <TaxFreeAmt> [0..1] Amount C1, C12 630
       TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C1, C12 631
       ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C1, C12 631
       StampDutyAmount <StmpDtyAmt> [0..1] Amount C1, C12 631
       TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C1, C12 632
       TaxCreditAmount <TaxCdtAmt> [0..1] Amount C1, C12 632
       AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C1, C12 633
       WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C12 633
       SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C12 633
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 579 February 2026
```

## File page 580

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       FiscalStampAmount <FsclStmpAmt> [0..1] Amount C1, C12 634
       ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C1, C12 634
       PayingAgentCommissionAmount
<PngAgtComssnAmt>
[0..1] Amount C1, C12 635
       LocalBrokerCommissionAmount
<LclBrkrComssnAmt>
[0..1] Amount C1, C12 635
       RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C1, C12 635
       ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C1, C12 636
       ChargesAmount <ChrgsAmt> [0..1] Amount C1, C12 636
       CashAmountBroughtForward <CshAmtBrghtFwd> [0..1] Amount C1, C12 637
       CashAmountCarriedForward <CshAmtCrrdFwd> [0..1] Amount C1, C12 637
       NotionalDividendPayableAmount
<NtnlDvddPyblAmt>
[0..1] Amount C1, C12 637
       NotionalTaxAmount <NtnlTaxAmt> [0..1] Amount C1, C12 638
       TaxArrearsAmount <TaxArrearsAmt> [0..1] Amount C1, C12 638
       OriginalAmount <OrgnlAmt> [0..1] Amount C1, C12 639
       PrincipalOrCorpus <PrncplOrCrps> [0..1] Amount C1, C12 639
       RedemptionPremiumAmount <RedPrmAmt> [0..1] Amount C1, C12 639
       IncomePortion <IncmPrtn> [0..1] Amount C1, C12 640
       StockExchangeTax <StockXchgTax> [0..1] Amount C1, C12 640
       EUTaxRetentionAmount <EUTaxRtntnAmt> [0..1] Amount C1, C12 641
       AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C1, C12 641
       EqualisationAmount <EqulstnAmt> [0..1] Amount C1, C12 641
       FATCATaxAmount <FATCATaxAmt> [0..1] Amount C1, C12 642
       NRATaxAmount <NRATaxAmt> [0..1] Amount C1, C12 642
       BackUpWithholdingTaxAmount
<BckUpWhldgTaxAmt>
[0..1] Amount C1, C12 643
       TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C1, C12 643
       TransactionTax <TxTax> [0..1] Amount C1, C12 643
       DeemedAmount <DmdAmt> [0..1] Amount C1, C12 644
       ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C1, C12 644
       DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C1, C12 645
       DeemedFundAmount <DmdFndAmt> [0..1] Amount C1, C12 645
       DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C1, C12 645
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 580 February 2026
```

## File page 581

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C1, C12 646
       AdjustedSubscriptionAmount <AdjstdSbcptAmt> [0..1] Amount C1, C12 646
       RefundedSubscriptionAmount <RfnddSbcptAmt> [0..1] Amount C1, C12 647
       BuyUpAmount <BuyUpAmt> [0..1] Amount C1, C12 647
     DateDetails <DtDtls> [1..1]  648
       PostingDate <PstngDt> [1..1] ± 648
       ValueDate <ValDt> [0..1] Date 648
       ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 648
       EarliestPaymentDate <EarlstPmtDt> [0..1] Date 648
       PaymentDate <PmtDt> [0..1] Date 649
     ForeignExchangeDetails <FXDtls> [0..*] ± 649
     TaxDocumentationDetails <TaxDcmnttnDtls> [0..1] ± C9, C71,
C72
649
     RateAndAmountDetails <RateAndAmtDtls> [0..1]  C13,
C14,
C25,
C27,
C43,
C45,
C64,
C66,
C68,
C74,
C76
650
       AdditionalTax <AddtlTax> [0..1] ± 652
       ChargesFees <ChrgsFees> [0..1] ± 653
       FiscalStamp <FsclStmp> [0..1] Rate 653
       GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 653
       EarlySolicitationFeeRate <EarlySlctnFeeRate> [0..1] ± 654
       ThirdPartyIncentiveRate <ThrdPtyIncntivRate> [0..1] ± 654
       GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 655
       NetDistributionRate <NetDstrbtnRate> [0..*] ± 655
       ApplicableRate <AplblRate> [0..1] ± 656
       SolicitationFeeRate <SlctnFeeRate> [0..1] ± 656
       TaxCreditRate <TaxCdtRate> [0..1] ± 657
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 657
       SecondLevelTax <ScndLvlTax> [0..*] ± 657
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 581 February 2026
```

