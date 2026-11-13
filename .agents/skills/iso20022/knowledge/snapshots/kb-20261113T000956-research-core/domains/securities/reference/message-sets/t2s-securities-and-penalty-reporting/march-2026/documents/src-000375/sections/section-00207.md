---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.2 BalanceForAccount <BalForAcct>", "7.1.5.14.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [279, 280]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 279 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 279

```text
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
7.1.5.14.2.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument other than an investment fund.
Impacted by: C5 "AdditionalDetailsRule", C28 "PlaceOfListingRule"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 279 March 2026
```

## File page 280

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes138" on page 325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 327
   DayCountBasis <DayCntBsis> [0..1] ± 327
   RegistrationForm <RegnForm> [0..1] ± 328
   PaymentFrequency <PmtFrqcy> [0..1] ± 328
   PaymentStatus <PmtSts> [0..1] ± 328
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 328
   ClassificationType <ClssfctnTp> [0..1] ± 329
   OptionStyle <OptnStyle> [0..1] ± 329
   OptionType <OptnTp> [0..1] ± 329
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 329
   CouponDate <CpnDt> [0..1] Date 330
   ExpiryDate <XpryDt> [0..1] Date 330
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 330
   MaturityDate <MtrtyDt> [0..1] Date 330
   IssueDate <IsseDt> [0..1] Date 330
   NextCallableDate <NxtCllblDt> [0..1] Date 330
   PutableDate <PutblDt> [0..1] Date 331
   DatedDate <DtdDt> [0..1] Date 331
   FirstPaymentDate <FrstPmtDt> [0..1] Date 331
   PreviousFactor <PrvsFctr> [0..1] Rate 331
   CurrentFactor <CurFctr> [0..1] Rate 331
   NextFactor <NxtFctr> [0..1] Rate 331
   InterestRate <IntrstRate> [0..1] Rate 331
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 331
   NextInterestRate <NxtIntrstRate> [0..1] Rate 332
   IndexRateBasis <IndxRateBsis> [0..1] Rate 332
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 332
   PoolNumber <PoolNb> [0..1] ± 332
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 332
   CallableIndicator <CllblInd> [0..1] Indicator 333
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 280 March 2026
```

