---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.35 CurrentFactor <CurFctr>"]
file_pages: [1887]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.35 CurrentFactor <CurFctr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1887 to 1887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1887

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
32.4.3.1.1.2.3.35  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Identifies the current factor expressed as a decimal between 0 and 1 defining the outstanding
principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 3325
32.4.3.1.1.2.3.36  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Identifies the new factor expressed as a decimal between 0 and 1 defining the outstanding
principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 3325
32.4.3.1.1.2.3.37  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Identifies the previous factor expressed as a decimal between 0 and 1 defining the
outstanding principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 3325
32.4.3.1.1.2.3.38  Pieces <Pcs>
Presence: [0..1]
Definition: Number of pieces composing a pool of financial assets.
Datatype: "DecimalNumber" on page 3324
32.4.3.1.1.2.3.39  PoolsMaximum <PlsMax>
Presence: [0..1]
Definition: Collection of assets by which a security is backed.
Datatype: "DecimalNumber" on page 3324
32.4.3.1.1.2.3.40  PoolsPerMillion <PlsPerMln>
Presence: [0..1]
Definition: Indicates per million the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 3324
32.4.3.1.1.2.3.41  PoolsPerLot <PlsPerLot>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1887 August 2026
```

