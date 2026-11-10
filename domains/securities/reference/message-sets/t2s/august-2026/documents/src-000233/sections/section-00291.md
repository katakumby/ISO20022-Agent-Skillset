---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.15 CreationDateTime <CreDtTm>"]
file_pages: [378]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.15 CreationDateTime <CreDtTm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 378 to 378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 378

```text
16.4.2.2.15  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Specifies the creation date/time of the intra-balance movement.
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  378
{Or     FromDate <FrDt> [1..1] Date 378
Or     ToDate <ToDt> [1..1] Date 379
Or     FromToDate <FrToDt> [1..1] ± 379
Or     EqualDate <EQDt> [1..1] Date 379
Or}     NotEqualDate <NEQDt> [1..1] Date 379
Or}   DateTime <DtTm> [1..1]  379
{Or     FromDateTime <FrDtTm> [1..1] DateTime 379
Or     ToDateTime <ToDtTm> [1..1] DateTime 380
Or     FromToDateTime <FrToDtTm> [1..1] ± 380
Or     EqualDateTime <EQDtTm> [1..1] DateTime 380
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 380
16.4.2.2.15.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 378
Or   ToDate <ToDt> [1..1] Date 379
Or   FromToDate <FrToDt> [1..1] ± 379
Or   EqualDate <EQDt> [1..1] Date 379
Or}   NotEqualDate <NEQDt> [1..1] Date 379
16.4.2.2.15.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 378 August 2026
```

