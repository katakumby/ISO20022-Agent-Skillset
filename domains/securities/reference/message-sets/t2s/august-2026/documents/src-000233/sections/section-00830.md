---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.49 WeightedAverageMaturity <WghtdAvrgMtrty>"]
file_pages: [1235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.49 WeightedAverageMaturity <WghtdAvrgMtrty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1235 to 1235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1235

```text
28.4.2.1.2.1.3.49  WeightedAverageMaturity <WghtdAvrgMtrty>
Presence: [0..1]
Definition: Contains the weighted average maturity of the fixed income instrument (expressed in
months).
Datatype: "DecimalNumber" on page 3324
28.4.2.1.2.1.3.50  InsuredIndicator <InsrdInd>
Presence: [0..1]
Definition: Indicates whether the instrument is backed by any kind of asset or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.2.1.3.51  BankQualifiedIndicator <BkQlfdInd>
Presence: [0..1]
Definition: Indicates whether the security is bank qualified (usually applies to loan products).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.2.1.3.52  YieldCalculation <YldClctn>
Presence: [0..*]
Definition: Rate of return on an investment, based on the price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1235 August 2026
```

