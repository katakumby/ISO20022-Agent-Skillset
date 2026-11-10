---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.1 QueryType <QryTp>"]
file_pages: [161, 162, 163, 164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.1 QueryType <QryTp>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 161 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateTime <DtTm> [1..1]  188
{Or         FromDateTime <FrDtTm> [1..1] DateTime 188
Or         ToDateTime <ToDtTm> [1..1] DateTime 189
Or         FromToDateTime <FrToDtTm> [1..1] ± 189
Or         EqualDateTime <EQDtTm> [1..1] DateTime 189
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 189
9.4.2.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 485
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
9.4.2.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to extract the intra-balance movement instruction information.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
161 March 2024
```

## File page 162

```text
SearchCriteria <SchCrit> contains the following IntraBalanceQueryCriteria11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   References <Refs> [0..*]  165
{Or     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 165
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 165
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 165
Or     ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 165
Or     PoolIdentification <PoolId> [1..1] Text 166
Or}     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 166
   Status <Sts> [0..1]  166
     Type <Tp> [1..1]  167
       ProcessingStatus <PrcgSts> [0..*] ± 167
       SettlementStatus <SttlmSts> [0..*] ± 167
       Settled <Sttld> [0..1] ± C3 167
     DatePeriod <DtPrd> [0..1]  168
{Or       Date <Dt> [1..1]  168
{Or         FromDate <FrDt> [1..1] Date 168
Or         ToDate <ToDt> [1..1] Date 169
Or         FromToDate <FrToDt> [1..1] ± 169
Or         EqualDate <EQDt> [1..1] Date 169
Or}         NotEqualDate <NEQDt> [1..1] Date 169
Or}       DateTime <DtTm> [1..1]  169
{Or         FromDateTime <FrDtTm> [1..1] DateTime 169
Or         ToDateTime <ToDtTm> [1..1] DateTime 170
Or         FromToDateTime <FrToDtTm> [1..1] ± 170
Or         EqualDateTime <EQDtTm> [1..1] DateTime 170
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 170
   CashAccount <CshAcct> [0..*]  170
{Or     Equal <EQ> [1..1] ± 170
Or     ContainText <CTTxt> [1..1] Text 171
Or}     NotContainText <NCTTxt> [1..1] Text 171
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
162 March 2024
```

## File page 163

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountOwner <CshAcctOwnr> [0..*] ± 171
   CashAccountServicer <CshAcctSvcr> [0..1] ± 171
   BalanceType <BalTp> [0..*]  C5 172
     BalanceFrom <BalFr> [0..1]  173
       Type <Tp> [1..1]  174
{Or         Code <Cd> [1..1] CodeSet 174
Or}         Proprietary <Prtry> [1..1] ± 174
       QuantityBreakdown <QtyBrkdwn> [0..*]  175
         LotNumber <LotNb> [0..1] ± 175
         LotAmount <LotAmt> [0..1] ± 175
         LotQuantity <LotQty> [0..1] ± 175
         CashSubBalanceType <CshSubBalTp> [0..1] ± 176
     BalanceTo <BalTo> [0..1]  176
       Type <Tp> [1..1]  176
{Or         Code <Cd> [1..1] CodeSet 177
Or}         Proprietary <Prtry> [1..1] ± 177
       QuantityBreakdown <QtyBrkdwn> [0..*]  177
         LotNumber <LotNb> [0..1] ± 177
         LotAmount <LotAmt> [0..1] ± 178
         LotQuantity <LotQty> [0..1] ± 178
         CashSubBalanceType <CshSubBalTp> [0..1] ± 178
   CashSubBalanceIdentification <CshSubBalId> [0..*] ± 179
   SettlementAmount <SttlmAmt> [0..1] ± 179
   SettledAmount <SttldAmt> [0..1] ± 179
   SettlementCurrency <SttlmCcy> [0..*] CodeSet C2 180
   IntendedSettlementDate <IntnddSttlmDt> [0..1]  180
{Or     Date <Dt> [1..1]  181
{Or       FromDate <FrDt> [1..1] Date 181
Or       ToDate <ToDt> [1..1] Date 181
Or       FromToDate <FrToDt> [1..1] ± 182
Or       EqualDate <EQDt> [1..1] Date 182
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
163 March 2024
```

## File page 164

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       NotEqualDate <NEQDt> [1..1] Date 182
Or}     DateTime <DtTm> [1..1]  182
{Or       FromDateTime <FrDtTm> [1..1] DateTime 182
Or       ToDateTime <ToDtTm> [1..1] DateTime 182
Or       FromToDateTime <FrToDtTm> [1..1] ± 183
Or       EqualDateTime <EQDtTm> [1..1] DateTime 183
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 183
   EffectiveSettlementDate <FctvSttlmDt> [0..1]  183
{Or     Date <Dt> [1..1]  184
{Or       FromDate <FrDt> [1..1] Date 184
Or       ToDate <ToDt> [1..1] Date 184
Or       FromToDate <FrToDt> [1..1] ± 185
Or       EqualDate <EQDt> [1..1] Date 185
Or}       NotEqualDate <NEQDt> [1..1] Date 185
Or}     DateTime <DtTm> [1..1]  185
{Or       FromDateTime <FrDtTm> [1..1] DateTime 185
Or       ToDateTime <ToDtTm> [1..1] DateTime 185
Or       FromToDateTime <FrToDtTm> [1..1] ± 186
Or       EqualDateTime <EQDtTm> [1..1] DateTime 186
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 186
   Priority <Prty> [0..*] ± 186
   MessageOriginator <MsgOrgtr> [0..*] ± 186
   CreationDateTime <CreDtTm> [0..1]  187
{Or     Date <Dt> [1..1]  187
{Or       FromDate <FrDt> [1..1] Date 187
Or       ToDate <ToDt> [1..1] Date 188
Or       FromToDate <FrToDt> [1..1] ± 188
Or       EqualDate <EQDt> [1..1] Date 188
Or}       NotEqualDate <NEQDt> [1..1] Date 188
Or}     DateTime <DtTm> [1..1]  188
{Or       FromDateTime <FrDtTm> [1..1] DateTime 188
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
164 March 2024
```

