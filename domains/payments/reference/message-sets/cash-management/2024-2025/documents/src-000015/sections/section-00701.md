---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.8 Rate", "37.2.8.2 PercentageRate"]
file_pages: [887]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.8.2 PercentageRate

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 887 to 887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 887

```text
37.2.8.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
37.2.9 Text
37.2.9.1  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
37.2.9.2  Max105Text
Definition: Specifies a character string with a maximum length of 105 characters.
Type: Text
Format
minLength 1
maxLength 105
37.2.9.3  Max10Text
Definition: Specifies a character string with a maximum length of 10 characters.
Type: Text
Format
minLength 1
maxLength 10
37.2.9.4  Max128Text
Definition: Specifies a character string with a maximum length of 128 characters.
Type: Text
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 887 February 2025
```

