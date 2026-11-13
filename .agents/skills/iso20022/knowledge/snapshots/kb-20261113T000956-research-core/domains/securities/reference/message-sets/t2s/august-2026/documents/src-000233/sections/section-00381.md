---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "20.4 Message Building Blocks", "20.4.2 QueryDefinition <QryDef>", "20.4.2.2 SearchCriteria <SchCrit>", "20.4.2.2.7 CreationDateTime <CreDtTm>", "20.4.2.2.7.1 Date <Dt>"]
file_pages: [488]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 20.4.2.2.7.1 Date <Dt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 488 to 488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 488

```text
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  488
{Or     FromDate <FrDt> [1..1] Date 488
Or     ToDate <ToDt> [1..1] Date 488
Or     FromToDate <FrToDt> [1..1] ± 489
Or     EqualDate <EQDt> [1..1] Date 489
Or}     NotEqualDate <NEQDt> [1..1] Date 489
Or}   DateTime <DtTm> [1..1]  489
{Or     FromDateTime <FrDtTm> [1..1] DateTime 489
Or     ToDateTime <ToDtTm> [1..1] DateTime 489
Or     FromToDateTime <FrToDtTm> [1..1] ± 490
Or     EqualDateTime <EQDtTm> [1..1] DateTime 490
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 490
20.4.2.2.7.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 488
Or   ToDate <ToDt> [1..1] Date 488
Or   FromToDate <FrToDt> [1..1] ± 489
Or   EqualDate <EQDt> [1..1] Date 489
Or}   NotEqualDate <NEQDt> [1..1] Date 489
20.4.2.2.7.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
20.4.2.2.7.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 488 August 2026
```

