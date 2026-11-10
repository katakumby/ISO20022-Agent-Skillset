---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.5 SecuritiesFinancingAdditionalDetails <SctiesFincgAddtlDtls>"]
file_pages: [1070, 1071]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.5 SecuritiesFinancingAdditionalDetails <SctiesFincgAddtlDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1070 to 1071.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1070

```text
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
30.4.5 SecuritiesFinancingAdditionalDetails
<SctiesFincgAddtlDtls>
Presence: [1..1]
Definition: Details of the closing of the securities financing transaction.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1070 March 2026
```

## File page 1071

```text
SecuritiesFinancingAdditionalDetails <SctiesFincgAddtlDtls> contains the following
SecuritiesFinancingTransactionDetails58 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 1072
   SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 1072
   ClosingLegIdentification <ClsgLegId> [0..1] Text 1072
   TerminationDate <TermntnDt> [0..1] ± 1072
   RateChangeDate <RateChngDt> [0..1] ± 1072
   EarliestCallBackDate <EarlstCallBckDt> [0..1] ± 1073
   CommissionCalculationDate <ComssnClctnDt> [0..1] ± 1073
   RateType <RateTp> [0..1] ± 1073
   Revaluation <Rvaltn> [0..1] ± 1073
   LegalFramework <LglFrmwk> [0..1] ± 1074
   InterestComputationMethod <IntrstCmptnMtd> [0..1] ± 1074
   MaturityDateModification <MtrtyDtMod> [0..1] Indicator 1074
   InterestPayment <IntrstPmt> [0..1] Indicator 1074
   VariableRateSupport <VarblRateSpprt> [0..1] ± 1075
   RepurchaseRate <RpRate> [0..1] ± C34 1075
   StockLoanMargin <StockLnMrgn> [0..1] ± C34 1075
   SecuritiesHaircut <SctiesHrcut> [0..1] ± C34 1076
   ChargesRate <ChrgsRate> [0..1] ± C34 1076
   PricingRate <PricgRate> [0..1] ± 1076
   Spread <Sprd> [0..1] ± C34 1077
   TransactionCallDelay <TxCallDely> [0..1] Text 1077
   TotalNumberOfCollateralInstructions
<TtlNbOfCollInstrs>
[0..1] Text 1077
   LocalBrokerCommission <LclBrkrComssn> [0..1] ± 1077
   DealAmount <DealAmt> [0..1] ± 1078
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1078
   ForfeitAmount <FrftAmt> [0..1] ± 1078
   PremiumAmount <PrmAmt> [0..1] ± 1078
   TerminationAmountPerPieceOfCollateral
<TermntnAmtPerPcOfColl>
[0..1] ± 1079
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1071 March 2026
```

