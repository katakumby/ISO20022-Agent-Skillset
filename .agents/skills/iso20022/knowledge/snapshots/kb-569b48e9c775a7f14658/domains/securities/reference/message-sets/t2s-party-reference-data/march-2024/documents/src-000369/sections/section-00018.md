---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.1 OpeningDate <OpngDt>", "3.4.2.1.4 EqualDate <EQDt>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.2.1.4 EqualDate <EQDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
3.4.2.1.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 184
3.4.2.1.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 184
3.4.2.2  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Specifies the closing date of the party.
ClosingDate <ClsgDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 24
Or   ToDate <ToDt> [1..1] Date 24
Or   FromToDate <FrToDt> [1..1] ± 24
Or   EqualDate <EQDt> [1..1] Date 25
Or}   NotEqualDate <NEQDt> [1..1] Date 25
3.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 184
3.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 184
3.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
24 March 2024
```

