---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>"]
file_pages: [613, 614, 615, 616, 617]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11 CashMovementDetails <CshMvmntDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 613 to 617.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 613

```text
Impacted by: C50 "Party2PresenceRule", C51 "Party3PresenceRule"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties129" on page 1133 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1]  C3 1134
     Identification <Id> [1..1]  1135
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1135
Or       NameAndAddress <NmAndAdr> [1..1] ± 1136
Or       Country <Ctry> [1..1] CodeSet C3 1136
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1136
     ProcessingIdentification <PrcgId> [0..1] Text 1136
     AlternateIdentification <AltrnId> [0..*] ± 1136
   Party1 <Pty1> [0..1] ± C4, C54,
C56,
C58
1137
   Party2 <Pty2> [0..1] ± C4, C54,
C56,
C58
1138
   Party3 <Pty3> [0..1] ± C4, C54,
C56,
C58
1139
Constraints
• Party2PresenceRule
If Party 2 is present, then Party 1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party 3 is present, then Party 2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
8.4.12.11  CashMovementDetails <CshMvmntDtls>
Presence: [0..*]
Definition: Provides information about the cash movement related to a corporate action option.
Impacted by: C20 "ExemptionTypeUsageRule", C32 "IncomeType2Rule", C34
"IncomeTypeUsageRule", C40 "IssuerOfferorTaxabilityIndicatorUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 613 February 2026
```

## File page 614

```text
CashMovementDetails <CshMvmntDtls> contains the following CashOption118 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 618
   ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 618
   IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  618
{Or     Code <Cd> [1..1] CodeSet 618
Or}     Proprietary <Prtry> [1..1] ± 619
   IncomeType <IncmTp> [0..1] ± 619
   OtherIncomeType <OthrIncmTp> [0..*] ± 619
   ExemptionType <XmptnTp> [0..*] ± 619
   CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C11 620
   Account <Acct> [0..1]  620
{Or     CashAccount <CshAcct> [1..1] ± 620
Or     ChargesAccount <ChrgsAcct> [1..1] ± 621
Or}     TaxAccount <TaxAcct> [1..1] ± 621
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
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 614 February 2026
```

## File page 615

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C1, C12 631
     ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C1, C12 631
     StampDutyAmount <StmpDtyAmt> [0..1] Amount C1, C12 631
     TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C1, C12 632
     TaxCreditAmount <TaxCdtAmt> [0..1] Amount C1, C12 632
     AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C1, C12 633
     WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C12 633
     SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C12 633
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
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 615 February 2026
```

## File page 616

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 616 February 2026
```

## File page 617

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     TaxOnIncome <TaxOnIncm> [0..1] ± 658
     TaxOnProfits <TaxOnPrfts> [0..1] Rate 658
     TaxReclaimRate <TaxRclmRate> [0..1] Rate 658
     EqualisationRate <EqulstnRate> [0..1] Amount C1 658
     DeemedRate <DmdRate> [0..*] ± 659
   PriceDetails <PricDtls> [0..1]  C22 659
     GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 660
     GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 660
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 661
Constraints
• ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
• IncomeType2Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
On Condition
    /OtherIncomeType[*] is present
Following Must be True
    /IncomeType Must be present
• IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-ITYP
Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
• IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the message
and it must not be used in events such as dividend or interest.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 617 February 2026
```

