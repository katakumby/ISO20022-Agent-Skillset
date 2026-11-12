---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.7 Quantity"]
file_pages: [666]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.7 Quantity

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 666 to 666.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 666

```text
Meaning When True: Yes
Meaning When False: No
7.2.7 Quantity
7.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
7.2.7.2  Max3Number
Definition: Number (max 999) of objects represented as an integer.
Type: Quantity
Format
totalDigits 3
fractionDigits 0
Constraints
• NumberRule
If Number is negative, then Sign must be present.
7.2.7.3  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
7.2.8 Rate
7.2.8.1  BaseOneRate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.
Type: Rate
Format
totalDigits 11
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 666 February 2025
```

