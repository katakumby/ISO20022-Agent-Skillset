---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.9 Text", "37.2.9.15 Max4AlphaNumericText"]
file_pages: [890]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.9.15 Max4AlphaNumericText

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 890 to 890.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 890

```text
Format
pattern [0-9]{1,3}
37.2.9.15  Max4AlphaNumericText
Definition: Specifies an alphanumeric string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
pattern [a-zA-Z0-9]{1,4}
37.2.9.16  Max4Text
Definition: Specifies a character string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
37.2.9.17  Max5NumericText
Definition: Specifies a numeric string with a maximum length of 5 digits.
Type: Text
Format
pattern [0-9]{1,5}
37.2.9.18  Max70Text
Definition: Specifies a character string with a maximum length of 70characters.
Type: Text
Format
minLength 1
maxLength 70
37.2.9.19  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 890 February 2025
```

