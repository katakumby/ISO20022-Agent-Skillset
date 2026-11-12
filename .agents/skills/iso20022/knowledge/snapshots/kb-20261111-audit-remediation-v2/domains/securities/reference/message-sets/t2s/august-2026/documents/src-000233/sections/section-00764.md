---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.30 ConversionRatioNumerator <ConvsRatioNmrtr>"]
file_pages: [1145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.30 ConversionRatioNumerator <ConvsRatioNmrtr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1145 to 1145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1145

```text
28.4.2.1.1.2.30  ConversionRatioNumerator <ConvsRatioNmrtr>
Presence: [0..1]
Definition: Number of target securities for the conversion.
ConversionRatioNumerator <ConvsRatioNmrtr> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
28.4.2.1.1.2.31  ConversionRatioDenominator <ConvsRatioDnmtr>
Presence: [0..1]
Definition: Number of held securities for the conversion.
ConversionRatioDenominator <ConvsRatioDnmtr> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
28.4.2.1.1.2.32  PrimaryPlaceOfDeposit <PmryPlcOfDpst>
Presence: [0..1]
Definition: Primary place of deposit.
PrimaryPlaceOfDeposit <PmryPlcOfDpst> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
28.4.2.1.1.2.33  TradingMethod <TradgMtd>
Presence: [0..1]
Definition: Indicates whether the notional amount value is to be traded in either an amount or in units.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1145 August 2026
```

