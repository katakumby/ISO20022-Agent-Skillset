---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.2 Structure"]
file_pages: [200, 201, 202, 203]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 200 to 203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxPstngRpt> [1..1]  C12,
C13,
C28,
C31,
C34,
C41,
C36
   Pagination <Pgntn> [1..1] ± 214
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± C27 0
   AccountOwner <AcctOwnr> [0..1] ± 0
   SafekeepingAccount <SfkpgAcct> [0..1] ± 215
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 0
   IntermediaryInformation <IntrmyInf> [0..10] ± 216
   FinancialInstrumentDetails <FinInstrmDtls> [0..*]  0
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
219
     InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 220
     PriceDetails <PricDtls> [0..1] ± C47 220
     SafekeepingPlace <SfkpgPlc> [0..1] ± C35 221
     OpeningBalance <OpngBal> [0..1] ± C38 221
     ClosingBalance <ClsgBal> [0..1] ± C39 222
     Transaction <Tx> [1..*]  C17 222
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 225
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 225
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 225
       CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 225
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 225
       TradeIdentification <TradId> [0..*] Text 225
       UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 225
       PoolIdentification <PoolId> [0..1] Text 226
       CommonIdentification <CmonId> [0..1] Text 226
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 200 March 2026
```

## File page 201

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 226
       TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 226
       ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 226
       ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 226
       TripartyAgentServiceProviderCollateralInstructionIdentific
ation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 226
       MasterReference <MstrRef> [0..1] Text 227
       ClientReference <ClntRef> [0..1] ± 227
       AccountOwnerLegIdentification <AcctOwnrLegId> [0..1] Text 227
       AccountServicerLegIdentification <AcctSvcrLegId> [0..1] Text 227
       TransactionDetails <TxDtls> [0..1]  C2, C25,
C43,
C45
227
         TransactionActivity <TxActvty> [1..1] ± 232
         SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 232
         SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 232
         Payment <Pmt> [1..1] CodeSet 232
         SettlementParameters <SttlmParams> [0..1] ± C5, C37 233
         PlaceOfTrade <PlcOfTrad> [0..1] ± 234
         SafekeepingPlace <SfkpgPlc> [0..1] ± C35 234
         PlaceOfClearing <PlcOfClr> [0..1] ± 234
         PostingQuantity <PstngQty> [1..1] ± 235
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 235
         PostingAmount <PstngAmt> [0..1] ± 235
         DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  235
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
236
           ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 237
           CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  237
{Or             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 237
Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C4 237
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 201 March 2026
```

## File page 202

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             LEI <LEI> [1..1] IdentifierSet 238
         AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 238
         TradeDate <TradDt> [0..1] ± 238
         EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 238
         SettlementDate <SttlmDt> [0..1] ± 239
         ValueDate <ValDt> [0..1] ± 239
         AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 239
         MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 239
         DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
239
         ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
240
         ReversalIndicator <RvslInd> [0..1] Indicator 242
         TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 242
       SupplementaryData <SplmtryData> [0..*] ± C42 242
   SubAccountDetails <SubAcctDtls> [0..*]  C30,
C33
242
     AccountOwner <AcctOwnr> [0..1] ± 245
     SafekeepingAccount <SfkpgAcct> [0..1] ± 245
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 246
     ActivityIndicator <ActvtyInd> [1..1] Indicator 246
     FinancialInstrumentDetails <FinInstrmDtls> [0..*]  246
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
249
       InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 250
       PriceDetails <PricDtls> [0..1] ± C47 250
       SafekeepingPlace <SfkpgPlc> [0..1] ± C35 251
       OpeningBalance <OpngBal> [0..1] ± C38 251
       ClosingBalance <ClsgBal> [0..1] ± C39 251
       Transaction <Tx> [1..*]  C18 252
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 202 March 2026
```

## File page 203

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 255
         AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 255
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 255
         CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 255
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 255
         TradeIdentification <TradId> [0..*] Text 255
         UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 255
         PoolIdentification <PoolId> [0..1] Text 256
         CommonIdentification <CmonId> [0..1] Text 256
         CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 256
         TripartyAgentServiceProviderCollateralTransactionIdentif
ication <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 256
         ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 256
         ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 256
         TripartyAgentServiceProviderCollateralInstructionIdentifi
cation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 256
         MasterReference <MstrRef> [0..1] Text 256
         ClientReference <ClntRef> [0..1] ± 257
         AccountOwnerLegIdentification <AcctOwnrLegId> [0..1] Text 257
         AccountServicerLegIdentification <AcctSvcrLegId> [0..1] Text 257
         TransactionDetails <TxDtls> [0..1]  C3, C26,
C44,
C46
257
           TransactionActivity <TxActvty> [1..1] ± 262
           SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 262
           SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 262
           Payment <Pmt> [1..1] CodeSet 262
           SettlementParameters <SttlmParams> [0..1] ± C5, C37 263
           PlaceOfTrade <PlcOfTrad> [0..1] ± 264
           SafekeepingPlace <SfkpgPlc> [0..1] ± C35 264
           PlaceOfClearing <PlcOfClr> [0..1] ± 264
           PostingQuantity <PstngQty> [1..1] ± 265
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 203 March 2026
```

