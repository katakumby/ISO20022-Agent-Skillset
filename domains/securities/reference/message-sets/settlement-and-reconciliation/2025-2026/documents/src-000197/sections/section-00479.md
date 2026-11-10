---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.2 Structure"]
file_pages: [729, 730]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 729 to 730.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 729

```text
22.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxAllgmtNtfctn> [1..1]  C13,
C33,
C41,
C42,
C48,
C49
   TransactionIdentification <TxId> [1..1] Text 738
   SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[1..1] ± 739
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 739
   CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 739
   TradeDetails <TradDtls> [1..1]  C23,
C32,
C47
0
     TradeIdentification <TradId> [0..*] Text 740
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 740
     CollateralTransactionIdentification <CollTxId> [0..*] Text 741
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..*] Text 741
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 741
     PlaceOfTrade <PlcOfTrad> [0..1] ± 741
     PlaceOfClearing <PlcOfClr> [0..1] ± 741
     TradeDate <TradDt> [0..1] ± 742
     SettlementDate <SttlmDt> [1..1] ± 742
     DealPrice <DealPric> [0..1] ± 742
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C25 743
     TradeTransactionCondition <TradTxCond> [0..*] ± 743
     TypeOfPrice <TpOfPric> [0..1] ± 743
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C16,
C17,
C21,
C22,
C26
743
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C3, C31 744
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1] ± C14,
C34,
C36,
0
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 729 March 2026
```

## File page 730

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C38,
C40
   SecuritiesFinancingDetails <SctiesFincgDtls> [0..1]  0
     SecuritiesFinancingTradeIdentification <SctiesFincgTradId> [0..1] Text 749
     SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 749
     ClosingLegIdentification <ClsgLegId> [0..1] Text 749
     TerminationDate <TermntnDt> [0..1] ± 750
     RateType <RateTp> [0..1] ± 750
     LegalFramework <LglFrmwk> [0..1] ± 750
     MaturityDateModification <MtrtyDtMod> [0..1] Indicator 750
     InterestPayment <IntrstPmt> [0..1] Indicator 751
     VariableRateSupport <VarblRateSpprt> [0..1] ± 751
     RepurchaseRate <RpRate> [0..1] ± C45 751
     TransactionCallDelay <TxCallDely> [0..1] Text 751
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 751
     TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 752
     SecondLegNarrative <ScndLegNrrtv> [0..1] Text 752
   SettlementParameters <SttlmParams> [1..1] ± C9, C44 0
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C8, C15,
C27,
C28,
C29,
C30,
C43
0
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C8, C15,
C27,
C28,
C29,
C30,
C43
755
   CashParties <CshPties> [0..1]  0
     Debtor <Dbtr> [0..1] ± 757
     DebtorAgent <DbtrAgt> [0..1] ± 758
     Creditor <Cdtr> [0..1] ± 758
     CreditorAgent <CdtrAgt> [0..1] ± 759
   SettlementAmount <SttlmAmt> [0..1] ± 759
   OtherAmounts <OthrAmts> [0..1] ± 760
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 730 March 2026
```

