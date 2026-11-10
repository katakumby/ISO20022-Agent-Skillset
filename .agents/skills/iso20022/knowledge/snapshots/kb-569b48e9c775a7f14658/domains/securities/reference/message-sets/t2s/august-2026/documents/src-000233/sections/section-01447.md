---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.2 SearchCriteria <SchCrit>", "35.4.2.1 OpeningDate <OpngDt>", "35.4.2.1.4 EqualDate <EQDt>"]
file_pages: [2061]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.2.1.4 EqualDate <EQDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2061 to 2061.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2061

```text
35.4.2.1.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
35.4.2.1.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
35.4.2.2  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Specifies the closing date of the party.
ClosingDate <ClsgDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2061
Or   ToDate <ToDt> [1..1] Date 2061
Or   FromToDate <FrToDt> [1..1] ± 2061
Or   EqualDate <EQDt> [1..1] Date 2062
Or}   NotEqualDate <NEQDt> [1..1] Date 2062
35.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
35.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
35.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2061 August 2026
```

