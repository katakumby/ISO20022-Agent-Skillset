---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.2 Structure"]
file_pages: [246, 247, 248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 246 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntModRpt> [1..1]  C3, C4,
C21,
C22
   Identification <Id> [0..1]  251
     Identification <Id> [1..1] Text 251
     CreationDateTime <CreDtTm> [0..1] ± 252
     CopyDuplicate <CpyDplct> [0..1] CodeSet 252
     MessageOriginator <MsgOrgtr> [0..1] ± 252
     MessageRecipient <MsgRcpt> [0..1] ± 252
   Pagination <Pgntn> [1..1] ± 253
   ReportGeneralDetails <RptGnlDtls> [1..1]  C23 253
     ReportNumber <RptNb> [0..1] ± 254
     QueryReference <QryRef> [0..1] Text 254
     ReportIdentification <RptId> [0..1] Text 254
     ReportDateTime <RptDtTm> [0..1] ± 254
     ReportPeriod <RptPrd> [0..1] ± 254
     QueryType <QryTp> [0..1] CodeSet 255
     Frequency <Frqcy> [0..1] ± 255
     UpdateType <UpdTp> [1..1] ± 255
     ActivityIndicator <ActvtyInd> [1..1] Indicator 255
   ReportOrError <RptOrErr> [0..1]  256
{Or     Modifications <Mods> [1..*]  C10,
C11,
C12,
C20
259
       CashAccount <CshAcct> [0..1] ± C17,
C16
262
       CashAccountOwner <CshAcctOwnr> [0..1] ± 263
       CashAccountServicer <CshAcctSvcr> [0..1] ± 263
       ProcessingStatus <PrcgSts> [0..1] ± 263
       Modification <Mod> [1..*]  264
         CashAccount <CshAcct> [0..1] ± C17,
C16
266
         CashAccountOwner <CshAcctOwnr> [0..1] ± 267
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
246 March 2024
```

## File page 247

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashAccountServicer <CshAcctSvcr> [0..1] ± 267
         ProcessingStatus <PrcgSts> [0..1] ± 268
         RequestReference <ReqRef> [1..1] Text 268
         StatusDate <StsDt> [0..1] DateTime 269
         RequestDetails <ReqDtls> [0..1]  C18,
C19
269
           Reference <Ref> [1..1]  271
             AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 271
             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 271
             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 271
             ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 271
             PoolIdentification <PoolId> [0..1] Text 272
           Linkage <Lkg> [0..1] ± 272
           Priority <Prty> [0..1] ± 272
           OtherProcessing <OthrPrcg> [0..*] ± 272
           PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 272
           ClearingChannel <ClrChanl> [0..1] CodeSet 273
           Linkages <Lnkgs> [0..*]  273
             ProcessingPosition <PrcgPos> [0..1] ± C26 273
             MessageNumber <MsgNb> [0..1] ± C24 274
             Reference <Ref> [1..1]  274
{Or               SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 275
Or               IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 275
Or               IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 275
Or               AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 275
Or               MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 275
Or               PoolIdentification <PoolId> [1..1] Text 276
Or}               OtherTransactionIdentification <OthrTxId> [1..1] Text 276
             ReferenceOwner <RefOwnr> [0..1] ± 276
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
247 March 2024
```

## File page 248

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 276
           SettlementAmount <SttlmAmt> [1..1] ± 278
           SettlementDate <SttlmDt> [1..1] ± 278
           BalanceFrom <BalFr> [1..1]  278
             Type <Tp> [1..1]  278
{Or               Code <Cd> [1..1] CodeSet 279
Or}               Proprietary <Prtry> [1..1] ± 279
             QuantityBreakdown <QtyBrkdwn> [0..*]  279
               LotNumber <LotNb> [0..1] ± 279
               LotAmount <LotAmt> [0..1] ± 280
               LotQuantity <LotQty> [0..1] ± 280
               CashSubBalanceType <CshSubBalTp> [0..1] ± 280
           BalanceTo <BalTo> [1..1]  281
             Type <Tp> [1..1]  281
{Or               Code <Cd> [1..1] CodeSet 281
Or}               Proprietary <Prtry> [1..1] ± 281
             QuantityBreakdown <QtyBrkdwn> [0..*]  282
               LotNumber <LotNb> [0..1] ± 282
               LotAmount <LotAmt> [0..1] ± 282
               LotQuantity <LotQty> [0..1] ± 283
               CashSubBalanceType <CshSubBalTp> [0..1] ± 283
           CashSubBalanceIdentification <CshSubBalId> [0..1] ± 283
           Priority <Prty> [0..1] ± 283
           InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 284
Or}     OperationalError <OprlErr> [1..*]  284
       Error <Err> [1..1]  284
{Or         Code <Cd> [1..1] CodeSet 284
Or}         Proprietary <Prtry> [1..1] Text 284
       Description <Desc> [0..1] Text 285
   SupplementaryData <SplmtryData> [0..*] ± C25 285
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
248 March 2024
```

