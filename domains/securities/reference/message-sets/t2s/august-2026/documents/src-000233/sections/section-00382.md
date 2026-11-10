---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "20.4 Message Building Blocks", "20.4.2 QueryDefinition <QryDef>", "20.4.2.2 SearchCriteria <SchCrit>", "20.4.2.2.7 CreationDateTime <CreDtTm>", "20.4.2.2.7.1 Date <Dt>", "20.4.2.2.7.1.3 FromToDate <FrToDt>"]
file_pages: [489]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 20.4.2.2.7.1.3 FromToDate <FrToDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 489 to 489.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 489

```text
20.4.2.2.7.1.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
20.4.2.2.7.1.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
20.4.2.2.7.1.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
20.4.2.2.7.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 489
Or   ToDateTime <ToDtTm> [1..1] DateTime 489
Or   FromToDateTime <FrToDtTm> [1..1] ± 490
Or   EqualDateTime <EQDtTm> [1..1] DateTime 490
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 490
20.4.2.2.7.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
20.4.2.2.7.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 489 August 2026
```

