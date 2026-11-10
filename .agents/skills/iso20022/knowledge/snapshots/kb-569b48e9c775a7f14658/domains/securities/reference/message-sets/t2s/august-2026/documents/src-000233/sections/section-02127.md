---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.3 SubAccountDetails <SubAcctDtls>", "82.1.5.16.3.4 BalanceForSubAccount <BalForSubAcct>", "82.1.5.16.3.4.3 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [2887, 2888]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.3.4.3 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2887 to 2888.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2887

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
82.1.5.16.3.4.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument other than an investment fund.
Impacted by: C5 "AdditionalDetailsRule", C28 "PlaceOfListingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2887 August 2026
```

## File page 2888

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes138" on page 2923 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 2925
   DayCountBasis <DayCntBsis> [0..1] ± 2925
   RegistrationForm <RegnForm> [0..1] ± 2926
   PaymentFrequency <PmtFrqcy> [0..1] ± 2926
   PaymentStatus <PmtSts> [0..1] ± 2926
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 2926
   ClassificationType <ClssfctnTp> [0..1] ± 2927
   OptionStyle <OptnStyle> [0..1] ± 2927
   OptionType <OptnTp> [0..1] ± 2927
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 2927
   CouponDate <CpnDt> [0..1] Date 2928
   ExpiryDate <XpryDt> [0..1] Date 2928
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 2928
   MaturityDate <MtrtyDt> [0..1] Date 2928
   IssueDate <IsseDt> [0..1] Date 2928
   NextCallableDate <NxtCllblDt> [0..1] Date 2928
   PutableDate <PutblDt> [0..1] Date 2929
   DatedDate <DtdDt> [0..1] Date 2929
   FirstPaymentDate <FrstPmtDt> [0..1] Date 2929
   PreviousFactor <PrvsFctr> [0..1] Rate 2929
   CurrentFactor <CurFctr> [0..1] Rate 2929
   NextFactor <NxtFctr> [0..1] Rate 2929
   InterestRate <IntrstRate> [0..1] Rate 2929
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 2929
   NextInterestRate <NxtIntrstRate> [0..1] Rate 2930
   IndexRateBasis <IndxRateBsis> [0..1] Rate 2930
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 2930
   PoolNumber <PoolNb> [0..1] ± 2930
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 2930
   CallableIndicator <CllblInd> [0..1] Indicator 2931
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2888 August 2026
```

