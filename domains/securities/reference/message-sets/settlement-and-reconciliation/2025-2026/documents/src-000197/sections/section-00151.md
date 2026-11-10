---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>"]
file_pages: [216, 217, 218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.6 IntermediaryInformation <IntrmyInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 216 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount36" on
page 1341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1341
   Type <Tp> [0..1] ± 1342
   Name <Nm> [0..1] Text 1342
   Designation <Dsgnt> [0..1] Text 1342
8.4.5 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet4" on page 1553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1553
   Type <Tp> [0..1] ± 1553
   Name <Nm> [0..1] Text 1553
   Designation <Dsgnt> [0..1] Text 1554
8.4.6 IntermediaryInformation <IntrmyInf>
Presence: [0..10]
Definition: Information about the party that provides services relating to financial products to investors,
for example, advice on products and placement of orders for the investment fund.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary44" on
page 1682 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1683
   Role <Role> [0..1] ± 1683
   Account <Acct> [0..1] ± 1683
8.4.7 FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..*]
Definition: Reporting per financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 216 March 2026
```

## File page 217

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrumentDetails48
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 225
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 225
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 225
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 225
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 225
     TradeIdentification <TradId> [0..*] Text 225
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 225
     PoolIdentification <PoolId> [0..1] Text 226
     CommonIdentification <CmonId> [0..1] Text 226
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 226
     TripartyAgentServiceProviderCollateralTransactionI
dentification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 226
     ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 226
     ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 226
     TripartyAgentServiceProviderCollateralInstructionId
entification <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 226
     MasterReference <MstrRef> [0..1] Text 227
     ClientReference <ClntRef> [0..1] ± 227
     AccountOwnerLegIdentification <AcctOwnrLegId> [0..1] Text 227
     AccountServicerLegIdentification <AcctSvcrLegId> [0..1] Text 227
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 217 March 2026
```

## File page 218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TransactionDetails <TxDtls> [0..1]  C2, C25,
C43,
C45
227
       TransactionActivity <TxActvty> [1..1] ± 232
       SettlementTransactionOrCorporateActionEventTyp
e <SttlmTxOrCorpActnEvtTp>
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
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 237
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C4 237
Or}           LEI <LEI> [1..1] IdentifierSet 238
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 218 March 2026
```

