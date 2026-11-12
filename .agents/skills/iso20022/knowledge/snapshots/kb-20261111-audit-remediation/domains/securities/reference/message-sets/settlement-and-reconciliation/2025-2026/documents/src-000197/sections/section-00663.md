---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.2 Structure"]
file_pages: [996, 997, 998, 999]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 996 to 999.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 996

```text
29.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesFincgConf> [1..1]  C10,
C16,
C38,
C49,
C50
   TransactionIdentificationDetails <TxIdDtls> [1..1] ± C56 1007
   AdditionalParameters <AddtlParams> [0..1] ± C30 1009
   TradeDetails <TradDtls> [1..1]  C3, C15,
C23,
C36,
C55
1010
     PlaceOfTrade <PlcOfTrad> [0..1] ± 1011
     PlaceOfClearing <PlcOfClr> [0..1] ± 1012
     TradeDate <TradDt> [0..1] ± 1012
     SettlementDate <SttlmDt> [0..1] ± 1012
     EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 1012
     DealPrice <DealPric> [0..1] ± 1013
     Reporting <Rptg> [0..*] ± 1013
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C28 1013
     TradeTransactionCondition <TradTxCond> [0..*] ± 1014
     InvestorCapacity <InvstrCpcty> [0..1] ± 1014
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1014
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1014
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1015
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
C26,
C29
1015
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C35 1016
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1]  C39,
C43,
C47
1018
     SettledQuantity <SttldQty> [1..1] ± 1019
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C20 1020
     RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C20 1020
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 996 March 2026
```

## File page 997

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 1021
     RemainingToBeSettledAmount <RmngToBeSttldAmt> [0..1] ± 1021
     AccountOwner <AcctOwnr> [0..1] ± 1021
     SafekeepingAccount <SfkpgAcct> [0..1] ± 1021
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1022
     CashAccount <CshAcct> [0..1] ± 1022
     SafekeepingPlace <SfkpgPlc> [0..1] ± C48 1022
   SecuritiesFinancingDetails <SctiesFincgDtls> [0..1]  1023
     SecuritiesFinancingTradeIdentification <SctiesFincgTradId> [0..1] Text 1025
     SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 1025
     ClosingLegIdentification <ClsgLegId> [0..1] Text 1025
     TerminationDate <TermntnDt> [0..1] ± 1025
     RateChangeDate <RateChngDt> [0..1] ± 1025
     EarliestCallBackDate <EarlstCallBckDt> [0..1] ± 1026
     CommissionCalculationDate <ComssnClctnDt> [0..1] ± 1026
     RateType <RateTp> [0..1] ± 1026
     Revaluation <Rvaltn> [0..1] ± 1026
     LegalFramework <LglFrmwk> [0..1] ± 1027
     InterestComputationMethod <IntrstCmptnMtd> [0..1] ± 1027
     MaturityDateModification <MtrtyDtMod> [0..1] Indicator 1027
     InterestPayment <IntrstPmt> [0..1] Indicator 1027
     VariableRateSupport <VarblRateSpprt> [0..1] ± 1028
     RepurchaseRate <RpRate> [0..1] ± C53 1028
     StockLoanMargin <StockLnMrgn> [0..1] ± C53 1028
     SecuritiesHaircut <SctiesHrcut> [0..1] ± C53 1029
     ChargesRate <ChrgsRate> [0..1] ± C53 1029
     PricingRate <PricgRate> [0..1] ± 1029
     Spread <Sprd> [0..1] ± C53 1030
     TransactionCallDelay <TxCallDely> [0..1] Text 1030
     TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs> [0..1] Text 1030
     DealAmount <DealAmt> [0..1] ± 1030
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 997 March 2026
```

## File page 998

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1031
     ForfeitAmount <FrftAmt> [0..1] ± 1031
     PremiumAmount <PrmAmt> [0..1] ± 1031
     TerminationAmountPerPieceOfCollateral
<TermntnAmtPerPcOfColl>
[0..1] ± 1032
     TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 1032
     SecondLegNarrative <ScndLegNrrtv> [0..1] Text 1032
   StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C57 1032
     SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 1033
     Counterparty <CtrPty> [1..1] ± 1033
     Vendor <Vndr> [0..1] ± 1034
     OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C9, C17,
C31,
C32,
C33,
C34,
C51
1034
     OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C9, C17,
C31,
C32,
C33,
C34,
C51
1036
   SettlementParameters <SttlmParams> [0..1]  C11,
C52
1038
     Priority <Prty> [0..1] ± 1038
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1039
     SettlingCapacity <SttlgCpcty> [0..1] ± 1039
     StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1039
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 1040
     BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1040
     CashClearingSystem <CshClrSys> [0..1] ± 1040
     TaxCapacity <TaxCpcty> [0..1] ± 1040
     MarketClientSide <MktClntSd> [0..1] ± 1041
     BlockTrade <BlckTrad> [0..1] ± 1041
     LegalRestrictions <LglRstrctns> [0..1] ± 1041
     SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1041
     NettingEligibility <NetgElgblty> [0..1] ± 1042
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 998 March 2026
```

## File page 999

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     CCPEligibility <CCPElgblty> [0..1] ± 1042
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1042
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1043
     EligibleForCollateral <ElgblForColl> [0..1] Indicator 1043
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C9, C17,
C31,
C32,
C33,
C34,
C51
1043
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C9, C17,
C31,
C32,
C33,
C34,
C51
1045
   CashParties <CshPties> [0..1] ± 1047
   SettledAmount <SttldAmt> [0..1] ± 1048
   OtherAmounts <OthrAmts> [0..1] ± 1048
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1049
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
C26,
C29
1050
     Quantity <Qty> [1..1]  1051
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1051
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1051
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1051
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1052
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C7 1052
Or}       LEI <LEI> [1..1] IdentifierSet 1052
   OtherBusinessParties <OthrBizPties> [0..1]  C24,
C37
1052
     Investor <Invstr> [0..*] ± C22,
C41,
C45
1053
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C42,
C46
1054
     StockExchange <StockXchg> [0..1] ± 1055
     TradeRegulator <TradRgltr> [0..1] ± 1055
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 999 March 2026
```

