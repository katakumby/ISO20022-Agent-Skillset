---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.2 Message Datatypes", "4.2.6 Indicator"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.6 Indicator

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
4.2.6 Indicator
4.2.6.1  RequestedIndicator
Definition: Indicates if requested or not.
Type: Indicator
Meaning When True: Requested
Meaning When False: Not Requested
4.2.6.2  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
4.2.7 Quantity
4.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
4.2.7.2  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
81 March 2024
```

