---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.2 Structure"]
file_pages: [882, 883, 884, 885]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 882 to 885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 882

```text
27.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesFincgInstr> [1..1]  C11,
C12,
C20,
C21,
C45,
C46,
C60,
C61,
C62,
C59
   TransactionIdentification <TxId> [1..1] Text 895
   TransactionTypeAndAdditionalParameters
<TxTpAndAddtlParams>
[1..1] ± 895
   NumberCounts <NbCounts> [0..1] ± C18 895
   Linkages <Lnkgs> [0..*]  C34 896
     ProcessingPosition <PrcgPos> [0..1] ± C70 896
     MessageNumber <MsgNb> [0..1] ± C65 897
     Reference <Ref> [1..1] ± 897
     LinkedQuantity <LkdQty> [0..1]  898
{Or       PairedOffQuantity <PairdOffQty> [1..1] ± C26 898
Or}       TurnedQuantity <TrndQty> [1..1] ± C26 899
     ReferenceOwner <RefOwnr> [0..1] ± 899
   TradeDetails <TradDtls> [1..1]  C3, C17,
C30,
C43,
C68
899
     PlaceOfTrade <PlcOfTrad> [0..1] ± 901
     PlaceOfClearing <PlcOfClr> [0..1] ± 901
     TradeDate <TradDt> [0..1] ± 902
     OpeningSettlementDate <OpngSttlmDt> [1..1] ± 902
     DealPrice <DealPric> [0..1] ± 902
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C36 903
     Reporting <Rptg> [0..*] ± 903
     TradeTransactionCondition <TradTxCond> [0..*] ± 903
     InvestorCapacity <InvstrCpcty> [0..1] ± 904
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 904
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 904
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 882 March 2026
```

## File page 883

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     AffirmationStatus <AffirmSts> [0..1] ± 904
     MatchingStatus <MtchgSts> [0..1] ± 905
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 905
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 905
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C24,
C25,
C32,
C33,
C37
905
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C42 906
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1]  C22,
C47,
C51,
C55,
C57,
C58
909
     SettlementQuantity <SttlmQty> [1..1] ± 911
     DenominationChoice <DnmtnChc> [0..1] Text 911
     AccountOwner <AcctOwnr> [0..1] ± 911
     SafekeepingAccount <SfkpgAcct> [0..1] ± 912
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 912
     CashAccount <CshAcct> [0..1] ± 912
     SafekeepingPlace <SfkpgPlc> [0..1] ± C56 913
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 913
   SecuritiesFinancingDetails <SctiesFincgDtls> [1..1]  914
     SecuritiesFinancingTradeIdentification <SctiesFincgTradId> [0..1] Text 916
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
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 883 March 2026
```

## File page 884

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
     TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs> [0..1] Text 921
     DealAmount <DealAmt> [0..1] ± 921
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 922
     ForfeitAmount <FrftAmt> [0..1] ± 922
     PremiumAmount <PrmAmt> [0..1] ± 922
     TerminationAmountPerPieceOfCollateral
<TermntnAmtPerPcOfColl>
[0..1] ± 923
     TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 923
     SecondLegNarrative <ScndLegNrrtv> [0..1] Text 923
   SettlementParameters <SttlmParams> [0..1]  C13,
C27,
C64
923
     HoldIndicator <HldInd> [0..1] Indicator 925
     Priority <Prty> [0..1] ± 925
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 925
     SettlingCapacity <SttlgCpcty> [0..1] ± 925
     StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 925
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 926
     BeneficialOwnership <BnfclOwnrsh> [0..1] ± 926
     CashClearingSystem <CshClrSys> [0..1] ± 926
     TaxCapacity <TaxCpcty> [0..1] ± 927
     MarketClientSide <MktClntSd> [0..1] ± 927
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 884 March 2026
```

## File page 885

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     FXStandingInstruction <FxStgInstr> [0..1] ± 927
     BlockTrade <BlckTrad> [0..1] ± 927
     LegalRestrictions <LglRstrctns> [0..1] ± 928
     SettlementSystemMethod <SttlmSysMtd> [0..1] ± 928
     NettingEligibility <NetgElgblty> [0..1] ± 928
     CCPEligibility <CCPElgblty> [0..1] ± 928
     Tracking <Trckg> [0..1] ± 929
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 929
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 929
     EligibleForCollateral <ElgblForColl> [0..1] Indicator 930
   StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C69 930
     SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 931
     Counterparty <CtrPty> [1..1] ± 931
     Vendor <Vndr> [0..1] ± 931
     OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C10,
C23,
C38,
C39,
C40,
C41,
C63
931
     OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C10,
C23,
C38,
C39,
C40,
C41,
C63
933
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C10,
C23,
C38,
C39,
C40,
C41,
C63
935
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C10,
C23,
C38,
C39,
C40,
C41,
C63
937
   CashParties <CshPties> [0..1] ± 939
   OpeningSettlementAmount <OpngSttlmAmt> [0..1] ± 940
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 885 March 2026
```

