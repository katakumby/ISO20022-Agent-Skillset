---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.9 Text", "13.2.9.6 Max256Text"]
file_pages: [534]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.9.6 Max256Text

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 534 to 534.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 534

```text
13.2.9.6  Max256Text
Definition: Specifies a character string with a maximum length of 256 characters.
Type: Text
Format
minLength 1
maxLength 256
13.2.9.7  Max350Text
Definition: Specifies a character string with a maximum length of 350 characters.
Type: Text
Format
minLength 1
maxLength 350
13.2.9.8  Max35Text
Definition: Specifies a character string with a maximum length of 35 characters.
Type: Text
Format
minLength 1
maxLength 35
13.2.9.9  Max3NumericText
Definition: Specifies a numeric string with a maximum length of 3 digits.
Type: Text
Format
pattern [0-9]{1,3}
13.2.9.10  Max4AlphaNumericText
Definition: Specifies an alphanumeric string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
pattern [a-zA-Z0-9]{1,4}
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 534 March 2024
```

