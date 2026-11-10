---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>"]
file_pages: [368, 369]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2 LimitQueryDefinition <LmtQryDef>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 368 to 369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader9" on page 810 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 810
   CreationDateTime <CreDtTm> [0..1] DateTime 810
   RequestType <ReqTp> [0..1]  810
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 810
Or     Enquiry <Enqry> [1..1] CodeSet 811
Or}     Proprietary <Prtry> [1..1] ± 811
8.4.2 LimitQueryDefinition <LmtQryDef>
Presence: [0..1]
Definition: Defines the limit query criteria.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 368 February 2025
```

## File page 369

```text
LimitQueryDefinition <LmtQryDef> contains the following LimitQuery5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [0..1] CodeSet 370
   LimitCriteria <LmtCrit> [0..1]  370
{Or     QueryName <QryNm> [1..1] Text 372
Or}     NewCriteria <NewCrit> [1..1]  C7, C8 372
       NewQueryName <NewQryNm> [0..1] Text 374
       SearchCriteria <SchCrit> [0..*]  C3, C4 374
         SystemIdentification <SysId> [0..1] ± 376
         BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..*] ± 377
         DefaultLimitType <DfltLmtTp> [0..*]  377
{Or           Code <Cd> [1..1] CodeSet 377
Or}           Proprietary <Prtry> [1..1] Text 379
         CurrentLimitType <CurLmtTp> [0..*]  379
{Or           Code <Cd> [1..1] CodeSet 380
Or}           Proprietary <Prtry> [1..1] Text 382
         AccountOwner <AcctOwnr> [0..1] ± 382
         AccountIdentification <AcctId> [0..1] ± 382
         UsedAmount <UsdAmt> [0..1] ± 383
         UsedPercentage <UsdPctg> [0..1]  383
{Or           From <Fr> [1..1]  384
             BoundaryRate <BdryRate> [1..1] Rate 384
             Included <Incl> [1..1] Indicator 384
Or           To <To> [1..1]  385
             BoundaryRate <BdryRate> [1..1] Rate 385
             Included <Incl> [1..1] Indicator 385
Or           FromTo <FrTo> [1..1]  385
             From <Fr> [1..1]  385
               BoundaryRate <BdryRate> [1..1] Rate 386
               Included <Incl> [1..1] Indicator 386
             To <To> [1..1]  386
               BoundaryRate <BdryRate> [1..1] Rate 386
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 369 February 2025
```

