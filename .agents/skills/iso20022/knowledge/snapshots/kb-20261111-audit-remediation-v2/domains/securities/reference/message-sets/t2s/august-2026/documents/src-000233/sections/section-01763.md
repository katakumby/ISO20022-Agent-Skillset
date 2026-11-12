---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>"]
file_pages: [2422, 2423, 2424, 2425, 2426]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2 SearchCriteria <SchCrit>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2422 to 2426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2422

```text
CodeName Name Definition
INST Instruction Queries settlement instructions based on
criteria excluding statuses.
STTS Status Queries settlement instructions based on
criteria that includes statuses.
STPD StatusPeriod Queries settlement instructions based on
criteria that includes statuses during a
period.
71.4.1.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to extract the securities settlement instruction information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2422 August 2026
```

## File page 2423

```text
SearchCriteria <SchCrit> contains the following SettlementInstructionQueryCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   References <Refs> [0..*]  2427
{Or     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 2428
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2428
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2428
Or     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2428
Or     ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 2428
Or     PoolIdentification <PoolId> [1..1] Text 2429
Or     CommonIdentification <CmonId> [1..1] Text 2429
Or     TradeIdentification <TradId> [1..1] Text 2429
Or}     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 2429
   Status <Sts> [0..*]  2429
     Type <Tp> [1..1]  2430
       ProcessingStatus <PrcgSts> [0..*] ± 2431
       InferredMatchingStatus <IfrrdMtchgSts> [0..*] ± 2431
       MatchingStatus <MtchgSts> [0..*] ± 2431
       SettlementStatus <SttlmSts> [0..*] ± 2431
       Settled <Sttld> [0..1] ± C3 2432
     DatePeriod <DtPrd> [0..1]  2432
{Or       Date <Dt> [1..1]  2432
{Or         FromDate <FrDt> [1..1] Date 2433
Or         ToDate <ToDt> [1..1] Date 2433
Or         FromToDate <FrToDt> [1..1] ± 2433
Or         EqualDate <EQDt> [1..1] Date 2433
Or}         NotEqualDate <NEQDt> [1..1] Date 2433
Or}       DateTime <DtTm> [1..1]  2433
{Or         FromDateTime <FrDtTm> [1..1] DateTime 2434
Or         ToDateTime <ToDtTm> [1..1] DateTime 2434
Or         FromToDateTime <FrToDtTm> [1..1] ± 2434
Or         EqualDateTime <EQDtTm> [1..1] DateTime 2434
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2423 August 2026
```

## File page 2424

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 2434
   SecuritiesMovementType <SctiesMvmntTp> [0..*] CodeSet 2434
   Payment <Pmt> [0..*] CodeSet 2435
   SecuritiesTransactionType <SctiesTxTp> [0..*] ± 2435
   FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C9, C10,
C11
2435
   Priority <Prty> [0..*] ± 2436
   SafekeepingAccount <SfkpgAcct> [0..*] ± 2437
   CashAccount <CshAcct> [0..*]  2437
{Or     Equal <EQ> [1..1] ± 2437
Or     ContainText <CTTxt> [1..1] Text 2438
Or}     NotContainText <NCTTxt> [1..1] Text 2438
   TradeDate <TradDt> [0..1]  2438
{Or     Date <Dt> [1..1]  2438
{Or       FromDate <FrDt> [1..1] Date 2439
Or       ToDate <ToDt> [1..1] Date 2439
Or       FromToDate <FrToDt> [1..1] ± 2439
Or       EqualDate <EQDt> [1..1] Date 2439
Or}       NotEqualDate <NEQDt> [1..1] Date 2439
Or}     DateTime <DtTm> [1..1]  2439
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2440
Or       ToDateTime <ToDtTm> [1..1] DateTime 2440
Or       FromToDateTime <FrToDtTm> [1..1] ± 2440
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2440
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2440
   SettlementQuantity <SttlmQty> [0..1]  2440
{Or     Quantity <Qty> [1..1]  2441
{Or       Unit <Unit> [1..1]  2442
{Or         FromQuantity <FrQty> [1..1]  2443
           Boundary <Bdry> [1..1] Quantity 2443
           Included <Incl> [1..1] Indicator 2443
Or         ToQuantity <ToQty> [1..1]  2444
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2424 August 2026
```

## File page 2425

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Boundary <Bdry> [1..1] Quantity 2444
           Included <Incl> [1..1] Indicator 2444
Or         FromToQuantity <FrToQty> [1..1]  2444
           FromQuantity <FrQty> [1..1]  2444
             Boundary <Bdry> [1..1] Quantity 2445
             Included <Incl> [1..1] Indicator 2445
           ToQuantity <ToQty> [1..1]  2445
             Boundary <Bdry> [1..1] Quantity 2445
             Included <Incl> [1..1] Indicator 2445
Or         EqualQuantity <EQQty> [1..1] Quantity 2446
Or}         NotEqualQuantity <NEQQty> [1..1] Quantity 2446
Or       FaceAmount <FaceAmt> [1..1] ± 2446
Or}       AmortisedValue <AmtsdVal> [1..1] ± 2446
Or}     OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  2447
       FaceAmount <FaceAmt> [1..1] ± 2447
       AmortisedValue <AmtsdVal> [1..1] ± 2448
   SettledQuantity <SttldQty> [0..1]  2448
{Or     Quantity <Qty> [1..1]  2449
{Or       Unit <Unit> [1..1]  2450
{Or         FromQuantity <FrQty> [1..1]  2451
           Boundary <Bdry> [1..1] Quantity 2451
           Included <Incl> [1..1] Indicator 2451
Or         ToQuantity <ToQty> [1..1]  2452
           Boundary <Bdry> [1..1] Quantity 2452
           Included <Incl> [1..1] Indicator 2452
Or         FromToQuantity <FrToQty> [1..1]  2452
           FromQuantity <FrQty> [1..1]  2452
             Boundary <Bdry> [1..1] Quantity 2453
             Included <Incl> [1..1] Indicator 2453
           ToQuantity <ToQty> [1..1]  2453
             Boundary <Bdry> [1..1] Quantity 2453
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2425 August 2026
```

## File page 2426

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Included <Incl> [1..1] Indicator 2453
Or         EqualQuantity <EQQty> [1..1] Quantity 2454
Or}         NotEqualQuantity <NEQQty> [1..1] Quantity 2454
Or       FaceAmount <FaceAmt> [1..1] ± 2454
Or}       AmortisedValue <AmtsdVal> [1..1] ± 2454
Or}     OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  2455
       FaceAmount <FaceAmt> [1..1] ± 2455
       AmortisedValue <AmtsdVal> [1..1] ± 2456
   SettlementAmount <SttlmAmt> [0..1] ± 2456
   SettledAmount <SttldAmt> [0..1] ± 2456
   IntendedSettlementDate <IntnddSttlmDt> [0..1]  2457
{Or     Date <Dt> [1..1]  2457
{Or       FromDate <FrDt> [1..1] Date 2457
Or       ToDate <ToDt> [1..1] Date 2458
Or       FromToDate <FrToDt> [1..1] ± 2458
Or       EqualDate <EQDt> [1..1] Date 2458
Or}       NotEqualDate <NEQDt> [1..1] Date 2458
Or}     DateTime <DtTm> [1..1]  2458
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2458
Or       ToDateTime <ToDtTm> [1..1] DateTime 2459
Or       FromToDateTime <FrToDtTm> [1..1] ± 2459
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2459
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2459
   EffectiveSettlementDate <FctvSttlmDt> [0..1]  2459
{Or     Date <Dt> [1..1]  2460
{Or       FromDate <FrDt> [1..1] Date 2460
Or       ToDate <ToDt> [1..1] Date 2460
Or       FromToDate <FrToDt> [1..1] ± 2461
Or       EqualDate <EQDt> [1..1] Date 2461
Or}       NotEqualDate <NEQDt> [1..1] Date 2461
Or}     DateTime <DtTm> [1..1]  2461
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2426 August 2026
```

