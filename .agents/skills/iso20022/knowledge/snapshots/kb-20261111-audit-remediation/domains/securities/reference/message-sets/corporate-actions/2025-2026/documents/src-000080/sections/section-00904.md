---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.14 RateAndAmountFormat58Choice", "16.1.22.14.1 Rate <Rate>"]
file_pages: [1122]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.14.1 Rate <Rate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1122 to 1122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1122

```text
16.1.22.14.1  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.14.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateValueType7Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.22.14.3  Amount <Amt>
Presence: [1..1]
Definition: Value is expressed as a currency and amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.14.4  IndexPoints <IndxPts>
Presence: [1..1]
Definition: Price expressed in index points.
Datatype: "DecimalNumber" on page 1246
16.1.22.15  RateFormat25Choice
Definition: Choice between a rate or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1122
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
16.1.22.15.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1122 February 2026
```

