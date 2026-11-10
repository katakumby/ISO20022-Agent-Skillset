---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.7 Quantity", "16.2.7.2 Max30DecimalNumber"]
file_pages: [1247]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.7.2 Max30DecimalNumber

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1247 to 1247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1247

```text
16.2.7.2  Max30DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6 with a
maximum of 30 digits and 29 fraction digits.
Type: Quantity
Format
totalDigits 30
fractionDigits 29
16.2.7.3  Max3Number
Definition: Number (max 999) of objects represented as an integer.
Type: Quantity
Format
totalDigits 3
fractionDigits 0
Constraints
• NumberRule
If Number is negative, then Sign must be present.
16.2.8 Rate
16.2.8.1  BaseOne14Rate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70% with 13 fractional digits
maximum and 14 total digits.
Type: Rate
Format
totalDigits 14
fractionDigits 13
baseValue 1.0
16.2.8.2  Percentage14Rate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7% with 13 fractional digits maximum and 14 total digits.
Type: Rate
Format
totalDigits 14
fractionDigits 13
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1247 February 2026
```

