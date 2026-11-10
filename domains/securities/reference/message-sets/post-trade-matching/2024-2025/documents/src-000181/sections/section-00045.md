---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [64, 65, 66]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 64 to 66.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C3 "AdditionalDetailsRule", C40 "PlaceOfListingRule"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 64 February 2025
```

## File page 65

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following
FinancialInstrumentAttributes124 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 67
   Rating <Ratg> [0..1] ± 67
   CertificateNumber <CertNb> [0..1] Text 67
   DayCountBasis <DayCntBsis> [0..1] ± 67
   RegistrationForm <RegnForm> [0..1] ± 67
   PaymentFrequency <PmtFrqcy> [0..1] ± 68
   VariableRateChangeFrequency
<VarblRateChngFrqcy>
[0..1] ± 68
   ClassificationType <ClssfctnTp> [0..1] ± 68
   OptionStyle <OptnStyle> [0..1] ± 68
   OptionType <OptnTp> [0..1] ± 69
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 69
   CouponDate <CpnDt> [0..1] Date 69
   ExpiryDate <XpryDt> [0..1] Date 69
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 70
   MaturityDate <MtrtyDt> [0..1] Date 70
   IssueDate <IsseDt> [0..1] Date 70
   NextCallableDate <NxtCllblDt> [0..1] Date 70
   ConversionDate <ConvsDt> [0..1] Date 70
   PutableDate <PutblDt> [0..1] Date 70
   DatedDate <DtdDt> [0..1] Date 70
   FirstPaymentDate <FrstPmtDt> [0..1] Date 70
   NextFactorDate <NxtFctrDt> [0..1] Date 71
   PreviousFactor <PrvsFctr> [0..1] Rate 71
   CurrentFactor <CurFctr> [0..1] Rate 71
   NextFactor <NxtFctr> [0..1] Rate 71
   EndFactor <EndFctr> [0..1] Rate 71
   InterestRate <IntrstRate> [0..1] Rate 71
   NextInterestRate <NxtIntrstRate> [0..1] Rate 71
   IndexRateBasis <IndxRateBsis> [0..1] Rate 72
   PercentageOfDebtClaims <PctgOfDebtClms> [0..1] Rate 72
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 65 February 2025
```

## File page 66

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 72
   PoolNumber <PoolNb> [0..1] ± 72
   VersionNumber <VrsnNb> [0..1] ± 72
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 73
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 73
   CoveredIndicator <CvrdInd> [0..1] Indicator 73
   CallableIndicator <CllblInd> [0..1] Indicator 73
   PutableIndicator <PutblInd> [0..1] Indicator 73
   WarrantAttachedOnDelivery <WarrtAttchdOnDlvry> [0..1] Indicator 74
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 74
   RedemptionYieldImpact <RedYldImpct> [0..1] Indicator 74
   YieldVariance <YldVar> [0..1] Indicator 74
   ExercisePrice <ExrcPric> [0..1] ± 75
   SubscriptionPrice <SbcptPric> [0..1] ± 75
   ConversionPrice <ConvsPric> [0..1] ± 75
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] ± 75
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± 76
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 76
   MinimumExercisableMultipleQuantity
<MinExrcblMltplQty>
[0..1] ± 76
   FaceAmount <FaceAmt> [0..1] Amount 77
   ContractSize <CtrctSz> [0..1] ± 77
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 77
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and a ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 66 February 2025
```

