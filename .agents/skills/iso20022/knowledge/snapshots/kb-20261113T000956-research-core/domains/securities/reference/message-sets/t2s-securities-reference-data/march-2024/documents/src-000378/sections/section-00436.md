---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.9 Text"]
file_pages: [533]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.9 Text

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 533 to 533.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 533

```text
13.2.9 Text
13.2.9.1  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
13.2.9.2  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
13.2.9.3  Max15NumericText
Definition: Specifies a numeric string with a maximum length of 15 digits.
Type: Text
Format
pattern [0-9]{1,15}
13.2.9.4  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
13.2.9.5  Max210Text
Definition: Specifies a character string with a maximum length of 210 characters.
Type: Text
Format
minLength 1
maxLength 210
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 533 March 2024
```

