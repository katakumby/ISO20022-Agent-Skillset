---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.5 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [1268, 1269]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.5 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1268 to 1269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1268

```text
32.4.2.3.5  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Attributes defining a financial instrument.
Impacted by: C4 "AdditionalDetailsRule", C53 "PlaceOfListingRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1268 March 2026
```

## File page 1269

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
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1269 March 2026
```

