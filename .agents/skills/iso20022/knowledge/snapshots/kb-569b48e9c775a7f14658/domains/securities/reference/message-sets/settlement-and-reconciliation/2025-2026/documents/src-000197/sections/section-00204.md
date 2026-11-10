---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.1 StatusAndReason <StsAndRsn>", "9.4.6.1.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.6.1.5.8 ModificationRequested <ModReqd>"]
file_pages: [304, 305, 306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.1.5.8 ModificationRequested <ModReqd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 304 to 306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 304

```text
9.4.6.1.5.8  ModificationRequested <ModReqd>
Presence: [1..1]
Definition: Modification request from your counterparty for this transaction is pending waiting for your
cancellation request or your consent.
Impacted by: C4 "AdditionalReasonInforrmationRule"
ModificationRequested <ModReqd> contains the following elements (see "ProprietaryReason4" on
page 1899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
9.4.6.2  Transaction <Tx>
Presence: [0..*]
Definition: Details of the transactions reported.
Impacted by: C19 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 304 March 2026
```

## File page 305

```text
Transaction <Tx> contains the following Transaction166 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 307
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 307
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 307
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 307
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 307
   TradeIdentification <TradId> [0..*] Text 307
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 307
   PoolIdentification <PoolId> [0..1] Text 308
   CommonIdentification <CmonId> [0..1] Text 308
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 308
   TripartyAgentServiceProviderCollateralTransactionId
entification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 308
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 308
   ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 308
   TripartyAgentServiceProviderCollateralInstructionIde
ntification <TrptyAgtSvcPrvdrCollInstrId>
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
     SettlementParameters <SttlmParams> [0..1] ± C6, C38 315
     PlaceOfTrade <PlcOfTrad> [0..1] ± 316
     SafekeepingPlace <SfkpgPlc> [0..1] ± C36 317
     PlaceOfClearing <PlcOfClr> [0..1] ± 317
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
317
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 305 March 2026
```

## File page 306

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C16,
C21
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
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 321
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C5 321
Or}         LEI <LEI> [1..1] IdentifierSet 322
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
     TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 326
     SupplementaryData <SplmtryData> [0..*] ± C40 326
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 306 March 2026
```

