---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.7 UnderlyingFinancialInstrument <UndrlygFinInstrm>", "3.4.7.1 Identification <Id>"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.7.1 Identification <Id>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     InterestRate <IntrstRate> [0..1] Rate 88
     NextInterestRate <NxtIntrstRate> [0..1] Rate 88
     IndexRateBasis <IndxRateBsis> [0..1] Rate 88
     PercentageOfDebtClaims <PctgOfDebtClms> [0..1] Rate 89
     CouponAttachedNumber <CpnAttchdNb> [0..1] ± 89
     PoolNumber <PoolNb> [0..1] ± 89
     VersionNumber <VrsnNb> [0..1] ± 89
     ConvertibleIndicator <ConvtblInd> [0..1] Indicator 90
     VariableRateIndicator <VarblRateInd> [0..1] Indicator 90
     CoveredIndicator <CvrdInd> [0..1] Indicator 90
     CallableIndicator <CllblInd> [0..1] Indicator 90
     PutableIndicator <PutblInd> [0..1] Indicator 90
     WarrantAttachedOnDelivery <WarrtAttchdOnDlvry> [0..1] Indicator 90
     OddCouponIndicator <OddCpnInd> [0..1] Indicator 91
     RedemptionYieldImpact <RedYldImpct> [0..1] Indicator 91
     YieldVariance <YldVar> [0..1] Indicator 91
     ExercisePrice <ExrcPric> [0..1] ± 91
     SubscriptionPrice <SbcptPric> [0..1] ± 92
     ConversionPrice <ConvsPric> [0..1] ± 92
     TaxableIncomePerShare <TaxblIncmPerShr> [0..1] ± 92
     MinimumNominalQuantity <MinNmnlQty> [0..1] ± 92
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 93
     MinimumExercisableMultipleQuantity
<MinExrcblMltplQty>
[0..1] ± 93
     FaceAmount <FaceAmt> [0..1] Amount 93
     ContractSize <CtrctSz> [0..1] ± 93
     FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 94
3.4.7.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the underlying security by an ISIN.
Impacted by: C19 "DescriptionPresenceRule", C20 "DescriptionUsageRule", C27 "ISINGuideline", C28
"ISINPresenceRule", C34 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 79 February 2025
```

