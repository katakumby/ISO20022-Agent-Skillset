---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.49 WeightedAverageMaturity <WghtdAvrgMtrty>"]
file_pages: [212]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.49 WeightedAverageMaturity <WghtdAvrgMtrty>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 212 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 212

```text
Datatype: "DecimalNumber" on page 532
13.1.2.3.49  WeightedAverageMaturity <WghtdAvrgMtrty>
Presence: [0..1]
Definition: Contains the weighted average maturity of the fixed income instrument (expressed in
months).
Datatype: "DecimalNumber" on page 532
13.1.2.3.50  InsuredIndicator <InsrdInd>
Presence: [0..1]
Definition: Indicates whether the instrument is backed by any kind of asset or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.51  BankQualifiedIndicator <BkQlfdInd>
Presence: [0..1]
Definition: Indicates whether the security is bank qualified (usually applies to loan products).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.52  YieldCalculation <YldClctn>
Presence: [0..*]
Definition: Rate of return on an investment, based on the price.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 212 March 2024
```

