---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks", "79.4.5 Movements <Mvmnts>", "79.4.5.2 Movement <Mvmnt>", "79.4.5.2.11 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [2739, 2740]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4.5.2.11 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2739 to 2740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2739

```text
79.4.5.2.11  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C4 "AdditionalDetailsRule", C16 "PlaceOfListingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2739 August 2026
```

## File page 2740

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes92" on page 2934 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 2936
   DayCountBasis <DayCntBsis> [0..1] ± 2936
   RegistrationForm <RegnForm> [0..1] ± 2937
   PaymentFrequency <PmtFrqcy> [0..1] ± 2937
   PaymentStatus <PmtSts> [0..1] ± 2937
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 2937
   ClassificationType <ClssfctnTp> [0..1] ± 2938
   OptionStyle <OptnStyle> [0..1] ± 2938
   OptionType <OptnTp> [0..1] ± 2938
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 2938
   CouponDate <CpnDt> [0..1] Date 2939
   ExpiryDate <XpryDt> [0..1] Date 2939
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 2939
   MaturityDate <MtrtyDt> [0..1] Date 2939
   IssueDate <IsseDt> [0..1] Date 2939
   NextCallableDate <NxtCllblDt> [0..1] Date 2939
   PutableDate <PutblDt> [0..1] Date 2940
   DatedDate <DtdDt> [0..1] Date 2940
   FirstPaymentDate <FrstPmtDt> [0..1] Date 2940
   PreviousFactor <PrvsFctr> [0..1] Rate 2940
   CurrentFactor <CurFctr> [0..1] Rate 2940
   NextFactor <NxtFctr> [0..1] Rate 2940
   InterestRate <IntrstRate> [0..1] Rate 2940
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 2940
   NextInterestRate <NxtIntrstRate> [0..1] Rate 2941
   IndexRateBasis <IndxRateBsis> [0..1] Rate 2941
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 2941
   PoolNumber <PoolNb> [0..1] ± 2941
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2941
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 2942
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2740 August 2026
```

