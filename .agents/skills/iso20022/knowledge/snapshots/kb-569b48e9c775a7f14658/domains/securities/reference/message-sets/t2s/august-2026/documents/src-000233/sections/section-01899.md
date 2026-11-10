---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.10 IntendedSettlementDate <IntnddSttlmDt>", "73.4.1.2.10.2 DateTime <DtTm>"]
file_pages: [2604]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.10.2 DateTime <DtTm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2604 to 2604.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2604

```text
73.4.1.2.10.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 2604
Or   ToDateTime <ToDtTm> [1..1] DateTime 2604
Or   FromToDateTime <FrToDtTm> [1..1] ± 2604
Or   EqualDateTime <EQDtTm> [1..1] DateTime 2604
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 2604
73.4.1.2.10.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
73.4.1.2.10.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
73.4.1.2.10.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on
page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
73.4.1.2.10.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 3320
73.4.1.2.10.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2604 August 2026
```

