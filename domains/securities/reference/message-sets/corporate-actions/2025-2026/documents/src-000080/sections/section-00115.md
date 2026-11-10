---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>"]
file_pages: [171, 172, 173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 171 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 171

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
3.4.11.24  SecuritiesMovementDetails <SctiesMvmntDtls>
Presence: [0..*]
Definition: Provides information about the securities movement linked to the corporate action option.
Impacted by: C34 "ExemptionTypeUsageRule", C50 "IncomeType1Rule", C52
"IncomeTypeUsageRule", C64 "IssuerOfferorTaxabilityIndicatorUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 171 February 2026
```

## File page 172

```text
SecuritiesMovementDetails <SctiesMvmntDtls> contains the following SecuritiesOption121
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 172 February 2026
```

## File page 173

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Code <Cd> [1..1] CodeSet 184
Or}     Proprietary <Prtry> [1..1] ± 184
   IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  184
{Or     Code <Cd> [1..1] CodeSet 184
Or}     Proprietary <Prtry> [1..1] ± 185
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
   RateDetails <RateDtls> [0..1]  191
     AdditionalQuantityForSubscribedResultantSecuritie
s <AddtlQtyForSbcbdRsltntScties>
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 173 February 2026
```

