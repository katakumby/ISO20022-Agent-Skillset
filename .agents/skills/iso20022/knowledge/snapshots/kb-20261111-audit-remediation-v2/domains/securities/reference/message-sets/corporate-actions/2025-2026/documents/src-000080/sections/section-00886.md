---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.5 RateFormat32Choice", "16.1.22.5.1 Rate <Rate>"]
file_pages: [1104]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.5.1 Rate <Rate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1104 to 1104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1104

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1104
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1104
16.1.22.5.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.5.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateType14Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
JLID IssuerDiscretion Indicates that there will not be a uniform
proration rate that applies to all
instructions or accounts.
16.1.22.6  RateFormat31Choice
Definition: Choice between a rate or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1104
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1104
Or}   Amount <Amt> [1..1] Amount C1 1105
16.1.22.6.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.6.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateType5Code" on page 1235
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1104 February 2026
```

