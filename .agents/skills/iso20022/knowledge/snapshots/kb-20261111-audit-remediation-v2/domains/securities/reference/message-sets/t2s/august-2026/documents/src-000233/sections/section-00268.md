---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.1 QueryType <QryTp>"]
file_pages: [352, 353, 354, 355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.1 QueryType <QryTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 352 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 352

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateTime <DtTm> [1..1]  379
{Or         FromDateTime <FrDtTm> [1..1] DateTime 379
Or         ToDateTime <ToDtTm> [1..1] DateTime 380
Or         FromToDateTime <FrToDtTm> [1..1] ± 380
Or         EqualDateTime <EQDtTm> [1..1] DateTime 380
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 380
16.4.2.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 3264
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
16.4.2.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to extract the intra-balance movement instruction information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 352 August 2026
```

## File page 353

```text
SearchCriteria <SchCrit> contains the following IntraBalanceQueryCriteria11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   References <Refs> [0..*]  356
{Or     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 356
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 356
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 356
Or     ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 356
Or     PoolIdentification <PoolId> [1..1] Text 357
Or}     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 357
   Status <Sts> [0..1]  357
     Type <Tp> [1..1]  358
       ProcessingStatus <PrcgSts> [0..*] ± 358
       SettlementStatus <SttlmSts> [0..*] ± 358
       Settled <Sttld> [0..1] ± C3 358
     DatePeriod <DtPrd> [0..1]  359
{Or       Date <Dt> [1..1]  359
{Or         FromDate <FrDt> [1..1] Date 359
Or         ToDate <ToDt> [1..1] Date 360
Or         FromToDate <FrToDt> [1..1] ± 360
Or         EqualDate <EQDt> [1..1] Date 360
Or}         NotEqualDate <NEQDt> [1..1] Date 360
Or}       DateTime <DtTm> [1..1]  360
{Or         FromDateTime <FrDtTm> [1..1] DateTime 360
Or         ToDateTime <ToDtTm> [1..1] DateTime 361
Or         FromToDateTime <FrToDtTm> [1..1] ± 361
Or         EqualDateTime <EQDtTm> [1..1] DateTime 361
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 361
   CashAccount <CshAcct> [0..*]  361
{Or     Equal <EQ> [1..1] ± 361
Or     ContainText <CTTxt> [1..1] Text 362
Or}     NotContainText <NCTTxt> [1..1] Text 362
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 353 August 2026
```

## File page 354

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountOwner <CshAcctOwnr> [0..*] ± 362
   CashAccountServicer <CshAcctSvcr> [0..1] ± 362
   BalanceType <BalTp> [0..*]  C5 363
     BalanceFrom <BalFr> [0..1]  364
       Type <Tp> [1..1]  365
{Or         Code <Cd> [1..1] CodeSet 365
Or}         Proprietary <Prtry> [1..1] ± 365
       QuantityBreakdown <QtyBrkdwn> [0..*]  366
         LotNumber <LotNb> [0..1] ± 366
         LotAmount <LotAmt> [0..1] ± 366
         LotQuantity <LotQty> [0..1] ± 366
         CashSubBalanceType <CshSubBalTp> [0..1] ± 367
     BalanceTo <BalTo> [0..1]  367
       Type <Tp> [1..1]  367
{Or         Code <Cd> [1..1] CodeSet 368
Or}         Proprietary <Prtry> [1..1] ± 368
       QuantityBreakdown <QtyBrkdwn> [0..*]  368
         LotNumber <LotNb> [0..1] ± 368
         LotAmount <LotAmt> [0..1] ± 369
         LotQuantity <LotQty> [0..1] ± 369
         CashSubBalanceType <CshSubBalTp> [0..1] ± 369
   CashSubBalanceIdentification <CshSubBalId> [0..*] ± 370
   SettlementAmount <SttlmAmt> [0..1] ± 370
   SettledAmount <SttldAmt> [0..1] ± 370
   SettlementCurrency <SttlmCcy> [0..*] CodeSet C2 371
   IntendedSettlementDate <IntnddSttlmDt> [0..1]  371
{Or     Date <Dt> [1..1]  372
{Or       FromDate <FrDt> [1..1] Date 372
Or       ToDate <ToDt> [1..1] Date 372
Or       FromToDate <FrToDt> [1..1] ± 373
Or       EqualDate <EQDt> [1..1] Date 373
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 354 August 2026
```

## File page 355

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       NotEqualDate <NEQDt> [1..1] Date 373
Or}     DateTime <DtTm> [1..1]  373
{Or       FromDateTime <FrDtTm> [1..1] DateTime 373
Or       ToDateTime <ToDtTm> [1..1] DateTime 373
Or       FromToDateTime <FrToDtTm> [1..1] ± 374
Or       EqualDateTime <EQDtTm> [1..1] DateTime 374
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 374
   EffectiveSettlementDate <FctvSttlmDt> [0..1]  374
{Or     Date <Dt> [1..1]  375
{Or       FromDate <FrDt> [1..1] Date 375
Or       ToDate <ToDt> [1..1] Date 375
Or       FromToDate <FrToDt> [1..1] ± 376
Or       EqualDate <EQDt> [1..1] Date 376
Or}       NotEqualDate <NEQDt> [1..1] Date 376
Or}     DateTime <DtTm> [1..1]  376
{Or       FromDateTime <FrDtTm> [1..1] DateTime 376
Or       ToDateTime <ToDtTm> [1..1] DateTime 376
Or       FromToDateTime <FrToDtTm> [1..1] ± 377
Or       EqualDateTime <EQDtTm> [1..1] DateTime 377
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 377
   Priority <Prty> [0..*] ± 377
   MessageOriginator <MsgOrgtr> [0..*] ± 377
   CreationDateTime <CreDtTm> [0..1]  378
{Or     Date <Dt> [1..1]  378
{Or       FromDate <FrDt> [1..1] Date 378
Or       ToDate <ToDt> [1..1] Date 379
Or       FromToDate <FrToDt> [1..1] ± 379
Or       EqualDate <EQDt> [1..1] Date 379
Or}       NotEqualDate <NEQDt> [1..1] Date 379
Or}     DateTime <DtTm> [1..1]  379
{Or       FromDateTime <FrDtTm> [1..1] DateTime 379
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 355 August 2026
```

