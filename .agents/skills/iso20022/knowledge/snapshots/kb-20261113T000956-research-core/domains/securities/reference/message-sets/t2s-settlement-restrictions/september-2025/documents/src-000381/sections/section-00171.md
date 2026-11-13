---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92"]
file_pages: [209, 210]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2 FinancialInstrumentAttributes92

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 209 to 210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 209

```text
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 344
9.1.9.2  FinancialInstrumentAttributes92
Definition: Elements characterising a financial instrument.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 209 September 2025
```

## File page 210

```text
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
   CallableIndicator <CllblInd> [0..1] Indicator 217
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 210 September 2025
```

