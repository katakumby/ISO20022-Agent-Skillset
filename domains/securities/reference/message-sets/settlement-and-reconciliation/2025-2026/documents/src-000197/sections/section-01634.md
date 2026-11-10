---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.8 Rate", "35.2.8.2 PercentageRate"]
file_pages: [2190]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.8.2 PercentageRate

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2190 to 2190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2190

```text
35.2.8.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
35.2.9 Text
35.2.9.1  Exact3NumericText
Definition: Specifies a numeric string with an exact length of 3 digits.
Type: Text
Format
pattern [0-9]{3}
35.2.9.2  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
35.2.9.3  Exact4NumericText
Definition: Specifies a numeric string with an exact length of 4 digits.
Type: Text
Format
pattern [0-9]{4}
35.2.9.4  Exact5NumericText
Definition: Specifies a numeric string with an exact length of 5 digits.
Type: Text
Format
pattern [0-9]{5}
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2190 March 2026
```

