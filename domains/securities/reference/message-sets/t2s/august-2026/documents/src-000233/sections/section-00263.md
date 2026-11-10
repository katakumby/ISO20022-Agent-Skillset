---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.2 Structure"]
file_pages: [342, 343, 344]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 342 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
16.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntQry> [1..1]  
   Identification <Id> [0..1]  346
     Identification <Id> [1..1] Text 346
     CreationDateTime <CreDtTm> [0..1] ± 347
     CopyDuplicate <CpyDplct> [0..1] CodeSet 347
     MessageOriginator <MsgOrgtr> [0..1] ± 347
     MessageRecipient <MsgRcpt> [0..1] ± 347
   QueryDefinition <QryDef> [1..1]  348
     QueryType <QryTp> [1..1] CodeSet 352
     SearchCriteria <SchCrit> [1..1]  352
       References <Refs> [0..*]  356
{Or         AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 356
Or         AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 356
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 356
Or         ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 356
Or         PoolIdentification <PoolId> [1..1] Text 357
Or}         CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 357
       Status <Sts> [0..1]  357
         Type <Tp> [1..1]  358
           ProcessingStatus <PrcgSts> [0..*] ± 358
           SettlementStatus <SttlmSts> [0..*] ± 358
           Settled <Sttld> [0..1] ± C3 358
         DatePeriod <DtPrd> [0..1]  359
{Or           Date <Dt> [1..1]  359
{Or             FromDate <FrDt> [1..1] Date 359
Or             ToDate <ToDt> [1..1] Date 360
Or             FromToDate <FrToDt> [1..1] ± 360
Or             EqualDate <EQDt> [1..1] Date 360
Or}             NotEqualDate <NEQDt> [1..1] Date 360
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 342 August 2026
```

## File page 343

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}           DateTime <DtTm> [1..1]  360
{Or             FromDateTime <FrDtTm> [1..1] DateTime 360
Or             ToDateTime <ToDtTm> [1..1] DateTime 361
Or             FromToDateTime <FrToDtTm> [1..1] ± 361
Or             EqualDateTime <EQDtTm> [1..1] DateTime 361
Or}             NotEqualDateTime <NEQDtTm> [1..1] DateTime 361
       CashAccount <CshAcct> [0..*]  361
{Or         Equal <EQ> [1..1] ± 361
Or         ContainText <CTTxt> [1..1] Text 362
Or}         NotContainText <NCTTxt> [1..1] Text 362
       CashAccountOwner <CshAcctOwnr> [0..*] ± 362
       CashAccountServicer <CshAcctSvcr> [0..1] ± 362
       BalanceType <BalTp> [0..*]  C5 363
         BalanceFrom <BalFr> [0..1]  364
           Type <Tp> [1..1]  365
{Or             Code <Cd> [1..1] CodeSet 365
Or}             Proprietary <Prtry> [1..1] ± 365
           QuantityBreakdown <QtyBrkdwn> [0..*]  366
             LotNumber <LotNb> [0..1] ± 366
             LotAmount <LotAmt> [0..1] ± 366
             LotQuantity <LotQty> [0..1] ± 366
             CashSubBalanceType <CshSubBalTp> [0..1] ± 367
         BalanceTo <BalTo> [0..1]  367
           Type <Tp> [1..1]  367
{Or             Code <Cd> [1..1] CodeSet 368
Or}             Proprietary <Prtry> [1..1] ± 368
           QuantityBreakdown <QtyBrkdwn> [0..*]  368
             LotNumber <LotNb> [0..1] ± 368
             LotAmount <LotAmt> [0..1] ± 369
             LotQuantity <LotQty> [0..1] ± 369
             CashSubBalanceType <CshSubBalTp> [0..1] ± 369
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 343 August 2026
```

## File page 344

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CashSubBalanceIdentification <CshSubBalId> [0..*] ± 370
       SettlementAmount <SttlmAmt> [0..1] ± 370
       SettledAmount <SttldAmt> [0..1] ± 370
       SettlementCurrency <SttlmCcy> [0..*] CodeSet C2 371
       IntendedSettlementDate <IntnddSttlmDt> [0..1]  371
{Or         Date <Dt> [1..1]  372
{Or           FromDate <FrDt> [1..1] Date 372
Or           ToDate <ToDt> [1..1] Date 372
Or           FromToDate <FrToDt> [1..1] ± 373
Or           EqualDate <EQDt> [1..1] Date 373
Or}           NotEqualDate <NEQDt> [1..1] Date 373
Or}         DateTime <DtTm> [1..1]  373
{Or           FromDateTime <FrDtTm> [1..1] DateTime 373
Or           ToDateTime <ToDtTm> [1..1] DateTime 373
Or           FromToDateTime <FrToDtTm> [1..1] ± 374
Or           EqualDateTime <EQDtTm> [1..1] DateTime 374
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 374
       EffectiveSettlementDate <FctvSttlmDt> [0..1]  374
{Or         Date <Dt> [1..1]  375
{Or           FromDate <FrDt> [1..1] Date 375
Or           ToDate <ToDt> [1..1] Date 375
Or           FromToDate <FrToDt> [1..1] ± 376
Or           EqualDate <EQDt> [1..1] Date 376
Or}           NotEqualDate <NEQDt> [1..1] Date 376
Or}         DateTime <DtTm> [1..1]  376
{Or           FromDateTime <FrDtTm> [1..1] DateTime 376
Or           ToDateTime <ToDtTm> [1..1] DateTime 376
Or           FromToDateTime <FrToDtTm> [1..1] ± 377
Or           EqualDateTime <EQDtTm> [1..1] DateTime 377
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 377
       Priority <Prty> [0..*] ± 377
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 344 August 2026
```

