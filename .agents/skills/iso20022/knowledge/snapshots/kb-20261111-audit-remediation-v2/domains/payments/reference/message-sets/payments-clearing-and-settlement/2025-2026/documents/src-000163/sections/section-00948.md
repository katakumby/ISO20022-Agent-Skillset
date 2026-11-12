---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.9 Rate", "10.2.9.2 PercentageRate"]
file_pages: [1243]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.9.2 PercentageRate

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1243 to 1243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1243

```text
10.2.9.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
10.2.10 Text
10.2.10.1  Exact2NumericText
Definition: Specifies a numeric string with an exact length of 2 digits.
Type: Text
Format
pattern [0-9]{2}
10.2.10.2  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
10.2.10.3  HexBinaryText
Definition: Specifies a character string with hexadecimal text characters.
Used for hex binary data only, supports only characters A-F, a-f and 0-9.
Type: Text
Format
pattern [0-9a-fA-F]+
10.2.10.4  Max1025Text
Definition: Specifies a character string with a maximum length of 1025 characters.
Type: Text
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1243 March 2026
```

