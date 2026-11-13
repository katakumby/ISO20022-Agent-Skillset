---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.68 MinimumQuantity <MinQty>"]
file_pages: [1902]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.68 MinimumQuantity <MinQty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1902 to 1902.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1902

```text
MinimumIncrement <MinIncrmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
32.4.3.1.1.2.3.68  MinimumQuantity <MinQty>
Presence: [0..1]
Definition: Indicates the minimum tradable quantity of a security.
MinimumQuantity <MinQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
32.4.3.1.1.2.3.69  Production <Pdctn>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond, particularly an mortgage back
security (MBS), issued in a particular year.
Datatype: "Max35Text" on page 3328
32.4.3.1.1.2.3.70  RestrictedIndicator <RstrctdInd>
Presence: [0..1]
Definition: Identifies if the securities is restricted or not (as per Rule 144).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.1.2.3.71  PriceFrequency <PricFrqcy>
Presence: [0..1]
Definition: Indicates the frequency at which the bond is re-rated and therefore re-priced (bond attribute,
particularly of floating rate and index linked instruments).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1902 August 2026
```

