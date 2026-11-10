---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "13.4 Message Building Blocks", "13.4.2 QueryDefinition <QryDef>", "13.4.2.1 QueryType <QryTp>"]
file_pages: [291]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 13.4.2.1 QueryType <QryTp>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 291 to 291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
QueryDefinition <QryDef> contains the following IntraBalanceQueryDefinition10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [1..1] CodeSet 291
   SearchCriteria <SchCrit> [1..1]  292
     CancellationRequestIdentification <CxlReqId> [0..*] Text 293
     ProcessingStatus <PrcgSts> [0..*]  293
{Or       Code <Cd> [1..1] CodeSet 294
Or}       Proprietary <Prtry> [1..1] ± 294
     CashAccount <CshAcct> [0..*]  294
{Or       Equal <EQ> [1..1] ± 295
Or       ContainText <CTTxt> [1..1] Text 295
Or}       NotContainText <NCTTxt> [1..1] Text 295
     CashAccountOwner <CshAcctOwnr> [0..*] ± 295
     CashAccountServicer <CshAcctSvcr> [0..1] ± 295
     MessageOriginator <MsgOrgtr> [0..*] ± 296
     CreationDateTime <CreDtTm> [0..1]  296
{Or       Date <Dt> [1..1]  297
{Or         FromDate <FrDt> [1..1] Date 297
Or         ToDate <ToDt> [1..1] Date 297
Or         FromToDate <FrToDt> [1..1] ± 298
Or         EqualDate <EQDt> [1..1] Date 298
Or}         NotEqualDate <NEQDt> [1..1] Date 298
Or}       DateTime <DtTm> [1..1]  298
{Or         FromDateTime <FrDtTm> [1..1] DateTime 298
Or         ToDateTime <ToDtTm> [1..1] DateTime 298
Or         FromToDateTime <FrToDtTm> [1..1] ± 299
Or         EqualDateTime <EQDtTm> [1..1] DateTime 299
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 299
13.4.2.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 485
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
291 March 2024
```

