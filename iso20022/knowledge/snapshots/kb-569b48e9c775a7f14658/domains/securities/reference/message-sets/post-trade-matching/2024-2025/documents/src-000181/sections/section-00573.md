---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.8 Rate", "7.2.8.2 PercentageRate"]
file_pages: [667]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.8.2 PercentageRate

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 667 to 667.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 667

```text
fractionDigits 10
baseValue 1.0
7.2.8.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
7.2.9 Text
7.2.9.1  Exact3NumericText
Definition: Specifies a numeric string with an exact length of 3 digits.
Type: Text
Format
pattern [0-9]{3}
7.2.9.2  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
7.2.9.3  Exact4NumericText
Definition: Specifies a numeric string with an exact length of 4 digits.
Type: Text
Format
pattern [0-9]{4}
7.2.9.4  ISO20022MessageIdentificationText
Definition: ISO 20022 Message identifier of an MX message.
Type: Text
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 667 February 2025
```

