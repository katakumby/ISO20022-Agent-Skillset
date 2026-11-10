---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.5 FinancialInstrumentDetails <FinInstrmDtls>", "8.4.8.5.7 Transaction <Tx>"]
file_pages: [252, 253, 254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.5.7 Transaction <Tx>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 252 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 252

```text
Definition: Closing balance for the statement period (final closing balance) or of this page (intermediary
closing balance).
Impacted by: C39 "ShortLongDefaultRule"
ClosingBalance <ClsgBal> contains the following elements (see "ClosingBalance5" on page 1432 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   ClosingBalance <ClsgBal> [1..1] ± 1433
Constraints
• ShortLongDefaultRule
If Shortlong is absent, then the default is long, that is, balance is positive.
8.4.8.5.7  Transaction <Tx>
Presence: [1..*]
Definition: Transaction details.
Impacted by: C18 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 252 March 2026
```

## File page 253

```text
Transaction <Tx> contains the following Transaction167 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 255
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 255
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 255
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 255
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 255
   TradeIdentification <TradId> [0..*] Text 255
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 255
   PoolIdentification <PoolId> [0..1] Text 256
   CommonIdentification <CmonId> [0..1] Text 256
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 256
   TripartyAgentServiceProviderCollateralTransactionId
entification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 256
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 256
   ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 256
   TripartyAgentServiceProviderCollateralInstructionIde
ntification <TrptyAgtSvcPrvdrCollInstrId>
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 253 March 2026
```

## File page 254

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 267
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 267
Or}         LEI <LEI> [1..1] IdentifierSet 268
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
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
270
     ReversalIndicator <RvslInd> [0..1] Indicator 272
     TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 272
   SupplementaryData <SplmtryData> [0..*] ± C42 272
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 254 March 2026
```

