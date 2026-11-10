---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.2 Message Datatypes", "11.2.5 Indicator", "11.2.5.3 YesNoIndicator"]
file_pages: [99]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.2.5.3 YesNoIndicator

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 99 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

```text
11.2.5.3  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
11.2.6 Text
11.2.6.1  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
11.2.6.2  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
11.2.6.3  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
11.2.6.4  Max256Text
Definition: Specifies a character string with a maximum length of 256 characters.
Type: Text
Format
minLength 1
maxLength 256
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 99 December 2019
```

