---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.7 Quantity"]
file_pages: [554]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.7 Quantity

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 554 to 554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 554

```text
Meaning When True: Yes
Meaning When False: No
7.2.7 Quantity
7.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
7.2.7.2  Max3Number
Definition: Number (max 999) of objects represented as an integer.
Type: Quantity
Format
totalDigits 3
fractionDigits 0
Constraints
• NumberRule
If Number is negative, then Sign must be present.
7.2.7.3  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
7.2.8 Rate
7.2.8.1  BaseOneRate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.
Type: Rate
Format
totalDigits 11
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 554 March 2026
```

