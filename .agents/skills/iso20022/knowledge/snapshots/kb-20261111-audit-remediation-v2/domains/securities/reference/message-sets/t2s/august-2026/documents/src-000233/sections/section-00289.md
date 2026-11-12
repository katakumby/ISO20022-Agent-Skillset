---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.12 EffectiveSettlementDate <FctvSttlmDt>", "16.4.2.2.12.1 Date <Dt>", "16.4.2.2.12.1.3 FromToDate <FrToDt>"]
file_pages: [376]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.12.1.3 FromToDate <FrToDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 376 to 376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 376

```text
16.4.2.2.12.1.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
16.4.2.2.12.1.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
16.4.2.2.12.1.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
16.4.2.2.12.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 376
Or   ToDateTime <ToDtTm> [1..1] DateTime 376
Or   FromToDateTime <FrToDtTm> [1..1] ± 377
Or   EqualDateTime <EQDtTm> [1..1] DateTime 377
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 377
16.4.2.2.12.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
16.4.2.2.12.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 376 August 2026
```

