---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.8 Rate", "82.2.8.2 PercentageRate"]
file_pages: [3325]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.8.2 PercentageRate

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3325 to 3325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3325

```text
82.2.8.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
82.2.9 Text
82.2.9.1  Exact3NumericText
Definition: Specifies a numeric string with an exact length of 3 digits.
Type: Text
Format
pattern [0-9]{3}
82.2.9.2  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
82.2.9.3  Exact4NumericText
Definition: Specifies a numeric string with an exact length of 4 digits.
Type: Text
Format
pattern [0-9]{4}
82.2.9.4  Exact5NumericText
Definition: Specifies a numeric string with an exact length of 5 digits.
Type: Text
Format
pattern [0-9]{5}
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3325 August 2026
```

