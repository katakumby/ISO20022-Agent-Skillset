---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.2 Structure"]
file_pages: [301, 302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 301 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
14.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlRpt> [1..1]  C3, C4,
C19,
C20
   Identification <Id> [0..1]  305
     Identification <Id> [1..1] Text 306
     CreationDateTime <CreDtTm> [0..1] ± 306
     CopyDuplicate <CpyDplct> [0..1] CodeSet 306
     MessageOriginator <MsgOrgtr> [0..1] ± 306
     MessageRecipient <MsgRcpt> [0..1] ± 307
   Pagination <Pgntn> [1..1] ± 307
   ReportGeneralDetails <RptGnlDtls> [1..1]  C21 307
     ReportNumber <RptNb> [0..1] ± 308
     QueryReference <QryRef> [0..1] Text 308
     ReportIdentification <RptId> [0..1] Text 308
     ReportDateTime <RptDtTm> [0..1] ± 308
     ReportPeriod <RptPrd> [0..1] ± 309
     QueryType <QryTp> [0..1] CodeSet 309
     Frequency <Frqcy> [0..1] ± 309
     UpdateType <UpdTp> [1..1] ± 309
     ActivityIndicator <ActvtyInd> [1..1] Indicator 310
   ReportOrError <RptOrErr> [0..1]  310
{Or     Cancellations <Cxls> [1..*]  C10,
C11,
C12,
C18
312
       CashAccount <CshAcct> [0..1] ± C17,
C16
314
       CashAccountOwner <CshAcctOwnr> [0..1] ± 315
       CashAccountServicer <CshAcctSvcr> [0..1] ± 315
       ProcessingStatus <PrcgSts> [0..1] ± 316
       Cancellation <Cxl> [1..*]  316
         CashAccount <CshAcct> [0..1] ± C17,
C16
318
         CashAccountOwner <CshAcctOwnr> [0..1] ± 318
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
301 March 2024
```

## File page 302

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashAccountServicer <CshAcctSvcr> [0..1] ± 319
         ProcessingStatus <PrcgSts> [0..1] ± 319
         RequestReference <ReqRef> [1..1] Text 320
         StatusDate <StsDt> [0..1] DateTime 320
         TransactionIdentification <TxId> [0..1]  320
           AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 320
           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 321
           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 321
           ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 321
           PoolIdentification <PoolId> [0..1] Text 321
         UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 321
           SettlementAmount <SttlmAmt> [1..1] ± 323
           SettlementDate <SttlmDt> [1..1] ± 323
           BalanceFrom <BalFr> [1..1]  323
             Type <Tp> [1..1]  323
{Or               Code <Cd> [1..1] CodeSet 324
Or}               Proprietary <Prtry> [1..1] ± 324
             QuantityBreakdown <QtyBrkdwn> [0..*]  324
               LotNumber <LotNb> [0..1] ± 324
               LotAmount <LotAmt> [0..1] ± 325
               LotQuantity <LotQty> [0..1] ± 325
               CashSubBalanceType <CshSubBalTp> [0..1] ± 325
           BalanceTo <BalTo> [1..1]  326
             Type <Tp> [1..1]  326
{Or               Code <Cd> [1..1] CodeSet 326
Or}               Proprietary <Prtry> [1..1] ± 326
             QuantityBreakdown <QtyBrkdwn> [0..*]  327
               LotNumber <LotNb> [0..1] ± 327
               LotAmount <LotAmt> [0..1] ± 327
               LotQuantity <LotQty> [0..1] ± 328
               CashSubBalanceType <CshSubBalTp> [0..1] ± 328
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
302 March 2024
```

