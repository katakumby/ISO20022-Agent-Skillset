---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.9 Text", "82.2.9.5 ISO20022MessageIdentificationText"]
file_pages: [3326]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.9.5 ISO20022MessageIdentificationText

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3326 to 3326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3326

```text
82.2.9.5  ISO20022MessageIdentificationText
Definition: ISO 20022 Message identifier of an MX message.
Type: Text
Format
pattern [a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}
82.2.9.6  Max128Text
Definition: Specifies a character string with a maximum length of 128 characters.
Type: Text
Format
minLength 1
maxLength 128
82.2.9.7  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
82.2.9.8  Max15NumericText
Definition: Specifies a numeric string with a maximum length of 15 digits.
Type: Text
Format
pattern [0-9]{1,15}
82.2.9.9  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
82.2.9.10  Max2048Text
Definition: Specifies a character string with a maximum length of 2048 characters.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3326 August 2026
```

