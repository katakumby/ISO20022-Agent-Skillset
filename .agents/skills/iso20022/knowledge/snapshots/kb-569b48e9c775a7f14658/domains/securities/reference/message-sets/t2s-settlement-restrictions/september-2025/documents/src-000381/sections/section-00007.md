---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks"]
file_pages: [13, 14, 15, 16, 17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4 Message Building Blocks

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 13 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 QueryDefinition <QryDef>
Presence: [1..1]
Definition: Defines the intra-position movement instruction query criteria.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 13 September 2025
```

## File page 14

```text
QueryDefinition <QryDef> contains the following IntraPositionQueryDefinition8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [1..1] CodeSet 18
   SearchCriteria <SchCrit> [1..1]  18
     References <Refs> [0..*]  23
{Or       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 23
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 23
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 23
Or       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 23
Or       ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 23
Or       PoolIdentification <PoolId> [1..1] Text 24
Or}       CorporateActionEventIdentification
<CorpActnEvtId>
[1..1] Text 24
     Status <Sts> [0..1]  24
       Type <Tp> [1..1]  25
         ProcessingStatus <PrcgSts> [0..*] ± 25
         SettlementStatus <SttlmSts> [0..*] ± 25
         Settled <Sttld> [0..1] ± C1 25
       DatePeriod <DtPrd> [0..1]  26
{Or         Date <Dt> [1..1]  26
{Or           FromDate <FrDt> [1..1] Date 26
Or           ToDate <ToDt> [1..1] Date 27
Or           FromToDate <FrToDt> [1..1] ± 27
Or           EqualDate <EQDt> [1..1] Date 27
Or}           NotEqualDate <NEQDt> [1..1] Date 27
Or}         DateTime <DtTm> [1..1]  27
{Or           FromDateTime <FrDtTm> [1..1] DateTime 27
Or           ToDateTime <ToDtTm> [1..1] DateTime 28
Or           FromToDateTime <FrToDtTm> [1..1] ± 28
Or           EqualDateTime <EQDtTm> [1..1] DateTime 28
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 28
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 14 September 2025
```

## File page 15

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C5, C6,
C7, C8,
C9
28
     SafekeepingAccountOwner <SfkpgAcctOwnr> [0..*] ± 29
     SafekeepingAccount <SfkpgAcct> [0..*] ± 30
     BalanceType <BalTp> [0..*]  C3 30
       BalanceFrom <BalFr> [0..1] ± 30
       BalanceTo <BalTo> [0..1] ± 31
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..*] ± 31
     SettlementQuantity <SttlmQty> [0..1]  31
{Or       Quantity <Qty> [1..1]  32
{Or         Unit <Unit> [1..1]  33
{Or           FromQuantity <FrQty> [1..1]  34
             Boundary <Bdry> [1..1] Quantity 34
             Included <Incl> [1..1] Indicator 34
Or           ToQuantity <ToQty> [1..1]  35
             Boundary <Bdry> [1..1] Quantity 35
             Included <Incl> [1..1] Indicator 35
Or           FromToQuantity <FrToQty> [1..1]  35
             FromQuantity <FrQty> [1..1]  35
               Boundary <Bdry> [1..1] Quantity 36
               Included <Incl> [1..1] Indicator 36
             ToQuantity <ToQty> [1..1]  36
               Boundary <Bdry> [1..1] Quantity 36
               Included <Incl> [1..1] Indicator 36
Or           EqualQuantity <EQQty> [1..1] Quantity 37
Or}           NotEqualQuantity <NEQQty> [1..1] Quantity 37
Or         FaceAmount <FaceAmt> [1..1] ± 37
Or}         AmortisedValue <AmtsdVal> [1..1] ± 37
Or}       OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  38
         FaceAmount <FaceAmt> [1..1] ± 38
         AmortisedValue <AmtsdVal> [1..1] ± 39
     SettledQuantity <SttldQty> [0..1]  39
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 15 September 2025
```

## File page 16

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Quantity <Qty> [1..1]  40
{Or         Unit <Unit> [1..1]  41
{Or           FromQuantity <FrQty> [1..1]  42
             Boundary <Bdry> [1..1] Quantity 42
             Included <Incl> [1..1] Indicator 42
Or           ToQuantity <ToQty> [1..1]  43
             Boundary <Bdry> [1..1] Quantity 43
             Included <Incl> [1..1] Indicator 43
Or           FromToQuantity <FrToQty> [1..1]  43
             FromQuantity <FrQty> [1..1]  43
               Boundary <Bdry> [1..1] Quantity 44
               Included <Incl> [1..1] Indicator 44
             ToQuantity <ToQty> [1..1]  44
               Boundary <Bdry> [1..1] Quantity 44
               Included <Incl> [1..1] Indicator 44
Or           EqualQuantity <EQQty> [1..1] Quantity 45
Or}           NotEqualQuantity <NEQQty> [1..1] Quantity 45
Or         FaceAmount <FaceAmt> [1..1] ± 45
Or}         AmortisedValue <AmtsdVal> [1..1] ± 45
Or}       OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  46
         FaceAmount <FaceAmt> [1..1] ± 46
         AmortisedValue <AmtsdVal> [1..1] ± 47
     IntendedSettlementDate <IntnddSttlmDt> [0..1]  47
{Or       Date <Dt> [1..1]  48
{Or         FromDate <FrDt> [1..1] Date 48
Or         ToDate <ToDt> [1..1] Date 48
Or         FromToDate <FrToDt> [1..1] ± 48
Or         EqualDate <EQDt> [1..1] Date 48
Or}         NotEqualDate <NEQDt> [1..1] Date 48
Or}       DateTime <DtTm> [1..1]  49
{Or         FromDateTime <FrDtTm> [1..1] DateTime 49
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 16 September 2025
```

## File page 17

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         ToDateTime <ToDtTm> [1..1] DateTime 49
Or         FromToDateTime <FrToDtTm> [1..1] ± 49
Or         EqualDateTime <EQDtTm> [1..1] DateTime 49
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 49
     EffectiveSettlementDate <FctvSttlmDt> [0..1]  50
{Or       Date <Dt> [1..1]  50
{Or         FromDate <FrDt> [1..1] Date 50
Or         ToDate <ToDt> [1..1] Date 51
Or         FromToDate <FrToDt> [1..1] ± 51
Or         EqualDate <EQDt> [1..1] Date 51
Or}         NotEqualDate <NEQDt> [1..1] Date 51
Or}       DateTime <DtTm> [1..1]  51
{Or         FromDateTime <FrDtTm> [1..1] DateTime 51
Or         ToDateTime <ToDtTm> [1..1] DateTime 52
Or         FromToDateTime <FrToDtTm> [1..1] ± 52
Or         EqualDateTime <EQDtTm> [1..1] DateTime 52
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 52
     Priority <Prty> [0..*] ± 52
     CountryOfIssue <CtryOfIsse> [0..*] CodeSet C4 52
     MessageOriginator <MsgOrgtr> [0..*] ± 53
     CreationDateTime <CreDtTm> [0..1]  53
{Or       Date <Dt> [1..1]  53
{Or         FromDate <FrDt> [1..1] Date 54
Or         ToDate <ToDt> [1..1] Date 54
Or         FromToDate <FrToDt> [1..1] ± 54
Or         EqualDate <EQDt> [1..1] Date 54
Or}         NotEqualDate <NEQDt> [1..1] Date 54
Or}       DateTime <DtTm> [1..1]  54
{Or         FromDateTime <FrDtTm> [1..1] DateTime 55
Or         ToDateTime <ToDtTm> [1..1] DateTime 55
Or         FromToDateTime <FrToDtTm> [1..1] ± 55
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 17 September 2025
```

