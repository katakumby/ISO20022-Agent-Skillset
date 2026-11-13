---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>"]
file_pages: [375, 376, 377, 378, 379, 380]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6 AllegementDetails <AllgmtDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 375 to 380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
10.4.6 AllegementDetails <AllgmtDtls>
Presence: [0..*]
Definition: Details of the allegement.
Impacted by: C14 "DeliveringParty1Rule", C24 "LateDeliveryDateRule", C33 "ReceivingParty1Rule",
C42 "SettlementAmountRule", C47 "TradeDateRule", C48 "TwoLegTransactionOpeningClosing1Rule",
C49 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 375 March 2026
```

## File page 376

```text
AllegementDetails <AllgmtDtls> contains the following SecuritiesTradeDetails152 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 381
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 381
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 381
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
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
     SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 390
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 376 March 2026
```

## File page 377

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   SettlementAmount <SttlmAmt> [0..1] ± 398
   OtherAmounts <OthrAmts> [0..1] ± 399
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  399
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C17,
C18,
C22,
C23,
C27
400
     Quantity <Qty> [1..1]  401
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 401
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 401
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  401
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 377 March 2026
```

## File page 378

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 402
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C8 402
Or}       LEI <LEI> [1..1] IdentifierSet 402
   OtherBusinessParties <OthrBizPties> [0..1]  C21 402
     Investor <Invstr> [0..1] ± 403
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 403
     StockExchange <StockXchg> [0..1] ± 404
     TradeRegulator <TradRgltr> [0..1] ± 404
     TripartyAgent <TrptyAgt> [0..1] ± 404
   SupplementaryData <SplmtryData> [0..*] ± C46 404
Constraints
• DeliveringParty1Rule
If the instruction is a receive, then DeliveringParty1 must be present.
On Condition
    /SecuritiesMovementType is equal to value 'Receive'
Following Must be True
    /DeliveringSettlementParties Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
• LateDeliveryDateRule
If LateDeliveryDate is present then the transaction must be a pool trade that results from the original
TBA (To Be Announced). The original TBA would be offset by an opposite transaction and replaced
by buys or sells of individual pools. It is a date greater than the settlement date stated in the trade,
for pools designed as settling late.
• ReceivingParty1Rule
If the instruction is a delivery, then ReceivingParty 1 must be present.
On Condition
    /SecuritiesMovementType is equal to value 'Delivery'
Following Must be True
    /ReceivingSettlementParties Must be present
 And    /ReceivingSettlementParties/Party1 Must be present
• SettlementAmountRule
If the instruction is against payment, then SettlementAmount must be present.
On Condition
    /Payment is equal to value 'AgainstPaymentSettlement'
Following Must be True
    /SettlementAmount Must be present
• TradeDateRule
If Trade Date/Time is present with a time or a time + UTC indicator, then it must be the local time of
the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 378 March 2026
```

## File page 379

```text
• TwoLegTransactionOpeningClosing1Rule
For settlement of two part transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the following combination of
TransactionIdentificationDetails/SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
TriParty Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 379 March 2026
```

## File page 380

```text
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
• TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is alleged by sending the following
combination of SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Sell-Buy Back: Sell
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Sell-Buy Back: Buy Back
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Buy-Sell Back: Buy
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 380 March 2026
```

