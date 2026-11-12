---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>", "9.4.6.2.15.23 TransactionAdditionalDetails <TxAddtlDtls>"]
file_pages: [326, 327, 328]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15.23 TransactionAdditionalDetails <TxAddtlDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 326 to 328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 326

```text
9.4.6.2.15.23  TransactionAdditionalDetails <TxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details on the transaction which cannot be included within the structured
fields of the message.
Datatype: "Max350Text" on page 2192
9.4.6.2.15.24  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C40 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
9.4.7 Transactions <Txs>
Presence: [0..*]
Definition: Details of the transactions reported.
Impacted by: C20 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 326 March 2026
```

## File page 327

```text
Transactions <Txs> contains the following Transaction164 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 329
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 330
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 330
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 330
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 330
   TradeIdentification <TradId> [0..*] Text 330
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 330
   PoolIdentification <PoolId> [0..1] Text 330
   CommonIdentification <CmonId> [0..1] Text 331
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 331
   TripartyAgentServiceProviderCollateralTransactionId
entification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 331
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 331
   ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 331
   TripartyAgentServiceProviderCollateralInstructionIde
ntification <TrptyAgtSvcPrvdrCollInstrId>
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
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
339
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 327 March 2026
```

## File page 328

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C16,
C21
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
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 343
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C5 343
Or}         LEI <LEI> [1..1] IdentifierSet 344
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
{Or     Proprietary <Prtry> [1..1] ± 350
Or     MatchingStatus <MtchgSts> [1..1] ± 350
Or     InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 350
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 328 March 2026
```

