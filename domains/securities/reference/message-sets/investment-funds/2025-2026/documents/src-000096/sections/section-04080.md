---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.8 Rate"]
file_pages: [5401]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.8 Rate

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5401 to 5401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5401

```text
Format
totalDigits 18
fractionDigits 0
66.2.8 Rate
66.2.8.1  BaseOneRate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 1.0
66.2.8.2  PercentageBoundedRate
Definition: Rate expressed as a percentage, ie, in hundredths, eg, 0.7 is 7/10 of a percent, and 7.0 is
7%.
Type: Rate
Format
minInclusive 0
maxInclusive 100
totalDigits 11
fractionDigits 10
baseValue 100.0
66.2.8.3  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5401 May 2026
```

