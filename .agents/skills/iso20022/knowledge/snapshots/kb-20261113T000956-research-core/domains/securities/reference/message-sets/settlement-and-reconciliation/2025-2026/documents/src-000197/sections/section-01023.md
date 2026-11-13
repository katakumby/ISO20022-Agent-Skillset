---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112"]
file_pages: [1461, 1462]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4 FinancialInstrumentAttributes112

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1461 to 1462.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1461

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.1.11.4  FinancialInstrumentAttributes112
Definition: Elements characterising a financial instrument.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1461 March 2026
```

## File page 1462

```text
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
   CallableIndicator <CllblInd> [0..1] Indicator 1469
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1462 March 2026
```

