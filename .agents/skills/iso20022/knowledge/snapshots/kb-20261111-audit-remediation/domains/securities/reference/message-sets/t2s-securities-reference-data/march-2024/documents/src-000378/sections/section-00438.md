---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.9 Text", "13.2.9.11 Max5NumericText"]
file_pages: [535]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.9.11 Max5NumericText

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 535 to 535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 535

```text
13.2.9.11  Max5NumericText
Definition: Specifies a numeric string with a maximum length of 5 digits.
Type: Text
Format
pattern [0-9]{1,5}
13.2.9.12  Max70Text
Definition: Specifies a character string with a maximum length of 70characters.
Type: Text
Format
minLength 1
maxLength 70
13.2.9.13  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
13.2.10 YearMonth
13.2.10.1  ISOYearMonth
Definition: Month within a particular calendar year represented by YYYY-MM (ISO 8601).
Type: YearMonth
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 535 March 2024
```

