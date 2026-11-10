---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.2 Message Datatypes", "11.2.6 Text", "11.2.6.8 Max35Text"]
file_pages: [188, 189]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.2.6.8 Max35Text

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 188 to 189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
11.2.6.8  Max35Text
Definition: Specifies a character string with a maximum length of 35 characters.
Type: Text
Format
minLength 1
maxLength 35
11.2.6.9  Max4AlphaNumericText
Definition: Specifies an alphanumeric string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
pattern [a-zA-Z0-9]{1,4}
11.2.6.10  Max4Text
Definition: Specifies a character string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
11.2.6.11  Max70Text
Definition: Specifies a character string with a maximum length of 70characters.
Type: Text
Format
minLength 1
maxLength 70
11.2.6.12  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
188 March 2024
```

## File page 189

```text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
189 March 2024
```

