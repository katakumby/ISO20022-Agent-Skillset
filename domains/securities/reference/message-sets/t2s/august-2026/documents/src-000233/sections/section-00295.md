---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.2 Structure"]
file_pages: [382, 383, 384]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 382 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
17.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntQryRspn> [1..1]  C3, C4,
C18,
C19
   Identification <Id> [0..1]  387
     Identification <Id> [1..1] Text 387
     CreationDateTime <CreDtTm> [0..1] ± 387
     CopyDuplicate <CpyDplct> [0..1] CodeSet 388
     MessageOriginator <MsgOrgtr> [0..1] ± 388
     MessageRecipient <MsgRcpt> [0..1] ± 388
   Pagination <Pgntn> [1..1] ± 389
   ReportGeneralDetails <RptGnlDtls> [1..1]  C20 389
     QueryReference <QryRef> [0..1] Text 390
     ReportIdentification <RptId> [0..1] Text 390
     QueryType <QryTp> [1..1] CodeSet 390
     ActivityIndicator <ActvtyInd> [1..1] Indicator 390
   ReportOrError <RptOrErr> [0..1]  390
{Or     Movements <Mvmnts> [1..*]  C8, C9,
C10,
C22
393
       CashAccount <CshAcct> [0..1] ± C15,
C14
396
       CashAccountOwner <CshAcctOwnr> [0..1] ± 397
       CashAccountServicer <CshAcctSvcr> [0..1] ± 397
       StatusAndReason <StsAndRsn> [0..1]  398
         ProcessingStatus <PrcgSts> [0..*] ± 398
         SettlementStatus <SttlmSts> [0..*] ± C17 399
         Settled <Sttld> [0..1] ± C5 399
       Movement <Mvmnt> [1..*]  C16 400
         CashAccount <CshAcct> [0..1] ± C15,
C14
403
         CashAccountOwner <CshAcctOwnr> [0..1] ± 403
         CashAccountServicer <CshAcctSvcr> [0..1] ± 404
         StatusAndReason <StsAndRsn> [0..1]  404
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 382 August 2026
```

## File page 383

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           ProcessingStatus <PrcgSts> [0..*] ± 404
           SettlementStatus <SttlmSts> [0..*] ± C17 405
           Settled <Sttld> [0..1] ± C5 405
         AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 406
         AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 406
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 406
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 406
         PoolIdentification <PoolId> [0..1] Text 406
         CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 406
         MovementDetails <MvmntDtls> [0..1]  407
           BalanceFrom <BalFr> [1..1]  409
             Type <Tp> [1..1]  409
{Or               Code <Cd> [1..1] CodeSet 410
Or}               Proprietary <Prtry> [1..1] ± 410
             QuantityBreakdown <QtyBrkdwn> [0..*]  410
               LotNumber <LotNb> [0..1] ± 410
               LotAmount <LotAmt> [0..1] ± 411
               LotQuantity <LotQty> [0..1] ± 411
               CashSubBalanceType <CshSubBalTp> [0..1] ± 411
           BalanceTo <BalTo> [1..1]  412
             Type <Tp> [1..1]  412
{Or               Code <Cd> [1..1] CodeSet 412
Or}               Proprietary <Prtry> [1..1] ± 412
             QuantityBreakdown <QtyBrkdwn> [0..*]  413
               LotNumber <LotNb> [0..1] ± 413
               LotAmount <LotAmt> [0..1] ± 413
               LotQuantity <LotQty> [0..1] ± 414
               CashSubBalanceType <CshSubBalTp> [0..1] ± 414
           SettlementAmount <SttlmAmt> [1..1] ± 414
           SettledAmount <SttldAmt> [0..1] ± 414
           PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 415
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 383 August 2026
```

## File page 384

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 415
           IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 415
           EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 415
           StatusDate <StsDt> [0..1] DateTime 416
           CashSubBalanceIdentification <CshSubBalId> [0..1] ± 416
           Linkages <Lnkgs> [0..*]  416
             ProcessingPosition <PrcgPos> [0..1] ± C24 417
             MessageNumber <MsgNb> [0..1] ± C21 417
             Reference <Ref> [1..1]  418
{Or               SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 418
Or               IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 418
Or               IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 419
Or               AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 419
Or               MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 419
Or               PoolIdentification <PoolId> [1..1] Text 419
Or}               OtherTransactionIdentification <OthrTxId> [1..1] Text 419
             ReferenceOwner <RefOwnr> [0..1] ± 419
           Priority <Prty> [0..1] ± 420
           MessageOriginator <MsgOrgtr> [0..1] ± 420
           CreationDateTime <CreDtTm> [1..1] DateTime 420
           InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 420
           SupplementaryData <SplmtryData> [0..*] ± C23 420
Or}     OperationalError <OprlErr> [1..*]  421
       Error <Err> [1..1]  421
{Or         Code <Cd> [1..1] CodeSet 421
Or}         Proprietary <Prtry> [1..1] Text 421
       Description <Desc> [0..1] Text 422
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 384 August 2026
```

