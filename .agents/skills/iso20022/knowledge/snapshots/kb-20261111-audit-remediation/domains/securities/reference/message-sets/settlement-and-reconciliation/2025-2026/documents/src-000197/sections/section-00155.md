---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.6 ClosingBalance <ClsgBal>"]
file_pages: [222, 223, 224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.6 ClosingBalance <ClsgBal>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 222 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

```text
OpeningBalance <OpngBal> contains the following elements (see "OpeningBalance5" on page 1422
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1422
   OpeningBalance <OpngBal> [1..1] ± 1422
Constraints
• ShortLongDefaultRule
If Shortlong is absent, then the default is long, that is, balance is positive.
8.4.7.6  ClosingBalance <ClsgBal>
Presence: [0..1]
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
8.4.7.7  Transaction <Tx>
Presence: [1..*]
Definition: Transaction details.
Impacted by: C17 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 222 March 2026
```

## File page 223

```text
Transaction <Tx> contains the following Transaction165 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 225
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 225
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 225
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 225
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 225
   TradeIdentification <TradId> [0..*] Text 225
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 225
   PoolIdentification <PoolId> [0..1] Text 226
   CommonIdentification <CmonId> [0..1] Text 226
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 226
   TripartyAgentServiceProviderCollateralTransactionId
entification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 226
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 226
   ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 226
   TripartyAgentServiceProviderCollateralInstructionIde
ntification <TrptyAgtSvcPrvdrCollInstrId>
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 223 March 2026
```

## File page 224

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 237
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 237
Or}         LEI <LEI> [1..1] IdentifierSet 238
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 224 March 2026
```

