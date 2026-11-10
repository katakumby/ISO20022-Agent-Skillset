---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.2 Structure"]
file_pages: [817, 818, 819, 820]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 817 to 820.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 817

```text
26.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxGnrtnNtfctn> [1..1]  C6, C18,
C19,
C22,
C50,
C63
   TransactionIdentificationDetails <TxIdDtls> [1..1] ± C39 0
   NumberCounts <NbCounts> [0..1] ± C20 830
   Linkages <Lnkgs> [0..*]  C37 831
     ProcessingPosition <PrcgPos> [0..1] ± C72 832
     MessageNumber <MsgNb> [0..1] ± C68 832
     Reference <Ref> [1..1]  833
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 833
Or       IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 833
Or       IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 833
Or       AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 834
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 834
Or       CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[1..1] Text 834
Or       PoolIdentification <PoolId> [1..1] Text 834
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 834
     LinkedQuantity <LkdQty> [0..1]  834
{Or       PairedOffQuantity <PairdOffQty> [1..1] ± C27 834
Or}       TurnedQuantity <TrndQty> [1..1] ± C27 835
     ReferenceOwner <RefOwnr> [0..1] ± 835
   TradeDetails <TradDtls> [1..1]  C3, C17,
C31,
C36,
C48,
C71,
C70
0
     TradeIdentification <TradId> [0..*] Text 839
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 839
     CollateralTransactionIdentification <CollTxId> [0..*] Text 839
     PlaceOfTrade <PlcOfTrad> [0..1] ± 839
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 817 March 2026
```

## File page 818

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PlaceOfClearing <PlcOfClr> [0..1] ± 839
     TradeDate <TradDt> [0..1] ± 840
     SettlementDate <SttlmDt> [1..1] ± 840
     LateDeliveryDate <LateDlvryDt> [0..1] ± 840
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 841
     MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 841
     DealPrice <DealPric> [0..1] ± 841
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C40 841
     OpeningClosing <OpngClsg> [0..1] ± 841
     Reporting <Rptg> [0..*] ± 842
     TradeTransactionCondition <TradTxCond> [0..*] ± 842
     InvestorCapacity <InvstrCpcty> [0..1] ± 842
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 842
     TypeOfPrice <TpOfPric> [0..1] ± 843
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 843
     MatchingStatus <MtchgSts> [0..1] ± 843
     AffirmationStatus <AffirmSts> [0..1] ± 843
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 844
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 844
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C25,
C26,
C33,
C34,
C41
844
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C47 845
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..*]  C23,
C51,
C55,
C59,
C61,
C62
847
     SettlementQuantity <SttlmQty> [1..1] ± 849
     DenominationChoice <DnmtnChc> [0..1] Text 849
     AccountOwner <AcctOwnr> [0..1] ± 849
     SafekeepingAccount <SfkpgAcct> [0..1] ± 850
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 850
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 818 March 2026
```

## File page 819

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     CashAccount <CshAcct> [0..1] ± 850
     SafekeepingPlace <SfkpgPlc> [0..1] ± C60 851
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 851
   SettlementParameters <SttlmParams> [1..1] ± C13,
C28,
C65,
C66
852
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C12,
C24,
C42,
C43,
C44,
C45,
C64
0
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C12,
C24,
C42,
C43,
C44,
C45,
C64
0
   CashParties <CshPties> [0..1] ± 0
   SettlementAmount <SttlmAmt> [0..1] ± 0
   OtherAmounts <OthrAmts> [0..1] ± 859
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  860
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C25,
C26,
C33,
C34,
C41
861
     Quantity <Qty> [1..1]  862
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 862
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 862
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  862
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 863
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C9 863
Or}       LEI <LEI> [1..1] IdentifierSet 863
   OtherBusinessParties <OthrBizPties> [0..1]  C32,
C49
0
     Investor <Invstr> [0..*] ± C30,
C53,
C57
864
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 819 March 2026
```

## File page 820

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C54,
C58
865
     StockExchange <StockXchg> [0..1] ± 866
     TradeRegulator <TradRgltr> [0..1] ± 866
     TripartyAgent <TrptyAgt> [0..1] ± C54,
C58
866
     Broker <Brkr> [0..1] ± C54,
C58
867
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  868
     CertificationIdentification <CertfctnId> [0..1] Text 869
     CertificationDateTime <CertfctnDtTm> [0..1] ± 869
     RegistrarAccount <RegarAcct> [0..1] Text 869
     CertificateNumber <CertNb> [0..*] ± C35 869
   GeneratedReason <GnrtdRsn> [0..*] ± 0
   StatusAndReason <StsAndRsn> [0..1]  C67 0
     ProcessingStatus <PrcgSts> [0..1]  871
{Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 871
Or       PendingProcessing <PdgPrcg> [1..1] ± 871
Or       Repair <Rpr> [1..1] ± 872
Or       PendingCancellation <PdgCxl> [1..1]  872
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 873
Or}         Reason <Rsn> [1..*]  873
           Code <Cd> [1..1]  873
{Or             Code <Cd> [1..1] CodeSet 874
Or}             Proprietary <Prtry> [1..1] ± 874
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 874
Or       Proprietary <Prtry> [1..1] ± 874
Or}       CancellationRequested <CxlReqd> [1..1] ± C7 875
     InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 875
     MatchingStatus <MtchgSts> [0..1] ± 876
     SettlementStatus <SttlmSts> [0..1] ± C46 876
   SupplementaryData <SplmtryData> [0..*] ± C69 0
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 820 March 2026
```

