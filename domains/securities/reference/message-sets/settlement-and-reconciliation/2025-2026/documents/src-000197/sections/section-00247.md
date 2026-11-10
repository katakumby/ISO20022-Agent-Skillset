---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.2 Structure"]
file_pages: [363, 364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 363 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxAllgmtRpt> [1..1]  C5, C6,
C7, C35,
C37,
C39
   Pagination <Pgntn> [1..1] ± 0
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± C34 373
   AccountOwner <AcctOwnr> [0..1] ± 0
   SafekeepingAccount <SfkpgAcct> [0..1] ± 0
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 0
   AllegementDetails <AllgmtDtls> [0..*]  C14,
C24,
C33,
C42,
C47,
C48,
C49
375
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 381
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 381
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 381
     CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 382
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 382
     TradeIdentification <TradId> [0..*] Text 382
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 382
     CommonIdentification <CmonId> [0..1] Text 382
     PoolIdentification <PoolId> [0..1] Text 382
     CollateralTransactionIdentification <CollTxId> [0..*] Text 382
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 382
     Payment <Pmt> [1..1] CodeSet 383
     Status <Sts> [0..1] ± 383
     PlaceOfTrade <PlcOfTrad> [0..1] ± 383
     PlaceOfClearing <PlcOfClr> [0..1] ± 384
     TradeDate <TradDt> [0..1] ± 384
     SettlementDate <SttlmDt> [1..1] ± 384
     DealPrice <DealPric> [0..1] ± 384
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 363 March 2026
```

## File page 364

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C26 385
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C17,
C18,
C22,
C23,
C27
385
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C3, C32 386
     TradeTransactionCondition <TradTxCond> [0..*] ± 388
     TypeOfPrice <TpOfPric> [0..1] ± 388
     QuantityAndAccountDetails <QtyAndAcctDtls> [1..1] ± C15,
C41
389
     SecuritiesFinancingDetails <SctiesFincgDtls> [0..1]  389
       SecuritiesFinancingTradeIdentification <SctiesFincgTradId> [0..1] Text 390
       SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 390
       ClosingLegIdentification <ClsgLegId> [0..1] Text 390
       TerminationDate <TermntnDt> [0..1] ± 390
       RateType <RateTp> [0..1] ± 391
       LegalFramework <LglFrmwk> [0..1] ± 391
       MaturityDateModification <MtrtyDtMod> [0..1] Indicator 391
       InterestPayment <IntrstPmt> [0..1] Indicator 391
       VariableRateSupport <VarblRateSpprt> [0..1] ± 392
       RepurchaseRate <RpRate> [0..1] ± C45 392
       TransactionCallDelay <TxCallDely> [0..1] Text 392
       AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 392
       TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 393
       SecondLegNarrative <ScndLegNrrtv> [0..1] Text 393
     SettlementParameters <SttlmParams> [1..1] ± C10,
C44
393
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C9, C16,
C28,
C29,
C30,
C31,
C43
394
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C9, C16,
C28,
C29,
C30,
C31,
C43
396
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 364 March 2026
```

