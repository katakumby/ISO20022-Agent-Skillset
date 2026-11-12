---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.2 Message Datatypes", "3.2.6 Text", "3.2.6.8 Max35Text"]
file_pages: [57]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.2.6.8 Max35Text

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 57 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
3.2.6.8  Max35Text
Definition: Specifies a character string with a maximum length of 35 characters.
Type: Text
Format
minLength 1
maxLength 35
3.2.6.9  Max4Text
Definition: Specifies a character string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
3.2.6.10  Max70Text
Definition: Specifies a character string with a maximum length of 70characters.
Type: Text
Format
minLength 1
maxLength 70
3.2.6.11  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 57 March 2024
```

