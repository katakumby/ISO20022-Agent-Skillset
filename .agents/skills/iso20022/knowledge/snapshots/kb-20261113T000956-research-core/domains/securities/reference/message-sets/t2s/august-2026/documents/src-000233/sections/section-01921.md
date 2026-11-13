---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.10 MovementDetails <MvmntDtls>", "74.4.3.4.10.4 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [2632, 2633]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.10.4 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2632 to 2633.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2632

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
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
74.4.3.4.10.4  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C5 "AdditionalDetailsRule", C17 "PlaceOfListingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2632 August 2026
```

## File page 2633

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
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2633 August 2026
```

