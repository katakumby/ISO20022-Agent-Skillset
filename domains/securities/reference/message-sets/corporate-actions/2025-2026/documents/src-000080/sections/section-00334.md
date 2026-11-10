---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>"]
file_pages: [454, 455, 456]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 454 to 456.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
BackEndOddLotQuantity <BckEndOddLotQty> contains one of the following elements (see
"FinancialInstrumentQuantity35Choice" on page 1092 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1093
Or   FaceAmount <FaceAmt> [1..1] Amount 1093
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1093
Or   Code <Cd> [1..1] CodeSet 1093
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1093
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
7.4.13.22  SecuritiesMovementDetails <SctiesMvmntDtls>
Presence: [0..*]
Definition: Provides information about securities movement related to a corporate action option.
Impacted by: C27 "ExemptionTypeUsageRule", C38 "IncomeType1Rule", C40
"IncomeTypeUsageRule", C46 "IssuerOfferorTaxabilityIndicatorUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 454 February 2026
```

## File page 455

```text
SecuritiesMovementDetails <SctiesMvmntDtls> contains the following SecuritiesOption122
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 455 February 2026
```

## File page 456

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Code <Cd> [1..1] CodeSet 467
Or}     Proprietary <Prtry> [1..1] ± 467
   IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  467
{Or     Code <Cd> [1..1] CodeSet 467
Or}     Proprietary <Prtry> [1..1] ± 468
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
     DividendRankingDate <DvddRnkgDt> [0..1] ± 472
     EarliestPaymentDate <EarlstPmtDt> [0..1] ± 473
     PariPassuDate <PrpssDt> [0..1] ± 473
     LastTradingDate <LastTradgDt> [0..1] ± 473
   RateDetails <RateDtls> [0..1]  474
     AdditionalQuantityForSubscribedResultantSecuritie
s <AddtlQtyForSbcbdRsltntScties>
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 456 February 2026
```

