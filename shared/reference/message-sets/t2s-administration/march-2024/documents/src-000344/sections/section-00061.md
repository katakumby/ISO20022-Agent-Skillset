---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.2 Message Datatypes", "5.2.5 Text"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.2.5 Text

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
5.2.5 Text
5.2.5.1  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
5.2.5.2  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
5.2.5.3  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
5.2.5.4  Max34Text
Definition: Specifies a character string with a maximum length of 34 characters.
Type: Text
Format
minLength 1
maxLength 34
5.2.5.5  Max350Text
Definition: Specifies a character string with a maximum length of 350 characters.
Type: Text
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
68 March 2024
```

