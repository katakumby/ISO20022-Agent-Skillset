---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.30 ConversionRatioNumerator <ConvsRatioNmrtr>"]
file_pages: [785]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.30 ConversionRatioNumerator <ConvsRatioNmrtr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 785 to 785.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 785

```text
27.4.2.3.30  ConversionRatioNumerator <ConvsRatioNmrtr>
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
27.4.2.3.31  ConversionRatioDenominator <ConvsRatioDnmtr>
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
27.4.2.3.32  PrimaryPlaceOfDeposit <PmryPlcOfDpst>
Presence: [0..1]
Definition: Primary place of deposit.
PrimaryPlaceOfDeposit <PmryPlcOfDpst> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
27.4.2.3.33  TradingMethod <TradgMtd>
Presence: [0..1]
Definition: Indicates whether the notional amount value is to be traded in either an amount or in units.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 785 August 2026
```

