---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.1 QueryType <QryTp>"]
file_pages: [370, 371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.1 QueryType <QryTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 370 to 371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Included <Incl> [1..1] Indicator 386
Or           Equal <EQ> [1..1] Rate 387
Or}           NotEqual <NEQ> [1..1] Rate 387
         LimitCurrency <LmtCcy> [0..1] CodeSet C1 387
         LimitAmount <LmtAmt> [0..1] ± 387
         LimitValidAsOfDate <LmtVldAsOfDt> [0..1]  387
{Or           Date <Dt> [1..1] Date 388
Or           Period <Prd> [1..1] ± 388
Or           FromDate <FrDt> [1..1] Date 388
Or}           ToDate <ToDt> [1..1] Date 388
       ReturnCriteria <RtrCrit> [0..1]  388
         StartDateTimeIndicator <StartDtTmInd> [0..1] Indicator 389
         StatusIndicator <StsInd> [0..1] Indicator 389
         UsedAmountIndicator <UsdAmtInd> [0..1] Indicator 389
         UsedPercentageIndicator <UsdPctgInd> [0..1] Indicator 389
8.4.2.1  QueryType <QryTp>
Presence: [0..1]
Definition: Specifies the type of matching items to be returned in the response to the query.
Datatype: "QueryType2Code" on page 872
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
DELD Deleted Specifies that the query requests that
items that have been deleted since the
last query be returned.
8.4.2.2  LimitCriteria <LmtCrit>
Presence: [0..1]
Definition: Defines the limit query criteria.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 370 February 2025
```

## File page 371

```text
LimitCriteria <LmtCrit> contains one of the following LimitCriteria7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 372
Or}   NewCriteria <NewCrit> [1..1]  C7, C8 372
     NewQueryName <NewQryNm> [0..1] Text 374
     SearchCriteria <SchCrit> [0..*]  C3, C4 374
       SystemIdentification <SysId> [0..1] ± 376
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..*] ± 377
       DefaultLimitType <DfltLmtTp> [0..*]  377
{Or         Code <Cd> [1..1] CodeSet 377
Or}         Proprietary <Prtry> [1..1] Text 379
       CurrentLimitType <CurLmtTp> [0..*]  379
{Or         Code <Cd> [1..1] CodeSet 380
Or}         Proprietary <Prtry> [1..1] Text 382
       AccountOwner <AcctOwnr> [0..1] ± 382
       AccountIdentification <AcctId> [0..1] ± 382
       UsedAmount <UsdAmt> [0..1] ± 383
       UsedPercentage <UsdPctg> [0..1]  383
{Or         From <Fr> [1..1]  384
           BoundaryRate <BdryRate> [1..1] Rate 384
           Included <Incl> [1..1] Indicator 384
Or         To <To> [1..1]  385
           BoundaryRate <BdryRate> [1..1] Rate 385
           Included <Incl> [1..1] Indicator 385
Or         FromTo <FrTo> [1..1]  385
           From <Fr> [1..1]  385
             BoundaryRate <BdryRate> [1..1] Rate 386
             Included <Incl> [1..1] Indicator 386
           To <To> [1..1]  386
             BoundaryRate <BdryRate> [1..1] Rate 386
             Included <Incl> [1..1] Indicator 386
Or         Equal <EQ> [1..1] Rate 387
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 371 February 2025
```

