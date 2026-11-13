---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.4 Message Building Blocks", "8.4.5 Movements <Mvmnts>", "8.4.5.2 Movement <Mvmnt>", "8.4.5.2.11 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [184, 185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.4.5.2.11 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 184 to 185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
8.4.5.2.11  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C4 "AdditionalDetailsRule", C16 "PlaceOfListingRule"
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 184 September 2025
```

## File page 185

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes92" on page 209 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 211
   DayCountBasis <DayCntBsis> [0..1] ± 211
   RegistrationForm <RegnForm> [0..1] ± 212
   PaymentFrequency <PmtFrqcy> [0..1] ± 212
   PaymentStatus <PmtSts> [0..1] ± 212
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 212
   ClassificationType <ClssfctnTp> [0..1] ± 213
   OptionStyle <OptnStyle> [0..1] ± 213
   OptionType <OptnTp> [0..1] ± 213
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 213
   CouponDate <CpnDt> [0..1] Date 214
   ExpiryDate <XpryDt> [0..1] Date 214
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 214
   MaturityDate <MtrtyDt> [0..1] Date 214
   IssueDate <IsseDt> [0..1] Date 214
   NextCallableDate <NxtCllblDt> [0..1] Date 214
   PutableDate <PutblDt> [0..1] Date 215
   DatedDate <DtdDt> [0..1] Date 215
   FirstPaymentDate <FrstPmtDt> [0..1] Date 215
   PreviousFactor <PrvsFctr> [0..1] Rate 215
   CurrentFactor <CurFctr> [0..1] Rate 215
   NextFactor <NxtFctr> [0..1] Rate 215
   InterestRate <IntrstRate> [0..1] Rate 215
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 215
   NextInterestRate <NxtIntrstRate> [0..1] Rate 216
   IndexRateBasis <IndxRateBsis> [0..1] Rate 216
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 216
   PoolNumber <PoolNb> [0..1] ± 216
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 216
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 217
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 185 September 2025
```

