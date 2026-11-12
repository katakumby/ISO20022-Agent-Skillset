---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.50 RateFormat12Choice"]
file_pages: [971]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.50 RateFormat12Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 971 to 971.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 971

```text
CodeName Name Definition
UNSO Unsolicited The corporate action instruction is
unsolicited, that is, the instruction has
not been preceded by a corporate action
notification.
16.1.15.50  RateFormat12Choice
Definition: Choice between a rate or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
16.1.15.50.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Datatype: "BaseOne14Rate" on page 1247
16.1.15.50.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateType5Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.15.51  CorporateActionEventProcessingType2Choice
Definition: Choice between a standard code or a proprietary code for specifying the processing type of a
corporate action event.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 971
Or}   Proprietary <Prtry> [1..1] ± 972
16.1.15.51.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the processing type of a corporate action event.
Datatype: "CorporateActionEventProcessingType1Code" on page 1168
CodeName Name Definition
GENL General No debit or credit of resources.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 971 February 2026
```

