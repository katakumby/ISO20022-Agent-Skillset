---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.10 Text"]
file_pages: [607]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.10 Text

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 607 to 607.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 607

```text
6.2.10 Text
6.2.10.1  Exact2NumericText
Definition: Specifies a numeric string with an exact length of 2 digits.
Type: Text
Format
pattern [0-9]{2}
6.2.10.2  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
6.2.10.3  Max1025Text
Definition: Specifies a character string with a maximum length of 1025 characters.
Type: Text
Format
minLength 1
maxLength 1025
6.2.10.4  Max105Text
Definition: Specifies a character string with a maximum length of 105 characters.
Type: Text
Format
minLength 1
maxLength 105
6.2.10.5  Max10Text
Definition: Specifies a character string with a maximum length of 10 characters.
Type: Text
Format
minLength 1
maxLength 10
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 607 March 2026
```

