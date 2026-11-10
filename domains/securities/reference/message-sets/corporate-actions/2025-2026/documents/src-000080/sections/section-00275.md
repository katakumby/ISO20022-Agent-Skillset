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
file_pages: [373, 374]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# Continuation at file page 373

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 373 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 373

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
         GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 524
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 373 February 2026
```

## File page 374

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 525
     AdditionalInformation <AddtlInf> [0..1]  C3 525
       AdditionalText <AddtlTxt> [0..1]  526
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
   AdditionalInformation <AddtlInf> [0..1]  C4 529
     AdditionalText <AddtlTxt> [0..1]  530
       AdditionalInformation <AddtlInf> [1..*] Text 531
     NarrativeVersion <NrrtvVrsn> [0..1]  531
       AdditionalInformation <AddtlInf> [1..*] Text 531
     InformationConditions <InfConds> [0..1]  531
       AdditionalInformation <AddtlInf> [1..*] Text 531
     InformationToComplyWith <InfToCmplyWth> [0..1]  532
       AdditionalInformation <AddtlInf> [1..*] Text 532
     TaxationConditions <TaxtnConds> [0..1]  532
       AdditionalInformation <AddtlInf> [1..*] Text 532
     Disclaimer <Dsclmr> [0..1]  532
       AdditionalInformation <AddtlInf> [1..*] Text 533
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 374 February 2026
```

