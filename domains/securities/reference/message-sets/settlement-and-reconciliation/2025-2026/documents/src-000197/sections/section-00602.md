---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.9 SecuritiesFinancingDetails <SctiesFincgDtls>"]
file_pages: [914, 915]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.9 SecuritiesFinancingDetails <SctiesFincgDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 914 to 915.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 914

```text
27.4.9 SecuritiesFinancingDetails <SctiesFincgDtls>
Presence: [1..1]
Definition: Details for the closing of the securities financing transaction.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 914 March 2026
```

## File page 915

```text
SecuritiesFinancingDetails <SctiesFincgDtls> contains the following
SecuritiesFinancingTransactionDetails56 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 916
   SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 916
   ClosingLegIdentification <ClsgLegId> [0..1] Text 916
   TerminationDate <TermntnDt> [0..1] ± 916
   RateChangeDate <RateChngDt> [0..1] ± 916
   EarliestCallBackDate <EarlstCallBckDt> [0..1] ± 917
   CommissionCalculationDate <ComssnClctnDt> [0..1] ± 917
   RateType <RateTp> [0..1] ± 917
   Revaluation <Rvaltn> [0..1] ± 917
   LegalFramework <LglFrmwk> [0..1] ± 918
   InterestComputationMethod <IntrstCmptnMtd> [0..1] ± 918
   MaturityDateModification <MtrtyDtMod> [0..1] Indicator 918
   InterestPayment <IntrstPmt> [0..1] Indicator 918
   VariableRateSupport <VarblRateSpprt> [0..1] ± 919
   RepurchaseRate <RpRate> [0..1] ± C66 919
   StockLoanMargin <StockLnMrgn> [0..1] ± C66 919
   SecuritiesHaircut <SctiesHrcut> [0..1] ± C66 920
   ChargesRate <ChrgsRate> [0..1] ± C66 920
   PricingRate <PricgRate> [0..1] ± 920
   Spread <Sprd> [0..1] ± C66 921
   TransactionCallDelay <TxCallDely> [0..1] Text 921
   TotalNumberOfCollateralInstructions
<TtlNbOfCollInstrs>
[0..1] Text 921
   DealAmount <DealAmt> [0..1] ± 921
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 922
   ForfeitAmount <FrftAmt> [0..1] ± 922
   PremiumAmount <PrmAmt> [0..1] ± 922
   TerminationAmountPerPieceOfCollateral
<TermntnAmtPerPcOfColl>
[0..1] ± 923
   TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 923
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 915 March 2026
```

