---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.3 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [246, 247, 248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.3 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 246 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount25" on
page 1345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1346
   Type <Tp> [0..1] ± 1346
   Name <Nm> [0..1] Text 1346
8.4.8.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet2" on page 1633 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1633
   Type <Tp> [0..1] ± 1633
   Name <Nm> [0..1] Text 1634
8.4.8.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
8.4.8.5  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..*]
Definition: Reporting per financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 246 March 2026
```

## File page 247

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrumentDetails49
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 255
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 255
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 255
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 255
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 255
     TradeIdentification <TradId> [0..*] Text 255
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 255
     PoolIdentification <PoolId> [0..1] Text 256
     CommonIdentification <CmonId> [0..1] Text 256
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 256
     TripartyAgentServiceProviderCollateralTransactionI
dentification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 256
     ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 256
     ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 256
     TripartyAgentServiceProviderCollateralInstructionId
entification <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 256
     MasterReference <MstrRef> [0..1] Text 256
     ClientReference <ClntRef> [0..1] ± 257
     AccountOwnerLegIdentification <AcctOwnrLegId> [0..1] Text 257
     AccountServicerLegIdentification <AcctSvcrLegId> [0..1] Text 257
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 247 March 2026
```

## File page 248

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TransactionDetails <TxDtls> [0..1]  C3, C26,
C44,
C46
257
       TransactionActivity <TxActvty> [1..1] ± 262
       SettlementTransactionOrCorporateActionEventTyp
e <SttlmTxOrCorpActnEvtTp>
[0..1] ± 262
       SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 262
       Payment <Pmt> [1..1] CodeSet 262
       SettlementParameters <SttlmParams> [0..1] ± C5, C37 263
       PlaceOfTrade <PlcOfTrad> [0..1] ± 264
       SafekeepingPlace <SfkpgPlc> [0..1] ± C35 264
       PlaceOfClearing <PlcOfClr> [0..1] ± 264
       PostingQuantity <PstngQty> [1..1] ± 265
       NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 265
       PostingAmount <PstngAmt> [0..1] ± 265
       DigitalPaymentPostingSettlement
<DgtlPmtPstngSttlm>
[0..1]  265
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
266
         ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 267
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  267
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 267
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C4 267
Or}           LEI <LEI> [1..1] IdentifierSet 268
       AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 268
       TradeDate <TradDt> [0..1] ± 268
       EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 268
       SettlementDate <SttlmDt> [0..1] ± 269
       ValueDate <ValDt> [0..1] ± 269
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 269
       MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 269
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
269
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 248 March 2026
```

