---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.2 Structure"]
file_pages: [78, 79, 80, 81, 82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.2 Structure

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 78 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxQryRspn> [1..1]  C3, C4,
C28
   Pagination <Pgntn> [1..1] ± 90
   ReportGeneralDetails <RptGnlDtls> [1..1]  C29 90
     ReportIdentification <RptId> [0..1] Text 91
     QueryReference <QryRef> [0..1] Text 91
     QueryType <QryTp> [1..1] CodeSet 91
     ActivityIndicator <ActvtyInd> [1..1] Indicator 91
   Transactions <Txs> [0..*]  C1, C30 92
     AccountOwner <AcctOwnr> [0..1] ± 98
     SafekeepingAccount <SfkpgAcct> [0..1] ± 98
     StatusAndReason <StsAndRsn> [0..1]  C25,
C34
99
       InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 101
       MatchingStatus <MtchgSts> [0..1] ± 101
       SettlementStatus <SttlmSts> [0..1] ± C26 102
       InstructionProcessingStatus <InstrPrcgSts> [0..1]  103
{Or         PendingProcessing <PdgPrcg> [1..1]  104
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 105
Or}           Reason <Rsn> [1..*]  105
             Code <Cd> [1..1]  105
{Or               Code <Cd> [1..1] CodeSet 106
Or}               Proprietary <Prtry> [1..1] ± 107
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 107
Or         CancellationRequested <CxlReqd> [1..1] ± C6 107
Or         AcknowledgedAccepted <AckdAccptd> [1..1] ± 108
Or         Cancelled <Canc> [1..1] ± 108
Or         Generated <Gnrtd> [1..1]  108
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 109
Or}           Reason <Rsn> [1..*] ± 109
Or         Repair <Rpr> [1..1] ± 109
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 78 March 2026
```

## File page 79

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         PendingCancellation <PdgCxl> [1..1]  109
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 110
Or}           Reason <Rsn> [1..*]  110
             Code <Cd> [1..1]  110
{Or               Code <Cd> [1..1] CodeSet 111
Or}               Proprietary <Prtry> [1..1] ± 111
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 111
Or}         ModificationRequested <ModReqd> [1..1] ± C6 112
       Settled <Sttld> [0..1] ± C6 112
       Proprietary <Prtry> [0..1] ± 112
     Transaction <Tx> [1..*]  C18 113
       AccountOwner <AcctOwnr> [0..1] ± 118
       SafekeepingAccount <SfkpgAcct> [0..1] ± 118
       StatusAndReason <StsAndRsn> [0..1]  C25,
C34
119
         InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 121
         MatchingStatus <MtchgSts> [0..1] ± 121
         SettlementStatus <SttlmSts> [0..1] ± C26 122
         InstructionProcessingStatus <InstrPrcgSts> [0..1]  123
{Or           PendingProcessing <PdgPrcg> [1..1]  124
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 125
Or}             Reason <Rsn> [1..*]  125
               Code <Cd> [1..1]  125
{Or                 Code <Cd> [1..1] CodeSet 126
Or}                 Proprietary <Prtry> [1..1] ± 127
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 127
Or           CancellationRequested <CxlReqd> [1..1] ± C6 127
Or           AcknowledgedAccepted <AckdAccptd> [1..1] ± 128
Or           Cancelled <Canc> [1..1] ± 128
Or           Generated <Gnrtd> [1..1]  128
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 129
Or}             Reason <Rsn> [1..*] ± 129
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 79 March 2026
```

## File page 80

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           Repair <Rpr> [1..1] ± 129
Or           PendingCancellation <PdgCxl> [1..1]  129
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 130
Or}             Reason <Rsn> [1..*]  130
               Code <Cd> [1..1]  130
{Or                 Code <Cd> [1..1] CodeSet 131
Or}                 Proprietary <Prtry> [1..1] ± 131
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 131
Or}           ModificationRequested <ModReqd> [1..1] ± C6 132
         Settled <Sttld> [0..1] ± C6 132
         Proprietary <Prtry> [0..1] ± 132
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 133
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 133
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 133
       CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 133
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 133
       TradeIdentification <TradId> [0..*] Text 133
       UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 133
       PoolIdentification <PoolId> [0..1] Text 133
       CommonIdentification <CmonId> [0..1] Text 134
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 134
       ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 134
       ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 134
       TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 134
       TripartyAgentServiceProviderCollateralInstructionIdentific
ation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 134
       TransactionDetails <TxDtls> [0..1]  C5, C27,
C37,
C38
134
         TransactionActivity <TxActvty> [1..1] ± 140
         SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 140
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 80 March 2026
```

## File page 81

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 141
         Payment <Pmt> [1..1] CodeSet 141
         SettlementParameters <SttlmParams> [0..1]  C8, C14,
C32,
C33
141
           HoldIndicator <HldInd> [0..1] ± 144
           Priority <Prty> [0..1] ± 144
           SecuritiesTransactionType <SctiesTxTp> [0..1] ± 144
           SettlementTransactionCondition <SttlmTxCond> [0..*] ± 144
           PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 145
           BeneficialOwnership <BnfclOwnrsh> [0..1] ± 145
           BlockTrade <BlckTrad> [0..1] ± 145
           CCPEligibility <CCPElgblty> [0..1] ± 146
           DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 146
           CashClearingSystem <CshClrSys> [0..1] ± 146
           ExposureType <XpsrTp> [0..1] ± 146
           FXStandingInstruction <FxStgInstr> [0..1] ± 147
           MarketClientSide <MktClntSd> [0..1] ± 147
           NettingEligibility <NetgElgblty> [0..1] ± 147
           Registration <Regn> [0..1] ± 147
           RepurchaseType <RpTp> [0..1] ± 148
           LegalRestrictions <LglRstrctns> [0..1] ± 148
           SecuritiesRTGS <SctiesRTGS> [0..1] ± 148
           SettlingCapacity <SttlgCpcty> [0..1] ± 148
           SettlementSystemMethod <SttlmSysMtd> [0..1] ± 149
           TaxCapacity <TaxCpcty> [0..1] ± 149
           StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 149
           Tracking <Trckg> [0..1] ± 149
           AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 150
           LetterOfGuarantee <LttrOfGrnt> [0..1] ± 150
           ReturnLeg <RtrLeg> [0..1] Indicator 150
           ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 150
           EligibleForCollateral <ElgblForColl> [0..1] Indicator 151
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 81 March 2026
```

## File page 82

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 151
           CashSubBalanceType <CshSubBalTp> [0..1] ± 151
         PlaceOfTrade <PlcOfTrad> [0..1] ± 151
         SafekeepingPlace <SfkpgPlc> [0..1] ± C31 152
         PlaceOfClearing <PlcOfClr> [0..1] ± 152
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C20
152
         CountryOfIssue <CtryOfIsse> [0..1] CodeSet C9 153
         ConditionalSecuritiesDelivery <CondlSctiesDlvry> [0..1] Indicator 154
         SettlementQuantity <SttlmQty> [1..1] ± 154
         SettledQuantity <SttldQty> [0..1] ± 154
         PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 155
         RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 155
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 155
         SettlementAmount <SttlmAmt> [1..1] ± 155
         SettledAmount <SttldAmt> [0..1] ± 156
         PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 156
         RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 156
         AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 156
         TradeDate <TradDt> [0..1] ± 157
         IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 157
         EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 157
         ValueDate <ValDt> [0..1] ± 158
         StatusDate <StsDt> [0..1] DateTime 158
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 158
         MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 158
         Linkages <Lnkgs> [0..*]  158
           ProcessingPosition <PrcgPos> [0..1] ± C39 159
           MessageNumber <MsgNb> [0..1] ± C35 159
           Reference <Ref> [1..1]  160
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 82 March 2026
```

