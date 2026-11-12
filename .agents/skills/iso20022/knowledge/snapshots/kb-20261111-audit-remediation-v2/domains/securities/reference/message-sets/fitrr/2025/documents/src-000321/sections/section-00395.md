---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.7 Quantity", "22.2.7.6 Max5Number"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.7.6 Max5Number

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

```text
Constraints
• NumberRule
If Number is negative, then Sign must be present.
22.2.7.6  Max5Number
Definition: Number (max 99999) of objects represented as an integer.
Type: Quantity
Format
totalDigits 5
fractionDigits 0
Constraints
• NumberRule
If Number is negative, then Sign must be present.
22.2.7.7  NonNegativeDecimalNumber
Definition: Number of objects represented as a non negative decimal number, for example, 0.75 or
45.6.
Type: Quantity
Format
minInclusive 0
totalDigits 18
fractionDigits 17
22.2.7.8  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
22.2.7.9  RestrictedMonthExact2Number
Definition: Two digit restricted list for use representing calendar months.
Type: Quantity
Format
minInclusive 1
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
453 July 2025
```

