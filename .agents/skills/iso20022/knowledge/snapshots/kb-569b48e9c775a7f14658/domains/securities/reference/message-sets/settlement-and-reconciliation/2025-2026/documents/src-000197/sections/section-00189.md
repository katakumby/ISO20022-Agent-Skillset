---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.2 Structure"]
file_pages: [275, 276, 277, 278, 279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 275 to 279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 275

```text
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxPdgRpt> [1..1]  C31,
C33,
C35,
C37
   Pagination <Pgntn> [1..1] ± 0
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± C30 287
   AccountOwner <AcctOwnr> [0..1] ± 0
   SafekeepingAccount <SfkpgAcct> [0..1] ± 0
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 0
   Status <Sts> [0..*]  289
     StatusAndReason <StsAndRsn> [1..1]  C26,
C39
292
{Or       Proprietary <Prtry> [1..1] ± 294
Or       MatchingStatus <MtchgSts> [1..1] ± 294
Or       InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 294
Or       SettlementStatus <SttlmSts> [1..1] ± C27 295
Or}       InstructionProcessingStatus <InstrPrcgSts> [1..1]  295
{Or         PendingProcessing <PdgPrcg> [1..1]  296
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 297
Or}           Reason <Rsn> [1..*]  297
             Code <Cd> [1..1]  297
{Or               Code <Cd> [1..1] CodeSet 298
Or}               Proprietary <Prtry> [1..1] ± 299
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 299
Or         CancellationRequested <CxlReqd> [1..1] ± C4 299
Or         AcknowledgedAccepted <AckdAccptd> [1..1] ± 300
Or         Cancelled <Canc> [1..1] ± 300
Or         Generated <Gnrtd> [1..1]  300
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 301
Or}           Reason <Rsn> [1..*] ± 301
Or         Repair <Rpr> [1..1] ± 301
Or         PendingCancellation <PdgCxl> [1..1]  301
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 275 March 2026
```

## File page 276

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 302
Or}           Reason <Rsn> [1..*]  302
             Code <Cd> [1..1]  302
{Or               Code <Cd> [1..1] CodeSet 303
Or}               Proprietary <Prtry> [1..1] ± 303
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 303
Or}         ModificationRequested <ModReqd> [1..1] ± C4 304
     Transaction <Tx> [0..*]  C19 304
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 307
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 307
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 307
       CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 307
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 307
       TradeIdentification <TradId> [0..*] Text 307
       UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 307
       PoolIdentification <PoolId> [0..1] Text 308
       CommonIdentification <CmonId> [0..1] Text 308
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 308
       TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 308
       ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 308
       ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 308
       TripartyAgentServiceProviderCollateralInstructionIdentific
ation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 308
       TransactionDetails <TxDtls> [0..1]  C3, C10,
C17,
C28,
C29,
C41,
C42
309
         TransactionActivity <TxActvty> [1..1] ± 314
         SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 314
         SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 314
         Payment <Pmt> [1..1] CodeSet 315
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 276 March 2026
```

## File page 277

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         SettlementParameters <SttlmParams> [0..1] ± C6, C38 315
         PlaceOfTrade <PlcOfTrad> [0..1] ± 316
         SafekeepingPlace <SfkpgPlc> [0..1] ± C36 317
         PlaceOfClearing <PlcOfClr> [0..1] ± 317
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
317
         PostingQuantity <PstngQty> [1..1] ± 318
         PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 319
         PostingAmount <PstngAmt> [0..1] ± 319
         DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  319
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
320
           ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 321
           CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  321
{Or             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 321
Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C5 321
Or}             LEI <LEI> [1..1] IdentifierSet 322
         TradeDate <TradDt> [0..1] ± 322
         ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 322
         SettlementDate <SttlmDt> [1..1] ± 322
         LateDeliveryDate <LateDlvryDt> [0..1] ± 323
         ExpectedValueDate <XpctdValDt> [0..1] ± 323
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 323
         MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 323
         DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
323
         ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
324
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 277 March 2026
```

## File page 278

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 326
         SupplementaryData <SplmtryData> [0..*] ± C40 326
   Transactions <Txs> [0..*]  C20 0
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 329
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 330
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 330
     CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 330
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 330
     TradeIdentification <TradId> [0..*] Text 330
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 330
     PoolIdentification <PoolId> [0..1] Text 330
     CommonIdentification <CmonId> [0..1] Text 331
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 331
     TripartyAgentServiceProviderCollateralTransactionIdentific
ation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 331
     ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 331
     ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 331
     TripartyAgentServiceProviderCollateralInstructionIdentificat
ion <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 331
     TransactionDetails <TxDtls> [0..1]  C3, C10,
C17,
C28,
C29,
C41,
C42
331
       TransactionActivity <TxActvty> [1..1] ± 336
       SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 336
       SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 336
       Payment <Pmt> [1..1] CodeSet 337
       SettlementParameters <SttlmParams> [0..1] ± C6, C38 337
       PlaceOfTrade <PlcOfTrad> [0..1] ± 338
       SafekeepingPlace <SfkpgPlc> [0..1] ± C36 339
       PlaceOfClearing <PlcOfClr> [0..1] ± 339
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 278 March 2026
```

## File page 279

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
339
       PostingQuantity <PstngQty> [1..1] ± 340
       PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 341
       PostingAmount <PstngAmt> [0..1] ± 341
       DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  341
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
342
         ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 343
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  343
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 343
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 343
Or}           LEI <LEI> [1..1] IdentifierSet 344
       TradeDate <TradDt> [0..1] ± 344
       ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 344
       SettlementDate <SttlmDt> [1..1] ± 344
       LateDeliveryDate <LateDlvryDt> [0..1] ± 345
       ExpectedValueDate <XpctdValDt> [0..1] ± 345
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 345
       MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 345
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
345
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
347
       TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 348
       SupplementaryData <SplmtryData> [0..*] ± C40 348
     StatusAndReason <StsAndRsn> [0..*]  C26,
C39
348
{Or       Proprietary <Prtry> [1..1] ± 350
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 279 March 2026
```

