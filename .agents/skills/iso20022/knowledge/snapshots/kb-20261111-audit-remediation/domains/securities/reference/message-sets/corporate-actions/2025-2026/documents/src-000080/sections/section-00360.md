---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.19 AmountDetails <AmtDtls>", "7.4.13.22.19.2 SecondLevelTaxAmount <ScndLvlTaxAmt>"]
file_pages: [483, 484, 485, 486]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.19.2 SecondLevelTaxAmount <ScndLvlTaxAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 483 to 486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 483

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.13.22.19.2  SecondLevelTaxAmount <ScndLvlTaxAmt>
Presence: [0..1]
Definition: Amount of money withheld by the jurisdiction other than the jurisdiction of the issuer's
country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is levied in
complement or offset of the withholding tax rate levied by the jurisdiction of the issuer's tax domicile.
Impacted by: C1 "ActiveCurrency", C14 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.13.23  CashMovementDetails <CshMvmntDtls>
Presence: [0..*]
Definition: Provides information about the cash movement linked to the corporate action option.
Impacted by: C28 "ExemptionTypeUsageRule", C39 "IncomeType2Rule", C41
"IncomeTypeUsageRule", C47 "IssuerOfferorTaxabilityIndicatorUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 483 February 2026
```

## File page 484

```text
CashMovementDetails <CshMvmntDtls> contains the following CashOption117 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 487
   ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 487
   NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1] ± 488
   IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  488
{Or     Code <Cd> [1..1] CodeSet 488
Or}     Proprietary <Prtry> [1..1] ± 488
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 484 February 2026
```

## File page 485

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxCreditAmount <TaxCdtAmt> [0..1] Amount C1, C14 499
     TaxArrearAmount <TaxArrearAmt> [0..1] Amount C1, C14 500
     AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C1, C14 500
     WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C14 501
     SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C14 501
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 485 February 2026
```

## File page 486

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PaymentDate <PmtDt> [1..1] ± 511
     ValueDate <ValDt> [0..1] ± 512
     ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 512
     EarliestPaymentDate <EarlstPmtDt> [0..1] ± 512
   ForeignExchangeDetails <FXDtls> [0..1] ± 513
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 486 February 2026
```

