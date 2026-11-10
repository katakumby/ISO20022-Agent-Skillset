---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>"]
file_pages: [289, 290, 291]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6 Status <Sts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 289 to 291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
9.4.6 Status <Sts>
Presence: [0..*]
Definition: Status information.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 289 March 2026
```

## File page 290

```text
Status <Sts> contains the following StatusAndReason49 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [1..1]  C26,
C39
292
{Or     Proprietary <Prtry> [1..1] ± 294
Or     MatchingStatus <MtchgSts> [1..1] ± 294
Or     InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 294
Or     SettlementStatus <SttlmSts> [1..1] ± C27 295
Or}     InstructionProcessingStatus <InstrPrcgSts> [1..1]  295
{Or       PendingProcessing <PdgPrcg> [1..1]  296
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 297
Or}         Reason <Rsn> [1..*]  297
           Code <Cd> [1..1]  297
{Or             Code <Cd> [1..1] CodeSet 298
Or}             Proprietary <Prtry> [1..1] ± 299
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 299
Or       CancellationRequested <CxlReqd> [1..1] ± C4 299
Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 300
Or       Cancelled <Canc> [1..1] ± 300
Or       Generated <Gnrtd> [1..1]  300
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 301
Or}         Reason <Rsn> [1..*] ± 301
Or       Repair <Rpr> [1..1] ± 301
Or       PendingCancellation <PdgCxl> [1..1]  301
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 302
Or}         Reason <Rsn> [1..*]  302
           Code <Cd> [1..1]  302
{Or             Code <Cd> [1..1] CodeSet 303
Or}             Proprietary <Prtry> [1..1] ± 303
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 303
Or}       ModificationRequested <ModReqd> [1..1] ± C4 304
   Transaction <Tx> [0..*]  C19 304
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 307
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 290 March 2026
```

## File page 291

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 307
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 307
     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 307
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 307
     TradeIdentification <TradId> [0..*] Text 307
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 307
     PoolIdentification <PoolId> [0..1] Text 308
     CommonIdentification <CmonId> [0..1] Text 308
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 308
     TripartyAgentServiceProviderCollateralTransactionI
dentification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 308
     ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 308
     ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 308
     TripartyAgentServiceProviderCollateralInstructionId
entification <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 308
     TransactionDetails <TxDtls> [0..1]  C3, C10,
C17,
C28,
C29,
C41,
C42
309
       TransactionActivity <TxActvty> [1..1] ± 314
       SettlementTransactionOrCorporateActionEventTyp
e <SttlmTxOrCorpActnEvtTp>
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
C16,
C21
317
       PostingQuantity <PstngQty> [1..1] ± 318
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 291 March 2026
```

