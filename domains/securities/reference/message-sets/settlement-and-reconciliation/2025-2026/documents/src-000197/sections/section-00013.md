---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.2 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [34, 35, 36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.2 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 34 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

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
2.4.8.2  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument other than a investment funds.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 34 March 2026
```

## File page 35

```text
Impacted by: C5 "AdditionalDetailsRule", C26 "PlaceOfListingRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 35 March 2026
```

## File page 36

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes111" on page 1445 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 1447
   DayCountBasis <DayCntBsis> [0..1] ± 1447
   RegistrationForm <RegnForm> [0..1] ± 1448
   PaymentFrequency <PmtFrqcy> [0..1] ± 1448
   PaymentStatus <PmtSts> [0..1] ± 1448
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 1448
   ClassificationType <ClssfctnTp> [0..1] ± 1449
   OptionStyle <OptnStyle> [0..1] ± 1449
   OptionType <OptnTp> [0..1] ± 1449
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1449
   CouponDate <CpnDt> [0..1] Date 1450
   ExpiryDate <XpryDt> [0..1] Date 1450
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 1450
   MaturityDate <MtrtyDt> [0..1] Date 1450
   IssueDate <IsseDt> [0..1] Date 1450
   NextCallableDate <NxtCllblDt> [0..1] Date 1450
   PutableDate <PutblDt> [0..1] Date 1451
   DatedDate <DtdDt> [0..1] Date 1451
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1451
   PreviousFactor <PrvsFctr> [0..1] Rate 1451
   CurrentFactor <CurFctr> [0..1] Rate 1451
   NextFactor <NxtFctr> [0..1] Rate 1451
   InterestRate <IntrstRate> [0..1] Rate 1451
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 1451
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1452
   IndexRateBasis <IndxRateBsis> [0..1] Rate 1452
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 1452
   PoolNumber <PoolNb> [0..1] ± 1452
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1452
   CallableIndicator <CllblInd> [0..1] Indicator 1453
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 36 March 2026
```

