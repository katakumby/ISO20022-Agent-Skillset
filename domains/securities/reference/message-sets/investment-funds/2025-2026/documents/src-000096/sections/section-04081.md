---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.9 Text"]
file_pages: [5402]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.9 Text

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5402 to 5402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5402

```text
66.2.9 Text
66.2.9.1  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
66.2.9.2  Extended350Code
Definition: Code and / or description for values that are not yet part of the related code list.
Type: Text
Format
minLength 1
maxLength 350
66.2.9.3  Max10Text
Definition: Specifies a character string with a maximum length of 10 characters.
Type: Text
Format
minLength 1
maxLength 10
66.2.9.4  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
66.2.9.5  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5402 May 2026
```

