---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.35 CurrentFactor <CurFctr>"]
file_pages: [1233]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.35 CurrentFactor <CurFctr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1233 to 1233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1233

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.1.2.1.3.35  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Identifies the current factor expressed as a decimal between 0 and 1 defining the outstanding
principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 3325
28.4.2.1.2.1.3.36  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Identifies the new factor expressed as a decimal between 0 and 1 defining the outstanding
principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 3325
28.4.2.1.2.1.3.37  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Identifies the previous factor expressed as a decimal between 0 and 1 defining the
outstanding principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 3325
28.4.2.1.2.1.3.38  Pieces <Pcs>
Presence: [0..1]
Definition: Number of pieces composing a pool of financial assets.
Datatype: "DecimalNumber" on page 3324
28.4.2.1.2.1.3.39  PoolsMaximum <PlsMax>
Presence: [0..1]
Definition: Collection of assets by which a security is backed.
Datatype: "DecimalNumber" on page 3324
28.4.2.1.2.1.3.40  PoolsPerMillion <PlsPerMln>
Presence: [0..1]
Definition: Indicates per million the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 3324
28.4.2.1.2.1.3.41  PoolsPerLot <PlsPerLot>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1233 August 2026
```

