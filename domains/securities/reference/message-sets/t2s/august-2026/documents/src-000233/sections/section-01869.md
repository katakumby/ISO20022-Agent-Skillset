---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.2 Structure"]
file_pages: [2563, 2564, 2565, 2566]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2563 to 2566.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2563

```text
73.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntQry> [1..1]  
   QueryDefinition <QryDef> [1..1]  2568
     QueryType <QryTp> [1..1] CodeSet 2573
     SearchCriteria <SchCrit> [1..1]  2573
       References <Refs> [0..*]  2578
{Or         AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 2578
Or         AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 2578
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2578
Or         CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2578
Or         ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 2578
Or         PoolIdentification <PoolId> [1..1] Text 2579
Or}         CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 2579
       Status <Sts> [0..1]  2579
         Type <Tp> [1..1]  2580
           ProcessingStatus <PrcgSts> [0..*] ± 2580
           SettlementStatus <SttlmSts> [0..*] ± 2580
           Settled <Sttld> [0..1] ± C1 2580
         DatePeriod <DtPrd> [0..1]  2581
{Or           Date <Dt> [1..1]  2581
{Or             FromDate <FrDt> [1..1] Date 2581
Or             ToDate <ToDt> [1..1] Date 2582
Or             FromToDate <FrToDt> [1..1] ± 2582
Or             EqualDate <EQDt> [1..1] Date 2582
Or}             NotEqualDate <NEQDt> [1..1] Date 2582
Or}           DateTime <DtTm> [1..1]  2582
{Or             FromDateTime <FrDtTm> [1..1] DateTime 2582
Or             ToDateTime <ToDtTm> [1..1] DateTime 2583
Or             FromToDateTime <FrToDtTm> [1..1] ± 2583
Or             EqualDateTime <EQDtTm> [1..1] DateTime 2583
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2563 August 2026
```

## File page 2564

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             NotEqualDateTime <NEQDtTm> [1..1] DateTime 2583
       FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C5, C6,
C7, C8,
C9
2583
       SafekeepingAccountOwner <SfkpgAcctOwnr> [0..*] ± 2584
       SafekeepingAccount <SfkpgAcct> [0..*] ± 2585
       BalanceType <BalTp> [0..*]  C3 2585
         BalanceFrom <BalFr> [0..1] ± 2585
         BalanceTo <BalTo> [0..1] ± 2586
       SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..*] ± 2586
       SettlementQuantity <SttlmQty> [0..1]  2586
{Or         Quantity <Qty> [1..1]  2587
{Or           Unit <Unit> [1..1]  2588
{Or             FromQuantity <FrQty> [1..1]  2589
               Boundary <Bdry> [1..1] Quantity 2589
               Included <Incl> [1..1] Indicator 2589
Or             ToQuantity <ToQty> [1..1]  2590
               Boundary <Bdry> [1..1] Quantity 2590
               Included <Incl> [1..1] Indicator 2590
Or             FromToQuantity <FrToQty> [1..1]  2590
               FromQuantity <FrQty> [1..1]  2590
                 Boundary <Bdry> [1..1] Quantity 2591
                 Included <Incl> [1..1] Indicator 2591
               ToQuantity <ToQty> [1..1]  2591
                 Boundary <Bdry> [1..1] Quantity 2591
                 Included <Incl> [1..1] Indicator 2591
Or             EqualQuantity <EQQty> [1..1] Quantity 2592
Or}             NotEqualQuantity <NEQQty> [1..1] Quantity 2592
Or           FaceAmount <FaceAmt> [1..1] ± 2592
Or}           AmortisedValue <AmtsdVal> [1..1] ± 2592
Or}         OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  2593
           FaceAmount <FaceAmt> [1..1] ± 2593
           AmortisedValue <AmtsdVal> [1..1] ± 2594
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2564 August 2026
```

## File page 2565

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       SettledQuantity <SttldQty> [0..1]  2594
{Or         Quantity <Qty> [1..1]  2595
{Or           Unit <Unit> [1..1]  2596
{Or             FromQuantity <FrQty> [1..1]  2597
               Boundary <Bdry> [1..1] Quantity 2597
               Included <Incl> [1..1] Indicator 2597
Or             ToQuantity <ToQty> [1..1]  2598
               Boundary <Bdry> [1..1] Quantity 2598
               Included <Incl> [1..1] Indicator 2598
Or             FromToQuantity <FrToQty> [1..1]  2598
               FromQuantity <FrQty> [1..1]  2598
                 Boundary <Bdry> [1..1] Quantity 2599
                 Included <Incl> [1..1] Indicator 2599
               ToQuantity <ToQty> [1..1]  2599
                 Boundary <Bdry> [1..1] Quantity 2599
                 Included <Incl> [1..1] Indicator 2599
Or             EqualQuantity <EQQty> [1..1] Quantity 2600
Or}             NotEqualQuantity <NEQQty> [1..1] Quantity 2600
Or           FaceAmount <FaceAmt> [1..1] ± 2600
Or}           AmortisedValue <AmtsdVal> [1..1] ± 2600
Or}         OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  2601
           FaceAmount <FaceAmt> [1..1] ± 2601
           AmortisedValue <AmtsdVal> [1..1] ± 2602
       IntendedSettlementDate <IntnddSttlmDt> [0..1]  2602
{Or         Date <Dt> [1..1]  2603
{Or           FromDate <FrDt> [1..1] Date 2603
Or           ToDate <ToDt> [1..1] Date 2603
Or           FromToDate <FrToDt> [1..1] ± 2603
Or           EqualDate <EQDt> [1..1] Date 2603
Or}           NotEqualDate <NEQDt> [1..1] Date 2603
Or}         DateTime <DtTm> [1..1]  2604
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2565 August 2026
```

## File page 2566

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           FromDateTime <FrDtTm> [1..1] DateTime 2604
Or           ToDateTime <ToDtTm> [1..1] DateTime 2604
Or           FromToDateTime <FrToDtTm> [1..1] ± 2604
Or           EqualDateTime <EQDtTm> [1..1] DateTime 2604
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 2604
       EffectiveSettlementDate <FctvSttlmDt> [0..1]  2605
{Or         Date <Dt> [1..1]  2605
{Or           FromDate <FrDt> [1..1] Date 2605
Or           ToDate <ToDt> [1..1] Date 2606
Or           FromToDate <FrToDt> [1..1] ± 2606
Or           EqualDate <EQDt> [1..1] Date 2606
Or}           NotEqualDate <NEQDt> [1..1] Date 2606
Or}         DateTime <DtTm> [1..1]  2606
{Or           FromDateTime <FrDtTm> [1..1] DateTime 2606
Or           ToDateTime <ToDtTm> [1..1] DateTime 2607
Or           FromToDateTime <FrToDtTm> [1..1] ± 2607
Or           EqualDateTime <EQDtTm> [1..1] DateTime 2607
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 2607
       Priority <Prty> [0..*] ± 2607
       CountryOfIssue <CtryOfIsse> [0..*] CodeSet C4 2607
       MessageOriginator <MsgOrgtr> [0..*] ± 2608
       CreationDateTime <CreDtTm> [0..1]  2608
{Or         Date <Dt> [1..1]  2608
{Or           FromDate <FrDt> [1..1] Date 2609
Or           ToDate <ToDt> [1..1] Date 2609
Or           FromToDate <FrToDt> [1..1] ± 2609
Or           EqualDate <EQDt> [1..1] Date 2609
Or}           NotEqualDate <NEQDt> [1..1] Date 2609
Or}         DateTime <DtTm> [1..1]  2609
{Or           FromDateTime <FrDtTm> [1..1] DateTime 2610
Or           ToDateTime <ToDtTm> [1..1] DateTime 2610
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2566 August 2026
```

