---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.74 SolicitationFeeRateFormat11Choice", "16.1.15.74.4 NotSpecifiedRate <NotSpcfdRate>"]
file_pages: [1026]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.74.4 NotSpecifiedRate <NotSpcfdRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1026 to 1026.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1026

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.74.4  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateValueType7Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.15.75  RateAndAmountFormat60Choice
Definition: Choice of format between a rate or a rate type and rate or an amount or a unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1026
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1026
Or   Amount <Amt> [1..1] Amount C1 1026
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1027
     RateType <RateTp> [1..1]  1027
{Or       Code <Cd> [1..1] CodeSet 1027
Or}       Proprietary <Prtry> [1..1] ± 1028
     Rate <Rate> [1..1] Rate 1028
16.1.15.75.1  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.15.75.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateValueType7Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.15.75.3  Amount <Amt>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1026 February 2026
```

