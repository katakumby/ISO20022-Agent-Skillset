---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.9 Text"]
file_pages: [1248]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.9 Text

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1248 to 1248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1248

```text
baseValue 100.0
16.2.9 Text
16.2.9.1  Exact3NumericText
Definition: Specifies a numeric string with an exact length of 3 digits.
Type: Text
Format
pattern [0-9]{3}
16.2.9.2  Exact3UpperCaseAlphaNumericText
Definition: Specifies an upper case alphanumeric string with a length of three characters.
Type: Text
Format
pattern [A-Z0-9]{3}
16.2.9.3  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
16.2.9.4  ISO20022MessageIdentificationText
Definition: ISO 20022 Message identifier of an MX message.
Type: Text
Format
pattern [a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}
16.2.9.5  Max128Text
Definition: Specifies a character string with a maximum length of 128 characters.
Type: Text
Format
minLength 1
maxLength 128
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1248 February 2026
```

