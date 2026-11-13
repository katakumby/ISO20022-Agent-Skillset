---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.10 MovementDetails <MvmntDtls>", "3.4.3.4.10.4 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [77, 78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.10.4 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 77 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 207 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 208
   OtherIdentification <OthrId> [0..*]  208
     Identification <Id> [1..1] Text 208
     Suffix <Sfx> [0..1] Text 208
     Type <Tp> [1..1] ± 208
   Description <Desc> [0..1] Text 208
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
3.4.3.4.10.4  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C5 "AdditionalDetailsRule", C17 "PlaceOfListingRule"
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 77 September 2025
```

## File page 78

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
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 78 September 2025
```

