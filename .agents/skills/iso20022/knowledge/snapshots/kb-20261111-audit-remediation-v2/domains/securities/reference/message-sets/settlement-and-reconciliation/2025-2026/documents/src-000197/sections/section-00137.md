---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.2 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [187, 188, 189]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.2 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 187 to 189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 187

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
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
7.4.6.2  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 187 March 2026
```

## File page 188

```text
Impacted by: C3 "AdditionalDetailsRule", C17 "PlaceOfListingRule"
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 188 March 2026
```

## File page 189

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes112" on page 1461 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 1463
   DayCountBasis <DayCntBsis> [0..1] ± 1463
   RegistrationForm <RegnForm> [0..1] ± 1464
   PaymentFrequency <PmtFrqcy> [0..1] ± 1464
   PaymentStatus <PmtSts> [0..1] ± 1464
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 1464
   ClassificationType <ClssfctnTp> [0..1] ± 1465
   OptionStyle <OptnStyle> [0..1] ± 1465
   OptionType <OptnTp> [0..1] ± 1465
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1465
   CouponDate <CpnDt> [0..1] Date 1466
   ExpiryDate <XpryDt> [0..1] Date 1466
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 1466
   MaturityDate <MtrtyDt> [0..1] Date 1466
   IssueDate <IsseDt> [0..1] Date 1466
   NextCallableDate <NxtCllblDt> [0..1] Date 1466
   PutableDate <PutblDt> [0..1] Date 1467
   DatedDate <DtdDt> [0..1] Date 1467
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1467
   PreviousFactor <PrvsFctr> [0..1] Rate 1467
   CurrentFactor <CurFctr> [0..1] Rate 1467
   NextFactor <NxtFctr> [0..1] Rate 1467
   InterestRate <IntrstRate> [0..1] Rate 1467
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 1467
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1468
   IndexRateBasis <IndxRateBsis> [0..1] Rate 1468
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 1468
   PoolNumber <PoolNb> [0..1] ± 1468
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1468
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1469
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 189 March 2026
```

