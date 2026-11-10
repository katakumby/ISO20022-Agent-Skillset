---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.2 Structure"]
file_pages: [1061, 1062]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1061 to 1062.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1061

```text
30.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesFincgModInstr> [1..1]  C31
   TransactionTypeAndModificationAdditionalParameters
<TxTpAndModAddtlParams>
[1..1] ± 1067
   TradeDetails <TradDtls> [1..1] ± C3, C36 1067
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C12,
C13,
C17,
C18,
C20
1068
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1] ± C25,
C27,
C29
1069
   SecuritiesFinancingAdditionalDetails <SctiesFincgAddtlDtls> [1..1]  1070
     SecuritiesFinancingTradeIdentification <SctiesFincgTradId> [0..1] Text 1072
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
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1061 March 2026
```

## File page 1062

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     TransactionCallDelay <TxCallDely> [0..1] Text 1077
     TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs> [0..1] Text 1077
     LocalBrokerCommission <LclBrkrComssn> [0..1] ± 1077
     DealAmount <DealAmt> [0..1] ± 1078
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1078
     ForfeitAmount <FrftAmt> [0..1] ± 1078
     PremiumAmount <PrmAmt> [0..1] ± 1078
     TerminationAmountPerPieceOfCollateral
<TermntnAmtPerPcOfColl>
[0..1] ± 1079
     TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 1079
     SecondLegNarrative <ScndLegNrrtv> [0..1] Text 1079
   SettlementParameters <SttlmParams> [0..1]  C7, C15,
C33
1079
     HoldIndicator <HldInd> [0..1] Indicator 1081
     Priority <Prty> [0..1] ± 1081
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1081
     SettlingCapacity <SttlgCpcty> [0..1] ± 1081
     StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1081
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 1082
     BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1082
     CashClearingSystem <CshClrSys> [0..1] ± 1082
     TaxCapacity <TaxCpcty> [0..1] ± 1083
     MarketClientSide <MktClntSd> [0..1] ± 1083
     FXStandingInstruction <FxStgInstr> [0..1] ± 1083
     BlockTrade <BlckTrad> [0..1] ± 1083
     LegalRestrictions <LglRstrctns> [0..1] ± 1084
     SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1084
     NettingEligibility <NetgElgblty> [0..1] ± 1084
     CCPEligibility <CCPElgblty> [0..1] ± 1084
     Tracking <Trckg> [0..1] ± 1085
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1085
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1085
     EligibleForCollateral <ElgblForColl> [0..1] Indicator 1086
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1062 March 2026
```

