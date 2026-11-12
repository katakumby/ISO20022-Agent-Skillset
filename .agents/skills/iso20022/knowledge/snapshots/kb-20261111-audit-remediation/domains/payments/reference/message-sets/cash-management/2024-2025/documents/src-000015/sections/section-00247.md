---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.2 Structure"]
file_pages: [365]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 365 to 365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 365

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <GetLmt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 367
   LimitQueryDefinition <LmtQryDef> [0..1]  368
     QueryType <QryTp> [0..1] CodeSet 370
     LimitCriteria <LmtCrit> [0..1]  370
{Or       QueryName <QryNm> [1..1] Text 372
Or}       NewCriteria <NewCrit> [1..1]  C7, C8 372
         NewQueryName <NewQryNm> [0..1] Text 374
         SearchCriteria <SchCrit> [0..*]  C3, C4 374
           SystemIdentification <SysId> [0..1] ± 376
           BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..*] ± 377
           DefaultLimitType <DfltLmtTp> [0..*]  377
{Or             Code <Cd> [1..1] CodeSet 377
Or}             Proprietary <Prtry> [1..1] Text 379
           CurrentLimitType <CurLmtTp> [0..*]  379
{Or             Code <Cd> [1..1] CodeSet 380
Or}             Proprietary <Prtry> [1..1] Text 382
           AccountOwner <AcctOwnr> [0..1] ± 382
           AccountIdentification <AcctId> [0..1] ± 382
           UsedAmount <UsdAmt> [0..1] ± 383
           UsedPercentage <UsdPctg> [0..1]  383
{Or             From <Fr> [1..1]  384
               BoundaryRate <BdryRate> [1..1] Rate 384
               Included <Incl> [1..1] Indicator 384
Or             To <To> [1..1]  385
               BoundaryRate <BdryRate> [1..1] Rate 385
               Included <Incl> [1..1] Indicator 385
Or             FromTo <FrTo> [1..1]  385
               From <Fr> [1..1]  385
                 BoundaryRate <BdryRate> [1..1] Rate 386
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 365 February 2025
```

