---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.2 Structure"]
file_pages: [2474, 2475, 2476, 2477, 2478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2474 to 2478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2474

```text
72.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxQryRspn> [1..1]  C3, C4,
C28
   Pagination <Pgntn> [1..1] ± 2486
   ReportGeneralDetails <RptGnlDtls> [1..1]  C29 2486
     ReportIdentification <RptId> [0..1] Text 2487
     QueryReference <QryRef> [0..1] Text 2487
     QueryType <QryTp> [1..1] CodeSet 2487
     ActivityIndicator <ActvtyInd> [1..1] Indicator 2487
   Transactions <Txs> [0..*]  C1, C30 2488
     AccountOwner <AcctOwnr> [0..1] ± 2494
     SafekeepingAccount <SfkpgAcct> [0..1] ± 2494
     StatusAndReason <StsAndRsn> [0..1]  C25,
C34
2495
       InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 2497
       MatchingStatus <MtchgSts> [0..1] ± 2497
       SettlementStatus <SttlmSts> [0..1] ± C26 2498
       InstructionProcessingStatus <InstrPrcgSts> [0..1]  2499
{Or         PendingProcessing <PdgPrcg> [1..1]  2500
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2501
Or}           Reason <Rsn> [1..*]  2501
             Code <Cd> [1..1]  2501
{Or               Code <Cd> [1..1] CodeSet 2502
Or}               Proprietary <Prtry> [1..1] ± 2503
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2503
Or         CancellationRequested <CxlReqd> [1..1] ± C6 2503
Or         AcknowledgedAccepted <AckdAccptd> [1..1] ± 2504
Or         Cancelled <Canc> [1..1] ± 2504
Or         Generated <Gnrtd> [1..1]  2504
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2505
Or}           Reason <Rsn> [1..*] ± 2505
Or         Repair <Rpr> [1..1] ± 2505
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2474 August 2026
```

## File page 2475

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         PendingCancellation <PdgCxl> [1..1]  2505
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2506
Or}           Reason <Rsn> [1..*]  2506
             Code <Cd> [1..1]  2506
{Or               Code <Cd> [1..1] CodeSet 2507
Or}               Proprietary <Prtry> [1..1] ± 2507
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2507
Or}         ModificationRequested <ModReqd> [1..1] ± C6 2508
       Settled <Sttld> [0..1] ± C6 2508
       Proprietary <Prtry> [0..1] ± 2508
     Transaction <Tx> [1..*]  C18 2509
       AccountOwner <AcctOwnr> [0..1] ± 2514
       SafekeepingAccount <SfkpgAcct> [0..1] ± 2514
       StatusAndReason <StsAndRsn> [0..1]  C25,
C34
2515
         InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 2517
         MatchingStatus <MtchgSts> [0..1] ± 2517
         SettlementStatus <SttlmSts> [0..1] ± C26 2518
         InstructionProcessingStatus <InstrPrcgSts> [0..1]  2519
{Or           PendingProcessing <PdgPrcg> [1..1]  2520
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2521
Or}             Reason <Rsn> [1..*]  2521
               Code <Cd> [1..1]  2521
{Or                 Code <Cd> [1..1] CodeSet 2522
Or}                 Proprietary <Prtry> [1..1] ± 2523
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2523
Or           CancellationRequested <CxlReqd> [1..1] ± C6 2523
Or           AcknowledgedAccepted <AckdAccptd> [1..1] ± 2524
Or           Cancelled <Canc> [1..1] ± 2524
Or           Generated <Gnrtd> [1..1]  2524
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2525
Or}             Reason <Rsn> [1..*] ± 2525
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2475 August 2026
```

## File page 2476

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           Repair <Rpr> [1..1] ± 2525
Or           PendingCancellation <PdgCxl> [1..1]  2525
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2526
Or}             Reason <Rsn> [1..*]  2526
               Code <Cd> [1..1]  2526
{Or                 Code <Cd> [1..1] CodeSet 2527
Or}                 Proprietary <Prtry> [1..1] ± 2527
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2527
Or}           ModificationRequested <ModReqd> [1..1] ± C6 2528
         Settled <Sttld> [0..1] ± C6 2528
         Proprietary <Prtry> [0..1] ± 2528
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 2529
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2529
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2529
       CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 2529
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2529
       TradeIdentification <TradId> [0..*] Text 2529
       UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 2529
       PoolIdentification <PoolId> [0..1] Text 2529
       CommonIdentification <CmonId> [0..1] Text 2530
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2530
       ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 2530
       ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 2530
       TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 2530
       TripartyAgentServiceProviderCollateralInstructionIdentific
ation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 2530
       TransactionDetails <TxDtls> [0..1]  C5, C27,
C37,
C38
2530
         TransactionActivity <TxActvty> [1..1] ± 2536
         SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 2536
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2476 August 2026
```

## File page 2477

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 2537
         Payment <Pmt> [1..1] CodeSet 2537
         SettlementParameters <SttlmParams> [0..1]  C8, C14,
C32,
C33
2537
           HoldIndicator <HldInd> [0..1] ± 2540
           Priority <Prty> [0..1] ± 2540
           SecuritiesTransactionType <SctiesTxTp> [0..1] ± 2540
           SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2540
           PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 2541
           BeneficialOwnership <BnfclOwnrsh> [0..1] ± 2541
           BlockTrade <BlckTrad> [0..1] ± 2541
           CCPEligibility <CCPElgblty> [0..1] ± 2542
           DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 2542
           CashClearingSystem <CshClrSys> [0..1] ± 2542
           ExposureType <XpsrTp> [0..1] ± 2542
           FXStandingInstruction <FxStgInstr> [0..1] ± 2543
           MarketClientSide <MktClntSd> [0..1] ± 2543
           NettingEligibility <NetgElgblty> [0..1] ± 2543
           Registration <Regn> [0..1] ± 2543
           RepurchaseType <RpTp> [0..1] ± 2544
           LegalRestrictions <LglRstrctns> [0..1] ± 2544
           SecuritiesRTGS <SctiesRTGS> [0..1] ± 2544
           SettlingCapacity <SttlgCpcty> [0..1] ± 2544
           SettlementSystemMethod <SttlmSysMtd> [0..1] ± 2545
           TaxCapacity <TaxCpcty> [0..1] ± 2545
           StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 2545
           Tracking <Trckg> [0..1] ± 2545
           AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 2546
           LetterOfGuarantee <LttrOfGrnt> [0..1] ± 2546
           ReturnLeg <RtrLeg> [0..1] Indicator 2546
           ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 2546
           EligibleForCollateral <ElgblForColl> [0..1] Indicator 2547
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2477 August 2026
```

## File page 2478

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 2547
           CashSubBalanceType <CshSubBalTp> [0..1] ± 2547
         PlaceOfTrade <PlcOfTrad> [0..1] ± 2547
         SafekeepingPlace <SfkpgPlc> [0..1] ± C31 2548
         PlaceOfClearing <PlcOfClr> [0..1] ± 2548
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C20
2548
         CountryOfIssue <CtryOfIsse> [0..1] CodeSet C9 2549
         ConditionalSecuritiesDelivery <CondlSctiesDlvry> [0..1] Indicator 2550
         SettlementQuantity <SttlmQty> [1..1] ± 2550
         SettledQuantity <SttldQty> [0..1] ± 2550
         PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 2551
         RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 2551
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 2551
         SettlementAmount <SttlmAmt> [1..1] ± 2551
         SettledAmount <SttldAmt> [0..1] ± 2552
         PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 2552
         RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 2552
         AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 2552
         TradeDate <TradDt> [0..1] ± 2553
         IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2553
         EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 2553
         ValueDate <ValDt> [0..1] ± 2554
         StatusDate <StsDt> [0..1] DateTime 2554
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2554
         MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 2554
         Linkages <Lnkgs> [0..*]  2554
           ProcessingPosition <PrcgPos> [0..1] ± C39 2555
           MessageNumber <MsgNb> [0..1] ± C35 2555
           Reference <Ref> [1..1]  2556
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2478 August 2026
```

