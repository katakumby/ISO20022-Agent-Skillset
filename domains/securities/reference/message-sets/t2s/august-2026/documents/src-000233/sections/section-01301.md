---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.49 WeightedAverageMaturity <WghtdAvrgMtrty>"]
file_pages: [1889]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.49 WeightedAverageMaturity <WghtdAvrgMtrty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1889 to 1889.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1889

```text
32.4.3.1.1.2.3.49  WeightedAverageMaturity <WghtdAvrgMtrty>
Presence: [0..1]
Definition: Contains the weighted average maturity of the fixed income instrument (expressed in
months).
Datatype: "DecimalNumber" on page 3324
32.4.3.1.1.2.3.50  InsuredIndicator <InsrdInd>
Presence: [0..1]
Definition: Indicates whether the instrument is backed by any kind of asset or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.1.2.3.51  BankQualifiedIndicator <BkQlfdInd>
Presence: [0..1]
Definition: Indicates whether the security is bank qualified (usually applies to loan products).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.1.2.3.52  YieldCalculation <YldClctn>
Presence: [0..*]
Definition: Rate of return on an investment, based on the price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1889 August 2026
```

